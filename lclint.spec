Summary:	An implementation of the lint program
Name:		lclint
Version:	2.5q
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://lclint.cs.virginia.edu/%{name}-%{version}.src.tar.gz
Source1:	http://lclint.cs.virginia.edu/guide/%{name}-guide.tar.gz
Source2:	%{name}.wmconfig
Patch0:		%{name}.patch
Patch1:		%{name}-optimization.patch
URL:		http://lclint.cs.virginia.edu/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
Scans C source code for mistakes and bad style.

%prep
%setup -q
%setup -q -a 1
%patch
#%patch1 -p1

%configure

%build
%{__make}
#make test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README lclint-guide emacs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/lclint
%{_libdir}/lclint
