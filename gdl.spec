%define name gdl
%define version 2.31.3
%define release %mkrel 1
%define api 1
%define major 3
%define libname %mklibname %name %api %major
%define libnamedev %mklibname -d %name

Summary: Gnome Devtool Libraries
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/gdl/%{name}-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxml2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gtk+2-devel
BuildRequires: intltool
BuildRequires: chrpath
BuildRequires: gtk-doc

%description
This package contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta2.

The current pieces of GDL include:

 - A symbol browser bonobo component (symbol-browser-control).

 - A docking widget (gdl).

 - A utility library that also contains the stubs and skels for
   the symbol browser and text editor components (gdl, idl).

%package -n %libname
Group: System/Libraries
Summary: Gnome Devtool Libraries - shared library
Requires: %name >= %version

%description -n %libname
This package contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta2.

The current pieces of GDL include:

 - A symbol browser bonobo component (symbol-browser-control).

 - A docking widget (gdl).

 - A utility library that also contains the stubs and skels for
   the symbol browser and text editor components (gdl, idl).

%package -n %libnamedev
Group: Development/C
Summary: Gnome Devtool Libraries - development components
Requires: %libname = %version
Provides: lib%name-devel = %version-%release
Obsoletes: %mklibname -d gdl 1

%description -n %libnamedev
This package contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta2.

The current pieces of GDL include:

 - A symbol browser bonobo component (symbol-browser-control).

 - A docking widget (gdl).

 - A utility library that also contains the stubs and skels for
   the symbol browser and text editor components (gdl, idl).


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT %name-1.lang
%makeinstall_std
%find_lang %name-%{api}
chrpath -d %buildroot%_libdir/lib*.so

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig
%endif

%files -f %name-%{api}.lang
%defattr(-,root,root)
%doc README NEWS MAINTAINERS AUTHORS
%_datadir/%name


%files -n %libname
%defattr(-,root,root)
%_libdir/girepository-1.0/Gdl-%{major}.typelib
%_libdir/libgdl-%{api}.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%doc ChangeLog
%_libdir/lib*.so
%_libdir/lib*.la
%_libdir/pkgconfig/*
%_includedir/*
%_datadir/gtk-doc/html/gdl
%_datadir/gir-1.0/Gdl-%{major}.gir
