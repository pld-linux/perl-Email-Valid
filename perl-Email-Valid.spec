%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	Valid
Summary:	Email::Valid - module determines whether an email address is valid
Summary(pl):	Email::Valid - modu³ sprawdzaj±cy poprawno¶æ adresu e-mail
Name:		perl-%{pdir}-%{pnam}
Version:	0.15
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	371b1552b81b93ffbf89cf2b1c1376c5
BuildRequires:	perl-devel >= 5.6
%if %{!?_without_tests:1}0
BuildRequires:	perl-MailTools
%endif
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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
