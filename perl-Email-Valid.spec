#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Email
%define		pnam	Valid
Summary:	Email::Valid - module determines whether an email address is valid
Summary(pl.UTF-8):	Email::Valid - moduł sprawdzający poprawność adresu e-mail
Name:		perl-Email-Valid
Version:	0.187
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	190b9293fde117c7f8ce30058c79745f
URL:		http://search.cpan.org/dist/Email-Valid/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-MailTools
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module determines whether an email address is well-formed, and
optionally, whether a mail host exists for the domain.

%description -l pl.UTF-8
Ten moduł sprawdza czy adres e-mail jest poprawnie zapisany i,
opcjonalnie, czy istnieje host przyjmujący pocztę.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Email/*.pm
%{_mandir}/man3/*
