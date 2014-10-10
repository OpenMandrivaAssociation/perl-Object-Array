%define realname   Object-Array
%define upstream_version    0.060

Name:       perl-%{realname}
Version:    %perl_convert_version %{upstream_version}
Release:    5
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Array references with accessors
Source:     http://www.cpan.org/modules/by-module/Object/Object-Array-%{upstream_version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRequires: perl-devel
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Sub::Install)
BuildRequires: perl(List::MoreUtils)

BuildArch: noarch

%description
Add methods to Object::Array corresponding to functions from
List::MoreUtils.

%prep
%setup -q -n %{realname}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
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


