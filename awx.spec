%define _prefix /opt/awx
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define ansible_version 2.4.3.0
%define service_user awx
%define service_group awx
%define service_homedir /var/lib/awx
%define service_logdir /var/log/awx
%define service_configdir /etc/awx

Summary: Ansible AWX
Name: awx
Version: ¤VERSION¤
Release: 1%{dist}
Source0: /dist/¤SOURCE¤
Source1: settings.py.dist
%if 0%{?amzn}
Source2: awx-cbreceiver.upstart
Source3: awx-celery-beat.upstart
Source4: awx-celery-worker.upstart
Source5: awx-channels-worker.upstart
Source6: awx-daphne.upstart
Source7: awx-web.upstart
%endif
%if 0%{?el7}
Source2: awx-cbreceiver.service
Source3: awx-celery-beat.service
Source4: awx-celery-worker.service
Source5: awx-channels-worker.service
Source6: awx-daphne.service
Source7: awx-web.service
%endif
Source8: nginx.conf.example
License: GPLv3
Group: AWX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
BuildRequires: gcc gcc-c++ git
BuildRequires: libffi-devel libxslt-devel xmlsec1-devel xmlsec1-openssl-devel libyaml-devel openldap-devel libtool-ltdl-devel libcurl-devel
%{?amzn:BuildRequires: python27 python27-virtualenv python27-devel postgresql95-devel}
%{?el7:BuildRequires: systemd python python-virtualenv python-devel postgresql-devel}
%{?fedora:BuildRequires: systemd python python-virtualenv python-devel postgresql-devel m2crypto}
Requires: git subversion curl bubblewrap
Requires(pre): /usr/sbin/useradd, /usr/bin/getent
%{?systemd_requires}

%description
%{summary}

%prep
%setup -q

%build
# Setup build environment
virtualenv _buildenv/
_buildenv/bin/pip install -U wheel
_buildenv/bin/pip install -U pip==9.0.1
_buildenv/bin/pip install -U setuptools

export PYTHONPATH="`pwd`/embedded/lib/python2.7/site-packages:`pwd`/embedded/lib64/python2.7/site-packages"

# Install dependencies
cat requirements/requirements_ansible.txt requirements/requirements_ansible_git.txt | \
    _buildenv/bin/pip install --no-binary cffi,pycparser,psycopg2,twilio --prefix=`pwd`/embedded/ -r /dev/stdin
cat requirements/requirements.txt requirements/requirements_git.txt | \
    _buildenv/bin/pip install --no-binary cffi,pycparser,psycopg2,twilio --prefix=`pwd`/embedded/ -r /dev/stdin

_buildenv/bin/pip install --no-binary cffi,pycparser,psycopg2,twilio --prefix=`pwd`/embedded/ ansible==%{ansible_version}
_buildenv/bin/pip install --no-binary cffi,pycparser,psycopg2,twilio --prefix=`pwd`/embedded/ .

# Fix nested packages
touch embedded/lib64/python2.7/site-packages/zope/__init__.py
touch embedded/lib/python2.7/site-packages/jaraco/__init__.py
touch embedded/lib64/python2.7/site-packages/dm/__init__.py
touch embedded/lib64/python2.7/site-packages/dm/xmlsec/__init__.py

# Collect django static
cat > _awx_rpmbuild_collectstatic_settings.py <<EOF
from awx.settings.defaults import *
DEFAULTS_SNAPSHOT = {}
STATIC_ROOT = "static/"
EOF

export DJANGO_SETTINGS_MODULE="_awx_rpmbuild_collectstatic_settings"
export PYTHONPATH="$PYTHONPATH:."
mkdir -p static/
embedded/bin/awx-manage collectstatic --noinput --clear

# Cleanup
unset PYTHONPATH
unset DJANGO_SETTINGS_MODULE

%install
mkdir -p %{buildroot}%{service_homedir}
mkdir -p %{buildroot}%{service_logdir}
mkdir -p %{buildroot}%{_prefix}/embedded
mkdir -p %{buildroot}%{_prefix}/embedded/bin
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}%{service_configdir}
mkdir -p %{buildroot}/var/lib/awx/
echo %{version} > %{buildroot}%{service_homedir}/.tower_version

