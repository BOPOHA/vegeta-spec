%global		debug_package	%{nil}

%define		pkg_release	1

Name:		vegeta
Version:	12.2.0
Release:	%{pkg_release}%{?dist}
Summary:	HTTP load testing tool

License:	MIT
URL:		https://github.com/tsenart/vegeta
Source0:        https://github.com/tsenart/vegeta/releases/download/cli/v%{version}/vegeta-%{version}-linux-amd64.tar.gz

#Requires(pre): shadow-utils

%description
    Vegeta is a versatile HTTP load testing tool built out of a need 
    to drill HTTP services with a constant request rate.

%prep
%setup -c 

%install
#   create installation hierarchy
    %{__mkdir} -p %{buildroot}%{_bindir}
    %{__mkdir} -p %{buildroot}%{_docdir}/%{name}
    %{__cp}   -p %{_builddir}/%{name}-%{version}/%{name}    %{buildroot}%{_bindir}/%{name}
    %{__cp}   -p %{_builddir}/%{name}-%{version}/CHANGELOG  %{buildroot}%{_docdir}/%{name}/
    %{__cp}   -p %{_builddir}/%{name}-%{version}/LICENSE    %{buildroot}%{_docdir}/%{name}/
    %{__cp}   -p %{_builddir}/%{name}-%{version}/README.md  %{buildroot}%{_docdir}/%{name}/


%files
%{_bindir}/%{name}
%doc %{_docdir}/%{name}/*
%docdir %{_docdir}/%{name}

%clean
%{__rm} -rf %{buildroot}
%{__rm} -rf %{_builddir}/%{name}-%{version}


%changelog
* Tue Jan 29 2019 Anatolii Vorona <vorona.tolik@gmail.com>
- init COPR repo

