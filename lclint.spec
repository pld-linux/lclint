Summary:	An implementation of the lint program
Summary(pl.UTF-8):	Implementacja programu lint
Name:		lclint
Version:	2.5q
Release:	7
License:	GPL
Group:		Development/Tools
Source0:	http://lclint.cs.virginia.edu/%{name}-%{version}.src.tar.gz
# Source0-md5:	c4c798823fe25780124dfd65933fe1ed
Source1:	http://lclint.cs.virginia.edu/%{name}-guide.tar.gz
# Source1-md5:	72ff5d63471f65f53427d6b7863363c4
Patch1:		%{name}-Makefile.patch
Patch2:		%{name}-proto.patch
Patch3:		%{name}-time.patch
URL:		http://lclint.cs.virginia.edu/
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scans C source code for mistakes and bad style.

%description -l pl.UTF-8
Program szukający w źródłach w C błędów i złego stylu.

%prep
%setup -q -a 1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure

# XXX Do NOT simplify the build here or lclint will NOT have correct defaults!
# XXX The lclint top level Makefile invokes "make -e" and is subtly BROKEN!
%{__make} -C src updateversion localconstants lclint \
	CC="%{__cc} %{rpmcflags} -DSTDC_HEADERS=1" \
	CCOPT="\$(CC)" \
	LINKFLAGS="%{rpmldflags} -lfl" \
	DEFAULT_CPP=cpp \
	BISON=/usr/bin/bison \
	FLEX=/usr/bin/flex \
	DEFAULT_LARCHPATH=\".:%{_libdir}/%{name}/lib\" \
	DEFAULT_LCLIMPORTDIR=\".:%{_libdir}/%{name}/imports\" \
	SYSTEM_LIBDIR=\"%{_prefix}\"

# " -for vim
mv src/lclint bin/lclint

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README lclint-guide emacs
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/%{name}
