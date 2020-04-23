%define  debug_package %{nil}
%define _prefix /var/lib/awx
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define service_user awx
%define service_group awx
%define service_homedir /var/lib/awx
%define service_logdir /var/log/tower
%define service_configdir /etc/tower

Summary: Ansible AWX
Name: ansible-awx
Version: ¤VERSION¤
Release: 1%{dist}
Source0: ¤SOURCE¤
Source2: awx-cbreceiver.service
Source3: awx-dispatcher.service
Source5: awx-channels-worker.service
Source6: awx-daphne.service
Source7: awx-web.service
Source8: nginx.conf.example
Source9: awx-create-venv
Source10: awx-rpm-logo.svg
Source11: awx.service
License: GPLv3
Group: AWX
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}.buildroot
Vendor: AWX
Prefix: %{_prefix}
AutoReqProv: false

BuildRequires: git
BuildRequires: tcl
BuildRequires: sqlite >= 3.8.3
BuildRequires: libcurl-devel
BuildRequires: libffi-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: libxslt-devel
BuildRequires: openldap-devel
BuildRequires: xmlsec1-devel
BuildRequires: xmlsec1-openssl-devel
BuildRequires: postgresql-devel

# Generated BuildRequires

Requires: bubblewrap
Requires: curl
Requires: git
Requires: libcurl-devel
Requires: libffi-devel
Requires: libtool-ltdl-devel
Requires: libxslt-devel
Requires: openldap-devel
Requires: sshpass
Requires: subversion
Requires: xmlsec1-devel
Requires: xmlsec1-openssl-devel

# Generated Requires

Requires(pre): /usr/sbin/useradd, /usr/bin/getent
%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n awx-¤VERSION¤

%build
make sdist

%install
# Setup build environment
pip3 install --root=$RPM_BUILD_ROOT .

# Collect django static
cat > _awx_rpmbuild_collectstatic_settings.py <<EOF
from awx.settings.defaults import *
DEFAULTS_SNAPSHOT = {}
CLUSTER_HOST_ID = "awx-static"
STATIC_ROOT = "static/"
LOG_AGGREGATOR_AUDIT = False
EOF

export DJANGO_SETTINGS_MODULE="_awx_rpmbuild_collectstatic_settings"
export PYTHONPATH="$PYTHONPATH:."
mkdir -p static/
sed -i 's$/usr/bin/awx-python$/usr/bin/python3$g' $RPM_BUILD_ROOT/usr/bin/awx-manage

#%if 0%{?el7}
#scl enable rh-postgresql10 "$RPM_BUILD_ROOT/usr/bin/awx-manage collectstatic --noinput --clear"
#%else
$RPM_BUILD_ROOT/usr/bin/awx-manage collectstatic --noinput --clear
#%endif

# Cleanup
unset PYTHONPATH
unset DJANGO_SETTINGS_MODULE

mkdir -p %{buildroot}%{service_homedir}
mkdir -p %{buildroot}%{service_logdir}
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}%{service_configdir}
mkdir -p %{buildroot}/var/lib/awx/
echo ¤VERSION¤ > %{buildroot}%{service_homedir}/.tower_version


cp installer/roles/image_build/files/settings.py %{buildroot}%{service_configdir}/settings.py
mkdir -p %{buildroot}/var/lib/awx/public/
mv static %{buildroot}/var/lib/awx/public/static

# Install systemd configuration
mkdir -p %{buildroot}%{_unitdir}
for service in awx-cbreceiver awx-dispatcher awx-channels-worker awx-daphne awx-web awx; do
    cp %{_sourcedir}/${service}.service %{buildroot}%{_unitdir}/
done

# Create fake python executable
#cat > %{buildroot}%{_prefix}/bin/python <<"EOF"
##!/bin/sh
#export AWX_SETTINGS_FILE=/etc/tower/settings.py
#exec scl enable rh-python36 "%{?el7:python3} \"$@\""
#EOF

# Create Virtualenv folder
mkdir -p %{buildroot}/var/lib/awx/venv

# Install docs
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/ansible-awx/
cp %{_sourcedir}/nginx.conf.example $RPM_BUILD_ROOT/usr/share/doc/ansible-awx/

# Install VENV Script
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp %{_sourcedir}/awx-create-venv $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT%{service_homedir}/venv