cp %{_sourcedir}/settings.py.dist %{buildroot}%{service_configdir}/settings.py
mv embedded/lib %{buildroot}%{_prefix}/embedded/lib
mv embedded/lib64 %{buildroot}%{_prefix}/embedded/lib64
mv static %{buildroot}%{_prefix}/static

%if 0%{?amzn}
# Install upstart configuration
mkdir -p %{buildroot}/etc/init
mkdir -p %{buildroot}/etc/rc.d/init.d
for service in awx-cbreceiver awx-celery-beat awx-celery-worker awx-channels-worker awx-daphne awx-web; do
    cp %{_sourcedir}/${service}.upstart %{buildroot}/etc/init/${service}.conf
    cat > %{buildroot}/etc/rc.d/init.d/${service} <<EOF
#!/bin/sh
#chkconfig: - 99 02
#description: $service

exec /sbin/initctl \$1 $service
EOF
done
%endif

%if 0%{?el7}
# Install systemd configuration
mkdir -p %{buildroot}%{_unitdir}
for service in awx-cbreceiver awx-celery-beat awx-celery-worker awx-channels-worker awx-daphne awx-web; do
    cp %{_sourcedir}/${service}.service %{buildroot}%{_unitdir}/
done
%endif

# Create fake python executable
cat > %{buildroot}%{_prefix}/bin/python <<"EOF"
#!/bin/sh
export PYTHONPATH="%{_prefix}/embedded/lib/python2.7/site-packages:%{_prefix}/embedded/lib64/python2.7/site-packages"
export AWX_SETTINGS_FILE=/etc/awx/settings.py
exec %{?amzn:python27}%{?el7:python2} "$@"
EOF

# Export usefull scripts
mv embedded/bin/uwsgi %{buildroot}%{_prefix}/bin/uwsgi
for script_name in awx-manage ansible ansible-playbook daphne celery;do
    mv embedded/bin/$script_name %{buildroot}%{_prefix}/bin/$script_name
    sed -i '1c#!%{_prefix}/bin/python' %{buildroot}%{_prefix}/bin/$script_name
done

# Create Virtualenv folder
mkdir -p %{buildroot}/var/lib/awx/venv

# Install docs
cp %{_sourcedir}/nginx.conf.example ./

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /sbin/nologin %{service_user}

%post
%if 0%{?el7}
%systemd_post awx-cbreceiver
%systemd_post awx-celery-beat
%systemd_post awx-celery-worker
%systemd_post awx-channels-worker
%systemd_post awx-daphne
%systemd_post awx-web
%endif

%if 0%{?amzn}
if [ $1 -eq 1 ]; then
    /sbin/chkconfig --add awx-cbreceiver
    /sbin/chkconfig --add awx-celery-beat
    /sbin/chkconfig --add awx-celery-worker
    /sbin/chkconfig --add awx-channels-worker
    /sbin/chkconfig --add awx-daphne
    /sbin/chkconfig --add awx-web
fi
%endif

%preun
%if 0%{?el7}
%systemd_preun awx-cbreceiver
%systemd_preun awx-celery-beat
%systemd_preun awx-celery-worker
%systemd_preun awx-channels-worker
%systemd_preun awx-daphne
%systemd_preun awx-web
%endif

%if 0%{?amzn}
if [ $1 -eq 0 ]; then
    /sbin/service awx-cbreceiver stop >/dev/null 2>&1
    /sbin/service awx-celery-beat stop >/dev/null 2>&1
    /sbin/service awx-celery-worker stop >/dev/null 2>&1
    /sbin/service awx-channels-worker stop >/dev/null 2>&1
    /sbin/service awx-daphne stop >/dev/null 2>&1
    /sbin/service awx-web stop >/dev/null 2>&1

    /sbin/chkconfig --del awx-cbreceiver
    /sbin/chkconfig --del awx-celery-beat
    /sbin/chkconfig --del awx-celery-worker
    /sbin/chkconfig --del awx-channels-worker
    /sbin/chkconfig --del awx-daphne
    /sbin/chkconfig --del awx-web
fi
%endif

