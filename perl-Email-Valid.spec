%include	/usr/lib/rpm/macros.perl
%define         pdir Email
%define         pnam Valid

Summary:	This module determines whether an email address is valid
Name:		perl-%{pdir}-%{pnam}
Version:	0.13
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	libpcap-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module determines whether an email address is well-formed, and                                    
optionally, whether a mail host exists for the domain.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
gzip -9nf README Changes
find $RPM_BUILD_ROOT -name .packlist | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
%doc *.gz
