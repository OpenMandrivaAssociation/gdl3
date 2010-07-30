%define oname gdl
%define version 2.90.0
%define release %mkrel 1
%define api 3
%define major 1
%define libname %mklibname %oname %api %major
%define libnamedev %mklibname -d %oname %api

Summary: Gnome Devtool Libraries
Name: %{oname}3
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/gdl/%{oname}-%{version}.tar.bz2
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{oname}-%{version}-%{release}-buildroot
BuildRequires: libxml2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gtk+3-devel
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
%setup -q -n %oname-%version

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT %oname-1.lang
%makeinstall_std
%find_lang %oname-%{api}
chrpath -d %buildroot%_libdir/lib*.so

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %oname-%{api}.lang
%defattr(-,root,root)
%doc README NEWS MAINTAINERS AUTHORS
%_datadir/%oname


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
