#
# Conditional build:
%bcond_without	tests	 # don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Interpolate
Summary:	String::Interpolate - wrapper for builtin the Perl interpolation engine
Summary(pl):	String::Interpolate - obudowanie do wbudowanego w Perla silnika interpolującego
Name:		perl-String-Interpolate
Version:	0.2
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8da264f3261422e32e118885be770943
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::Interpolate provides a neat interface to the solution to that
perennial Perl problem - how to invoke the Perl string interpolation
engine on a string contained in a scalar variable.

%description -l pl
String::Interpolate udostępnia miły interfejs rozwiązujący ten
odwieczny problem Perla - jak wywołać perlowy silnik interpolujący
łańcuchy na łańcuchu zawartym w zmiennej skalarnej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