%postun
%if 0%{?el7}
%systemd_postun awx-cbreceiver
%systemd_postun awx-celery-beat
%systemd_postun awx-celery-worker
%systemd_postun awx-channels-worker
%systemd_postun awx-daphne
%systemd_postun awx-web
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644, awx, awx, 0755)
%doc nginx.conf.example
%attr(0755, root, root) %{_prefix}/bin/uwsgi
%attr(0755, root, root) %{_prefix}/bin/python
%attr(0755, root, root) %{_prefix}/bin/celery
%attr(0755, root, root) %{_prefix}/bin/awx-manage
%attr(0755, root, root) %{_prefix}/bin/daphne
%attr(0755, root, root) %{_prefix}/bin/ansible
%attr(0755, root, root) %{_prefix}/bin/ansible-playbook
%{_prefix}/static
%{_prefix}/embedded/lib
%{_prefix}/embedded/lib64
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}
%{service_homedir}/.tower_version
%dir %attr(0750, root, %{service_group}) %{service_logdir}
%config(noreplace) %{service_configdir}/settings.py

%if 0%{?amzn}
%attr(0644, root, root) /etc/init/awx-cbreceiver.conf
%attr(0644, root, root) /etc/init/awx-celery-beat.conf
%attr(0644, root, root) /etc/init/awx-celery-worker.conf
%attr(0644, root, root) /etc/init/awx-channels-worker.conf
%attr(0644, root, root) /etc/init/awx-daphne.conf
%attr(0644, root, root) /etc/init/awx-web.conf

%attr(0755, root, root) /etc/rc.d/init.d/awx-cbreceiver
%attr(0755, root, root) /etc/rc.d/init.d/awx-celery-beat
%attr(0755, root, root) /etc/rc.d/init.d/awx-celery-worker
%attr(0755, root, root) /etc/rc.d/init.d/awx-channels-worker
%attr(0755, root, root) /etc/rc.d/init.d/awx-daphne
%attr(0755, root, root) /etc/rc.d/init.d/awx-web
%endif

%if 0%{?el7}
%attr(0644, root, root) %{_unitdir}/awx-cbreceiver.service
%attr(0644, root, root) %{_unitdir}/awx-celery-beat.service
%attr(0644, root, root) %{_unitdir}/awx-celery-worker.service
%attr(0644, root, root) %{_unitdir}/awx-channels-worker.service
%attr(0644, root, root) %{_unitdir}/awx-daphne.service
%attr(0644, root, root) %{_unitdir}/awx-web.service
%endif

%changelog
* Tue Mar 20 2018 21:35:19 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.114
- New Git version build: 1.0.4.114
* Tue Mar 20 2018 16:05:39 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.113
- New Git version build: 1.0.4.113
* Tue Mar 20 2018 14:35:18 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.112
- New Git version build: 1.0.4.112
* Tue Mar 20 2018 11:35:17 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.110
- New Git version build: 1.0.4.110
* Tue Mar 20 2018 01:35:21 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.109
- New Git version build: 1.0.4.109
* Mon Mar 19 2018 17:35:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.108
- New Git version build: 1.0.4.108
* Mon Mar 19 2018 17:08:44 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.107
* Mon Mar 19 2018 15:05:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.107
- New Git version build: 1.0.4.107
* Sat Mar 17 2018 21:05:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.106
- New Git version build: 1.0.4.106
* Sat Mar 17 2018 03:05:30 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.105
- New Git version build: 1.0.4.105
* Fri Mar 16 2018 20:05:44 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.104
- New Git version build: 1.0.4.104
* Fri Mar 16 2018 19:35:42 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.103
- New Git version build: 1.0.4.103
* Fri Mar 16 2018 19:05:51 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.102
- New Git version build: 1.0.4.102
* Fri Mar 16 2018 18:05:33 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.100
- New Git version build: 1.0.4.100
* Fri Mar 16 2018 15:35:17 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.99
- New Git version build: 1.0.4.99
* Fri Mar 16 2018 14:05:24 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.98
- New Git version build: 1.0.4.98
* Thu Mar 15 2018 20:35:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.97
- New Git version build: 1.0.4.97
* Thu Mar 15 2018 19:05:18 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.95
- New Git version build: 1.0.4.95
* Thu Mar 15 2018 18:35:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.94
- New Git version build: 1.0.4.94
* Wed Mar 14 2018 21:04:51 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.93
- New Git version build: 1.0.4.93
* Wed Mar 14 2018 19:35:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.92
- New Git version build: 1.0.4.92
* Wed Mar 14 2018 19:05:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.91
- New Git version build: 1.0.4.91
* Wed Mar 14 2018 15:34:50 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.89
- New Git version build: 1.0.4.89
* Wed Mar 14 2018 15:04:54 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.88
- New Git version build: 1.0.4.88
* Wed Mar 14 2018 14:34:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.87
- New Git version build: 1.0.4.87
* Wed Mar 14 2018 13:34:45 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.86
- New Git version build: 1.0.4.86
* Wed Mar 14 2018 13:04:44 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.85
- New Git version build: 1.0.4.85
* Wed Mar 14 2018 11:34:48 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.84
- New Git version build: 1.0.4.84
* Wed Mar 14 2018 10:10:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.83
- New Git version build: 1.0.4.83
* Fri Mar 09 2018 21:14:34 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.70
- New Git version build

