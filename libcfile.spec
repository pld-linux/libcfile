# see m4/${libname}.m4 />= for required version of particular library
%define		libcerror_ver	20120425
%define		libclocale_ver	20120425
%define		libcnotify_ver	20120425
%define		libuna_ver	20181006
Summary:	Library to support cross-platform C file functions
Summary(pl.UTF-8):	Biblioteka wspierająca wieloplatformowe funkcje obsługi plików w C
Name:		libcfile
Version:	20190314
Release:	1
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libcfile/releases
Source0:	https://github.com/libyal/libcfile/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	12751f850be67cf3b9aac14dc885f210
URL:		https://github.com/libyal/libcfile/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	libcerror >= %{libcerror_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libuna >= %{libuna_ver}
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
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libclocale-devel >= %{libclocale_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libuna-devel >= %{libuna_ver}

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

%build
%{__gettextize}
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
