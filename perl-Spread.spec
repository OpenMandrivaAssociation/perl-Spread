%define upstream_name    Spread
%define upstream_version 3.17.4.4

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Perl extension for the Spread group communication system 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/J/JE/JESUS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	libspread-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Spread is a Perl module that conveniently wraps the Spread C libraries provided
with the Spread 3.17.3 distribution. Spread is available at
http://www.spread.org/. Spread is a local/wide area group communication toolkit
that runs on most modern operating systems. It allows convenient mechanisms for
reliable multicasting information between applications as well as providing
many more complicate assurances.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# fix paths
perl -pi -e "s|^\\\$SPLIB_LIB.*|\\\$SPLIB_LIB=\'-L%{_libdir}\'\;|g" Makefile.PL
perl -pi -e "s|^\\\$SPLIB_INCLUDE.*|\\\$SPLIB_INCLUDE=\'-I%{_includedir}\'\;|g" Makefile.PL

# fix permissions
chmod 644 README

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/auto/Spread
%{perl_vendorarch}/Spread.pm
%{_mandir}/*/*
