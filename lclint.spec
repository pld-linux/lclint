Summary:	An implementation of the lint program
Name:		lclint
Version:	2.5q
Release:	1
Source0:        http://lclint.cs.virginia.edu/%{name}-%{version}.src.tar.gz
Source1:        http://lclint.cs.virginia.edu/%{name}-guide.tar.gz
Patch1:		%{name}-Makefile.patch
Patch2:		%{name}-proto.patch
Patch3:		%{name}-time.patch
URL:		http://lclint.cs.virginia.edu
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
Scans C source code for mistakes and bad style.

%prep
%setup -q -a 1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure

# XXX Do NOT simplify the build here or lclint will NOT have correct defaults!
# XXX The lclint top level Makefile invokes "make -e" and is subtly BROKEN!
make -C src \
    CC="cc -DSTDC_HEADERS=1 $CFLAGS" \
    LINKFLAGS="$LDFLAGS -lfl" \
    DEFAULT_CPP=cpp \
    BISON=/usr/bin/bison \
    FLEX=/usr/bin/flex \
    DEFAULT_LARCHPATH=\".:%{_libdir}/%{name}/lib\" \
    DEFAULT_LCLIMPORTDIR=\".:%{_libdir}/%{name}/imports\" \
    SYSTEM_LIBDIR=\"%{_prefix}\" \
	updateversion localconstants lclint && mv src/lclint bin/lclint

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz lclint-guide emacs
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
