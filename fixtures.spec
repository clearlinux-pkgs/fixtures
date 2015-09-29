#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fixtures
Version  : 1.3.1
Release  : 17
URL      : https://pypi.python.org/packages/source/f/fixtures/fixtures-1.3.1.tar.gz
Source0  : https://pypi.python.org/packages/source/f/fixtures/fixtures-1.3.1.tar.gz
Summary  : Fixtures, reusable state for writing clean tests and more.
Group    : Development/Tools
License  : Apache-2.0
Requires: fixtures-python
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
Requires: six-python
Requires: testtools-python

%description python
python components for the fixtures package.


%prep
%setup -q -n fixtures-1.3.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check ||:
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
