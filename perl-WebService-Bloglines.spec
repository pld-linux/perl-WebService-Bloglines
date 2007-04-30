#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WebService
%define	pnam	Bloglines
Summary:	WebService::Bloglines - Easy-to-use Interface for Bloglines Web Services
#Summary(pl.UTF-8):	
Name:		perl-WebService-Bloglines
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WebService/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	11b0b072a9bc6b1f4301d8a7c8b4e69f
URL:		http://search.cpan.org/dist/WebService-Bloglines/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-libwww
BuildRequires:	perl-XML-Liberal >= 0.02
BuildRequires:	perl-XML-RSS-LibXML >= 0.09
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WebService::Bloglines priovides you an Object Oriented interface for
Bloglines Web Services (BWS). It currently supports Notifier API and
Sync API. See http://www.bloglines.com/services/api/ for details.

# %description -l pl.UTF-8
# TODO

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
%doc Changes
%{perl_vendorlib}/WebService/*.pm
%{perl_vendorlib}/WebService/Bloglines
%{_mandir}/man3/*
