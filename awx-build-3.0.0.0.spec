%define  debug_package %{nil}
%define _prefix /opt/awx
%define _mandir %{_prefix}/share/man
%global __os_install_post %{nil}

%define ansible_version 3.0.0.0
%define service_user awx
%define service_group awx
%define service_homedir /var/lib/awx
%define service_logdir /var/log/tower
%define service_configdir /etc/tower

Summary: Ansible AWX
Name: ansible-awx
Version: 3.0.0
Release: 7%{dist}
Source0: /dist/awx-3.0.0.tar.gz
Source1: settings.py.dist
%if 0%{?el7}
Source2: awx-cbreceiver.service
Source3: awx-dispatcher.service
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
AutoReqProv: false

BuildRequires: libcurl-devel
BuildRequires: libffi-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: libxslt-devel
BuildRequires: openldap-devel
BuildRequires: rh-postgresql10-postgresql-devel
BuildRequires: rh-python36-Django
BuildRequires: rh-python36-PyYAML
BuildRequires: rh-python36-Twisted
BuildRequires: rh-python36-autobahn
BuildRequires: rh-python36-build
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
BuildRequires: rh-python36-idna
BuildRequires: rh-python36-incremental
BuildRequires: rh-python36-inflect
BuildRequires: rh-python36-irc
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
BuildRequires: rh-python36-more-itertools
BuildRequires: rh-python36-oauthlib
BuildRequires: rh-python36-pexpect
BuildRequires: rh-python36-psutil
BuildRequires: rh-python36-psycopg2
BuildRequires: rh-python36-ptyprocess
BuildRequires: rh-python36-pyasn1
BuildRequires: rh-python36-pyasn1-modules
BuildRequires: rh-python36-pygerduty
BuildRequires: rh-python36-pyparsing
BuildRequires: rh-python36-python
BuildRequires: rh-python36-python-dateutil
BuildRequires: rh-python36-python-devel
BuildRequires: rh-python36-python-djangorestframework
BuildRequires: rh-python36-python-djangorestframework-yaml
BuildRequires: rh-python36-python-jinja2
BuildRequires: rh-python36-python-ldap
BuildRequires: rh-python36-python-logstash
BuildRequires: rh-python36-python-pip
BuildRequires: rh-python36-python-pygments
BuildRequires: rh-python36-python-wheel
BuildRequires: rh-python36-python3-openid
BuildRequires: rh-python36-pytz
BuildRequires: rh-python36-requests
BuildRequires: rh-python36-requests-futures
BuildRequires: rh-python36-scldevel
BuildRequires: rh-python36-six
BuildRequires: rh-python36-slackclient
BuildRequires: rh-python36-social-auth-app-django
BuildRequires: rh-python36-social-auth-core
BuildRequires: rh-python36-tempora
BuildRequires: rh-python36-twilio
BuildRequires: rh-python36-txaio
BuildRequires: rh-python36-urllib3
BuildRequires: rh-python36-websocket_client
BuildRequires: rh-python36-zope.interface
BuildRequires: xmlsec1-devel
BuildRequires: xmlsec1-openssl-devel

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
Requires: rh-python36-PyYAML
Requires: rh-python36-Twisted
Requires: rh-python36-autobahn
Requires: rh-python36-build
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
Requires: rh-python36-idna
Requires: rh-python36-incremental
Requires: rh-python36-inflect
Requires: rh-python36-irc
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
Requires: rh-python36-more-itertools
Requires: rh-python36-oauthlib
Requires: rh-python36-pexpect
Requires: rh-python36-psutil
Requires: rh-python36-psycopg2
Requires: rh-python36-ptyprocess
Requires: rh-python36-pyasn1
Requires: rh-python36-pyasn1-modules
Requires: rh-python36-pygerduty
Requires: rh-python36-pyparsing
Requires: rh-python36-python
Requires: rh-python36-python
Requires: rh-python36-python-dateutil
Requires: rh-python36-python-devel
Requires: rh-python36-python-djangorestframework
Requires: rh-python36-python-djangorestframework-yaml
Requires: rh-python36-python-jinja2
Requires: rh-python36-python-jinja2
Requires: rh-python36-python-ldap
Requires: rh-python36-python-logstash
Requires: rh-python36-python-markupsafe
Requires: rh-python36-python-pip
Requires: rh-python36-python-pygments
Requires: rh-python36-python-pygments
Requires: rh-python36-python-wheel
Requires: rh-python36-python3-openid
Requires: rh-python36-pytz
Requires: rh-python36-requests
Requires: rh-python36-requests-futures
Requires: rh-python36-runtime
Requires: rh-python36-scldevel
Requires: rh-python36-scldevel
Requires: rh-python36-six
Requires: rh-python36-slackclient
Requires: rh-python36-social-auth-app-django
Requires: rh-python36-social-auth-core
Requires: rh-python36-tempora
Requires: rh-python36-twilio
Requires: rh-python36-txaio
Requires: rh-python36-urllib3
Requires: rh-python36-websocket_client
Requires: rh-python36-zope.interface
Requires: subversion
Requires: xmlsec1-devel
Requires: xmlsec1-openssl-devel

