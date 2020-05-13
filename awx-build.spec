%define  debug_package %{nil}
%define _prefix /opt/awx
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define service_user awx
%define service_group awx
%define service_homedir /var/lib/awx
%define service_logdir /var/log/tower
%define service_configdir /etc/tower

Summary: Ansible AWX
Name: ansible-awx
Version: 9.3.0.213
Release: 1%{dist}
Source0: awx-9.3.0.213.tar.gz
Source1: settings.py.dist
%if 0%{?el7}
Source2: awx-cbreceiver.service
Source3: awx-dispatcher.service
Source5: awx-channels-worker.service
Source6: awx-daphne.service
Source7: awx-web.service
%endif
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
BuildRequires: libcurl-devel
BuildRequires: libffi-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: libxslt-devel
BuildRequires: openldap-devel
BuildRequires: rh-postgresql10-postgresql-devel
BuildRequires: rh-python36-Django
BuildRequires: rh-python36-PyJWT
BuildRequires: rh-python36-PyYAML
BuildRequires: rh-python36-Twisted
BuildRequires: rh-python36-adal
BuildRequires: rh-python36-ansible-runner
BuildRequires: rh-python36-attrs
BuildRequires: rh-python36-autobahn
BuildRequires: rh-python36-azure-common
BuildRequires: rh-python36-azure-keyvault
BuildRequires: rh-python36-azure-nspkg
BuildRequires: rh-python36-build
BuildRequires: rh-python36-cachetools
BuildRequires: rh-python36-celery
BuildRequires: rh-python36-certifi
BuildRequires: rh-python36-cffi
BuildRequires: rh-python36-channels
BuildRequires: rh-python36-chardet
BuildRequires: rh-python36-constantly
BuildRequires: rh-python36-cryptography
BuildRequires: rh-python36-daphne
BuildRequires: rh-python36-django-auth-ldap
BuildRequires: rh-python36-django-cors-headers
BuildRequires: rh-python36-django-crum
BuildRequires: rh-python36-django-extensions
BuildRequires: rh-python36-django-jsonfield
BuildRequires: rh-python36-django-oauth-toolkit
BuildRequires: rh-python36-django-pglocks
BuildRequires: rh-python36-django-polymorphic
BuildRequires: rh-python36-django-solo
BuildRequires: rh-python36-django-taggit
BuildRequires: rh-python36-djangorestframework
BuildRequires: rh-python36-djangorestframework-yaml
BuildRequires: rh-python36-google-auth
BuildRequires: rh-python36-gitdb2
BuildRequires: rh-python36-GitPython
BuildRequires: rh-python36-idna
BuildRequires: rh-python36-importlib_metadata
BuildRequires: rh-python36-incremental
BuildRequires: rh-python36-inflect
BuildRequires: rh-python36-irc
BuildRequires: rh-python36-isodate
BuildRequires: rh-python36-jaraco.classes
BuildRequires: rh-python36-jaraco.collections
BuildRequires: rh-python36-jaraco.functools
BuildRequires: rh-python36-jaraco.itertools
BuildRequires: rh-python36-jaraco.logging
BuildRequires: rh-python36-jaraco.stream
BuildRequires: rh-python36-jaraco.text
BuildRequires: rh-python36-jsonbfield
BuildRequires: rh-python36-jsonschema
BuildRequires: rh-python36-kombu
BuildRequires: rh-python36-kubernetes
BuildRequires: rh-python36-more-itertools
BuildRequires: rh-python36-msrest
BuildRequires: rh-python36-msrestazure
BuildRequires: rh-python36-oauthlib
BuildRequires: rh-python36-pexpect
BuildRequires: rh-python36-psutil
BuildRequires: rh-python36-psycopg2
BuildRequires: rh-python36-ptyprocess
BuildRequires: rh-python36-pyasn1
BuildRequires: rh-python36-pyasn1-modules
BuildRequires: rh-python36-pygerduty
BuildRequires: rh-python36-pyparsing
BuildRequires: rh-python36-pyrsistent
BuildRequires: rh-python36-pytest-runner
BuildRequires: rh-python36-python
BuildRequires: rh-python36-python-dateutil
BuildRequires: rh-python36-python-devel
BuildRequires: rh-python36-python-jinja2
BuildRequires: rh-python36-python-ldap
BuildRequires: rh-python36-python-logstash
BuildRequires: rh-python36-python-markupsafe
BuildRequires: rh-python36-python-pip
BuildRequires: rh-python36-python-pygments
BuildRequires: rh-python36-python3-openid
BuildRequires: rh-python36-pytz
BuildRequires: rh-python36-requests
BuildRequires: rh-python36-requests-futures
BuildRequires: rh-python36-requests-oauthlib
BuildRequires: rh-python36-scldevel
BuildRequires: rh-python36-six
BuildRequires: rh-python36-slackclient
BuildRequires: rh-python36-smmap2
BuildRequires: rh-python36-social-auth-app-django
BuildRequires: rh-python36-social-auth-core
BuildRequires: rh-python36-sqlparse
BuildRequires: rh-python36-tempora
BuildRequires: rh-python36-twilio
BuildRequires: rh-python36-txaio
BuildRequires: rh-python36-urllib3
BuildRequires: rh-python36-websocket_client
BuildRequires: rh-python36-zipp
BuildRequires: rh-python36-zope.interface
BuildRequires: xmlsec1-devel
BuildRequires: xmlsec1-openssl-devel

Requires: bubblewrap
Requires: curl
Requires: git
Requires: libcurl-devel
Requires: libffi-devel
Requires: libtool-ltdl-devel
Requires: libxslt-devel
Requires: openldap-devel
Requires: rh-postgresql10-postgresql-devel
Requires: rh-python36-Django
Requires: rh-python36-Django
Requires: rh-python36-PyHamcrest
Requires: rh-python36-PyJWT
Requires: rh-python36-PyYAML
Requires: rh-python36-Twisted
Requires: rh-python36-adal
Requires: rh-python36-ansible-runner
Requires: rh-python36-attrs
Requires: rh-python36-autobahn
Requires: rh-python36-azure-common
Requires: rh-python36-azure-keyvault
Requires: rh-python36-azure-nspkg
Requires: rh-python36-build
Requires: rh-python36-cachetools
Requires: rh-python36-celery
Requires: rh-python36-certifi
Requires: rh-python36-cffi
Requires: rh-python36-channels
Requires: rh-python36-chardet
Requires: rh-python36-constantly
Requires: rh-python36-cryptography
Requires: rh-python36-daphne
Requires: rh-python36-django-auth-ldap
Requires: rh-python36-django-cors-headers
Requires: rh-python36-django-crum
Requires: rh-python36-django-extensions
Requires: rh-python36-django-jsonfield
Requires: rh-python36-django-oauth-toolkit
Requires: rh-python36-django-pglocks
Requires: rh-python36-django-polymorphic
Requires: rh-python36-django-solo
Requires: rh-python36-django-taggit
Requires: rh-python36-djangorestframework
Requires: rh-python36-djangorestframework-yaml
Requires: rh-python36-gitdb2
Requires: rh-python36-GitPython
Requires: rh-python36-google-auth
Requires: rh-python36-idna
Requires: rh-python36-importlib_metadata
Requires: rh-python36-incremental
Requires: rh-python36-inflect
Requires: rh-python36-irc
Requires: rh-python36-isodate
Requires: rh-python36-jaraco.classes
Requires: rh-python36-jaraco.collections
Requires: rh-python36-jaraco.functools
Requires: rh-python36-jaraco.itertools
Requires: rh-python36-jaraco.logging
Requires: rh-python36-jaraco.stream
Requires: rh-python36-jaraco.text
Requires: rh-python36-jsonbfield
Requires: rh-python36-jsonschema
Requires: rh-python36-kombu
Requires: rh-python36-kubernetes
Requires: rh-python36-more-itertools
Requires: rh-python36-msrest
Requires: rh-python36-msrestazure
Requires: rh-python36-oauthlib
Requires: rh-python36-pexpect
Requires: rh-python36-psutil
Requires: rh-python36-psycopg2
Requires: rh-python36-ptyprocess
Requires: rh-python36-pyasn1
Requires: rh-python36-pyasn1-modules
Requires: rh-python36-pygerduty
Requires: rh-python36-pyparsing
Requires: rh-python36-pyrsistent
Requires: rh-python36-python
Requires: rh-python36-python
Requires: rh-python36-python-dateutil
Requires: rh-python36-python-devel
Requires: rh-python36-python-jinja2
Requires: rh-python36-python-jinja2
Requires: rh-python36-python-ldap
Requires: rh-python36-python-logstash
Requires: rh-python36-python-markupsafe
Requires: rh-python36-python-markupsafe
Requires: rh-python36-python-pip
Requires: rh-python36-python-pygments
Requires: rh-python36-python-pygments
Requires: rh-python36-python3-openid
Requires: rh-python36-pytz
Requires: rh-python36-requests
Requires: rh-python36-requests-futures
Requires: rh-python36-requests-oauthlib
Requires: rh-python36-runtime
Requires: rh-python36-scldevel
Requires: rh-python36-scldevel
Requires: rh-python36-six
Requires: rh-python36-slackclient
Requires: rh-python36-smmap2
Requires: rh-python36-social-auth-app-django
Requires: rh-python36-social-auth-core
Requires: rh-python36-tempora
Requires: rh-python36-twilio
Requires: rh-python36-txaio
Requires: rh-python36-urllib3
Requires: rh-python36-websocket_client
Requires: rh-python36-wheel
Requires: rh-python36-zipp
Requires: rh-python36-zope.interface
Requires: sshpass
Requires: subversion
Requires: xmlsec1-devel
Requires: xmlsec1-openssl-devel

Requires(pre): /usr/sbin/useradd, /usr/bin/getent
%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n awx-9.3.0

%install
# Setup build environment
mkdir -p $RPM_BUILD_ROOT/opt/rh/rh-python36/root/usr/
scl enable rh-python36 "pip3 install --root=$RPM_BUILD_ROOT ."

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
sed -i 's$/usr/bin/awx-python$/opt/rh/rh-python36/root/usr/bin/python3$g' $RPM_BUILD_ROOT/opt/rh/rh-python36/root/usr/bin/awx-manage

scl enable rh-python36 rh-postgresql10 "$RPM_BUILD_ROOT/opt/rh/rh-python36/root/usr/bin/awx-manage collectstatic --noinput --clear"

# Cleanup
unset PYTHONPATH
unset DJANGO_SETTINGS_MODULE

mkdir -p %{buildroot}%{service_homedir}
mkdir -p %{buildroot}%{service_logdir}
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}%{service_configdir}
mkdir -p %{buildroot}/var/lib/awx/
echo 9.3.0 > %{buildroot}%{service_homedir}/.tower_version


cp %{_sourcedir}/settings.py.dist %{buildroot}%{service_configdir}/settings.py
mv static %{buildroot}%{_prefix}/static

%if 0%{?el7}
# Install systemd configuration
mkdir -p %{buildroot}%{_unitdir}
for service in awx-cbreceiver awx-dispatcher awx-channels-worker awx-daphne awx-web awx; do
    cp %{_sourcedir}/${service}.service %{buildroot}%{_unitdir}/
done
%endif

# Create fake python executable
cat > %{buildroot}%{_prefix}/bin/python <<"EOF"
#!/bin/sh
export AWX_SETTINGS_FILE=/etc/tower/settings.py
exec scl enable rh-python36 "%{?el7:python3} \"$@\""
EOF

# Create Virtualenv folder
mkdir -p %{buildroot}/var/lib/awx/venv

# Install docs
cp %{_sourcedir}/nginx.conf.example ./

# Install VENV Script
cp %{_sourcedir}/awx-create-venv $RPM_BUILD_ROOT/opt/rh/rh-python36/root/usr/bin/
mkdir -p $RPM_BUILD_ROOT/usr/bin/
ln -s /opt/rh/rh-python36/root/usr/bin/awx-create-venv $RPM_BUILD_ROOT/usr/bin/awx-create-venv
mkdir -p $RPM_BUILD_ROOT%{service_homedir}/venv

cp %{_sourcedir}/awx-rpm-logo.svg $RPM_BUILD_ROOT/opt/awx/static/assets/awx-rpm-logo.svg
mv $RPM_BUILD_ROOT/opt/awx/static/assets/logo-header.svg $RPM_BUILD_ROOT/opt/awx/static/assets/logo-header.svg.orig
mv $RPM_BUILD_ROOT/opt/awx/static/assets/logo-login.svg $RPM_BUILD_ROOT/opt/awx/static/assets/logo-login.svg.orig
ln -s /opt/awx/static/assets/awx-rpm-logo.svg $RPM_BUILD_ROOT/opt/awx/static/assets/logo-header.svg
ln -s /opt/awx/static/assets/awx-rpm-logo.svg $RPM_BUILD_ROOT/opt/awx/static/assets/logo-login.svg

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /bin/bash %{service_user}
/usr/sbin/usermod -s /bin/bash %{service_user}

%post
%if 0%{?el7}
%systemd_post awx-cbreceiver
%systemd_post awx-dispatcher
%systemd_post awx-channels-worker
%systemd_post awx-daphne
%systemd_post awx-web
%endif
ln -sfn /opt/rh/rh-python36/root /var/lib/awx/venv/awx

%preun
%if 0%{?el7}
%systemd_preun awx-cbreceiver
%systemd_preun awx-dispatcher
%systemd_preun awx-channels-worker
%systemd_preun awx-daphne
%systemd_preun awx-web
%endif

%postun
%if 0%{?el7}
%systemd_postun awx-cbreceiver
%systemd_postun awx-dispatcher
%systemd_postun awx-channels-worker
%systemd_postun awx-daphne
%systemd_postun awx-web
%endif

%clean

