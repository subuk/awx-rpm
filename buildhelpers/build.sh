#!/bin/sh
set -e
set -x

SPECFILE="/source/$1"

yum install -y rpmdevtools yum-utils fakeroot centos-release-scl
yum install -y wget
wget -O /etc/yum.repos.d/ansible-awx.repo https://copr.fedorainfracloud.org/coprs/mrmeee/ansible-awx/repo/epel-7/mrmeee-ansible-awx-epel-7.repo

yum -y install python3-rpm-macros python-rpm-macros rh-python36-build rh-python36-python rh-python36-python-devel gcc make libffi-devel openssl-devel libxml2-devel libxslt-devel gcc-c++ rh-postgresql10-postgresql-devel openldap-devel xmlsec1-devel libxml2-devel xmlsec1-openssl-devel libtool-ltdl-devel rh-python36-python-sphinx rh-python36-python-six

ln -s /opt/rh/rh-python36/root/usr/bin/python3 /usr/bin/python3.6

ln -s /opt/rh/rh-python36/root/usr/bin/sphinx-build /opt/rh/rh-python36/root/usr/bin/sphinx-build-3

ln -s /opt/rh/rh-postgresql10/root/usr/bin/pg_config /usr/bin/pg_config

ln -s /usr/include/libxml2/libxml /usr/include/libxml

export LC_CTYPE=en_US.UTF-8

useradd -s /bin/bash builder || true
chown builder. /cache -R

pushd /source
	spectool -g $SPECFILE
	yum-builddep -y $SPECFILE
popd

su builder -c /bin/bash <<EOF
set -e
set -x

mkdir -p /cache/builder-cache-dir
ln -sf /cache/builder-cache-dir ~/.cache

cat > ~/.rpmmacros <<EOT
%_topdir /tmp/buildd
EOT

mkdir -p /tmp/buildd/{BUILD,BUILDROOT,RPMS,SPECS,SRPMS}

ln -s /source /tmp/buildd/SOURCES

fakeroot-sysv rpmbuild -ba $SPECFILE
EOF

find /tmp/buildd/RPMS /tmp/buildd/SRPMS -type f |xargs -I{} -n1 cp {} /result