* Fri Mar 09 2018 18:13:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.69
- New Git version build

* Fri Mar 09 2018 17:14:08 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.68
- New Git version build

* Fri Mar 09 2018 16:14:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.67
- New Git version build

* Fri Mar 09 2018 15:14:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.65
- New Git version build

* Fri Mar 09 2018 00:14:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.64
- New Git version build

* Thu Mar 08 2018 23:14:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.63
- New Git version build

* Thu Mar 08 2018 18:14:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.62
- New Git version build

* Thu Mar 08 2018 16:14:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.61
- New Git version build

* Thu Mar 08 2018 15:14:16 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.59
- New Git version build

* Thu Mar 08 2018 14:14:22 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.58
- New Git version build

* Wed Mar 07 2018 21:14:24 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.57
- New Git version build

* Wed Mar 07 2018 17:14:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.56
- New Git version build

* Wed Mar 07 2018 14:14:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.54
- New Git version build

* Tue Mar 06 2018 21:14:12 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.53
- New Git version build

* Tue Mar 06 2018 20:14:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.52
- New Git version build

* Tue Mar 06 2018 19:14:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.51
- New Git version build

* Tue Mar 06 2018 17:14:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.50
- New Git version build

* Tue Mar 06 2018 13:14:00 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.49
- New Git version build

* Tue Mar 06 2018 00:04:00 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.48
- New Git version build

* Mon Mar 05 2018 22:34:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.48
- New Git version build

* Mon Mar 05 2018 22:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.47
- New Git version build

* Mon Mar 05 2018 21:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.46
- New Git version build

* Mon Mar 05 2018 20:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.45
- New Git version build

* Sat Mar 03 2018 16:11:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.43
- New Git version build

* Sat Mar 03 2018 02:11:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.42
- New Git version build

* Fri Mar 02 2018 21:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.41
- New Git version build

* Fri Mar 02 2018 17:11:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.40
- New Git version build

* Fri Mar 02 2018 15:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.39
- New Git version build

* Thu Mar 01 2018 23:11:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.38
- New Git version build

* Thu Mar 01 2018 18:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.37
- New Git version build

* Thu Mar 01 2018 17:11:08 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.36
- New Git version build

* Thu Mar 01 2018 16:11:08 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.35
- New Git version build

* Thu Mar 01 2018 15:11:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.34
- New Git version build

* Wed Feb 28 2018 21:11:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.33
- New Git version build

* Wed Feb 28 2018 19:11:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.32
- New Git version build

* Wed Feb 28 2018 18:11:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.31
- New Git version build

* Wed Feb 28 2018 14:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.29
- New Git version build

* Wed Feb 28 2018 02:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.27
- New Git version build

* Tue Feb 27 2018 22:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.26
- New Git version build

* Tue Feb 27 2018 21:11:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.23
- New Git version build

* Tue Feb 27 2018 19:11:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.22
- New Git version build

* Tue Feb 27 2018 16:11:52 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.21
- New Git version build

* Tue Feb 27 2018 16:11:12 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.21
- New Git version build

* Tue Feb 27 2018 15:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.20
- New Git version build

