#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x597240FE94E60165 (rbtcollins@hp.com)
#
Name     : fixtures
Version  : 3.0.0
Release  : 31
URL      : http://pypi.debian.net/fixtures/fixtures-3.0.0.tar.gz
Source0  : http://pypi.debian.net/fixtures/fixtures-3.0.0.tar.gz
Source99 : http://pypi.debian.net/fixtures/fixtures-3.0.0.tar.gz.asc
Summary  : Fixtures, reusable state for writing clean tests and more.
Group    : Development/Tools
License  : Apache-2.0
Requires: fixtures-python
Requires: docutils
Requires: pbr
Requires: python-mock
Requires: six
Requires: testtools
BuildRequires : configparser-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : linecache2-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : traceback2-python
BuildRequires : unittest2-python

%description
*************************************************************
fixtures: Fixtures with cleanups for testing and convenience.
*************************************************************

%package python
Summary: python components for the fixtures package.
Group: Default

%description python
python components for the fixtures package.


%prep
%setup -q -n fixtures-3.0.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489279986
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check ||:
%install
export SOURCE_DATE_EPOCH=1489279986
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
