#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Interpolate
Summary:	String::Interpolate - Wrapper for builtin the Perl interpolation engine
Summary(pl):	String::Interpolate - obudowanie do wbudowanego w Perla silnika interpoluj�cego
Name:		perl-String-Interpolate
Version:	0.1
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9cb6615142b1f29822d6bde1a22cdbc7
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::Interpolate provides a neat interface to the solution to that
perennial Perl problem - how to invoke the Perl string interpolation
engine on a string contained in a scalar variable.

%description -l pl
String::Interpolate udost�pnia mi�y interfejs rozwi�zuj�cy ten
odwieczny problem Perla - jak wywo�a� perlowy silnik interpoluj�cy
�a�cuchy na �a�cuchu zawartym w zmiennej skalarnej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