* Mon Feb 26 2018 22:11:19 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.18
- New Git version build

* Mon Feb 26 2018 21:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.17
- New Git version build

* Mon Feb 26 2018 18:11:00 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.16
- New Git version build

* Mon Feb 26 2018 17:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.15
- New Git version build

* Fri Feb 23 2018 21:11:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.14
- New Git version build

* Thu Feb 22 2018 22:00:52 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.12
- New Git version build

* Fri Feb 16 2018 22:11:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.56
- New Git version build

* Thu Feb 15 2018 22:11:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.55
- New Git version build

* Thu Feb 15 2018 20:11:30 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.54
- New Git version build

* Thu Feb 15 2018 15:11:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.53
- New Git version build

* Wed Feb 14 2018 21:11:12 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.52
- New Git version build

* Wed Feb 14 2018 19:11:23 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.51
- New Git version build

* Wed Feb 14 2018 16:11:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.50
- New Git version build

* Wed Feb 14 2018 14:11:17 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.48
- New Git version build

* Tue Feb 13 2018 23:11:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.47
- New Git version build

* Tue Feb 13 2018 21:11:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.46
- New Git version build

* Tue Feb 13 2018 18:11:29 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.44
- New Git version build

* Tue Feb 13 2018 17:11:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.42
- New Git version build

* Tue Feb 13 2018 14:19:47 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.41
- New Git version build

* Tue Feb 13 2018 14:16:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.41
- New Git version build

* Tue Feb 13 2018 14:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.41
- New Git version build

* Tue Feb 13 2018 14:10:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.41
- New Git version build

* Tue Feb 13 2018 14:09:38 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.41
- New Git version build

* Tue Feb 13 2018 14:09:20 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.41
- New Git version build

* Thu Feb 08 2018 16:11:12 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.23
- New Git version build

* Thu Feb 08 2018 15:11:13 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.20
- New Git version build

* Wed Feb 07 2018 23:11:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.18
- New Git version build

* Wed Feb 07 2018 22:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.17
- New Git version build

* Wed Feb 07 2018 21:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.16
- New Git version build

* Wed Feb 07 2018 17:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.15
- New Git version build

* Wed Feb 07 2018 15:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.14
- New Git version build

* Wed Feb 07 2018 01:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.13
- New Git version build

* Tue Feb 06 2018 20:11:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.12
- New Git version build

* Tue Feb 06 2018 17:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.11
- New Git version build

* Mon Feb 05 2018 21:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.9
- New Git version build

* Mon Feb 05 2018 20:11:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.8
- New Git version build

* Mon Feb 05 2018 15:11:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.7
- New Git version build

* Sun Feb 04 2018 00:03:52 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.5
- New Git version build

* Sat Feb 03 2018 23:39:39 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.33
- New Git version build

* Sat Feb 03 2018 23:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.3.33
- New Git version build

* Thu Jan 25 2018 18:10:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.445
- New Git version build

* Thu Jan 25 2018 16:10:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.443
- New Git version build

* Wed Jan 24 2018 21:11:45 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.440
- New Git version build

* Wed Jan 24 2018 15:11:49 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.438
- New Git version build

* Tue Jan 23 2018 19:11:35 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.436
- New Git version build

* Mon Jan 22 2018 20:11:21 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.432
- New Git version build

* Mon Jan 22 2018 16:11:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.430
- New Git version build

* Fri Jan 19 2018 19:11:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.428
- New Git version build

* Fri Jan 19 2018 14:11:24 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.426
- New Git version build

* Thu Jan 18 2018 22:11:22 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.424
- New Git version build

* Thu Jan 18 2018 21:11:35 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.424
- New Git version build

* Thu Jan 18 2018 20:11:28 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.424
- New Git version build

* Thu Jan 18 2018 19:11:26 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.422
- New Git version build

* Thu Jan 18 2018 18:11:33 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.422
- New Git version build

* Thu Jan 18 2018 17:11:24 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.418
- New Git version build

* Thu Jan 18 2018 16:11:32 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.416
- New Git version build

* Thu Jan 18 2018 14:11:28 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.414
- New Git version build

* Thu Jan 18 2018 05:11:32 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.411
- New Git version build

