%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	Valid
Summary:	This module determines whether an email address is valid
Summary(pl):	Modu³ sprawdzaj±cy poprawno¶æ adresu e-mail
Name:		perl-%{pdir}-%{pnam}
Version:	0.14
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8cd22c54c580d6709ec71448f2332da2
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-MailTools
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module determines whether an email address is well-formed, and
optionally, whether a mail host exists for the domain.

%description -l pl
Ten modu³ sprawdza czy adres e-mail jest poprawnie zapisany i,
opcjonalnie, czy istnieje host przyjmuj±cy pocztê.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name .packlist | xargs -r rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/man3/*
