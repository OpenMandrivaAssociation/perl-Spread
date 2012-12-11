%define upstream_name    Spread
%define upstream_version 3.17.4.4

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.17.4.4-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 3.17.4.4-2mdv2011.0
+ Revision: 556146
- rebuild for perl 5.12

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 3.17.4.4-1mdv2010.1
+ Revision: 460775
- update to 3.17.4.4

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 3.17.4.3-1mdv2010.0
+ Revision: 409060
- update to 3.17.4.3

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 3.17.4.2-1mdv2010.0
+ Revision: 408857
- update to 3.17.4.2

* Tue Feb 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.17.4.1-2mdv2009.1
+ Revision: 344580
- rebuild

* Fri Aug 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.17.4.1-1mdv2009.0
+ Revision: 272264
- new version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.07-6mdv2009.0
+ Revision: 258361
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.07-5mdv2009.0
+ Revision: 246423
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.07-3mdv2008.1
+ Revision: 152760
- fix libspread-devel BR
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.07-2mdv2007.0
+ Revision: 113870
- Import perl-Spread

* Fri Jan 26 2007 Oden Eriksson <oeriksson@mandriva.com> 1.07-2mdv2007.1
- rebuild

* Tue Dec 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.07-1mdk
- initial Mandriva package

