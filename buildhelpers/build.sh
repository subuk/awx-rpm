#!/bin/sh
set -e
set -x

SPECFILE="/root/rpmbuild/SOURCES/$1"
#cat $SPECFILE

yum install -y centos-release-scl wget

yum -y update

wget -O /etc/yum.repos.d/ansible-awx.repo https://copr.fedorainfracloud.org/coprs/mrmeee/ansible-awx/repo/epel-7/mrmeee-ansible-awx-epel-7.repo

yum -y install scl-utils-build libcurl-devel rh-python36-pycparser rh-python36-pbr rh-python36-cffi python3-rpm-macros python-rpm-macros rh-python36-build rh-python36-setuptools_scm rh-python36-python rh-python36-python-devel gcc make libffi-devel openssl-devel libxml2-devel libxslt-devel gcc-c++ rh-postgresql10-postgresql-devel openldap-devel xmlsec1-devel libxml2-devel xmlsec1-openssl-devel libtool-ltdl-devel rh-python36-python-sphinx rh-python36-six sqlite

yum-builddep -y $SPECFILE

rpmbuild -ba $SPECFILE

cp /root/rpmbuild/SRPMS/* /result
cp /root/rpmbuild/RPMS/*/* /result
