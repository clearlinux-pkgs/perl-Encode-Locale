#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Encode-Locale
Version  : 1.05
Release  : 40
URL      : https://cpan.metacpan.org/authors/id/G/GA/GAAS/Encode-Locale-1.05.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GAAS/Encode-Locale-1.05.tar.gz
Summary  : 'Determine the locale encoding'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Encode-Locale-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Encode-Locale
==============
The purpose of this Perl module is try determine what encodings should be used
when interfacing to various external interfaces.  You will need perl-5.8 or
better to use this module.

%package dev
Summary: dev components for the perl-Encode-Locale package.
Group: Development
Provides: perl-Encode-Locale-devel = %{version}-%{release}
Requires: perl-Encode-Locale = %{version}-%{release}

%description dev
dev components for the perl-Encode-Locale package.


%package perl
Summary: perl components for the perl-Encode-Locale package.
Group: Default
Requires: perl-Encode-Locale = %{version}-%{release}

%description perl
perl components for the perl-Encode-Locale package.


%prep
%setup -q -n Encode-Locale-1.05
cd %{_builddir}/Encode-Locale-1.05

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Encode::Locale.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Encode/Locale.pm
