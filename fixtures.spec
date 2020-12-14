#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x597240FE94E60165 (rbtcollins@hp.com)
#
Name     : fixtures
Version  : 3.0.0
Release  : 62
URL      : http://pypi.debian.net/fixtures/fixtures-3.0.0.tar.gz
Source0  : http://pypi.debian.net/fixtures/fixtures-3.0.0.tar.gz
Source1  : http://pypi.debian.net/fixtures/fixtures-3.0.0.tar.gz.asc
Summary  : Fixtures, reusable state for writing clean tests and more.
Group    : Development/Tools
License  : Apache-2.0
Requires: fixtures-license = %{version}-%{release}
Requires: fixtures-python = %{version}-%{release}
Requires: fixtures-python3 = %{version}-%{release}
Requires: six
Requires: testtools
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : python-mock
BuildRequires : six
BuildRequires : testtools

%description
*************************************************************
fixtures: Fixtures with cleanups for testing and convenience.
*************************************************************

%package license
Summary: license components for the fixtures package.
Group: Default

%description license
license components for the fixtures package.


%package python
Summary: python components for the fixtures package.
Group: Default
Requires: fixtures-python3 = %{version}-%{release}

%description python
python components for the fixtures package.


%package python3
Summary: python3 components for the fixtures package.
Group: Default
Requires: python3-core
Provides: pypi(fixtures)
Requires: pypi(pbr)
Requires: pypi(six)
Requires: pypi(testtools)

%description python3
python3 components for the fixtures package.


%prep
%setup -q -n fixtures-3.0.0
cd %{_builddir}/fixtures-3.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603392030
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check ||:
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fixtures
cp %{_builddir}/fixtures-3.0.0/Apache-2.0 %{buildroot}/usr/share/package-licenses/fixtures/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/fixtures-3.0.0/COPYING %{buildroot}/usr/share/package-licenses/fixtures/f1d3863d5c6cea245b5c0fdb48328da659094db7
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fixtures/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/fixtures/f1d3863d5c6cea245b5c0fdb48328da659094db7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
