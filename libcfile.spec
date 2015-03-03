Summary:	Library to support cross-platform C file functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje obsługi plików w C
Name:		libcfile
Version:	20150101
Release:	2
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libcfile/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d0be08f6cdbb85262e9943596d3b256d
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libcfile/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libclocale-devel >= 20120425
BuildRequires:	libcnotify-devel >= 20120425
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libuna-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Requires:	libcerror >= 20120425
Requires:	libclocale >= 20120425
Requires:	libcnotify >= 20120425
Requires:	libcstring >= 20120425
Requires:	libuna >= 20120425
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libcfile is a library to support cross-platform C file functions.

%description -l pl.UTF-8
libcfile to biblioteka wspierająca wieloplatformowe funkcje obsługi
plików w C.

%package devel
Summary:	Header files for libcfile library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libcfile
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libcerror-devel >= 20120425
Requires:	libclocale-devel >= 20120425
Requires:	libcnotify-devel >= 20120425
Requires:	libcstring-devel >= 20120425
Requires:	libuna-devel >= 20120425

%description devel
Header files for libcfile library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libcfile.

%package static
Summary:	Static libcfile library
Summary(pl.UTF-8):	Statyczna biblioteka libcfile
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libcfile library.

%description static -l pl.UTF-8
Statyczna biblioteka libcfile.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libcfile.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libcfile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcfile.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcfile.so
%{_includedir}/libcfile
%{_includedir}/libcfile.h
%{_pkgconfigdir}/libcfile.pc
%{_mandir}/man3/libcfile.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libcfile.a
