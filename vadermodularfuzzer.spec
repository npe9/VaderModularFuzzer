Name:           vadermodularfuzzer
Version:        1.0.0
Release:        1%{?dist}
Summary:        Vader Modular Fuzzer (VMF)
License:        GPLv2
URL:            https://github.com/draperlaboratory/vadermodularfuzzer
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.10
BuildRequires:  clang
BuildRequires:  llvm-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  libcurl-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-rtd-theme

Requires:       python3
Requires:       python3-pip
Requires:       afl++
Requires:       afl++-clang

%description
A modular fuzzer that is easily reconfigurable to use many different
capabilities and approaches. Also includes a web-based distributed
fuzzing infrastructure.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
This package contains the documentation for VMF, including:
* API documentation
* User manual
* Developer guide

%prep
%autosetup -p1

%build
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_BUILD_TYPE=Release \
    -DPYTHON_SITE_PACKAGES=%{python3_sitelib}
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datadir}/%{name}/*
%{_mandir}/man1/*

%files doc
%doc docs/
%{_docdir}/%{name}/

%changelog
* Tue Apr 09 2024 VMF Team <vmf@draper.com> - 1.0.0-1
- Initial package 