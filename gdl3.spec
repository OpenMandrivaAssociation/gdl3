%define oname gdl
%define api 3
%define major 1

%define libname 	%mklibname %{oname} %api %major
%define develname	%mklibname -d %{oname} %api
%define girname 	%mklibname %{oname}-gir %{api}

Summary: Gnome Development/Docking library
Name: %{oname}3
Version: 3.2.0
Release: 1
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org
Source0: http://ftp.gnome.org/pub/GNOME/sources/gdl/%{oname}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: pkgconfig(gdk-3.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(libxml-2.0)

%description
This package contains components and libraries that are intended to be
shared between GNOME development tools, including gnome-debug,
gnome-build, and anjuta2.

The current pieces of GDL include:
 - A symbol browser bonobo component (symbol-browser-control).
 - A docking widget (gdl).
 - A utility library that also contains the stubs and skels for
   the symbol browser and text editor components (gdl, idl).

%package -n %{libname}
Group: System/Libraries
Summary: Gnome Development/Docking library - shared libraries

%description -n %{libname}
This package contains the dynamic libraries from %{name}.

%package -n %{girname}
Group: System/Libraries
Summary: GObject Introspection interface library for %{name}
Requires: %{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{develname}
Group: Development/C
Summary: Gnome Development/Docking library headers and development libraries
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{develname}
This packages contains the headers and libraries for %{name}.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x \
	--disable-rpath \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unpackaged files
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{oname}-%{api}


%files -f %{oname}-%{api}.lang
%doc README NEWS MAINTAINERS AUTHORS
%{_datadir}/gdl-%{api}

%files -n %{libname}
%{_libdir}/libgdl-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Gdl-%{api}.typelib

%files -n %{develname}
%doc ChangeLog
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/gdl-*
%{_datadir}/gir-1.0/Gdl-%{api}.gir

