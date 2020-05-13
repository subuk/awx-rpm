#!/bin/bash
set -e
mkdir -p /tmp/cache

BUILD_SCRIPT=`pwd`/buildhelpers/build.sh
case "$1" in
    "amazonlinux-2017.03")
        DOCKER_IMAGE=ctbuild/amazonlinux:2017.03
        YUM_CONFIG=`pwd`/buildhelpers/amazonlinux2017.03.yum.conf
    ;;
    "centos-7")
        DOCKER_IMAGE=ctbuild/centos:7
        YUM_CONFIG=`pwd`/buildhelpers/centos7.yum.conf
    ;;
    *)
        echo "Usage: $0 [centos-7|amazonlinux-2017.03]"
        exit 1
esac

exec docker run --rm -i \
    -v /home/awx/awx-rpm:/source \
    -v /home/awx/awx-rpm/result:/result \
    -v /tmp/cache:/cache \
    -v $YUM_CONFIG:/etc/yum.conf \
    -v $BUILD_SCRIPT:/build.sh \
    $DOCKER_IMAGE /build.sh awx-build.spec
