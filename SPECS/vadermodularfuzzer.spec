Name:           vadermodularfuzzer
Version:        0.0.3
Release:        1%{?dist}
Summary:        Vader Modular Fuzzer - A modular fuzzing framework for security testing

License:        MIT
URL:            https://github.com/draperlaboratory/VaderModularFuzzer
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools

Requires:       python3
Requires:       python3-pip
Requires:       python3-setuptools

%description
Vader Modular Fuzzer is a modular fuzzing framework for security testing.
This package provides the Vader Modular Fuzzer tool for automated
security testing and vulnerability discovery.

%prep
%autosetup

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make_build

%install
%make_install
install -d %{buildroot}%{_docdir}/%{name}
install -m 644 README.md %{buildroot}%{_docdir}/%{name}/
install -m 644 LICENSE %{buildroot}%{_docdir}/%{name}/

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_libdir}/*
%{_datadir}/%{name}/*

%changelog
* $(date +"%a %b %d %Y") Draper Laboratory <vadermodularfuzzer@draper.com> - 0.0.3-1
- Initial package release 