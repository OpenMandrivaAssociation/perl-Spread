Summary:	Perl extension for the Spread group communication system 
Name:		perl-Spread
Version:	1.07
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org
Source0:	http://search.cpan.org/CPAN/authors/id/J/JE/JESUS/Spread-3.17.3-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	spread-devel
BuildRequires:	chrpath
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Spread is a Perl module that conveniently wraps the Spread C libraries provided
with the Spread 3.17.3 distribution. Spread is available at
http://www.spread.org/. Spread is a local/wide area group communication toolkit
that runs on most modern operating systems. It allows convenient mechanisms for
reliable multicasting information between applications as well as providing
many more complicate assurances.

%prep

%setup -q -n Spread-3.17.3-%{version} 

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

# nuke rpath
find %{buildroot} -name "*.so" | xargs chrpath -d

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/*/auto/Spread/*
%{perl_vendorlib}/*/*.pm
%{_mandir}/*/*