Requires(pre): /usr/sbin/useradd, /usr/bin/getent
%{?systemd_requires}

%description
%{summary}

%prep
%setup -q -n awx-3.0.0

%install
# Setup build environment
mkdir -p $RPM_BUILD_ROOT/opt/rh/rh-python36/root/usr/
scl enable rh-python36 "pip3 install --root=$RPM_BUILD_ROOT ."

# Collect django static
cat > _awx_rpmbuild_collectstatic_settings.py <<EOF
from awx.settings.defaults import *
DEFAULTS_SNAPSHOT = {}
STATIC_ROOT = "static/"
EOF

export DJANGO_SETTINGS_MODULE="_awx_rpmbuild_collectstatic_settings"
export PYTHONPATH="$PYTHONPATH:."
mkdir -p static/
scl enable rh-python36 rh-postgresql10 "$RPM_BUILD_ROOT/opt/rh/rh-python36/root/usr/bin/awx-manage collectstatic --noinput --clear"

# Cleanup
unset PYTHONPATH
unset DJANGO_SETTINGS_MODULE

mkdir -p %{buildroot}%{service_homedir}
mkdir -p %{buildroot}%{service_logdir}
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}%{service_configdir}
mkdir -p %{buildroot}/var/lib/awx/
echo 3.0.0 > %{buildroot}%{service_homedir}/.tower_version


cp %{_sourcedir}/settings.py.dist %{buildroot}%{service_configdir}/settings.py
mv static %{buildroot}%{_prefix}/static

%if 0%{?el7}
# Install systemd configuration
mkdir -p %{buildroot}%{_unitdir}
for service in awx-cbreceiver awx-dispatcher awx-channels-worker awx-daphne awx-web; do
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

%pre
/usr/bin/getent group %{service_group} >/dev/null || /usr/sbin/groupadd --system %{service_group}
/usr/bin/getent passwd %{service_user} >/dev/null || /usr/sbin/useradd --no-create-home --system -g %{service_group} --home-dir %{service_homedir} -s /sbin/nologin %{service_user}

%post
%if 0%{?el7}
%systemd_post awx-cbreceiver
%systemd_post awx-dispatcher
%systemd_post awx-channels-worker
%systemd_post awx-daphne
%systemd_post awx-web
%endif

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
%attr(0755, awx, awx) %{_prefix}/static
%dir %attr(0750, %{service_user}, %{service_group}) %{service_homedir}
%{service_homedir}/.tower_version
%dir %attr(0770, root, %{service_group}) %{service_logdir}
%config(noreplace) %{service_configdir}/settings.py
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/usr/share/doc/awx/
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/awx
/opt/awx/bin/python
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/awx-3.0.0.dist-info
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/usr/bin/ansible-tower-service
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/usr/bin/ansible-tower-setup
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/usr/bin/awx-python
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/usr/bin/failure-event-handler
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/usr/share/awx
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/usr/share/sosreport/sos/plugins/__pycache__/tower.cpython-36.pyc
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/usr/share/sosreport/sos/plugins/tower.py
/opt/rh/rh-python36/root/usr/lib/python3.6/site-packages/var/lib/awx

%if 0%{?el7}
%attr(0644, root, root) %{_unitdir}/awx-cbreceiver.service
%attr(0644, root, root) %{_unitdir}/awx-dispatcher.service
%attr(0644, root, root) %{_unitdir}/awx-channels-worker.service
%attr(0644, root, root) %{_unitdir}/awx-daphne.service
%attr(0644, root, root) %{_unitdir}/awx-web.service
%endif

%changelog
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