%files
%defattr(0644, awx, awx, 0755)
%doc nginx.conf.example
%attr(0755, root, root) /opt/rh/rh-python36/root/usr/bin/awx-manage
%attr(0755, root, root) /opt/rh/rh-python36/root/usr/bin/awx-create-venv
/usr/bin/awx-create-venv
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/awx
%attr(0755, root, root) /opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/awx/plugins/*/*.py
%attr(0755, awx, awx) %{_prefix}/static
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}/venv
%{service_homedir}/.tower_version
%dir %attr(0770, %{service_user}, %{service_group}) %{service_logdir}
%config %{service_configdir}/settings.py
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/awx-*.egg-info/
/usr/share/doc/awx/
/opt/awx/bin/python
/usr/bin/ansible-tower-service
/usr/bin/ansible-tower-setup
/usr/bin/awx-python
/usr/bin/failure-event-handler
/usr/share/awx
/usr/share/sosreport/sos/plugins/tower.py
/var/lib/awx/favicon.ico
/var/lib/awx/wsgi.py


%if 0%{?el7}
%attr(0644, root, root) %{_unitdir}/awx-cbreceiver.service
%attr(0644, root, root) %{_unitdir}/awx-dispatcher.service
%attr(0644, root, root) %{_unitdir}/awx-channels-worker.service
%attr(0644, root, root) %{_unitdir}/awx-daphne.service
%attr(0644, root, root) %{_unitdir}/awx-web.service
%attr(0644, root, root) %{_unitdir}/awx.service
%endif

%changelog
* Mon Mar 23 2020 08:22:09 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 07:52:03 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 07:22:00 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 06:51:56 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 06:21:50 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 05:52:16 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 05:22:12 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 04:52:07 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 04:22:03 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 03:52:03 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 03:21:59 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 02:51:55 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 02:21:50 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 01:52:23 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 01:22:12 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 00:52:10 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Mon Mar 23 2020 00:22:02 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 23:51:59 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 23:21:52 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 22:51:47 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 22:22:13 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 21:52:09 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 21:22:04 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 20:52:00 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 20:21:55 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 19:51:52 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 19:21:47 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 18:52:13 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 18:22:11 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 17:52:04 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 17:22:00 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 16:51:57 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 16:21:55 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 15:52:14 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 15:22:10 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 14:52:06 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 14:22:02 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 13:51:57 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 13:21:52 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 12:51:47 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 12:22:14 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 11:52:09 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 11:22:05 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 10:52:00 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 10:21:56 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 09:51:52 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 09:22:17 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 08:52:14 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 08:22:08 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 07:52:04 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 07:22:00 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 06:51:55 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 06:21:51 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 05:52:17 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 05:22:12 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 04:52:09 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 04:22:04 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 03:52:01 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 03:21:56 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 02:51:51 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 02:22:18 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 01:52:22 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 01:22:09 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 00:52:07 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sun Mar 22 2020 00:22:00 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 23:51:56 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 23:21:51 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 22:52:17 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 22:22:12 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 21:52:08 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 21:22:04 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 20:52:00 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 20:21:55 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 19:51:50 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 19:22:16 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 18:52:12 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 18:22:09 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 17:52:03 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 17:21:58 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 16:51:55 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 16:21:49 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 15:52:15 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 15:22:11 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 14:52:07 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 14:22:03 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 13:51:57 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 13:21:53 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 12:51:48 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 12:22:14 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 11:52:10 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
* Sat Mar 21 2020 11:25:56 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.213
- New Git version build: 9.3.0.213
* Sat Mar 21 2020 10:52:01 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 10:21:58 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 09:51:52 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 09:22:17 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 08:52:15 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 08:22:08 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 07:52:08 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 07:22:01 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 06:51:55 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 06:21:52 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 05:52:17 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 05:22:12 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 04:52:09 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 04:22:04 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 03:52:00 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 03:21:57 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 02:51:52 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 02:22:19 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
* Sat Mar 21 2020 01:55:49 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.208
- New Git version build: 9.3.0.208
* Sat Mar 21 2020 01:22:16 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.206
* Sat Mar 21 2020 00:55:44 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.206
- New Git version build: 9.3.0.206
* Sat Mar 21 2020 00:21:59 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.202
* Fri Mar 20 2020 23:51:55 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.202
* Fri Mar 20 2020 23:21:49 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.202
* Fri Mar 20 2020 22:52:15 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.202
* Fri Mar 20 2020 22:22:11 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.202
* Fri Mar 20 2020 21:52:07 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.202
* Fri Mar 20 2020 21:25:28 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.202
- New Git version build: 9.3.0.202
* Fri Mar 20 2020 20:51:58 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.197
* Fri Mar 20 2020 20:25:30 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.197
- New Git version build: 9.3.0.197
* Fri Mar 20 2020 19:51:49 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.193
* Fri Mar 20 2020 19:25:42 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.193
- New Git version build: 9.3.0.193
* Fri Mar 20 2020 18:52:14 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.183
* Fri Mar 20 2020 18:25:32 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.183
- New Git version build: 9.3.0.183
* Fri Mar 20 2020 17:52:01 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.181
* Fri Mar 20 2020 17:21:57 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.181
* Fri Mar 20 2020 16:51:54 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.181
* Fri Mar 20 2020 16:21:49 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.181
* Fri Mar 20 2020 15:52:14 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.181
* Fri Mar 20 2020 15:25:47 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.181
- New Git version build: 9.3.0.181
* Fri Mar 20 2020 14:52:05 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.176
* Fri Mar 20 2020 14:22:03 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.176
* Fri Mar 20 2020 13:55:36 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.176
- New Git version build: 9.3.0.176
* Fri Mar 20 2020 13:25:33 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.172
- New Git version build: 9.3.0.172
* Fri Mar 20 2020 12:51:48 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 12:22:14 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 11:52:10 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 11:22:06 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 10:52:02 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 10:21:57 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 09:51:51 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 09:22:17 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 08:52:13 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 08:22:08 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 07:52:03 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 07:22:00 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 06:51:54 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 06:21:50 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 05:52:17 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 05:22:12 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 04:52:07 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 04:22:04 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 03:52:03 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 03:21:58 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 02:51:55 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 02:21:50 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 01:52:26 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 01:22:17 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 00:52:09 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Fri Mar 20 2020 00:22:03 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Thu Mar 19 2020 23:51:57 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Thu Mar 19 2020 23:21:53 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Thu Mar 19 2020 22:51:49 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Thu Mar 19 2020 22:22:14 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Thu Mar 19 2020 21:52:11 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Thu Mar 19 2020 21:22:05 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
* Thu Mar 19 2020 20:55:36 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.166
- New Git version build: 9.3.0.166
* Thu Mar 19 2020 20:25:32 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.164
- New Git version build: 9.3.0.164
* Thu Mar 19 2020 19:55:13 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.162
- New Git version build: 9.3.0.162
* Thu Mar 19 2020 19:25:33 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.159
- New Git version build: 9.3.0.159
* Thu Mar 19 2020 18:52:14 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.157
* Thu Mar 19 2020 18:22:09 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.157
* Thu Mar 19 2020 17:55:27 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.157
- New Git version build: 9.3.0.157
* Thu Mar 19 2020 17:22:00 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.155
* Thu Mar 19 2020 16:51:55 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.155
* Thu Mar 19 2020 16:21:51 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.155
* Thu Mar 19 2020 15:55:47 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.155
- New Git version build: 9.3.0.155
* Thu Mar 19 2020 15:22:12 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.153
* Thu Mar 19 2020 14:52:07 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.153
* Thu Mar 19 2020 14:25:42 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.153
- New Git version build: 9.3.0.153
* Thu Mar 19 2020 13:51:58 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 13:21:57 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 12:51:49 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 12:22:16 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 11:52:11 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 11:22:06 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 10:52:01 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 10:21:57 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 09:51:52 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 09:22:18 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 08:52:14 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 08:22:10 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 07:52:05 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 07:22:01 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 06:51:56 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 06:21:51 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 05:52:18 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 05:22:16 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 04:52:08 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 04:22:05 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 03:52:02 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 03:21:55 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 02:51:50 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 02:22:18 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 01:52:26 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 01:22:12 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 00:52:05 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Thu Mar 19 2020 00:21:57 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Wed Mar 18 2020 23:51:54 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Wed Mar 18 2020 23:21:48 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Wed Mar 18 2020 22:52:15 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Wed Mar 18 2020 22:22:11 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Wed Mar 18 2020 21:52:06 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
* Wed Mar 18 2020 21:25:27 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.146
- New Git version build: 9.3.0.146
* Wed Mar 18 2020 19:55:16 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.104
- New Git version build: 9.3.0.104
* Wed Mar 18 2020 18:25:33 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.98
- New Git version build: 9.3.0.98
* Wed Mar 18 2020 17:55:26 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.96
- New Git version build: 9.3.0.96
* Wed Mar 18 2020 16:25:56 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.92
- New Git version build: 9.3.0.92
* Wed Mar 18 2020 15:25:42 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.90
- New Git version build: 9.3.0.90
* Wed Mar 18 2020 14:55:32 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.88
- New Git version build: 9.3.0.88
* Wed Mar 18 2020 03:25:30 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.86
- New Git version build: 9.3.0.86
* Wed Mar 18 2020 02:25:45 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.83
- New Git version build: 9.3.0.83
* Wed Mar 18 2020 01:25:40 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.81
- New Git version build: 9.3.0.81
* Tue Mar 17 2020 23:25:38 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.79
- New Git version build: 9.3.0.79
* Tue Mar 17 2020 21:55:27 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.77
- New Git version build: 9.3.0.77
* Tue Mar 17 2020 20:55:11 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.75
- New Git version build: 9.3.0.75
* Tue Mar 17 2020 19:55:50 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.73
- New Git version build: 9.3.0.73
* Tue Mar 17 2020 17:55:27 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.71
- New Git version build: 9.3.0.71
* Tue Mar 17 2020 16:55:25 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.69
- New Git version build: 9.3.0.69
* Mon Mar 16 2020 20:55:21 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.67
- New Git version build: 9.3.0.67
* Mon Mar 16 2020 20:25:14 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.65
- New Git version build: 9.3.0.65
* Mon Mar 16 2020 19:25:35 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.55
- New Git version build: 9.3.0.55
* Mon Mar 16 2020 18:55:39 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.48
- New Git version build: 9.3.0.48
* Fri Mar 13 2020 22:55:16 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.42
- New Git version build: 9.3.0.42
* Fri Mar 13 2020 22:25:14 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.38
- New Git version build: 9.3.0.38
* Fri Mar 13 2020 21:25:09 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.23
- New Git version build: 9.3.0.23
* Fri Mar 13 2020 19:55:37 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.21
- New Git version build: 9.3.0.21
* Fri Mar 13 2020 17:25:28 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.12
- New Git version build: 9.3.0.12
* Fri Mar 13 2020 16:55:41 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.9
- New Git version build: 9.3.0.9
* Thu Mar 12 2020 19:55:26 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.7
- New Git version build: 9.3.0.7
* Thu Mar 12 2020 19:25:21 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.2
- New Git version build: 9.3.0.2
* Thu Mar 12 2020 17:25:10 +0000 Martin Juhl <mj@casalogic.dk> 9.3.0.0
- New Git version build: 9.3.0.0
* Wed Mar 11 2020 18:25:21 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.456
- New Git version build: 9.2.0.456
* Wed Mar 11 2020 16:54:18 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.435
- New Git version build: 9.2.0.435
* Wed Mar 11 2020 13:25:38 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.433
- New Git version build: 9.2.0.433
* Wed Mar 11 2020 00:25:20 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.431
- New Git version build: 9.2.0.431
* Tue Mar 10 2020 23:25:29 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.429
- New Git version build: 9.2.0.429
* Tue Mar 10 2020 22:25:53 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.426
- New Git version build: 9.2.0.426
* Mon Mar 09 2020 23:55:35 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.409
- New Git version build: 9.2.0.409
* Mon Mar 09 2020 21:25:42 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.407
- New Git version build: 9.2.0.407
* Mon Mar 09 2020 20:55:38 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.405
- New Git version build: 9.2.0.405
* Mon Mar 09 2020 20:25:28 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.403
- New Git version build: 9.2.0.403
* Mon Mar 09 2020 18:55:16 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.400
- New Git version build: 9.2.0.400
* Mon Mar 09 2020 17:55:46 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.398
- New Git version build: 9.2.0.398
* Mon Mar 09 2020 13:55:34 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.396
- New Git version build: 9.2.0.396
* Fri Mar 06 2020 22:25:05 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.391
- New Git version build: 9.2.0.391
* Fri Mar 06 2020 21:25:27 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.385
- New Git version build: 9.2.0.385
* Fri Mar 06 2020 20:55:19 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.383
- New Git version build: 9.2.0.383
* Fri Mar 06 2020 20:25:14 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.376
- New Git version build: 9.2.0.376
* Fri Mar 06 2020 17:25:16 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.372
- New Git version build: 9.2.0.372
* Fri Mar 06 2020 15:55:40 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.368
- New Git version build: 9.2.0.368
* Fri Mar 06 2020 14:55:27 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.366
- New Git version build: 9.2.0.366
* Thu Mar 05 2020 23:55:22 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.364
- New Git version build: 9.2.0.364
* Thu Mar 05 2020 20:55:31 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.362
- New Git version build: 9.2.0.362
* Thu Mar 05 2020 19:52:00 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.358
* Thu Mar 05 2020 19:25:20 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.358
- New Git version build: 9.2.0.358
* Thu Mar 05 2020 15:55:12 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.356
- New Git version build: 9.2.0.356
* Wed Mar 04 2020 23:25:20 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.354
- New Git version build: 9.2.0.354
* Wed Mar 04 2020 19:25:10 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.351
- New Git version build: 9.2.0.351
* Wed Mar 04 2020 18:25:37 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.343
- New Git version build: 9.2.0.343
* Wed Mar 04 2020 16:55:27 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.341
- New Git version build: 9.2.0.341
* Wed Mar 04 2020 15:25:37 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.326
- New Git version build: 9.2.0.326
* Wed Mar 04 2020 00:55:35 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.324
- New Git version build: 9.2.0.324
* Wed Mar 04 2020 00:25:30 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.322
- New Git version build: 9.2.0.322
* Tue Mar 03 2020 22:55:34 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.320
- New Git version build: 9.2.0.320
* Tue Mar 03 2020 22:25:08 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.318
- New Git version build: 9.2.0.318
* Tue Mar 03 2020 21:55:35 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.316
- New Git version build: 9.2.0.316
* Tue Mar 03 2020 21:25:27 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.313
- New Git version build: 9.2.0.313
* Tue Mar 03 2020 20:55:23 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.311
- New Git version build: 9.2.0.311
* Tue Mar 03 2020 19:55:17 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.306
- New Git version build: 9.2.0.306
* Tue Mar 03 2020 18:55:45 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.304
- New Git version build: 9.2.0.304
* Tue Mar 03 2020 18:25:34 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.300
- New Git version build: 9.2.0.300
* Tue Mar 03 2020 16:25:12 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.298
- New Git version build: 9.2.0.298
* Mon Mar 02 2020 18:55:16 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.296
- New Git version build: 9.2.0.296
* Mon Mar 02 2020 16:55:55 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.294
- New Git version build: 9.2.0.294
* Mon Mar 02 2020 15:55:16 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.287
- New Git version build: 9.2.0.287
* Fri Feb 28 2020 21:25:48 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.285
- New Git version build: 9.2.0.285
* Fri Feb 28 2020 20:25:24 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.283
- New Git version build: 9.2.0.283
* Fri Feb 28 2020 17:25:27 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.281
- New Git version build: 9.2.0.281
* Fri Feb 28 2020 14:25:26 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.278
- New Git version build: 9.2.0.278
* Fri Feb 28 2020 00:55:47 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.276
- New Git version build: 9.2.0.276
* Fri Feb 28 2020 00:25:30 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.274
- New Git version build: 9.2.0.274
* Thu Feb 27 2020 22:25:12 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.272
- New Git version build: 9.2.0.272
* Thu Feb 27 2020 21:25:41 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.269
- New Git version build: 9.2.0.269
* Thu Feb 27 2020 09:25:10 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.267
- New Git version build: 9.2.0.267
* Wed Feb 26 2020 22:55:05 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.261
- New Git version build: 9.2.0.261
* Wed Feb 26 2020 20:55:36 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.258
- New Git version build: 9.2.0.258
* Wed Feb 26 2020 20:25:28 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.212
- New Git version build: 9.2.0.212
* Wed Feb 26 2020 19:25:11 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.208
- New Git version build: 9.2.0.208
* Wed Feb 26 2020 14:25:35 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.202
- New Git version build: 9.2.0.202
* Wed Feb 26 2020 13:25:27 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.200
- New Git version build: 9.2.0.200
* Tue Feb 25 2020 23:25:38 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.198
- New Git version build: 9.2.0.198
* Tue Feb 25 2020 21:25:33 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.191
- New Git version build: 9.2.0.191
* Tue Feb 25 2020 20:25:34 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.189
- New Git version build: 9.2.0.189
* Tue Feb 25 2020 16:55:24 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.187
- New Git version build: 9.2.0.187
* Tue Feb 25 2020 14:55:38 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.185
- New Git version build: 9.2.0.185
* Tue Feb 25 2020 14:25:28 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.180
- New Git version build: 9.2.0.180
* Mon Feb 24 2020 18:25:39 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.175
- New Git version build: 9.2.0.175
* Mon Feb 24 2020 15:25:50 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.173
- New Git version build: 9.2.0.173
* Mon Feb 24 2020 14:55:44 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.168
- New Git version build: 9.2.0.168
* Sat Feb 22 2020 13:25:29 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.164
- New Git version build: 9.2.0.164
* Fri Feb 21 2020 21:55:13 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.162
- New Git version build: 9.2.0.162
* Fri Feb 21 2020 20:55:30 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.160
- New Git version build: 9.2.0.160
* Fri Feb 21 2020 20:25:34 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.155
- New Git version build: 9.2.0.155
* Fri Feb 21 2020 17:55:32 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.135
- New Git version build: 9.2.0.135
* Fri Feb 21 2020 17:25:47 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.133
- New Git version build: 9.2.0.133
* Fri Feb 21 2020 15:55:08 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.131
- New Git version build: 9.2.0.131
* Thu Feb 20 2020 23:55:23 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.127
- New Git version build: 9.2.0.127
* Thu Feb 20 2020 23:25:29 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.125
- New Git version build: 9.2.0.125
* Thu Feb 20 2020 19:55:23 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.119
- New Git version build: 9.2.0.119
* Thu Feb 20 2020 14:25:31 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.107
- New Git version build: 9.2.0.107
* Wed Feb 19 2020 22:25:17 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.105
- New Git version build: 9.2.0.105
* Wed Feb 19 2020 19:55:22 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.103
- New Git version build: 9.2.0.103
* Wed Feb 19 2020 19:25:26 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.96
- New Git version build: 9.2.0.96
* Wed Feb 19 2020 17:25:30 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.92
- New Git version build: 9.2.0.92
* Wed Feb 19 2020 16:55:23 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.90
- New Git version build: 9.2.0.90
* Tue Feb 18 2020 16:55:34 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.85
- New Git version build: 9.2.0.85
* Tue Feb 18 2020 16:25:37 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.80
- New Git version build: 9.2.0.80
* Mon Feb 17 2020 19:25:24 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.77
- New Git version build: 9.2.0.77
* Mon Feb 17 2020 16:25:21 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.30
- New Git version build: 9.2.0.30
* Fri Feb 14 2020 18:55:27 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.28
- New Git version build: 9.2.0.28
* Thu Feb 13 2020 21:25:43 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.23
- New Git version build: 9.2.0.23
* Thu Feb 13 2020 20:25:24 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.19
- New Git version build: 9.2.0.19
* Thu Feb 13 2020 19:55:27 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.16
- New Git version build: 9.2.0.16
* Thu Feb 13 2020 16:25:29 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.14
- New Git version build: 9.2.0.14
* Thu Feb 13 2020 14:25:44 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.12
- New Git version build: 9.2.0.12
* Wed Feb 12 2020 21:55:35 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.10
- New Git version build: 9.2.0.10
* Wed Feb 12 2020 16:25:22 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.2
- New Git version build: 9.2.0.2
* Tue Feb 11 2020 22:26:00 +0000 Martin Juhl <mj@casalogic.dk> 9.2.0.0
- New Git version build: 9.2.0.0
* Tue Feb 11 2020 21:25:45 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.313
- New Git version build: 9.1.1.313
* Tue Feb 11 2020 19:26:05 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.311
- New Git version build: 9.1.1.311
* Tue Feb 11 2020 18:26:01 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.309
- New Git version build: 9.1.1.309
* Tue Feb 11 2020 16:55:46 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.305
- New Git version build: 9.1.1.305
* Tue Feb 11 2020 15:26:02 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.303
- New Git version build: 9.1.1.303
* Tue Feb 11 2020 14:55:36 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.301
- New Git version build: 9.1.1.301
* Tue Feb 11 2020 14:25:42 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.299
- New Git version build: 9.1.1.299
* Tue Feb 11 2020 03:26:23 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.297
- New Git version build: 9.1.1.297
* Tue Feb 11 2020 01:25:53 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.295
- New Git version build: 9.1.1.295
* Mon Feb 10 2020 23:55:47 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.281
- New Git version build: 9.1.1.281
* Mon Feb 10 2020 23:25:47 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.277
- New Git version build: 9.1.1.277
* Mon Feb 10 2020 22:55:49 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.275
- New Git version build: 9.1.1.275
* Mon Feb 10 2020 18:25:34 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.273
- New Git version build: 9.1.1.273
* Mon Feb 10 2020 16:55:31 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.271
- New Git version build: 9.1.1.271
* Mon Feb 10 2020 15:55:49 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.269
- New Git version build: 9.1.1.269
* Sun Feb 09 2020 14:25:56 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.267
- New Git version build: 9.1.1.267
* Fri Feb 07 2020 20:26:04 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.259
- New Git version build: 9.1.1.259
* Fri Feb 07 2020 19:25:52 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.257
- New Git version build: 9.1.1.257
* Fri Feb 07 2020 14:26:18 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.255
- New Git version build: 9.1.1.255
* Thu Feb 06 2020 21:55:46 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.253
- New Git version build: 9.1.1.253
* Thu Feb 06 2020 17:55:49 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.247
- New Git version build: 9.1.1.247
* Thu Feb 06 2020 15:55:37 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.245
- New Git version build: 9.1.1.245
* Wed Feb 05 2020 23:55:40 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.220
- New Git version build: 9.1.1.220
* Wed Feb 05 2020 23:25:39 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.213
- New Git version build: 9.1.1.213
* Wed Feb 05 2020 16:25:55 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.211
- New Git version build: 9.1.1.211
* Wed Feb 05 2020 15:25:32 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.209
- New Git version build: 9.1.1.209
* Wed Feb 05 2020 14:55:37 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.207
- New Git version build: 9.1.1.207
* Wed Feb 05 2020 00:26:04 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.205
- New Git version build: 9.1.1.205
* Tue Feb 04 2020 13:26:04 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.203
- New Git version build: 9.1.1.203
* Tue Feb 04 2020 03:26:00 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.201
- New Git version build: 9.1.1.201
* Mon Feb 03 2020 20:55:49 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.196
- New Git version build: 9.1.1.196
* Mon Feb 03 2020 17:55:48 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.194
- New Git version build: 9.1.1.194
* Mon Feb 03 2020 16:55:46 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.188
- New Git version build: 9.1.1.188
* Mon Feb 03 2020 14:55:57 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.185
- New Git version build: 9.1.1.185
* Fri Jan 31 2020 13:55:52 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.182
- New Git version build: 9.1.1.182
* Thu Jan 30 2020 22:25:53 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.180
- New Git version build: 9.1.1.180
* Wed Jan 29 2020 19:56:03 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.178
- New Git version build: 9.1.1.178
* Tue Jan 28 2020 22:26:38 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.176
- New Git version build: 9.1.1.176
* Tue Jan 28 2020 21:25:50 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.174
- New Git version build: 9.1.1.174
* Tue Jan 28 2020 20:55:49 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.172
- New Git version build: 9.1.1.172
* Tue Jan 28 2020 17:56:06 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.169
- New Git version build: 9.1.1.169
* Tue Jan 28 2020 15:26:01 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.167
- New Git version build: 9.1.1.167
* Tue Jan 28 2020 13:26:02 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.165
- New Git version build: 9.1.1.165
* Tue Jan 28 2020 04:25:54 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.163
- New Git version build: 9.1.1.163
* Mon Jan 27 2020 21:26:02 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.161
- New Git version build: 9.1.1.161
* Mon Jan 27 2020 20:25:55 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.158
- New Git version build: 9.1.1.158
* Mon Jan 27 2020 17:56:24 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.156
- New Git version build: 9.1.1.156
* Mon Jan 27 2020 15:26:01 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.154
- New Git version build: 9.1.1.154
* Fri Jan 24 2020 22:55:38 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.146
- New Git version build: 9.1.1.146
* Fri Jan 24 2020 19:55:50 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.144
- New Git version build: 9.1.1.144
* Fri Jan 24 2020 14:55:53 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.140
- New Git version build: 9.1.1.140
* Thu Jan 23 2020 22:25:45 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.138
- New Git version build: 9.1.1.138
* Thu Jan 23 2020 22:12:04 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.136
* Thu Jan 23 2020 21:22:12 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.136
* Thu Jan 23 2020 20:55:39 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.136
- New Git version build: 9.1.1.136
* Thu Jan 23 2020 20:25:50 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.133
- New Git version build: 9.1.1.133
* Thu Jan 23 2020 19:52:13 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.129
* Thu Jan 23 2020 19:26:00 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.129
- New Git version build: 9.1.1.129
* Thu Jan 23 2020 18:56:09 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.127
- New Git version build: 9.1.1.127
* Thu Jan 23 2020 18:22:11 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 17:52:11 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 17:22:11 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 16:52:11 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 16:22:13 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 15:52:13 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 15:22:10 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 14:52:10 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 14:22:10 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 13:52:10 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 13:22:10 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 12:52:10 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 12:22:10 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 11:52:10 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 11:22:10 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 10:52:09 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 10:22:10 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 09:52:08 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 09:22:10 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 08:52:10 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 08:22:08 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 07:52:08 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 07:22:08 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 06:52:07 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 06:22:07 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 05:52:07 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 05:22:07 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 04:52:06 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 04:22:07 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 03:52:07 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 03:22:06 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 02:52:07 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 02:22:06 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 01:52:13 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 01:22:13 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 00:52:06 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Thu Jan 23 2020 00:22:06 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Wed Jan 22 2020 23:52:08 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Wed Jan 22 2020 23:22:16 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
* Wed Jan 22 2020 22:55:36 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.123
- New Git version build: 9.1.1.123
* Wed Jan 22 2020 22:25:38 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.121
- New Git version build: 9.1.1.121
* Wed Jan 22 2020 21:55:54 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.119
- New Git version build: 9.1.1.119
* Wed Jan 22 2020 17:25:59 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.117
- New Git version build: 9.1.1.117
* Wed Jan 22 2020 16:26:06 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.115
- New Git version build: 9.1.1.115
* Wed Jan 22 2020 15:25:46 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.113
- New Git version build: 9.1.1.113
* Wed Jan 22 2020 14:55:45 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.111
- New Git version build: 9.1.1.111
* Tue Jan 21 2020 21:55:51 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.108
- New Git version build: 9.1.1.108
* Tue Jan 21 2020 20:56:00 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.106
- New Git version build: 9.1.1.106
* Tue Jan 21 2020 19:26:13 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.104
- New Git version build: 9.1.1.104
* Tue Jan 21 2020 18:26:05 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.102
- New Git version build: 9.1.1.102
* Tue Jan 21 2020 16:26:01 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.96
- New Git version build: 9.1.1.96
* Mon Jan 20 2020 23:55:55 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.94
- New Git version build: 9.1.1.94
* Mon Jan 20 2020 19:25:53 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.92
- New Git version build: 9.1.1.92
* Mon Jan 20 2020 18:55:56 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.90
- New Git version build: 9.1.1.90
* Mon Jan 20 2020 17:25:55 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.88
- New Git version build: 9.1.1.88
* Mon Jan 20 2020 14:25:50 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.86
- New Git version build: 9.1.1.86
* Fri Jan 17 2020 23:55:35 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.84
- New Git version build: 9.1.1.84
* Fri Jan 17 2020 22:55:15 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.79
- New Git version build: 9.1.1.79
* Fri Jan 17 2020 21:55:56 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.77
- New Git version build: 9.1.1.77
* Fri Jan 17 2020 20:55:32 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.71
- New Git version build: 9.1.1.71
* Fri Jan 17 2020 19:55:40 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.69
- New Git version build: 9.1.1.69
* Fri Jan 17 2020 18:25:41 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.64
- New Git version build: 9.1.1.64
* Fri Jan 17 2020 15:25:49 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.56
- New Git version build: 9.1.1.56
* Fri Jan 17 2020 13:55:43 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.50
- New Git version build: 9.1.1.50
* Thu Jan 16 2020 21:55:53 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.48
- New Git version build: 9.1.1.48
* Thu Jan 16 2020 16:55:38 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.46
- New Git version build: 9.1.1.46
* Thu Jan 16 2020 15:25:40 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.43
- New Git version build: 9.1.1.43
* Thu Jan 16 2020 14:25:33 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.41
- New Git version build: 9.1.1.41
* Thu Jan 16 2020 00:25:38 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.37
- New Git version build: 9.1.1.37
* Wed Jan 15 2020 22:55:25 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.35
- New Git version build: 9.1.1.35
* Wed Jan 15 2020 21:25:29 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.33
- New Git version build: 9.1.1.33
* Wed Jan 15 2020 20:25:35 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.31
- New Git version build: 9.1.1.31
* Wed Jan 15 2020 19:55:11 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.19
- New Git version build: 9.1.1.19
* Wed Jan 15 2020 19:25:50 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.17
- New Git version build: 9.1.1.17
* Wed Jan 15 2020 17:25:22 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.13
- New Git version build: 9.1.1.13
* Wed Jan 15 2020 16:55:25 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.11
- New Git version build: 9.1.1.11
* Wed Jan 15 2020 08:14:00 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 07:22:12 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 06:52:11 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 06:22:09 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 05:52:09 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 05:22:09 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 04:52:08 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 04:22:08 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 03:51:54 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 03:21:55 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 02:51:54 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 02:21:55 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 01:52:00 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 01:22:04 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 00:51:53 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Wed Jan 15 2020 00:21:53 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Tue Jan 14 2020 23:51:53 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Tue Jan 14 2020 23:21:54 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Tue Jan 14 2020 22:51:53 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Tue Jan 14 2020 22:21:53 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
* Tue Jan 14 2020 21:55:06 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.9
- New Git version build: 9.1.1.9
* Tue Jan 14 2020 21:21:54 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.6
* Tue Jan 14 2020 20:55:01 +0000 Martin Juhl <mj@casalogic.dk> 9.1.1.6
- New Git version build: 9.1.1.6
* Tue Jan 14 2020 20:25:09 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.135
- New Git version build: 9.1.0.135
* Tue Jan 14 2020 19:55:05 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.133
- New Git version build: 9.1.0.133
* Tue Jan 14 2020 19:21:52 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.131
* Tue Jan 14 2020 18:51:52 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.131
* Tue Jan 14 2020 18:21:53 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.131
* Tue Jan 14 2020 17:55:00 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.131
- New Git version build: 9.1.0.131
* Tue Jan 14 2020 13:03:00 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.129
- New Git version build: 9.1.0.129
* Mon Jan 13 2020 23:22:06 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.127
* Mon Jan 13 2020 22:55:13 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.127
- New Git version build: 9.1.0.127
* Mon Jan 13 2020 22:22:05 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.125
* Mon Jan 13 2020 21:55:11 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.125
- New Git version build: 9.1.0.125
* Mon Jan 13 2020 21:22:04 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.121
* Mon Jan 13 2020 20:52:04 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.121
* Mon Jan 13 2020 20:22:05 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.121
* Mon Jan 13 2020 19:55:22 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.121
- New Git version build: 9.1.0.121
* Mon Jan 13 2020 19:22:04 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.119
* Mon Jan 13 2020 18:52:03 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.119
* Mon Jan 13 2020 18:22:03 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.119
* Mon Jan 13 2020 17:52:04 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.119
* Mon Jan 13 2020 17:25:24 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.119
- New Git version build: 9.1.0.119
* Mon Jan 13 2020 16:52:04 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.117
* Mon Jan 13 2020 16:25:07 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.117
- New Git version build: 9.1.0.117
* Fri Jan 10 2020 21:55:14 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.98
- New Git version build: 9.1.0.98
* Fri Jan 10 2020 19:25:08 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.96
- New Git version build: 9.1.0.96
* Fri Jan 10 2020 18:55:33 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.94
- New Git version build: 9.1.0.94
* Thu Jan 09 2020 22:25:18 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.84
- New Git version build: 9.1.0.84
* Thu Jan 09 2020 15:25:19 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.75
- New Git version build: 9.1.0.75
* Wed Jan 08 2020 20:55:13 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.73
- New Git version build: 9.1.0.73
* Wed Jan 08 2020 18:55:18 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.71
- New Git version build: 9.1.0.71
* Wed Jan 08 2020 14:55:11 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.67
- New Git version build: 9.1.0.67
* Tue Jan 07 2020 16:55:18 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.65
- New Git version build: 9.1.0.65
* Mon Jan 06 2020 14:55:32 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.63
- New Git version build: 9.1.0.63
* Mon Jan 06 2020 04:25:12 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.58
- New Git version build: 9.1.0.58
* Fri Jan 03 2020 15:55:12 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.56
- New Git version build: 9.1.0.56
* Fri Jan 03 2020 14:55:25 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.54
- New Git version build: 9.1.0.54
* Thu Jan 02 2020 18:55:24 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.52
- New Git version build: 9.1.0.52
* Thu Jan 02 2020 15:25:19 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.50
- New Git version build: 9.1.0.50
* Thu Jan 02 2020 14:25:21 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.47
- New Git version build: 9.1.0.47
* Fri Dec 20 2019 21:55:34 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.45
- New Git version build: 9.1.0.45
* Fri Dec 20 2019 18:55:38 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.43
- New Git version build: 9.1.0.43
* Thu Dec 19 2019 21:25:34 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.41
- New Git version build: 9.1.0.41
* Thu Dec 19 2019 20:25:39 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.36
- New Git version build: 9.1.0.36
* Thu Dec 19 2019 18:55:38 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.22
- New Git version build: 9.1.0.22
* Thu Dec 19 2019 15:55:31 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.20
- New Git version build: 9.1.0.20
* Thu Dec 19 2019 14:25:27 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.18
- New Git version build: 9.1.0.18
* Thu Dec 19 2019 10:23:11 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.16
- New Git version build: 9.1.0.16
* Tue Dec 17 2019 20:25:36 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.4
- New Git version build: 9.1.0.4
* Tue Dec 17 2019 19:25:15 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.2
- New Git version build: 9.1.0.2
* Tue Dec 17 2019 16:55:00 +0000 Martin Juhl <mj@casalogic.dk> 9.1.0.0
- New Git version build: 9.1.0.0
* Tue Dec 17 2019 00:25:16 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.451
- New Git version build: 9.0.1.451
* Mon Dec 16 2019 23:55:08 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.449
- New Git version build: 9.0.1.449
* Mon Dec 16 2019 23:25:08 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.447
- New Git version build: 9.0.1.447
* Mon Dec 16 2019 20:25:16 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.445
- New Git version build: 9.0.1.445
* Mon Dec 16 2019 17:55:16 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.443
- New Git version build: 9.0.1.443
* Mon Dec 16 2019 17:25:22 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.385
- New Git version build: 9.0.1.385
* Mon Dec 16 2019 16:25:16 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.383
- New Git version build: 9.0.1.383
* Mon Dec 16 2019 04:55:08 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.379
- New Git version build: 9.0.1.379
* Fri Dec 13 2019 22:55:11 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.376
- New Git version build: 9.0.1.376
* Fri Dec 13 2019 14:25:17 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.366
- New Git version build: 9.0.1.366
* Fri Dec 13 2019 08:55:08 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.364
- New Git version build: 9.0.1.364
* Thu Dec 12 2019 22:25:07 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.361
- New Git version build: 9.0.1.361
* Thu Dec 12 2019 14:55:08 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.359
- New Git version build: 9.0.1.359
* Tue Dec 10 2019 22:25:31 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.347
- New Git version build: 9.0.1.347
* Tue Dec 10 2019 19:25:32 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.327
- New Git version build: 9.0.1.327
* Tue Dec 10 2019 18:25:36 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.323
- New Git version build: 9.0.1.323
* Tue Dec 10 2019 17:55:12 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.320
- New Git version build: 9.0.1.320
* Tue Dec 10 2019 16:57:05 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.316
- New Git version build: 9.0.1.316
* Mon Dec 09 2019 20:55:13 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.313
- New Git version build: 9.0.1.313
* Mon Dec 09 2019 18:25:12 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.310
- New Git version build: 9.0.1.310
* Mon Dec 09 2019 16:25:16 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.307
- New Git version build: 9.0.1.307
* Fri Dec 06 2019 20:25:29 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.303
- New Git version build: 9.0.1.303
* Fri Dec 06 2019 19:25:22 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.301
- New Git version build: 9.0.1.301
* Thu Dec 05 2019 21:55:13 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.299
- New Git version build: 9.0.1.299
* Thu Dec 05 2019 16:25:32 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.297
- New Git version build: 9.0.1.297
* Thu Dec 05 2019 15:25:28 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.295
- New Git version build: 9.0.1.295
* Thu Dec 05 2019 14:55:25 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.293
- New Git version build: 9.0.1.293
* Thu Dec 05 2019 00:25:02 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.291
- New Git version build: 9.0.1.291
* Wed Dec 04 2019 23:54:54 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.285
- New Git version build: 9.0.1.285
* Wed Dec 04 2019 23:24:59 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.282
- New Git version build: 9.0.1.282
* Wed Dec 04 2019 22:24:47 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.280
- New Git version build: 9.0.1.280
* Wed Dec 04 2019 19:55:00 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.278
- New Git version build: 9.0.1.278
* Wed Dec 04 2019 16:25:12 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.276
- New Git version build: 9.0.1.276
* Wed Dec 04 2019 15:54:58 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.274
- New Git version build: 9.0.1.274
* Wed Dec 04 2019 13:55:10 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.272
- New Git version build: 9.0.1.272
* Wed Dec 04 2019 01:34:23 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.270
- New Git version build: 9.0.1.270
* Tue Dec 03 2019 21:25:11 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.268
- New Git version build: 9.0.1.268
* Tue Dec 03 2019 20:54:49 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.266
- New Git version build: 9.0.1.266
* Tue Dec 03 2019 20:25:04 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.264
- New Git version build: 9.0.1.264
* Mon Dec 02 2019 23:10:39 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.262
* Mon Dec 02 2019 21:52:04 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.262
* Mon Dec 02 2019 21:22:04 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.262
* Mon Dec 02 2019 20:52:04 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.262
* Mon Dec 02 2019 20:27:31 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.262
* Mon Dec 02 2019 19:22:03 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.262
* Mon Dec 02 2019 18:52:03 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.262
* Mon Dec 02 2019 18:22:03 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.262
* Mon Dec 02 2019 17:54:55 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.262
- New Git version build: 9.0.1.262
* Mon Dec 02 2019 17:22:02 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.258
* Mon Dec 02 2019 16:52:03 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.258
* Mon Dec 02 2019 16:22:02 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.258
* Mon Dec 02 2019 15:52:03 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.258
* Mon Dec 02 2019 15:22:03 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.258
* Mon Dec 02 2019 14:52:02 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.258
* Mon Dec 02 2019 14:22:02 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.258
* Mon Dec 02 2019 13:55:03 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.258
- New Git version build: 9.0.1.258
* Wed Nov 27 2019 19:24:52 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.256
- New Git version build: 9.0.1.256
* Wed Nov 27 2019 17:54:59 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.254
- New Git version build: 9.0.1.254
* Wed Nov 27 2019 10:24:45 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.249
- New Git version build: 9.0.1.249
* Tue Nov 26 2019 20:25:07 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.247
- New Git version build: 9.0.1.247
* Tue Nov 26 2019 03:54:56 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.240
- New Git version build: 9.0.1.240
* Mon Nov 25 2019 22:54:55 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.238
- New Git version build: 9.0.1.238
* Mon Nov 25 2019 21:54:54 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.236
- New Git version build: 9.0.1.236
* Mon Nov 25 2019 21:24:49 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.234
- New Git version build: 9.0.1.234
* Mon Nov 25 2019 17:54:55 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.232
- New Git version build: 9.0.1.232
* Mon Nov 25 2019 15:54:58 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.227
- New Git version build: 9.0.1.227
* Mon Nov 25 2019 14:25:07 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.145
- New Git version build: 9.0.1.145
* Fri Nov 22 2019 18:54:54 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.142
- New Git version build: 9.0.1.142
* Fri Nov 22 2019 18:24:57 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.140
- New Git version build: 9.0.1.140
* Fri Nov 22 2019 16:24:51 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.138
- New Git version build: 9.0.1.138
* Fri Nov 22 2019 00:54:58 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.135
- New Git version build: 9.0.1.135
* Thu Nov 21 2019 18:55:04 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.133
- New Git version build: 9.0.1.133
* Thu Nov 21 2019 17:25:07 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.131
- New Git version build: 9.0.1.131
* Thu Nov 21 2019 13:54:57 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.129
- New Git version build: 9.0.1.129
* Thu Nov 21 2019 11:55:05 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.125
- New Git version build: 9.0.1.125
* Thu Nov 21 2019 04:54:57 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.122
- New Git version build: 9.0.1.122
* Wed Nov 20 2019 22:25:13 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.120
- New Git version build: 9.0.1.120
* Wed Nov 20 2019 21:54:57 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.118
- New Git version build: 9.0.1.118
* Wed Nov 20 2019 18:54:59 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.116
- New Git version build: 9.0.1.116
* Wed Nov 20 2019 16:54:52 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.112
- New Git version build: 9.0.1.112
* Wed Nov 20 2019 16:24:51 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.110
- New Git version build: 9.0.1.110
* Wed Nov 20 2019 15:54:56 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.108
- New Git version build: 9.0.1.108
* Wed Nov 20 2019 08:24:48 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.106
- New Git version build: 9.0.1.106
* Mon Nov 18 2019 16:54:59 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.98
- New Git version build: 9.0.1.98
* Mon Nov 18 2019 14:54:49 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.96
- New Git version build: 9.0.1.96
* Sat Nov 16 2019 01:54:43 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.94
- New Git version build: 9.0.1.94
* Sat Nov 16 2019 01:30:34 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.92
- New Git version build: 9.0.1.92
* Fri Nov 15 2019 21:54:58 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.90
- New Git version build: 9.0.1.90
* Fri Nov 15 2019 21:24:54 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.88
- New Git version build: 9.0.1.88
* Fri Nov 15 2019 17:54:50 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.81
- New Git version build: 9.0.1.81
* Thu Nov 14 2019 21:55:01 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.79
- New Git version build: 9.0.1.79
* Thu Nov 14 2019 19:54:54 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.77
- New Git version build: 9.0.1.77
* Thu Nov 14 2019 19:24:43 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.73
- New Git version build: 9.0.1.73
* Thu Nov 14 2019 17:54:51 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.71
- New Git version build: 9.0.1.71
* Thu Nov 14 2019 13:55:03 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.69
- New Git version build: 9.0.1.69
* Wed Nov 13 2019 21:25:06 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.67
- New Git version build: 9.0.1.67
* Wed Nov 13 2019 19:24:56 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.64
- New Git version build: 9.0.1.64
* Tue Nov 12 2019 21:25:05 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.62
- New Git version build: 9.0.1.62
* Tue Nov 12 2019 20:25:04 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.56
- New Git version build: 9.0.1.56
* Tue Nov 12 2019 19:24:54 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.52
- New Git version build: 9.0.1.52
* Tue Nov 12 2019 16:54:54 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.50
- New Git version build: 9.0.1.50
* Tue Nov 12 2019 15:54:54 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.48
- New Git version build: 9.0.1.48
* Mon Nov 11 2019 21:54:20 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.43
- New Git version build: 9.0.1.43
* Mon Nov 11 2019 21:24:36 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.40
- New Git version build: 9.0.1.40
* Mon Nov 11 2019 20:24:32 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.35
- New Git version build: 9.0.1.35
* Fri Nov 08 2019 21:54:30 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.32
- New Git version build: 9.0.1.32
* Thu Nov 07 2019 15:54:31 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.26
- New Git version build: 9.0.1.26
* Thu Nov 07 2019 12:54:25 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.22
- New Git version build: 9.0.1.22
* Wed Nov 06 2019 19:24:34 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.20
- New Git version build: 9.0.1.20
* Wed Nov 06 2019 16:54:25 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.18
- New Git version build: 9.0.1.18
* Wed Nov 06 2019 15:54:21 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.16
- New Git version build: 9.0.1.16
* Wed Nov 06 2019 14:54:28 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.12
- New Git version build: 9.0.1.12
* Tue Nov 05 2019 23:24:32 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.10
- New Git version build: 9.0.1.10
* Tue Nov 05 2019 22:24:27 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.8
- New Git version build: 9.0.1.8
* Tue Nov 05 2019 18:54:30 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.6
- New Git version build: 9.0.1.6
* Mon Nov 04 2019 18:54:31 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.2
- New Git version build: 9.0.1.2
* Mon Nov 04 2019 17:24:30 +0000 Martin Juhl <mj@casalogic.dk> 9.0.1.0
- New Git version build: 9.0.1.0
* Mon Nov 04 2019 16:24:23 +0000 Martin Juhl <mj@casalogic.dk> 9.0.0.31
- New Git version build: 9.0.0.31
* Mon Nov 04 2019 14:24:44 +0000 Martin Juhl <mj@casalogic.dk> 9.0.0.26
- New Git version build: 9.0.0.26
* Fri Nov 01 2019 19:54:54 +0000 Martin Juhl <mj@casalogic.dk> 9.0.0.24
- New Git version build: 9.0.0.24
* Fri Nov 01 2019 15:54:19 +0000 Martin Juhl <mj@casalogic.dk> 9.0.0.21
- New Git version build: 9.0.0.21
* Fri Nov 01 2019 15:24:59 +0000 Martin Juhl <mj@casalogic.dk> 9.0.0.19
- New Git version build: 9.0.0.19
* Fri Nov 01 2019 13:55:10 +0000 Martin Juhl <mj@casalogic.dk> 9.0.0.9
- New Git version build: 9.0.0.9
* Thu Oct 31 2019 19:27:32 +0000 Martin Juhl <mj@casalogic.dk> 9.0.0.4
- New Git version build: 9.0.0.4
* Thu Oct 31 2019 18:26:13 +0000 Martin Juhl <mj@casalogic.dk> 9.0.0.2
- New Git version build: 9.0.0.2
* Thu Oct 31 2019 17:53:42 +0000 Martin Juhl <mj@casalogic.dk> 9.0.0.6
- New Git version build: 9.0.0.6
* Thu Oct 31 2019 15:25:11 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.154
- New Git version build: 8.0.0.154
* Thu Oct 31 2019 01:37:03 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.152
- New Git version build: 8.0.0.152
* Thu Oct 31 2019 00:55:08 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.150
- New Git version build: 8.0.0.150
* Wed Oct 30 2019 22:55:06 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.145
- New Git version build: 8.0.0.145
* Wed Oct 30 2019 21:54:32 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.139
- New Git version build: 8.0.0.139
* Wed Oct 30 2019 21:25:17 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.136
- New Git version build: 8.0.0.136
* Wed Oct 30 2019 19:55:01 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.133
- New Git version build: 8.0.0.133
* Wed Oct 30 2019 19:27:10 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.131
- New Git version build: 8.0.0.131
* Wed Oct 30 2019 18:26:48 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.129
- New Git version build: 8.0.0.129
* Wed Oct 30 2019 17:55:21 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.124
- New Git version build: 8.0.0.124
* Wed Oct 30 2019 13:25:55 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.122
- New Git version build: 8.0.0.122
* Wed Oct 30 2019 00:25:07 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.119
- New Git version build: 8.0.0.119
* Tue Oct 29 2019 22:25:25 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.116
- New Git version build: 8.0.0.116
* Tue Oct 29 2019 20:54:48 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.114
- New Git version build: 8.0.0.114
* Tue Oct 29 2019 18:25:11 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.106
- New Git version build: 8.0.0.106
* Tue Oct 29 2019 01:39:26 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.58
- New Git version build: 8.0.0.58
* Mon Oct 28 2019 22:26:03 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.54
- New Git version build: 8.0.0.54
* Mon Oct 28 2019 21:25:26 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.52
- New Git version build: 8.0.0.52
* Mon Oct 28 2019 19:54:54 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.50
- New Git version build: 8.0.0.50
* Mon Oct 28 2019 15:54:36 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.48
- New Git version build: 8.0.0.48
* Mon Oct 28 2019 15:26:02 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.46
- New Git version build: 8.0.0.46
* Sun Oct 27 2019 23:55:10 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.42
- New Git version build: 8.0.0.42
* Sun Oct 27 2019 15:55:28 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.40
- New Git version build: 8.0.0.40
* Sun Oct 27 2019 14:25:02 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.38
- New Git version build: 8.0.0.38
* Fri Oct 25 2019 21:25:23 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.36
- New Git version build: 8.0.0.36
* Fri Oct 25 2019 19:54:46 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.28
- New Git version build: 8.0.0.28
* Fri Oct 25 2019 16:53:43 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.26
- New Git version build: 8.0.0.26
* Fri Oct 25 2019 16:26:50 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.21
- New Git version build: 8.0.0.21
* Fri Oct 25 2019 15:53:34 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.19
- New Git version build: 8.0.0.19
* Fri Oct 25 2019 13:25:15 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.13
- New Git version build: 8.0.0.13
* Thu Oct 24 2019 15:54:17 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.11
- New Git version build: 8.0.0.11
* Thu Oct 24 2019 00:31:53 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.9
- New Git version build: 8.0.0.9
* Tue Oct 22 2019 20:56:48 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.7
- New Git version build: 8.0.0.7
* Tue Oct 22 2019 13:57:08 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.5
- New Git version build: 8.0.0.5
* Tue Oct 22 2019 11:27:09 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.3
- New Git version build: 8.0.0.3
* Mon Oct 21 2019 22:51:57 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.0
* Mon Oct 21 2019 22:27:23 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.0
* Mon Oct 21 2019 22:16:36 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.0
* Mon Oct 21 2019 22:14:27 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.0
* Mon Oct 21 2019 21:49:21 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.0
* Mon Oct 21 2019 17:56:45 +0000 Martin Juhl <mj@casalogic.dk> 8.0.0.0
- New Git version build: 8.0.0.0
* Mon Oct 21 2019 16:56:54 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.757
- New Git version build: 7.0.0.757
* Fri Oct 18 2019 19:56:23 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.712
- New Git version build: 7.0.0.712
* Fri Oct 18 2019 19:26:24 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.708
- New Git version build: 7.0.0.708
* Fri Oct 18 2019 16:56:19 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.705
- New Git version build: 7.0.0.705
* Wed Oct 16 2019 22:49:32 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.697
- New Git version build: 7.0.0.697
* Wed Oct 16 2019 22:23:16 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.695
* Wed Oct 16 2019 21:22:45 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.695
* Wed Oct 16 2019 20:56:48 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.695
- New Git version build: 7.0.0.695
* Wed Oct 16 2019 20:22:44 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.693
* Wed Oct 16 2019 19:52:44 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.693
* Wed Oct 16 2019 19:22:44 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.693
* Wed Oct 16 2019 18:52:45 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.693
* Wed Oct 16 2019 18:28:10 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.693
- New Git version build: 7.0.0.693
* Tue Oct 15 2019 20:56:53 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.647
- New Git version build: 7.0.0.647
* Mon Oct 14 2019 18:57:16 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.637
- New Git version build: 7.0.0.637
* Mon Oct 14 2019 15:56:57 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.634
- New Git version build: 7.0.0.634
* Thu Oct 10 2019 09:13:07 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.632
- New Git version build: 7.0.0.632
* Thu Oct 10 2019 08:25:41 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.630
- New Git version build: 7.0.0.630
* Fri Sep 13 2019 18:27:17 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.146
- New Git version build: 7.0.0.146
* Fri Sep 13 2019 17:56:21 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.143
- New Git version build: 7.0.0.143
* Fri Sep 13 2019 17:26:28 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.125
- New Git version build: 7.0.0.125
* Fri Sep 13 2019 15:56:26 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.121
- New Git version build: 7.0.0.121
* Fri Sep 13 2019 14:56:27 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.119
- New Git version build: 7.0.0.119
* Fri Sep 13 2019 13:57:12 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.117
- New Git version build: 7.0.0.117
* Thu Sep 12 2019 23:26:31 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.115
- New Git version build: 7.0.0.115
* Thu Sep 12 2019 19:27:08 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.112
- New Git version build: 7.0.0.112
* Thu Sep 12 2019 17:56:35 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.105
- New Git version build: 7.0.0.105
* Thu Sep 12 2019 14:56:39 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.103
- New Git version build: 7.0.0.103
* Thu Sep 12 2019 14:26:50 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.100
- New Git version build: 7.0.0.100
* Thu Sep 12 2019 13:56:19 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.96
- New Git version build: 7.0.0.96
* Thu Sep 12 2019 10:56:38 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.94
- New Git version build: 7.0.0.94
* Thu Sep 12 2019 01:56:28 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.92
- New Git version build: 7.0.0.92
* Wed Sep 11 2019 21:26:33 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.90
- New Git version build: 7.0.0.90
* Wed Sep 11 2019 18:27:48 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.88
- New Git version build: 7.0.0.88
* Wed Sep 11 2019 15:56:30 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.79
- New Git version build: 7.0.0.79
* Wed Sep 11 2019 14:56:50 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.76
- New Git version build: 7.0.0.76
* Tue Sep 10 2019 20:56:23 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.74
- New Git version build: 7.0.0.74
* Tue Sep 10 2019 20:26:17 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.72
- New Git version build: 7.0.0.72
* Tue Sep 10 2019 19:56:21 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.68
- New Git version build: 7.0.0.68
* Tue Sep 10 2019 17:56:02 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.65
- New Git version build: 7.0.0.65
* Tue Sep 10 2019 17:26:07 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.62
- New Git version build: 7.0.0.62
* Tue Sep 10 2019 15:26:16 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.56
- New Git version build: 7.0.0.56
* Tue Sep 10 2019 14:26:32 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.54
- New Git version build: 7.0.0.54
* Tue Sep 10 2019 13:26:27 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.52
- New Git version build: 7.0.0.52
* Mon Sep 09 2019 21:56:46 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.50
- New Git version build: 7.0.0.50
* Mon Sep 09 2019 20:26:56 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.48
- New Git version build: 7.0.0.48
* Mon Sep 09 2019 19:26:57 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.44
- New Git version build: 7.0.0.44
* Sun Sep 08 2019 19:57:01 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.40
- New Git version build: 7.0.0.40
* Fri Sep 06 2019 23:26:21 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.37
- New Git version build: 7.0.0.37
* Fri Sep 06 2019 21:26:56 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.20
- New Git version build: 7.0.0.20
* Fri Sep 06 2019 16:26:53 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.18
- New Git version build: 7.0.0.18
* Thu Sep 05 2019 21:56:55 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.16
- New Git version build: 7.0.0.16
* Thu Sep 05 2019 20:56:52 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.14
- New Git version build: 7.0.0.14
* Thu Sep 05 2019 17:56:34 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.12
- New Git version build: 7.0.0.12
* Thu Sep 05 2019 13:56:48 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.9
- New Git version build: 7.0.0.9
* Wed Sep 04 2019 20:56:56 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.2
- New Git version build: 7.0.0.2
* Wed Sep 04 2019 18:26:53 +0000 Martin Juhl <mj@casalogic.dk> 7.0.0.0
- New Git version build: 7.0.0.0
* Wed Sep 04 2019 16:26:26 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.483
- New Git version build: 6.1.0.483
* Wed Sep 04 2019 14:56:19 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.481
- New Git version build: 6.1.0.481
* Wed Sep 04 2019 14:26:35 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.479
- New Git version build: 6.1.0.479
* Wed Sep 04 2019 02:56:41 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.477
- New Git version build: 6.1.0.477
* Tue Sep 03 2019 22:26:33 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.475
- New Git version build: 6.1.0.475
* Tue Sep 03 2019 19:56:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.473
- New Git version build: 6.1.0.473
* Tue Sep 03 2019 15:26:40 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.469
- New Git version build: 6.1.0.469
* Tue Sep 03 2019 13:27:01 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.467
- New Git version build: 6.1.0.467
* Fri Aug 30 2019 22:26:49 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.465
- New Git version build: 6.1.0.465
* Fri Aug 30 2019 19:57:07 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.462
- New Git version build: 6.1.0.462
* Thu Aug 29 2019 22:56:47 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.460
- New Git version build: 6.1.0.460
* Thu Aug 29 2019 21:26:46 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.456
- New Git version build: 6.1.0.456
* Thu Aug 29 2019 14:56:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.454
- New Git version build: 6.1.0.454
* Thu Aug 29 2019 14:27:03 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.452
- New Git version build: 6.1.0.452
* Wed Aug 28 2019 22:57:06 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.446
- New Git version build: 6.1.0.446
* Tue Aug 27 2019 22:56:33 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.387
- New Git version build: 6.1.0.387
* Tue Aug 27 2019 20:57:14 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.384
- New Git version build: 6.1.0.384
* Tue Aug 27 2019 16:56:38 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.382
- New Git version build: 6.1.0.382
* Tue Aug 27 2019 15:56:36 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.338
- New Git version build: 6.1.0.338
* Tue Aug 27 2019 15:26:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.336
- New Git version build: 6.1.0.336
* Tue Aug 27 2019 14:57:30 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.334
- New Git version build: 6.1.0.334
* Mon Aug 26 2019 21:56:43 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.330
- New Git version build: 6.1.0.330
* Mon Aug 26 2019 21:26:41 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.328
- New Git version build: 6.1.0.328
* Mon Aug 26 2019 20:26:53 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.325
- New Git version build: 6.1.0.325
* Mon Aug 26 2019 19:57:16 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.321
- New Git version build: 6.1.0.321
* Mon Aug 26 2019 19:27:25 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.315
- New Git version build: 6.1.0.315
* Mon Aug 26 2019 15:56:45 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.311
- New Git version build: 6.1.0.311
* Mon Aug 26 2019 13:57:07 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.308
- New Git version build: 6.1.0.308
* Fri Aug 23 2019 21:27:07 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.306
- New Git version build: 6.1.0.306
* Fri Aug 23 2019 20:27:20 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.300
- New Git version build: 6.1.0.300
* Fri Aug 23 2019 17:26:34 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.298
- New Git version build: 6.1.0.298
* Fri Aug 23 2019 16:56:39 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.296
- New Git version build: 6.1.0.296
* Fri Aug 23 2019 15:56:50 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.294
- New Git version build: 6.1.0.294
* Thu Aug 22 2019 22:27:12 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.292
- New Git version build: 6.1.0.292
* Thu Aug 22 2019 15:27:05 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.288
- New Git version build: 6.1.0.288
* Thu Aug 22 2019 14:26:54 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.284
- New Git version build: 6.1.0.284
* Wed Aug 21 2019 22:27:04 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.280
- New Git version build: 6.1.0.280
* Wed Aug 21 2019 16:57:08 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.277
- New Git version build: 6.1.0.277
* Tue Aug 20 2019 21:56:46 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.275
- New Git version build: 6.1.0.275
* Tue Aug 20 2019 19:27:03 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.273
- New Git version build: 6.1.0.273
* Tue Aug 20 2019 18:57:06 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.271
- New Git version build: 6.1.0.271
* Tue Aug 20 2019 16:56:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.265
- New Git version build: 6.1.0.265
* Mon Aug 19 2019 23:56:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.258
- New Git version build: 6.1.0.258
* Mon Aug 19 2019 21:27:47 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.256
- New Git version build: 6.1.0.256
* Mon Aug 19 2019 16:56:42 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.254
- New Git version build: 6.1.0.254
* Mon Aug 19 2019 14:57:17 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.252
- New Git version build: 6.1.0.252
* Mon Aug 19 2019 14:27:11 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.250
- New Git version build: 6.1.0.250
* Mon Aug 19 2019 13:27:26 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.248
- New Git version build: 6.1.0.248
* Fri Aug 16 2019 23:57:04 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.246
- New Git version build: 6.1.0.246
* Fri Aug 16 2019 22:27:04 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.244
- New Git version build: 6.1.0.244
* Fri Aug 16 2019 18:56:55 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.242
- New Git version build: 6.1.0.242
* Fri Aug 16 2019 17:56:41 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.240
- New Git version build: 6.1.0.240
* Fri Aug 16 2019 17:26:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.238
- New Git version build: 6.1.0.238
* Fri Aug 16 2019 16:57:14 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.236
- New Git version build: 6.1.0.236
* Thu Aug 15 2019 18:27:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.229
- New Git version build: 6.1.0.229
* Thu Aug 15 2019 16:26:37 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.225
- New Git version build: 6.1.0.225
* Thu Aug 15 2019 15:26:45 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.223
- New Git version build: 6.1.0.223
* Thu Aug 15 2019 14:57:00 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.221
- New Git version build: 6.1.0.221
* Thu Aug 15 2019 08:22:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 07:44:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 06:22:59 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 05:52:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 05:22:57 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 04:52:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 04:22:57 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 03:52:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 03:22:57 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 02:52:57 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 02:22:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 01:52:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 01:22:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 00:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Thu Aug 15 2019 00:48:18 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Wed Aug 14 2019 23:52:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
* Wed Aug 14 2019 23:26:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.219
- New Git version build: 6.1.0.219
* Wed Aug 14 2019 22:52:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.215
* Wed Aug 14 2019 22:22:56 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.215
* Wed Aug 14 2019 22:13:33 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.215
* Wed Aug 14 2019 20:56:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.215
- New Git version build: 6.1.0.215
* Wed Aug 14 2019 20:27:00 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.213
- New Git version build: 6.1.0.213
* Wed Aug 14 2019 19:57:12 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.211
- New Git version build: 6.1.0.211
* Wed Aug 14 2019 19:22:57 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.205
* Wed Aug 14 2019 18:57:20 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.205
- New Git version build: 6.1.0.205
* Wed Aug 14 2019 18:23:23 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.203
* Wed Aug 14 2019 17:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.203
* Wed Aug 14 2019 17:27:06 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.203
- New Git version build: 6.1.0.203
* Wed Aug 14 2019 16:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.201
* Wed Aug 14 2019 16:22:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.201
* Wed Aug 14 2019 15:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.201
* Wed Aug 14 2019 15:27:45 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.201
- New Git version build: 6.1.0.201
* Tue Aug 13 2019 21:57:21 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.183
- New Git version build: 6.1.0.183
* Tue Aug 13 2019 19:27:33 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.168
- New Git version build: 6.1.0.168
* Tue Aug 13 2019 18:27:54 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.166
- New Git version build: 6.1.0.166
* Tue Aug 13 2019 17:57:15 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.159
- New Git version build: 6.1.0.159
* Tue Aug 13 2019 13:28:09 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.157
- New Git version build: 6.1.0.157
* Mon Aug 12 2019 23:57:19 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.155
- New Git version build: 6.1.0.155
* Mon Aug 12 2019 20:57:42 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.150
- New Git version build: 6.1.0.150
* Mon Aug 12 2019 19:27:37 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.148
- New Git version build: 6.1.0.148
* Mon Aug 12 2019 15:27:30 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.146
- New Git version build: 6.1.0.146
* Fri Aug 09 2019 20:57:09 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.144
- New Git version build: 6.1.0.144
* Fri Aug 09 2019 16:27:35 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.142
- New Git version build: 6.1.0.142
* Thu Aug 08 2019 18:57:18 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.139
- New Git version build: 6.1.0.139
* Thu Aug 08 2019 18:28:40 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.137
- New Git version build: 6.1.0.137
* Thu Aug 08 2019 15:27:47 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.134
- New Git version build: 6.1.0.134
* Wed Aug 07 2019 20:27:29 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.132
- New Git version build: 6.1.0.132
* Tue Aug 06 2019 19:58:03 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.128
- New Git version build: 6.1.0.128
* Tue Aug 06 2019 14:57:27 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.126
- New Git version build: 6.1.0.126
* Mon Aug 05 2019 17:57:39 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.124
- New Git version build: 6.1.0.124
* Mon Aug 05 2019 13:27:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.121
- New Git version build: 6.1.0.121
* Sat Aug 03 2019 16:27:33 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.119
- New Git version build: 6.1.0.119
* Sat Aug 03 2019 13:57:36 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.116
- New Git version build: 6.1.0.116
* Fri Aug 02 2019 22:56:59 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.114
- New Git version build: 6.1.0.114
* Fri Aug 02 2019 15:27:19 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.110
- New Git version build: 6.1.0.110
* Fri Aug 02 2019 00:54:33 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Fri Aug 02 2019 00:51:41 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Thu Aug 01 2019 23:52:54 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Thu Aug 01 2019 23:22:54 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Thu Aug 01 2019 22:52:52 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Thu Aug 01 2019 22:22:50 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Thu Aug 01 2019 21:52:57 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
* Thu Aug 01 2019 21:27:09 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.108
- New Git version build: 6.1.0.108
* Thu Aug 01 2019 20:52:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.99
* Thu Aug 01 2019 20:22:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.99
* Thu Aug 01 2019 19:52:50 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.99
* Thu Aug 01 2019 19:26:54 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.99
- New Git version build: 6.1.0.99
* Thu Aug 01 2019 18:52:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.97
* Thu Aug 01 2019 18:26:38 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.97
- New Git version build: 6.1.0.97
* Thu Aug 01 2019 16:27:03 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.94
- New Git version build: 6.1.0.94
* Thu Aug 01 2019 12:27:15 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.92
- New Git version build: 6.1.0.92
* Thu Aug 01 2019 00:52:58 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.88
- New Git version build: 6.1.0.88
* Wed Jul 31 2019 21:57:03 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.86
- New Git version build: 6.1.0.86
* Wed Jul 31 2019 20:57:34 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.84
- New Git version build: 6.1.0.84
* Tue Jul 30 2019 22:57:12 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.82
- New Git version build: 6.1.0.82
* Tue Jul 30 2019 22:27:03 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.79
- New Git version build: 6.1.0.79
* Tue Jul 30 2019 21:27:07 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.75
- New Git version build: 6.1.0.75
* Tue Jul 30 2019 19:57:36 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.73
- New Git version build: 6.1.0.73
* Tue Jul 30 2019 15:57:13 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.70
- New Git version build: 6.1.0.70
* Tue Jul 30 2019 13:57:51 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.66
- New Git version build: 6.1.0.66
* Mon Jul 29 2019 17:57:04 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.64
- New Git version build: 6.1.0.64
* Mon Jul 29 2019 16:57:14 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.53
- New Git version build: 6.1.0.53
* Mon Jul 29 2019 12:57:30 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.50
- New Git version build: 6.1.0.50
* Fri Jul 26 2019 16:57:25 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.48
- New Git version build: 6.1.0.48
* Thu Jul 25 2019 21:56:53 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.46
- New Git version build: 6.1.0.46
* Thu Jul 25 2019 20:57:17 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.44
- New Git version build: 6.1.0.44
* Thu Jul 25 2019 19:57:34 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.42
- New Git version build: 6.1.0.42
* Thu Jul 25 2019 19:27:35 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.40
- New Git version build: 6.1.0.40
* Wed Jul 24 2019 21:27:32 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.38
- New Git version build: 6.1.0.38
* Wed Jul 24 2019 18:27:55 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.20
- New Git version build: 6.1.0.20
* Wed Jul 24 2019 00:02:16 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.18
- New Git version build: 6.1.0.18
* Thu Jul 18 2019 19:00:33 +0000 Martin Juhl <mj@casalogic.dk> 6.1.0.14
- New Git version build: 6.1.0.14
* Thu Jul 18 2019 17:27:10 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.747
- New Git version build: 6.0.0.747
* Thu Jul 18 2019 16:27:56 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.732
- New Git version build: 6.0.0.732
* Thu Jul 18 2019 15:58:45 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.728
- New Git version build: 6.0.0.728
* Wed Jul 17 2019 20:53:24 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.726
- New Git version build: 6.0.0.726
* Wed Jul 17 2019 16:53:30 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.721
* Wed Jul 17 2019 16:27:25 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.721
- New Git version build: 6.0.0.721
* Tue Jul 16 2019 22:18:46 +0000 Martin Juhl <mj@casalogic.dk> 05a1137
* Tue Jul 16 2019 22:02:45 +0000 Martin Juhl <mj@casalogic.dk> 05a1137
- New version build: 05a1137
* Tue Jul 16 2019 20:53:15 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.719
* Tue Jul 16 2019 18:57:21 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.719
- New Git version build: 6.0.0.719
* Tue Jul 16 2019 18:32:47 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.717
- New Git version build: 6.0.0.717
* Tue Jul 16 2019 18:21:09 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.715
- New Git version build: 6.0.0.715
* Tue Jul 16 2019 17:23:24 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.713
* Tue Jul 16 2019 17:19:25 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.713
* Tue Jul 16 2019 16:23:18 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.713
* Tue Jul 16 2019 15:53:17 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.713
* Tue Jul 16 2019 15:27:13 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.713
- New Git version build: 6.0.0.713
* Tue Jul 16 2019 14:58:02 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.710
- New Git version build: 6.0.0.710
* Mon Jul 15 2019 23:27:40 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.703
- New Git version build: 6.0.0.703
* Mon Jul 15 2019 13:28:25 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.675
- New Git version build: 6.0.0.675
* Fri Jul 12 2019 19:27:15 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.673
- New Git version build: 6.0.0.673
* Fri Jul 12 2019 18:57:04 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.671
- New Git version build: 6.0.0.671
* Fri Jul 12 2019 02:26:42 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.669
- New Git version build: 6.0.0.669
* Thu Jul 11 2019 18:56:53 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.667
- New Git version build: 6.0.0.667
* Thu Jul 11 2019 17:27:05 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.665
- New Git version build: 6.0.0.665
* Thu Jul 11 2019 16:57:31 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.663
- New Git version build: 6.0.0.663
* Wed Jul 10 2019 14:57:31 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.656
- New Git version build: 6.0.0.656
* Tue Jul 09 2019 21:27:04 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.652
- New Git version build: 6.0.0.652
* Tue Jul 09 2019 18:57:03 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.650
- New Git version build: 6.0.0.650
* Tue Jul 09 2019 17:27:07 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.644
- New Git version build: 6.0.0.644
* Tue Jul 09 2019 13:57:30 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.638
- New Git version build: 6.0.0.638
* Tue Jul 09 2019 13:27:24 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.636
- New Git version build: 6.0.0.636
* Tue Jul 09 2019 05:57:02 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.630
- New Git version build: 6.0.0.630
* Mon Jul 08 2019 21:27:16 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.628
- New Git version build: 6.0.0.628
* Fri Jul 05 2019 16:27:54 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.618
- New Git version build: 6.0.0.618
* Wed Jul 03 2019 12:57:13 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.616
- New Git version build: 6.0.0.616
* Wed Jul 03 2019 12:27:21 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.614
- New Git version build: 6.0.0.614
* Tue Jul 02 2019 19:26:32 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.610
* Tue Jul 02 2019 19:22:56 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.610
* Tue Jul 02 2019 18:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.610
* Tue Jul 02 2019 18:22:59 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.610
* Tue Jul 02 2019 17:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.610
* Tue Jul 02 2019 17:26:51 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.610
- New Git version build: 6.0.0.610
* Tue Jul 02 2019 16:52:55 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.608
* Tue Jul 02 2019 16:26:55 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.608
- New Git version build: 6.0.0.608
* Tue Jul 02 2019 12:57:36 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.603
- New Git version build: 6.0.0.603
* Mon Jul 01 2019 23:26:57 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.600
- New Git version build: 6.0.0.600
* Mon Jul 01 2019 21:56:51 +0000 Martin Juhl <mj@casalogic.dk> 6.0.0.597
- New Git version build: 6.0.0.597
* Mon Jul 01 2019 16:27:13 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.69
- New Git version build: 5.0.0.69
* Mon Jul 01 2019 15:57:33 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.67
- New Git version build: 5.0.0.67
* Fri Jun 28 2019 16:57:42 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.65
- New Git version build: 5.0.0.65
* Thu Jun 27 2019 20:27:03 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.63
- New Git version build: 5.0.0.63
* Thu Jun 27 2019 18:57:09 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.61
- New Git version build: 5.0.0.61
* Wed Jun 26 2019 20:26:52 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.59
- New Git version build: 5.0.0.59
* Wed Jun 26 2019 12:57:07 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.57
- New Git version build: 5.0.0.57
* Wed Jun 26 2019 01:26:53 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.55
- New Git version build: 5.0.0.55
* Tue Jun 25 2019 21:57:28 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.53
- New Git version build: 5.0.0.53
* Mon Jun 24 2019 21:28:41 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.51
- New Git version build: 5.0.0.51
* Sat Jun 22 2019 22:51:49 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.49
* Sat Jun 22 2019 22:46:12 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.49
* Sat Jun 22 2019 21:37:08 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.49
- New Git version build: 5.0.0.49
* Thu Jun 20 2019 23:49:15 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.0
* Thu Jun 20 2019 23:31:16 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.0
* Tue Jun 18 2019 21:00:21 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.0
* Tue Jun 18 2019 20:47:31 +0000 Martin Juhl <mj@casalogic.dk> 5.0.0.0
- New Git version build: 5.0.0.0
* Mon Jun 17 2019 21:12:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.746
- New Git version build: 4.0.0.746
* Sat Jun 15 2019 01:27:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.742
- New Git version build: 4.0.0.742
* Fri Jun 14 2019 14:57:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.740
- New Git version build: 4.0.0.740
* Fri Jun 14 2019 14:27:16 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.738
- New Git version build: 4.0.0.738
* Fri Jun 14 2019 13:57:11 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.734
- New Git version build: 4.0.0.734
* Thu Jun 13 2019 22:26:32 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.731
- New Git version build: 4.0.0.731
* Thu Jun 13 2019 21:57:04 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.729
- New Git version build: 4.0.0.729
* Thu Jun 13 2019 20:26:36 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.725
- New Git version build: 4.0.0.725
* Thu Jun 13 2019 14:27:36 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.723
- New Git version build: 4.0.0.723
* Thu Jun 13 2019 12:31:44 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.721
* Wed Jun 12 2019 21:26:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.721
- New Git version build: 4.0.0.721
* Wed Jun 12 2019 18:56:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.719
- New Git version build: 4.0.0.719
* Wed Jun 12 2019 17:56:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.707
- New Git version build: 4.0.0.707
* Wed Jun 12 2019 16:26:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.705
- New Git version build: 4.0.0.705
* Wed Jun 12 2019 15:26:18 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.703
- New Git version build: 4.0.0.703
* Wed Jun 12 2019 13:56:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.701
- New Git version build: 4.0.0.701
* Wed Jun 12 2019 12:27:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.699
- New Git version build: 4.0.0.699
* Tue Jun 11 2019 18:56:30 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.697
- New Git version build: 4.0.0.697
* Tue Jun 11 2019 16:26:54 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.695
- New Git version build: 4.0.0.695
* Tue Jun 11 2019 15:56:59 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.693
- New Git version build: 4.0.0.693
* Tue Jun 11 2019 14:57:10 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.691
- New Git version build: 4.0.0.691
* Mon Jun 10 2019 17:58:18 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.689
- New Git version build: 4.0.0.689
* Thu Jun 06 2019 18:56:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.682
- New Git version build: 4.0.0.682
* Thu Jun 06 2019 16:26:42 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.678
- New Git version build: 4.0.0.678
* Thu Jun 06 2019 15:26:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.676
- New Git version build: 4.0.0.676
* Thu Jun 06 2019 14:56:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.674
- New Git version build: 4.0.0.674
* Wed Jun 05 2019 20:26:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.672
- New Git version build: 4.0.0.672
* Wed Jun 05 2019 17:26:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.670
- New Git version build: 4.0.0.670
* Wed Jun 05 2019 11:56:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.668
- New Git version build: 4.0.0.668
* Tue Jun 04 2019 20:27:01 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.663
- New Git version build: 4.0.0.663
* Mon Jun 03 2019 21:56:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.661
- New Git version build: 4.0.0.661
* Mon Jun 03 2019 18:26:45 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.658
- New Git version build: 4.0.0.658
* Mon Jun 03 2019 17:56:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.656
- New Git version build: 4.0.0.656
* Mon Jun 03 2019 14:57:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.652
- New Git version build: 4.0.0.652
* Fri May 31 2019 16:27:11 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.650
- New Git version build: 4.0.0.650
* Fri May 31 2019 15:28:01 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.648
- New Git version build: 4.0.0.648
* Fri May 31 2019 12:27:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.646
- New Git version build: 4.0.0.646
* Fri May 31 2019 01:57:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.644
- New Git version build: 4.0.0.644
* Thu May 30 2019 19:27:30 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.642
- New Git version build: 4.0.0.642
* Thu May 30 2019 17:27:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.640
- New Git version build: 4.0.0.640
* Thu May 30 2019 14:58:14 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.638
- New Git version build: 4.0.0.638
* Wed May 29 2019 20:58:15 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.631
- New Git version build: 4.0.0.631
* Tue May 28 2019 20:28:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.629
- New Git version build: 4.0.0.629
* Tue May 28 2019 19:57:52 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.627
- New Git version build: 4.0.0.627
* Tue May 28 2019 17:27:59 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.625
- New Git version build: 4.0.0.625
* Tue May 28 2019 16:58:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.623
- New Git version build: 4.0.0.623
* Tue May 28 2019 13:58:44 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.619
- New Git version build: 4.0.0.619
* Fri May 24 2019 20:57:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.616
- New Git version build: 4.0.0.616
* Fri May 24 2019 19:58:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.614
- New Git version build: 4.0.0.614
* Thu May 23 2019 19:27:26 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.612
- New Git version build: 4.0.0.612
* Thu May 23 2019 17:27:34 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.610
- New Git version build: 4.0.0.610
* Thu May 23 2019 15:27:37 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.608
- New Git version build: 4.0.0.608
* Thu May 23 2019 12:58:13 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.605
- New Git version build: 4.0.0.605
* Wed May 22 2019 23:59:15 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.601
- New Git version build: 4.0.0.601
* Wed May 22 2019 20:57:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.599
- New Git version build: 4.0.0.599
* Wed May 22 2019 19:27:10 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.597
- New Git version build: 4.0.0.597
* Wed May 22 2019 14:28:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.595
- New Git version build: 4.0.0.595
* Tue May 21 2019 14:58:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.593
- New Git version build: 4.0.0.593
* Mon May 20 2019 17:27:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.590
- New Git version build: 4.0.0.590
* Mon May 20 2019 16:57:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.588
- New Git version build: 4.0.0.588
* Mon May 20 2019 15:58:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.586
- New Git version build: 4.0.0.586
* Fri May 17 2019 18:53:08 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.582
* Fri May 17 2019 18:27:23 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.582
- New Git version build: 4.0.0.582
* Fri May 17 2019 15:58:00 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.577
- New Git version build: 4.0.0.577
* Thu May 16 2019 20:27:23 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.573
- New Git version build: 4.0.0.573
* Thu May 16 2019 18:57:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.569
- New Git version build: 4.0.0.569
* Thu May 16 2019 18:27:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.567
- New Git version build: 4.0.0.567
* Thu May 16 2019 17:27:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.565
- New Git version build: 4.0.0.565
* Thu May 16 2019 15:27:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.563
- New Git version build: 4.0.0.563
* Thu May 16 2019 03:58:13 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.561
- New Git version build: 4.0.0.561
* Wed May 15 2019 18:58:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.558
- New Git version build: 4.0.0.558
* Mon May 13 2019 22:23:17 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.547
* Mon May 13 2019 21:50:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.547
* Mon May 13 2019 21:23:28 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.547
* Mon May 13 2019 20:58:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.547
- New Git version build: 4.0.0.547
* Fri May 10 2019 19:23:06 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.541
- New Git version build: 4.0.0.541
* Thu May 09 2019 21:27:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.521
- New Git version build: 4.0.0.521
* Thu May 09 2019 19:57:29 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.516
- New Git version build: 4.0.0.516
* Thu May 09 2019 18:27:37 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.514
- New Git version build: 4.0.0.514
* Thu May 09 2019 16:57:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.512
- New Git version build: 4.0.0.512
* Thu May 09 2019 14:27:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.510
- New Git version build: 4.0.0.510
* Thu May 09 2019 13:57:34 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.508
- New Git version build: 4.0.0.508
* Thu May 09 2019 13:28:04 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.505
- New Git version build: 4.0.0.505
* Thu May 09 2019 01:28:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.503
- New Git version build: 4.0.0.503
* Wed May 08 2019 19:57:08 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.501
- New Git version build: 4.0.0.501
* Wed May 08 2019 16:27:34 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.494
- New Git version build: 4.0.0.494
* Wed May 08 2019 13:59:13 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.492
- New Git version build: 4.0.0.492
* Tue May 07 2019 14:28:28 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.490
- New Git version build: 4.0.0.490
* Mon May 06 2019 16:29:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.488
- New Git version build: 4.0.0.488
* Fri May 03 2019 21:29:12 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.483
- New Git version build: 4.0.0.483
* Fri May 03 2019 13:03:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.456
- New Git version build: 4.0.0.456
* Thu May 02 2019 17:27:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.444
- New Git version build: 4.0.0.444
* Thu May 02 2019 13:58:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.442
- New Git version build: 4.0.0.442
* Thu May 02 2019 00:50:55 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.440
- New Git version build: 4.0.0.440
* Wed May 01 2019 20:27:57 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.438
- New Git version build: 4.0.0.438
* Wed May 01 2019 17:28:29 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.430
- New Git version build: 4.0.0.430
* Sat Apr 27 2019 06:30:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 05:53:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 05:23:00 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 04:53:00 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 04:23:19 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 03:53:07 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 03:23:04 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 02:53:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 02:23:10 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 01:52:55 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 01:23:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 00:53:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Sat Apr 27 2019 00:41:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 23:52:54 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 23:23:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 22:52:54 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 22:23:21 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 21:53:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 21:23:28 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 20:53:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 20:23:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 19:53:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
* Fri Apr 26 2019 19:28:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.428
- New Git version build: 4.0.0.428
* Fri Apr 26 2019 18:53:32 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.426
* Fri Apr 26 2019 18:28:10 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.426
- New Git version build: 4.0.0.426
* Fri Apr 26 2019 17:53:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.424
* Fri Apr 26 2019 17:28:20 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.424
- New Git version build: 4.0.0.424
* Fri Apr 26 2019 16:53:37 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.378
* Fri Apr 26 2019 16:23:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.378
* Fri Apr 26 2019 15:59:11 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.378
- New Git version build: 4.0.0.378
* Wed Apr 24 2019 16:57:29 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.376
- New Git version build: 4.0.0.376
* Wed Apr 24 2019 15:27:18 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.374
- New Git version build: 4.0.0.374
* Wed Apr 24 2019 13:27:59 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.372
- New Git version build: 4.0.0.372
* Tue Apr 23 2019 20:57:38 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.370
- New Git version build: 4.0.0.370
* Tue Apr 23 2019 18:27:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.367
- New Git version build: 4.0.0.367
* Tue Apr 23 2019 17:58:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.365
- New Git version build: 4.0.0.365
* Mon Apr 22 2019 17:57:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.363
- New Git version build: 4.0.0.363
* Mon Apr 22 2019 16:57:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.361
- New Git version build: 4.0.0.361
* Mon Apr 22 2019 15:58:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.356
- New Git version build: 4.0.0.356
* Mon Apr 22 2019 01:40:11 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Mon Apr 22 2019 01:30:15 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 02:27:04 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 02:12:04 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 02:04:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 01:57:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 01:51:02 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:19:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:18:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:14:41 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:13:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:07:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:03:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Sat Apr 20 2019 00:01:54 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Fri Apr 19 2019 23:58:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
* Fri Apr 19 2019 23:55:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.354
- New Git version build: 4.0.0.354
* Thu Apr 18 2019 17:27:38 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.347
- New Git version build: 4.0.0.347
* Thu Apr 18 2019 16:57:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.345
- New Git version build: 4.0.0.345
* Thu Apr 18 2019 16:27:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.343
- New Git version build: 4.0.0.343
* Thu Apr 18 2019 12:57:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.341
- New Git version build: 4.0.0.341
* Thu Apr 18 2019 11:27:48 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.339
- New Git version build: 4.0.0.339
* Wed Apr 17 2019 23:28:51 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.337
- New Git version build: 4.0.0.337
* Wed Apr 17 2019 22:03:11 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 21:52:36 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 21:41:31 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 21:22:49 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 20:52:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 20:22:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 19:52:32 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 19:22:30 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 18:52:30 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 18:22:28 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 17:52:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 17:22:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 16:52:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 16:22:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 15:52:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 15:22:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 14:52:45 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 14:22:44 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 13:52:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
* Wed Apr 17 2019 13:27:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.335
- New Git version build: 4.0.0.335
* Wed Apr 17 2019 12:57:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.333
- New Git version build: 4.0.0.333
* Wed Apr 17 2019 10:57:26 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.329
- New Git version build: 4.0.0.329
* Tue Apr 16 2019 20:57:33 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.327
- New Git version build: 4.0.0.327
* Tue Apr 16 2019 20:27:13 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.325
- New Git version build: 4.0.0.325
* Tue Apr 16 2019 17:57:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.323
- New Git version build: 4.0.0.323
* Mon Apr 15 2019 21:27:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.321
- New Git version build: 4.0.0.321
* Mon Apr 15 2019 20:57:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.319
- New Git version build: 4.0.0.319
* Mon Apr 15 2019 18:57:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.315
- New Git version build: 4.0.0.315
* Mon Apr 15 2019 18:33:59 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.313
- New Git version build: 4.0.0.313
* Mon Apr 15 2019 17:27:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.311
- New Git version build: 4.0.0.311
* Mon Apr 15 2019 16:52:49 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.309
* Mon Apr 15 2019 16:23:07 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.309
* Mon Apr 15 2019 15:52:59 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.309
* Mon Apr 15 2019 15:27:38 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.309
- New Git version build: 4.0.0.309
* Mon Apr 15 2019 14:52:56 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.307
* Mon Apr 15 2019 14:27:34 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.307
- New Git version build: 4.0.0.307
* Mon Apr 15 2019 13:58:26 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.305
- New Git version build: 4.0.0.305
* Sat Apr 13 2019 11:57:41 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.301
- New Git version build: 4.0.0.301
* Fri Apr 12 2019 21:57:31 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.299
- New Git version build: 4.0.0.299
* Fri Apr 12 2019 20:57:58 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.297
- New Git version build: 4.0.0.297
* Fri Apr 12 2019 20:27:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.295
- New Git version build: 4.0.0.295
* Fri Apr 12 2019 17:27:19 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.291
- New Git version build: 4.0.0.291
* Fri Apr 12 2019 16:27:23 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.289
- New Git version build: 4.0.0.289
* Fri Apr 12 2019 15:57:51 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.284
- New Git version build: 4.0.0.284
* Thu Apr 11 2019 22:02:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.282
- New Git version build: 4.0.0.282
* Thu Apr 11 2019 18:27:26 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.280
- New Git version build: 4.0.0.280
* Thu Apr 11 2019 18:03:02 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.278
- New Git version build: 4.0.0.278
* Thu Apr 11 2019 16:28:19 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.276
- New Git version build: 4.0.0.276
* Wed Apr 10 2019 20:57:06 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.274
- New Git version build: 4.0.0.274
* Wed Apr 10 2019 20:27:06 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.272
- New Git version build: 4.0.0.272
* Wed Apr 10 2019 19:57:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.270
- New Git version build: 4.0.0.270
* Wed Apr 10 2019 19:28:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.266
- New Git version build: 4.0.0.266
* Wed Apr 10 2019 15:27:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.264
- New Git version build: 4.0.0.264
* Wed Apr 10 2019 14:57:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.259
- New Git version build: 4.0.0.259
* Wed Apr 10 2019 14:28:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.257
- New Git version build: 4.0.0.257
* Tue Apr 09 2019 21:27:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.255
- New Git version build: 4.0.0.255
* Tue Apr 09 2019 21:01:56 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.252
- New Git version build: 4.0.0.252
* Tue Apr 09 2019 19:57:08 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.248
- New Git version build: 4.0.0.248
* Tue Apr 09 2019 17:57:17 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.246
- New Git version build: 4.0.0.246
* Tue Apr 09 2019 15:57:17 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.244
- New Git version build: 4.0.0.244
* Tue Apr 09 2019 14:27:32 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.233
- New Git version build: 4.0.0.233
* Tue Apr 09 2019 11:57:57 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.229
- New Git version build: 4.0.0.229
* Mon Apr 08 2019 22:44:26 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.227
* Mon Apr 08 2019 21:22:48 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.227
* Mon Apr 08 2019 20:52:56 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.227
* Mon Apr 08 2019 20:27:31 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.227
- New Git version build: 4.0.0.227
* Mon Apr 08 2019 19:52:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.225
* Mon Apr 08 2019 19:22:48 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.225
* Mon Apr 08 2019 18:52:54 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.225
* Mon Apr 08 2019 18:27:41 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.225
- New Git version build: 4.0.0.225
* Mon Apr 08 2019 17:52:55 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.223
* Mon Apr 08 2019 17:27:50 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.223
- New Git version build: 4.0.0.223
* Mon Apr 08 2019 16:52:45 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.220
* Mon Apr 08 2019 16:22:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.220
* Mon Apr 08 2019 16:16:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.220
* Mon Apr 08 2019 15:22:52 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.220
* Mon Apr 08 2019 14:57:52 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.220
- New Git version build: 4.0.0.220
* Mon Apr 08 2019 01:25:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.216
* Mon Apr 08 2019 00:20:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.216
* Fri Apr 05 2019 19:27:08 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.216
- New Git version build: 4.0.0.216
* Fri Apr 05 2019 18:56:57 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.214
- New Git version build: 4.0.0.214
* Fri Apr 05 2019 17:26:42 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.212
- New Git version build: 4.0.0.212
* Fri Apr 05 2019 16:27:20 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.203
- New Git version build: 4.0.0.203
* Fri Apr 05 2019 15:57:21 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.201
- New Git version build: 4.0.0.201
* Fri Apr 05 2019 15:27:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.194
- New Git version build: 4.0.0.194
* Fri Apr 05 2019 14:57:20 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.186
- New Git version build: 4.0.0.186
* Fri Apr 05 2019 01:28:18 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.182
- New Git version build: 4.0.0.182
* Thu Apr 04 2019 23:28:23 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.180
- New Git version build: 4.0.0.180
* Thu Apr 04 2019 18:57:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.177
- New Git version build: 4.0.0.177
* Thu Apr 04 2019 15:56:55 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.175
- New Git version build: 4.0.0.175
* Thu Apr 04 2019 13:56:57 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.171
- New Git version build: 4.0.0.171
* Thu Apr 04 2019 13:28:09 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.169
- New Git version build: 4.0.0.169
* Wed Apr 03 2019 21:29:57 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.164
- New Git version build: 4.0.0.164
* Wed Apr 03 2019 19:57:17 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.162
- New Git version build: 4.0.0.162
* Wed Apr 03 2019 19:27:48 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.160
- New Git version build: 4.0.0.160
* Wed Apr 03 2019 18:57:05 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.158
- New Git version build: 4.0.0.158
* Wed Apr 03 2019 17:57:00 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.150
- New Git version build: 4.0.0.150
* Wed Apr 03 2019 16:27:31 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.148
- New Git version build: 4.0.0.148
* Wed Apr 03 2019 15:57:08 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.146
- New Git version build: 4.0.0.146
* Wed Apr 03 2019 14:57:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.144
- New Git version build: 4.0.0.144
* Wed Apr 03 2019 09:25:17 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 08:22:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 07:52:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 07:22:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 06:52:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 06:22:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 06:09:10 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 05:22:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 04:52:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 04:22:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 03:52:24 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 03:22:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 02:52:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 02:22:27 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 01:52:22 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 01:22:47 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 01:20:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
* Wed Apr 03 2019 01:15:03 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.142
- New Git version build: 4.0.0.142
* Tue Apr 02 2019 23:52:21 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 23:22:51 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 22:52:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 22:22:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 21:52:40 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 21:22:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 20:52:34 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 20:43:10 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 20:23:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 20:22:36 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 19:52:29 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 19:22:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 18:52:28 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
* Tue Apr 02 2019 18:27:15 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.140
- New Git version build: 4.0.0.140
* Tue Apr 02 2019 17:52:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.138
* Tue Apr 02 2019 17:22:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.138
* Tue Apr 02 2019 16:52:44 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.138
* Tue Apr 02 2019 16:27:18 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.138
- New Git version build: 4.0.0.138
* Tue Apr 02 2019 13:26:45 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.63
- New Git version build: 4.0.0.63
* Tue Apr 02 2019 12:27:21 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.61
- New Git version build: 4.0.0.61
* Mon Apr 01 2019 21:56:36 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.58
- New Git version build: 4.0.0.58
* Mon Apr 01 2019 20:56:39 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.56
- New Git version build: 4.0.0.56
* Mon Apr 01 2019 19:56:38 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.54
- New Git version build: 4.0.0.54
* Mon Apr 01 2019 18:32:21 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.52
- New Git version build: 4.0.0.52
* Mon Apr 01 2019 15:57:43 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.50
- New Git version build: 4.0.0.50
* Sun Mar 31 2019 02:57:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.48
- New Git version build: 4.0.0.48
* Fri Mar 29 2019 20:56:30 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.43
- New Git version build: 4.0.0.43
* Fri Mar 29 2019 19:56:44 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.41
- New Git version build: 4.0.0.41
* Fri Mar 29 2019 18:26:49 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.39
- New Git version build: 4.0.0.39
* Fri Mar 29 2019 17:26:58 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.37
- New Git version build: 4.0.0.37
* Fri Mar 29 2019 16:56:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.35
- New Git version build: 4.0.0.35
* Fri Mar 29 2019 15:27:23 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.33
- New Git version build: 4.0.0.33
* Fri Mar 29 2019 14:26:57 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.25
- New Git version build: 4.0.0.25
* Fri Mar 29 2019 13:27:16 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.23
- New Git version build: 4.0.0.23
* Fri Mar 29 2019 00:29:26 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.17
- New Git version build: 4.0.0.17
* Thu Mar 28 2019 23:48:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.15
* Thu Mar 28 2019 22:57:04 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.15
- New Git version build: 4.0.0.15
* Thu Mar 28 2019 18:27:25 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.2
- New Git version build: 4.0.0.2
* Thu Mar 28 2019 12:41:35 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.6
* Thu Mar 28 2019 12:00:16 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.6
* Thu Mar 28 2019 01:26:46 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.0
- New Git version build: 4.0.0.0
* Thu Mar 28 2019 00:57:53 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.6
- New Git version build: 4.0.0.6
* Wed Mar 27 2019 22:57:42 +0000 Martin Juhl <mj@casalogic.dk> 4.0.0.4
- New Git version build: 4.0.0.4
* Wed Mar 27 2019 17:56:43 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.398
- New Git version build: 3.0.1.398
* Wed Mar 27 2019 16:57:17 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.396
- New Git version build: 3.0.1.396
* Wed Mar 27 2019 16:27:11 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.394
- New Git version build: 3.0.1.394
* Wed Mar 27 2019 15:56:53 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.392
- New Git version build: 3.0.1.392
* Wed Mar 27 2019 14:27:17 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.390
- New Git version build: 3.0.1.390
* Tue Mar 26 2019 19:57:25 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.387
- New Git version build: 3.0.1.387
* Tue Mar 26 2019 19:27:51 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.384
- New Git version build: 3.0.1.384
* Tue Mar 26 2019 16:57:00 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.377
- New Git version build: 3.0.1.377
* Tue Mar 26 2019 15:29:25 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.375
- New Git version build: 3.0.1.375
* Tue Mar 26 2019 12:57:47 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.361
- New Git version build: 3.0.1.361
* Tue Mar 26 2019 12:29:27 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.358
- New Git version build: 3.0.1.358
* Mon Mar 25 2019 23:26:47 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.356
- New Git version build: 3.0.1.356
* Mon Mar 25 2019 22:56:55 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.353
- New Git version build: 3.0.1.353
* Mon Mar 25 2019 20:27:14 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.351
- New Git version build: 3.0.1.351
* Mon Mar 25 2019 19:57:03 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.349
- New Git version build: 3.0.1.349
* Mon Mar 25 2019 17:29:20 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.344
- New Git version build: 3.0.1.344
* Mon Mar 25 2019 16:07:53 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.340
- New Git version build: 3.0.1.340
* Mon Mar 25 2019 15:27:56 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.340
- New Git version build: 3.0.1.340
* Fri Mar 22 2019 20:57:05 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.338
- New Git version build: 3.0.1.338
* Fri Mar 22 2019 18:56:55 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.335
- New Git version build: 3.0.1.335
* Fri Mar 22 2019 16:57:07 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.333
- New Git version build: 3.0.1.333
* Fri Mar 22 2019 15:57:17 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.331
- New Git version build: 3.0.1.331
* Fri Mar 22 2019 01:23:03 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.327
- New Git version build: 3.0.1.327
* Fri Mar 22 2019 00:22:50 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.327
- New Git version build: 3.0.1.327
* Thu Mar 21 2019 23:52:53 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.327
- New Git version build: 3.0.1.327
* Thu Mar 21 2019 23:22:56 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.327
- New Git version build: 3.0.1.327
* Thu Mar 21 2019 23:01:33 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.327
- New Git version build: 3.0.1.327
* Thu Mar 21 2019 20:57:02 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.311
- New Git version build: 3.0.1.311
* Thu Mar 21 2019 19:27:03 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.309
- New Git version build: 3.0.1.309
* Thu Mar 21 2019 16:57:17 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.307
- New Git version build: 3.0.1.307
* Thu Mar 21 2019 16:26:27 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.305
- New Git version build: 3.0.1.305
* Thu Mar 21 2019 15:26:47 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.303
- New Git version build: 3.0.1.303
* Thu Mar 21 2019 14:56:31 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.281
- New Git version build: 3.0.1.281
* Thu Mar 21 2019 12:57:52 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.275
- New Git version build: 3.0.1.275
* Wed Mar 20 2019 20:26:45 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.273
- New Git version build: 3.0.1.273
* Wed Mar 20 2019 16:26:49 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.271
- New Git version build: 3.0.1.271
* Wed Mar 20 2019 15:57:09 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.269
- New Git version build: 3.0.1.269
* Tue Mar 19 2019 19:56:59 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.267
- New Git version build: 3.0.1.267
* Tue Mar 19 2019 12:27:25 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.265
- New Git version build: 3.0.1.265
* Mon Mar 18 2019 16:52:25 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.263
- New Git version build: 3.0.1.263
* Mon Mar 18 2019 14:56:30 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.261
- New Git version build: 3.0.1.261
* Mon Mar 18 2019 13:58:38 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.259
- New Git version build: 3.0.1.259
* Mon Mar 18 2019 13:27:29 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.257
- New Git version build: 3.0.1.257
* Sat Mar 16 2019 12:57:06 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.255
- New Git version build: 3.0.1.255
* Fri Mar 15 2019 15:26:32 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.253
- New Git version build: 3.0.1.253
* Fri Mar 15 2019 13:57:40 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.251
- New Git version build: 3.0.1.251
* Fri Mar 15 2019 13:27:19 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.246
- New Git version build: 3.0.1.246
* Fri Mar 15 2019 12:27:20 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.244
- New Git version build: 3.0.1.244
* Thu Mar 14 2019 20:28:02 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.242
- New Git version build: 3.0.1.242
* Thu Mar 14 2019 00:27:26 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.238
- New Git version build: 3.0.1.238
* Wed Mar 13 2019 18:57:18 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.236
- New Git version build: 3.0.1.236
* Wed Mar 13 2019 14:57:08 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.234
- New Git version build: 3.0.1.234
* Tue Mar 12 2019 19:58:48 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.232
- New Git version build: 3.0.1.232
* Tue Mar 12 2019 16:26:49 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.230
- New Git version build: 3.0.1.230
* Tue Mar 12 2019 15:26:57 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.228
- New Git version build: 3.0.1.228
* Tue Mar 12 2019 15:02:55 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.226
- New Git version build: 3.0.1.226
* Tue Mar 12 2019 14:27:03 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.226
- New Git version build: 3.0.1.226
* Mon Mar 11 2019 20:56:50 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.223
- New Git version build: 3.0.1.223
* Mon Mar 11 2019 15:57:54 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.221
- New Git version build: 3.0.1.221
* Fri Mar 08 2019 17:56:44 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.219
- New Git version build: 3.0.1.219
* Fri Mar 08 2019 16:27:12 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.217
- New Git version build: 3.0.1.217
* Fri Mar 08 2019 15:26:57 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.214
- New Git version build: 3.0.1.214
* Fri Mar 08 2019 14:26:46 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.212
- New Git version build: 3.0.1.212
* Thu Mar 07 2019 18:56:48 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.205
- New Git version build: 3.0.1.205
* Thu Mar 07 2019 17:26:47 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.201
- New Git version build: 3.0.1.201
* Thu Mar 07 2019 16:26:54 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.199
- New Git version build: 3.0.1.199
* Thu Mar 07 2019 15:56:49 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.194
- New Git version build: 3.0.1.194
* Thu Mar 07 2019 15:27:01 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.189
- New Git version build: 3.0.1.189
* Thu Mar 07 2019 14:57:09 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.186
- New Git version build: 3.0.1.186
* Wed Mar 06 2019 23:57:33 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.184
- New Git version build: 3.0.1.184
* Tue Mar 05 2019 17:26:56 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.182
- New Git version build: 3.0.1.182
* Mon Mar 04 2019 21:57:08 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.177
- New Git version build: 3.0.1.177
* Mon Mar 04 2019 21:27:56 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.173
- New Git version build: 3.0.1.173
* Fri Mar 01 2019 20:32:17 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.170
- New Git version build: 3.0.1.170
* Fri Mar 01 2019 16:27:20 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.167
- New Git version build: 3.0.1.167
* Thu Feb 28 2019 21:57:07 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.165
- New Git version build: 3.0.1.165
* Thu Feb 28 2019 21:27:37 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.137
- New Git version build: 3.0.1.137
* Thu Feb 28 2019 18:57:16 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.135
- New Git version build: 3.0.1.135
* Thu Feb 28 2019 14:56:54 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.130
- New Git version build: 3.0.1.130
* Thu Feb 28 2019 13:57:31 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.128
- New Git version build: 3.0.1.128
* Wed Feb 27 2019 17:27:04 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.126
- New Git version build: 3.0.1.126
* Wed Feb 27 2019 16:27:22 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.124
- New Git version build: 3.0.1.124
* Mon Feb 25 2019 18:27:14 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.120
- New Git version build: 3.0.1.120
* Fri Feb 22 2019 18:56:39 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.114
- New Git version build: 3.0.1.114
* Fri Feb 22 2019 18:26:47 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.109
- New Git version build: 3.0.1.109
* Thu Feb 21 2019 21:26:44 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.107
- New Git version build: 3.0.1.107
* Thu Feb 21 2019 18:57:13 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.105
- New Git version build: 3.0.1.105
* Thu Feb 21 2019 18:26:35 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.102
- New Git version build: 3.0.1.102
* Thu Feb 21 2019 16:27:00 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.99
- New Git version build: 3.0.1.99
* Wed Feb 20 2019 20:26:44 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.97
- New Git version build: 3.0.1.97
* Wed Feb 20 2019 19:56:30 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.94
- New Git version build: 3.0.1.94
* Wed Feb 20 2019 17:26:40 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.92
- New Git version build: 3.0.1.92
* Wed Feb 20 2019 16:26:22 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.89
- New Git version build: 3.0.1.89
* Wed Feb 20 2019 15:56:49 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.87
- New Git version build: 3.0.1.87
* Tue Feb 19 2019 17:56:34 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.84
- New Git version build: 3.0.1.84
* Tue Feb 19 2019 17:27:12 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.82
- New Git version build: 3.0.1.82
* Mon Feb 18 2019 21:27:11 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.80
- New Git version build: 3.0.1.80
* Fri Feb 15 2019 22:26:55 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.78
- New Git version build: 3.0.1.78
* Fri Feb 15 2019 16:56:54 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.72
- New Git version build: 3.0.1.72
* Fri Feb 15 2019 15:57:11 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.70
- New Git version build: 3.0.1.70
* Thu Feb 14 2019 22:56:32 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.68
- New Git version build: 3.0.1.68
* Thu Feb 14 2019 21:56:29 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.65
- New Git version build: 3.0.1.65
* Thu Feb 14 2019 21:26:45 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.63
- New Git version build: 3.0.1.63
* Thu Feb 14 2019 16:56:35 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.59
- New Git version build: 3.0.1.59
* Thu Feb 14 2019 16:26:35 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.55
- New Git version build: 3.0.1.55
* Thu Feb 14 2019 15:56:25 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.53
- New Git version build: 3.0.1.53
* Thu Feb 14 2019 15:26:17 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.42
- New Git version build: 3.0.1.42
* Thu Feb 14 2019 14:26:39 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.39
- New Git version build: 3.0.1.39
* Thu Feb 14 2019 13:57:35 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.37
- New Git version build: 3.0.1.37
* Wed Feb 13 2019 23:26:44 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.35
- New Git version build: 3.0.1.35
* Wed Feb 13 2019 22:27:08 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.33
- New Git version build: 3.0.1.33
* Wed Feb 13 2019 20:26:48 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.31
- New Git version build: 3.0.1.31
* Wed Feb 13 2019 18:29:35 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.29
- New Git version build: 3.0.1.29
* Wed Feb 13 2019 15:26:35 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.27
- New Git version build: 3.0.1.27
* Wed Feb 13 2019 14:56:48 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.25
- New Git version build: 3.0.1.25
* Tue Feb 12 2019 22:56:45 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.17
- New Git version build: 3.0.1.17
* Tue Feb 12 2019 18:56:43 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.14
- New Git version build: 3.0.1.14
* Mon Feb 11 2019 19:00:13 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.12
- New Git version build: 3.0.1.12
* Mon Feb 11 2019 17:32:16 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.10
- New Git version build: 3.0.1.10
* Mon Feb 11 2019 16:57:26 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.7
- New Git version build: 3.0.1.7
* Mon Feb 11 2019 15:28:24 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.5
- New Git version build: 3.0.1.5
* Mon Feb 11 2019 14:57:09 +0000 Martin Juhl <mj@casalogic.dk> 3.0.1.2
- New Git version build: 3.0.1.2
* Fri Feb 08 2019 19:57:06 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.128
- New Git version build: 3.0.0.128
* Fri Feb 08 2019 14:57:13 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.126
- New Git version build: 3.0.0.126
* Thu Feb 07 2019 21:56:14 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.124
- New Git version build: 3.0.0.124
* Thu Feb 07 2019 21:26:31 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.122
- New Git version build: 3.0.0.122
* Thu Feb 07 2019 19:56:46 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.120
- New Git version build: 3.0.0.120
* Thu Feb 07 2019 16:57:22 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.118
- New Git version build: 3.0.0.118
* Thu Feb 07 2019 15:27:55 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.113
- New Git version build: 3.0.0.113
* Wed Feb 06 2019 17:26:54 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.111
- New Git version build: 3.0.0.111
* Wed Feb 06 2019 16:57:07 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.109
- New Git version build: 3.0.0.109
* Wed Feb 06 2019 01:58:08 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.107
- New Git version build: 3.0.0.107
* Wed Feb 06 2019 01:28:52 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.105
- New Git version build: 3.0.0.105
* Tue Feb 05 2019 22:58:19 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.102
- New Git version build: 3.0.0.102
* Tue Feb 05 2019 19:27:06 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.100
- New Git version build: 3.0.0.100
* Tue Feb 05 2019 17:57:18 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.98
- New Git version build: 3.0.0.98
* Tue Feb 05 2019 13:57:42 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.96
- New Git version build: 3.0.0.96
* Mon Feb 04 2019 17:27:34 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.94
- New Git version build: 3.0.0.94
* Sat Feb 02 2019 12:27:23 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.92
- New Git version build: 3.0.0.92
* Fri Feb 01 2019 21:57:03 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.90
- New Git version build: 3.0.0.90
* Fri Feb 01 2019 17:57:08 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.88
- New Git version build: 3.0.0.88
* Fri Feb 01 2019 14:27:12 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.84
- New Git version build: 3.0.0.84
* Thu Jan 31 2019 16:59:19 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.82
- New Git version build: 3.0.0.82
* Thu Jan 31 2019 14:57:28 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.80
- New Git version build: 3.0.0.80
* Wed Jan 30 2019 18:57:09 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.78
- New Git version build: 3.0.0.78
* Wed Jan 30 2019 18:26:54 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.74
- New Git version build: 3.0.0.74
* Wed Jan 30 2019 17:57:31 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.72
- New Git version build: 3.0.0.72
* Tue Jan 29 2019 21:57:00 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.68
- New Git version build: 3.0.0.68
* Tue Jan 29 2019 21:27:01 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.66
- New Git version build: 3.0.0.66
* Tue Jan 29 2019 20:27:41 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.63
- New Git version build: 3.0.0.63
* Tue Jan 29 2019 12:34:40 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.59
- New Git version build: 3.0.0.59
* Tue Jan 29 2019 12:21:57 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.59
- New Git version build: 3.0.0.59
* Tue Jan 29 2019 11:38:33 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 11:28:55 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 11:21:49 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 11:15:39 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 11:00:51 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:43:34 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:40:44 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:38:02 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:36:15 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:34:50 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:19:27 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 10:06:59 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 08:41:56 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 08:30:13 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 08:26:27 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 08:23:31 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Tue Jan 29 2019 08:15:00 +0000 Martin Juhl <mj@casalogic.dk> 3.0.0.0
- New Git version build: 3.0.0.0
* Thu Jan 17 2019 14:50:45 +0000 Martin Juhl <m@rtinjuhl.dk> 3.0.0.0
- New Version v.3.0.0
* Thu Jan 17 2019 14:50:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 14:42:30 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 14:14:13 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 14:12:06 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 13:34:11 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 13:15:48 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 12:51:30 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 06:45:28 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 06:43:54 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 01:34:56 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Thu Jan 17 2019 00:52:54 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:52:46 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:46:16 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:27:19 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:14:55 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:11:23 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:08:25 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 23:05:55 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 22:59:19 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Wed Jan 16 2019 22:23:41 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.75
- New Git version build: 2.1.2.75
* Tue Jan 15 2019 18:28:18 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.59
- New Git version build: 2.1.2.59
* Tue Jan 15 2019 14:29:14 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.57
- New Git version build: 2.1.2.57
* Mon Jan 14 2019 17:59:01 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.48
- New Git version build: 2.1.2.48
* Fri Jan 11 2019 20:28:52 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.46
- New Git version build: 2.1.2.46
* Fri Jan 11 2019 15:27:53 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.44
- New Git version build: 2.1.2.44
* Fri Jan 11 2019 13:57:54 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.42
- New Git version build: 2.1.2.42
* Fri Jan 11 2019 13:28:36 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.40
- New Git version build: 2.1.2.40
* Mon Jan 07 2019 19:58:42 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.38
- New Git version build: 2.1.2.38
* Sat Jan 05 2019 01:21:20 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.36
- New Git version build: 2.1.2.36
* Sat Jan 05 2019 00:56:33 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.36
- New Git version build: 2.1.2.36
* Sat Jan 05 2019 00:35:25 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.36
- New Git version build: 2.1.2.36
* Fri Jan 04 2019 23:25:59 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.36
- New Git version build: 2.1.2.36
* Wed Jan 02 2019 19:32:59 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.34
- New Git version build: 2.1.2.34
* Thu Dec 20 2018 22:45:08 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.32
- New Git version build: 2.1.2.32
* Wed Dec 19 2018 14:28:21 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.29
- New Git version build: 2.1.2.29
* Tue Dec 18 2018 12:29:18 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.26
- New Git version build: 2.1.2.26
* Mon Dec 17 2018 15:28:37 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.15
- New Git version build: 2.1.2.15
* Fri Dec 14 2018 20:00:49 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.13
- New Git version build: 2.1.2.13
* Thu Dec 13 2018 18:29:17 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.9
- New Git version build: 2.1.2.9
* Thu Dec 13 2018 13:28:34 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.7
- New Git version build: 2.1.2.7
* Thu Dec 13 2018 01:32:09 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.5
- New Git version build: 2.1.2.5
* Wed Dec 12 2018 15:58:24 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.3
- New Git version build: 2.1.2.3
* Tue Dec 11 2018 18:31:09 +0000 Martin Juhl <mj@casalogic.dk> 2.1.2.1
- New Git version build: 2.1.2.1
* Tue Dec 11 2018 17:58:57 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.42
- New Git version build: 2.1.1.42
* Mon Dec 10 2018 16:58:41 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.40
- New Git version build: 2.1.1.40
* Mon Dec 10 2018 01:13:38 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.0
- New Git version build: 2.1.1.0
* Fri Dec 07 2018 21:57:57 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.36
- New Git version build: 2.1.1.36
* Fri Dec 07 2018 20:58:13 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.34
- New Git version build: 2.1.1.34
* Fri Dec 07 2018 20:28:23 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.32
- New Git version build: 2.1.1.32
* Fri Dec 07 2018 15:04:01 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.30
- New Git version build: 2.1.1.30
* Fri Dec 07 2018 09:55:25 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.27
- New Git version build: 2.1.1.27
* Thu Dec 06 2018 14:47:37 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.23
- New Git version build: 2.1.1.23
* Tue Dec 04 2018 23:22:48 +0000 Martin Juhl <mj@casalogic.dk> 2.1.1.21
- New Git version build: 2.1.1.21
* Wed Nov 28 2018 04:38:17 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.384
- New Git version build: 2.1.0.384
* Wed Nov 28 2018 04:07:46 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.382
- New Git version build: 2.1.0.382
* Tue Nov 27 2018 22:38:39 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.380
- New Git version build: 2.1.0.380
* Tue Nov 27 2018 18:08:36 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.280
- New Git version build: 2.1.0.280
* Tue Nov 27 2018 16:08:46 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.276
- New Git version build: 2.1.0.276
* Tue Nov 27 2018 15:38:12 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.274
- New Git version build: 2.1.0.274
* Mon Nov 26 2018 19:08:27 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.272
- New Git version build: 2.1.0.272
* Mon Nov 26 2018 17:08:02 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.270
- New Git version build: 2.1.0.270
* Mon Nov 26 2018 16:09:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.267
- New Git version build: 2.1.0.267
* Wed Nov 21 2018 20:38:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.265
- New Git version build: 2.1.0.265
* Wed Nov 21 2018 19:38:36 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.263
- New Git version build: 2.1.0.263
* Wed Nov 21 2018 15:37:46 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.261
- New Git version build: 2.1.0.261
* Wed Nov 21 2018 03:37:59 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.258
- New Git version build: 2.1.0.258
* Tue Nov 20 2018 21:38:35 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.256
- New Git version build: 2.1.0.256
* Tue Nov 20 2018 20:39:48 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.254
- New Git version build: 2.1.0.254
* Tue Nov 20 2018 18:38:57 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.251
- New Git version build: 2.1.0.251
* Tue Nov 20 2018 17:08:09 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.249
- New Git version build: 2.1.0.249
* Tue Nov 20 2018 16:08:18 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.247
- New Git version build: 2.1.0.247
* Tue Nov 20 2018 15:37:36 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.245
- New Git version build: 2.1.0.245
* Tue Nov 20 2018 14:38:05 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.243
- New Git version build: 2.1.0.243
* Tue Nov 20 2018 09:07:37 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.241
- New Git version build: 2.1.0.241
* Tue Nov 20 2018 03:38:05 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.239
- New Git version build: 2.1.0.239
* Mon Nov 19 2018 19:39:36 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.196
- New Git version build: 2.1.0.196
* Mon Nov 19 2018 19:09:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.194
- New Git version build: 2.1.0.194
* Mon Nov 19 2018 18:09:32 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.192
- New Git version build: 2.1.0.192
* Mon Nov 19 2018 17:38:37 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.190
- New Git version build: 2.1.0.190
* Mon Nov 19 2018 17:07:52 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.186
- New Git version build: 2.1.0.186
* Mon Nov 19 2018 16:09:21 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.181
- New Git version build: 2.1.0.181
* Mon Nov 19 2018 15:38:37 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.179
- New Git version build: 2.1.0.179
* Mon Nov 19 2018 14:38:21 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.177
- New Git version build: 2.1.0.177
* Mon Nov 19 2018 14:08:32 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.169
- New Git version build: 2.1.0.169
* Fri Nov 16 2018 22:38:23 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.167
- New Git version build: 2.1.0.167
* Fri Nov 16 2018 22:10:24 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.164
- New Git version build: 2.1.0.164
* Fri Nov 16 2018 20:07:58 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.162
- New Git version build: 2.1.0.162
* Fri Nov 16 2018 16:08:06 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.160
- New Git version build: 2.1.0.160
* Fri Nov 16 2018 15:38:20 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.158
- New Git version build: 2.1.0.158
* Thu Nov 15 2018 20:41:16 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.155
- New Git version build: 2.1.0.155
* Thu Nov 15 2018 20:09:49 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.153
- New Git version build: 2.1.0.153
* Thu Nov 15 2018 15:38:13 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.151
- New Git version build: 2.1.0.151
* Thu Nov 15 2018 14:38:26 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.147
- New Git version build: 2.1.0.147
* Wed Nov 14 2018 22:37:50 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.143
- New Git version build: 2.1.0.143
* Wed Nov 14 2018 16:38:00 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.141
- New Git version build: 2.1.0.141
* Tue Nov 13 2018 21:39:33 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.139
- New Git version build: 2.1.0.139
* Tue Nov 13 2018 20:41:43 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.137
- New Git version build: 2.1.0.137
* Tue Nov 13 2018 16:08:16 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.135
- New Git version build: 2.1.0.135
* Mon Nov 12 2018 19:09:05 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.131
- New Git version build: 2.1.0.131
* Mon Nov 12 2018 11:17:22 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.129
- New Git version build: 2.1.0.129
* Fri Nov 09 2018 05:39:07 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.119
- New Git version build: 2.1.0.119
* Thu Nov 08 2018 23:09:35 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.0
- New Git version build: 2.1.0.0
* Thu Nov 08 2018 21:13:19 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.117
- New Git version build: 2.1.0.117
* Thu Nov 08 2018 20:39:11 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.115
- New Git version build: 2.1.0.115
* Thu Nov 08 2018 16:38:18 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.113
- New Git version build: 2.1.0.113
* Thu Nov 08 2018 15:38:09 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.97
- New Git version build: 2.1.0.97
* Thu Nov 08 2018 13:08:08 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.94
- New Git version build: 2.1.0.94
* Thu Nov 08 2018 12:38:12 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.92
- New Git version build: 2.1.0.92
* Thu Nov 08 2018 07:07:47 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.89
- New Git version build: 2.1.0.89
* Thu Nov 08 2018 03:07:57 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.86
- New Git version build: 2.1.0.86
* Wed Nov 07 2018 21:37:34 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.83
- New Git version build: 2.1.0.83
* Wed Nov 07 2018 21:10:18 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.81
- New Git version build: 2.1.0.81
* Wed Nov 07 2018 20:39:30 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.78
- New Git version build: 2.1.0.78
* Wed Nov 07 2018 18:09:03 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.76
- New Git version build: 2.1.0.76
* Wed Nov 07 2018 09:50:18 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.74
- New Git version build: 2.1.0.74
* Tue Nov 06 2018 21:39:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.74
- New Git version build: 2.1.0.74
* Tue Nov 06 2018 20:40:32 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.72
- New Git version build: 2.1.0.72
* Tue Nov 06 2018 20:10:16 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.68
- New Git version build: 2.1.0.68
* Tue Nov 06 2018 17:37:32 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.66
- New Git version build: 2.1.0.66
* Tue Nov 06 2018 17:07:29 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.64
- New Git version build: 2.1.0.64
* Tue Nov 06 2018 15:37:51 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.60
- New Git version build: 2.1.0.60
* Tue Nov 06 2018 02:07:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.58
- New Git version build: 2.1.0.58
* Mon Nov 05 2018 16:37:31 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.49
- New Git version build: 2.1.0.49
* Mon Nov 05 2018 15:38:34 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.47
- New Git version build: 2.1.0.47
* Mon Nov 05 2018 14:18:37 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Mon Nov 05 2018 14:11:03 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Mon Nov 05 2018 14:05:06 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Mon Nov 05 2018 14:02:44 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Mon Nov 05 2018 13:51:04 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Mon Nov 05 2018 13:32:55 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Mon Nov 05 2018 13:29:55 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Fri Nov 02 2018 19:08:19 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.45
- New Git version build: 2.1.0.45
* Fri Nov 02 2018 15:38:15 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.43
- New Git version build: 2.1.0.43
* Fri Nov 02 2018 15:08:22 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.40
- New Git version build: 2.1.0.40
* Thu Nov 01 2018 21:08:45 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.38
- New Git version build: 2.1.0.38
* Thu Nov 01 2018 17:07:42 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.36
- New Git version build: 2.1.0.36
* Thu Nov 01 2018 16:08:02 +0000 Martin Juhl <mj@casalogic.dk> 2.1.0.0
- New Git version build: 2.1.0.0
* Thu Nov 01 2018 15:08:07 +0000 Martin Juhl <mj@casalogic.dk> 2.0.2.0
- New Git version build: 2.0.2.0
* Fri Oct 12 2018 09:43:14 +0000 Martin Juhl <mj@casalogic.dk> 2.0.1
- New Git version build: 2.0.1
* Thu Oct 11 2018 13:51:00 +0000 Martin Juhl <mj@casalogic.dk> 2.0.1
- New Git version build: 2.0.1
* Thu Oct 04 2018 08:59:15 +0000 Martin Juhl <mj@casalogic.dk> 2.0.0
- New Git version build: 2.0.0
* Mon Oct 01 2018 14:36:51 +0000 Martin Juhl <mj@casalogic.dk> 1.0.8.22
- New Git version build: 1.0.8.22
* Fri Sep 28 2018 14:36:30 +0000 Martin Juhl <mj@casalogic.dk> 1.0.8.18
- New Git version build: 1.0.8.18
* Wed Sep 26 2018 21:07:06 +0000 Martin Juhl <mj@casalogic.dk> 1.0.8.16
- New Git version build: 1.0.8.16
* Wed Sep 26 2018 12:17:23 +0000 Martin Juhl <mj@casalogic.dk> 1.0.8.14
- New Git version build: 1.0.8.14
* Mon Sep 24 2018 19:37:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.9
- New Git version build: 1.0.7.9
* Thu Sep 20 2018 22:07:18 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.8
- New Git version build: 1.0.7.8
* Tue Sep 18 2018 18:36:45 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.7
- New Git version build: 1.0.7.7
* Tue Sep 18 2018 17:06:39 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.6
- New Git version build: 1.0.7.6
* Tue Sep 18 2018 13:07:22 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.5
- New Git version build: 1.0.7.5
* Tue Aug 28 2018 08:53:44 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.4
- New Git version build: 1.0.7.4
* Fri Aug 17 2018 23:43:22 +0000 Martin Juhl <mj@casalogic.dk> 1.0.7.3
- New Git version build: 1.0.7.3
* Fri Aug 10 2018 04:08:26 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.47
- New Git version build: 1.0.6.47
* Fri Aug 10 2018 03:39:33 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.46
- New Git version build: 1.0.6.46
* Thu Aug 09 2018 14:10:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.44
- New Git version build: 1.0.6.44
* Thu Aug 02 2018 20:10:18 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.43
- New Git version build: 1.0.6.43
* Thu Aug 02 2018 17:39:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.42
- New Git version build: 1.0.6.42
* Thu Jul 26 2018 16:37:26 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.41
- New Git version build: 1.0.6.41
* Thu Jul 26 2018 13:37:43 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.40
- New Git version build: 1.0.6.40
* Tue Jul 24 2018 16:37:24 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.39
- New Git version build: 1.0.6.39
* Tue Jul 24 2018 16:08:29 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.38
- New Git version build: 1.0.6.38
* Wed Jul 18 2018 20:37:48 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.37
- New Git version build: 1.0.6.37
* Wed Jul 18 2018 16:38:26 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.36
- New Git version build: 1.0.6.36
* Mon Jul 16 2018 19:08:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.35
- New Git version build: 1.0.6.35
* Mon Jul 16 2018 18:37:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.34
- New Git version build: 1.0.6.34
* Mon Jul 16 2018 18:06:37 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.33
- New Git version build: 1.0.6.33
* Mon Jul 16 2018 17:07:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.31
- New Git version build: 1.0.6.31
* Mon Jul 16 2018 14:37:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.30
- New Git version build: 1.0.6.30
* Mon Jul 16 2018 14:09:16 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.29
- New Git version build: 1.0.6.29
* Fri Jul 13 2018 16:17:23 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.28
- New Git version build: 1.0.6.28
* Fri Jul 13 2018 13:53:22 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.27
- New Git version build: 1.0.6.27
* Tue Jul 10 2018 19:52:42 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.26
- New Git version build: 1.0.6.26
* Mon Jul 09 2018 16:49:21 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.25
- New Git version build: 1.0.6.25
* Mon Jul 09 2018 14:54:38 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.24
- New Git version build: 1.0.6.24
* Mon Jun 25 2018 20:37:47 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.23
- New Git version build: 1.0.6.23
* Mon Jun 25 2018 20:08:45 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.22
- New Git version build: 1.0.6.22
* Mon Jun 25 2018 17:38:52 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.18
- New Git version build: 1.0.6.18
* Mon Jun 18 2018 18:39:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.17
- New Git version build: 1.0.6.17
* Tue Jun 12 2018 12:38:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.16
- New Git version build: 1.0.6.16
* Mon Jun 04 2018 21:10:31 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.15
- New Git version build: 1.0.6.15
* Thu May 31 2018 20:38:37 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.14
- New Git version build: 1.0.6.14
* Thu May 31 2018 14:08:30 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.13
- New Git version build: 1.0.6.13
* Wed May 30 2018 14:39:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.12
- New Git version build: 1.0.6.12
* Thu May 24 2018 19:07:22 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.11
- New Git version build: 1.0.6.11
* Thu May 24 2018 17:00:21 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.10
- New Git version build: 1.0.6.10
* Thu May 24 2018 16:06:56 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.10
- New Git version build: 1.0.6.10
* Thu May 17 2018 20:37:49 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.8
- New Git version build: 1.0.6.8
* Tue May 15 2018 20:36:48 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.7
- New Git version build: 1.0.6.7
* Tue May 15 2018 18:07:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.6
- New Git version build: 1.0.6.6
* Fri May 04 2018 23:19:25 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.5
- New Git version build: 1.0.6.5
* Fri May 04 2018 23:02:53 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.5
- New Git version build: 1.0.6.5
* Tue May 01 2018 08:06:33 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.3
- New Git version build: 1.0.6.3
* Fri Apr 27 2018 20:35:57 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.1
- New Git version build: 1.0.6.1
* Fri Apr 27 2018 16:36:01 +0000 Martin Juhl <mj@casalogic.dk> 1.0.6.0
- New Git version build: 1.0.6.0
* Fri Apr 27 2018 16:06:08 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.33
- New Git version build: 1.0.5.33
* Thu Apr 26 2018 18:06:36 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.32
- New Git version build: 1.0.5.32
* Wed Apr 25 2018 19:35:55 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.31
- New Git version build: 1.0.5.31
* Wed Apr 25 2018 15:36:18 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.30
- New Git version build: 1.0.5.30
* Fri Apr 20 2018 18:06:30 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.29
- New Git version build: 1.0.5.29
* Fri Apr 20 2018 13:36:30 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.28
- New Git version build: 1.0.5.28
* Fri Apr 20 2018 03:06:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.27
- New Git version build: 1.0.5.27
* Wed Apr 18 2018 15:06:13 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.26
- New Git version build: 1.0.5.26
* Tue Apr 17 2018 15:36:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.25
- New Git version build: 1.0.5.25
* Mon Apr 16 2018 21:36:32 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.24
- New Git version build: 1.0.5.24
* Wed Apr 11 2018 17:06:05 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.23
- New Git version build: 1.0.5.23
* Thu Apr 05 2018 18:35:28 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.22
- New Git version build: 1.0.5.22
* Thu Apr 05 2018 15:35:37 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.21
- New Git version build: 1.0.5.21
* Tue Apr 03 2018 23:35:33 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.20
- New Git version build: 1.0.5.20
* Thu Mar 29 2018 00:19:40 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.19
- New Git version build: 1.0.5.19
* Wed Mar 28 2018 13:08:48 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.14
- New Git version build: 1.0.5.14
* Tue Mar 27 2018 16:05:37 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.13
- New Git version build: 1.0.5.13
* Mon Mar 26 2018 19:35:13 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.11
- New Git version build: 1.0.5.11
* Mon Mar 26 2018 18:35:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.7
- New Git version build: 1.0.5.7
* Mon Mar 26 2018 17:35:32 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.6
- New Git version build: 1.0.5.6
* Mon Mar 26 2018 16:35:28 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.5
- New Git version build: 1.0.5.5
* Mon Mar 26 2018 15:36:50 +0000 Martin Juhl <mj@casalogic.dk> 1.0.5.3
- New Git version build: 1.0.5.3
* Mon Mar 26 2018 14:35:15 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.134
- New Git version build: 1.0.4.134
* Mon Mar 26 2018 14:05:17 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.132
- New Git version build: 1.0.4.132
* Mon Mar 26 2018 13:35:13 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.131
- New Git version build: 1.0.4.131
* Fri Mar 23 2018 17:05:03 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.130
- New Git version build: 1.0.4.130
* Fri Mar 23 2018 15:04:58 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.129
- New Git version build: 1.0.4.129
* Fri Mar 23 2018 14:04:52 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.128
- New Git version build: 1.0.4.128
* Thu Mar 22 2018 19:35:04 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.126
- New Git version build: 1.0.4.126
* Thu Mar 22 2018 12:35:13 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.125
- New Git version build: 1.0.4.125
* Thu Mar 22 2018 02:04:48 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.124
- New Git version build: 1.0.4.124
* Thu Mar 22 2018 00:04:51 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.123
- New Git version build: 1.0.4.123
* Wed Mar 21 2018 20:05:11 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.122
- New Git version build: 1.0.4.122
* Wed Mar 21 2018 19:05:14 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.121
- New Git version build: 1.0.4.121
* Wed Mar 21 2018 18:35:09 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.119
- New Git version build: 1.0.4.119
* Wed Mar 21 2018 16:05:10 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.118
- New Git version build: 1.0.4.118
* Wed Mar 21 2018 03:35:28 +0000 Martin Juhl <mj@casalogic.dk> 1.0.4.115
- New Git version build: 1.0.4.115
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
