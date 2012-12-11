
%define realname   Object-Array
%define version    0.060
%define release    %mkrel 3

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Array references with accessors
Source:     http://www.cpan.org/modules/by-module/Object/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Install)
BuildRequires: perl(List::MoreUtils)

BuildArch: noarch

%description
Add methods to Object::Array corresponding to functions from
List::MoreUtils.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.060-3mdv2011.0
+ Revision: 655150
- rebuild for updated spec-helper

* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.060-2mdv2011.0
+ Revision: 375936
- rebuild

* Sun Mar 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.060-1mdv2009.1
+ Revision: 355237
- adding missing buildrequires
- import perl-Object-Array


* Fri Feb 20 2009 cpan2dist 0.060-1mdv
- initial mdv release, generated with cpan2dist