* Wed Jan 17 2018 20:11:21 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.403
- New Git version build

* Wed Jan 17 2018 18:11:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.399
- New Git version build

* Wed Jan 17 2018 17:11:19 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.397
- New Git version build

* Tue Jan 16 2018 20:11:13 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.388
- New Git version build

* Tue Jan 16 2018 06:11:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.386
- New Git version build

* Tue Jan 16 2018 02:11:19 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.384
- New Git version build

* Mon Jan 15 2018 17:18:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.380
- New Git version build

* Mon Jan 15 2018 17:11:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.380
- New Git version build

* Mon Jan 15 2018 17:05:29 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.380
- New Git version build

* Mon Jan 15 2018 16:11:19 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.374
- New Git version build

* Sat Jan 13 2018 02:11:12 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.372
- New Git version build

* Thu Jan 11 2018 22:10:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.370
- New Git version build

* Thu Jan 11 2018 20:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.368
- New Git version build

* Thu Jan 11 2018 17:12:23 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.364
- New Git version build

* Thu Jan 11 2018 00:10:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.358
- New Git version build

* Wed Jan 10 2018 20:10:55 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.356
- New Git version build

* Wed Jan 10 2018 18:10:54 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.352
- New Git version build

* Wed Jan 10 2018 15:10:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.350
- New Git version build

* Wed Jan 10 2018 06:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.339
- New Git version build

* Wed Jan 10 2018 01:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.337
- New Git version build

* Mon Jan 08 2018 16:10:55 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.335
- New Git version build

* Fri Jan 05 2018 14:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.327
- New Git version build

* Fri Jan 05 2018 13:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.325
- New Git version build

* Thu Jan 04 2018 20:10:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.322
- New Git version build

* Thu Jan 04 2018 18:11:00 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.317
- New Git version build

* Thu Jan 04 2018 17:10:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.315
- New Git version build

* Tue Jan 02 2018 19:10:56 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.307
- New Git version build

* Tue Jan 02 2018 15:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.305
- New Git version build

* Thu Dec 21 2017 19:11:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.303
- New Git version build

* Mon Dec 18 2017 22:11:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.301
- New Git version build

* Fri Dec 15 2017 16:11:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.293
- New Git version build

* Fri Dec 15 2017 05:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.291
- New Git version build

* Thu Dec 14 2017 16:11:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.289
- New Git version build

* Thu Dec 14 2017 04:10:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.285
- New Git version build

* Thu Dec 14 2017 01:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.283
- New Git version build

* Thu Dec 14 2017 00:10:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.281
- New Git version build

* Wed Dec 13 2017 22:10:51 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.279
- New Git version build

* Wed Dec 13 2017 21:12:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.278
- New Git version build

* Wed Dec 13 2017 20:12:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.274
- New Git version build

* Wed Dec 13 2017 19:10:59 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.272
- New Git version build

* Wed Dec 13 2017 18:10:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.268
- New Git version build

* Wed Dec 13 2017 17:11:08 +0000 Martin Juhl <mj@casalogic.dk> 1.0.2.0
- New Git version build

* Wed Dec 13 2017 15:10:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.325
- New Git version build

* Wed Dec 13 2017 00:11:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.323
- New Git version build

* Tue Dec 12 2017 20:11:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.321
- New Git version build

* Tue Dec 12 2017 16:10:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.319
- New Git version build

* Tue Dec 12 2017 02:10:56 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.316
- New Git version build

* Mon Dec 11 2017 22:11:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.314
- New Git version build

* Mon Dec 11 2017 20:01:02 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.314
- New Git version build

* Mon Dec 11 2017 18:36:07 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.312
- New Git version build

* Mon Dec 11 2017 15:01:48 +0000 Martin Juhl <mj@casalogic.dk> 1.0.1.310
- New Git version build

* Thu Nov 21 2017 18:14:55 +0300 Matvey Kruglov <kubuzzzz@gmail.com> 1.0.1.225-1
- Update upstream version
- Improve centos 7 support

* Wed Sep 21 2017 14:44:23 +0300 Matvey Kruglov <kubuzzzz@gmail.com> 1.0.0.505-1
- Initial RPM release