cp %{_sourcedir}/awx-rpm-logo.svg $RPM_BUILD_ROOT/var/lib/awx/public/static/assets/awx-rpm-logo.svg
mv $RPM_BUILD_ROOT/var/lib/awx/public/static/assets/logo-header.svg $RPM_BUILD_ROOT/var/lib/awx/public/static/assets/logo-header.svg.orig
mv $RPM_BUILD_ROOT/var/lib/awx/public/static/assets/logo-login.svg $RPM_BUILD_ROOT/var/lib/awx/public/static/assets/logo-login.svg.orig
ln -s /var/lib/awx/public/static/assets/awx-rpm-logo.svg $RPM_BUILD_ROOT/var/lib/awx/public/static/assets/logo-header.svg
ln -s /var/lib/awx/public/static/assets/awx-rpm-logo.svg $RPM_BUILD_ROOT/var/lib/awx/public/static/assets/logo-login.svg

#Move stuff
mv $RPM_BUILD_ROOT/usr/lib/python3.6/site-packages/usr/share/doc/awx/* $RPM_BUILD_ROOT/usr/share/doc/ansible-awx/
mv $RPM_BUILD_ROOT/usr/lib/python3.6/site-packages/usr/bin/* $RPM_BUILD_ROOT/usr/bin/
mv $RPM_BUILD_ROOT/usr/lib/python3.6/site-packages/usr/share/sosreport $RPM_BUILD_ROOT/usr/share/
mkdir -p $RPM_BUILD_ROOT/var/lib/awx/__pycache__/
mv $RPM_BUILD_ROOT/usr/lib/python3.6/site-packages/var/lib/awx/__pycache__/wsgi.cpython-36.pyc $RPM_BUILD_ROOT/var/lib/awx/__pycache__/
mv $RPM_BUILD_ROOT/usr/lib/python3.6/site-packages/var/lib/awx/* $RPM_BUILD_ROOT/var/lib/awx/public/static/
rm -rf $RPM_BUILD_ROOT/usr/lib/python3.6/site-packages/usr



%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%post
%systemd_post awx-cbreceiver
%systemd_post awx-dispatcher
%systemd_post awx-channels-worker
%systemd_post awx-daphne
%systemd_post awx-web

%preun
%systemd_preun awx-cbreceiver
%systemd_preun awx-dispatcher
%systemd_preun awx-channels-worker
%systemd_preun awx-daphne
%systemd_preun awx-web

%postun
%systemd_postun awx-cbreceiver
%systemd_postun awx-dispatcher
%systemd_postun awx-channels-worker
%systemd_postun awx-daphne
%systemd_postun awx-web

%clean

%files
%defattr(0644, awx, awx, 0755)
%doc /usr/share/doc/ansible-awx/nginx.conf.example
%attr(0755, root, root) /usr/bin/awx-manage
%attr(0755, root, root) /usr/bin/awx-create-venv
/usr/bin/awx-create-venv
/usr/lib/python3.6/site-packages/awx
%attr(0755, root, root) /usr/lib/python3.6/site-packages/awx/plugins/*/*.py
/var/lib/awx/public/static/assets/logo-login.svg
/var/lib/awx/public/static/assets/logo-header.svg
/var/lib/awx/public/static
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}/venv
%{service_homedir}/.tower_version
%dir %attr(0770, %{service_user}, %{service_group}) %{service_logdir}
%config %{service_configdir}/settings.py
/usr/share/doc/ansible-awx/
/usr/lib/python3.6/site-packages/awx-%{version}.dist-info
/usr/share/sosreport/sos/plugins/__pycache__/tower.cpython-36.pyc
/usr/share/sosreport/sos/plugins/tower.py
/var/lib/awx/__pycache__/wsgi.cpython-36.pyc
/usr/bin/ansible-tower-service
/usr/bin/ansible-tower-setup
/usr/bin/failure-event-handler
/usr/bin/awx-python


%attr(0644, root, root) %{_unitdir}/awx-cbreceiver.service
%attr(0644, root, root) %{_unitdir}/awx-dispatcher.service
%attr(0644, root, root) %{_unitdir}/awx-channels-worker.service
%attr(0644, root, root) %{_unitdir}/awx-daphne.service
%attr(0644, root, root) %{_unitdir}/awx-web.service
%attr(0644, root, root) %{_unitdir}/awx.service

%changelog
* Wed Apr 22 2020 10:00:00 +0000 Martin Juhl <mju@miracle.dk> 11.0.0
- New build
