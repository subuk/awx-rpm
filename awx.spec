%define _prefix /opt/awx
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define ansible_version 2.3.1.0
%define service_user awx
%define service_group awx
%define service_homedir /var/lib/awx
%define service_logdir /var/log/awx
%define service_configdir /etc/awx

Summary: Ansible AWX
Name: awx
Version: 1.0.0.550
Release: 1%{dist}
Source0: https://dl.bintray.com/subuk/awx-sources/awx-%{version}.tar.gz
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
License: GPLv3
Group: AWX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
BuildRequires: gcc gcc-c++ git
BuildRequires: libffi-devel libxslt-devel xmlsec1-devel xmlsec1-openssl-devel libyaml-devel openldap-devel libtool-ltdl-devel
%{?amzn:BuildRequires: python27 python27-virtualenv python27-devel postgresql95-devel}
%{?el7:BuildRequires: systemd python python-virtualenv python-devel postgresql-devel}
Requires: git subversion curl
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
_buildenv/bin/pip install -U pip
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
for script_name in awx-manage ansible ansible-playbook daphne;do
    mv embedded/bin/$script_name %{buildroot}%{_prefix}/bin/$script_name
    sed -i '1c#!%{_prefix}/bin/python' %{buildroot}%{_prefix}/bin/$script_name
done

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
%defattr(0644, root, root, 0755)
%attr(0755, root, root) %{_prefix}/bin/uwsgi
%attr(0755, root, root) %{_prefix}/bin/python
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
* Wed Sep 21 2017 00:12:57 +0300 Matvey Kruglov <kubuzzzz@gmail.com> 1.0.0.550-1
- New upstream version

%changelog
* Wed Sep 21 2017 14:44:23 +0300 Matvey Kruglov <kubuzzzz@gmail.com> 1.0.0.505-1
- Initial RPM release
