%global commit e4bcf6b50c81684e63a612577237929f7a7944ad
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       davs2
Version:    1.6
Release:    1%{?dist}
Summary:    An open-source decoder of AVS2-P2/IEEE1857.4 video coding standard
URL:        https://github.com/pkuvcl/davs2
License:    GPLv2

Source:     https://github.com/pkuvcl/davs2/archive/%{commit}.tar.gz#/%{name}-%{shortcommit}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  nasm >= 2.13
Requires:   %{name}-libs = %{version}-%{release}

%description
davs2 is an open-source decoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the command line decoder.

%package libs
Summary:    AVS2-P2/IEEE1857.4 decoder library

%description libs
davs2 is an open-source decoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the shared library.

%package devel
Summary:    AVS2-P2/IEEE1857.4 decoder library development files
Requires:   %{name} = %{version}-%{release}

%description devel
davs2 is an open-source decoder of AVS2-P2/IEEE1857.4 video coding standard.

This package contains the shared library development files.

%prep
%autosetup -n %{name}-%{commit}

%build
pushd build/linux
%configure \
    --bit-depth='8' \
    --chroma-format='all' \
    --disable-static \
    --enable-pic \
    --enable-shared

%make_build

%install
pushd build/linux
%make_install install-cli install-lib-shared

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}

%files libs
%{_libdir}/lib%{name}.so.16

%files devel
%{_includedir}/%{name}.h
%{_includedir}/%{name}_config.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog

* Thu Jul 11 2019 Unitedrpms Project <unitedrpms AT protonmail DOT com> - 1.6-1
- Initial build.
