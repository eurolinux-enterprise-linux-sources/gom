Name:           gom
Version:        0.2.1
Release:        3%{?dist}
Summary:        GObject to SQLite object mapper library

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/Gom
Source0:        https://download.gnome.org/sources/gom/0.2/gom-%{version}.tar.xz

BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(sqlite3)

Patch0: 0001-gom-Fix-converting-pointer-to-GType.patch

%description
Gom provides an object mapper from GObjects to SQLite. It helps you write
applications that need to store structured data as well as make complex queries
upon that data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -delete

%find_lang gom

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f gom.lang
%license COPYING
%{_libdir}/girepository-1.0/Gom-1.0.typelib
%{_libdir}/libgom-1.0.so.0*

%files devel
%{_includedir}/gom-1.0/
%{_libdir}/libgom-1.0.so
%{_libdir}/pkgconfig/gom-1.0.pc
%{_datadir}/gir-1.0/Gom-1.0.gir
%doc %{_datadir}/gtk-doc/

%changelog
* Fri Sep 11 2015 Bastien Nocera <bnocera@redhat.com> 0.2.1-3
- Fix crasher during startup
Resolves: #1261939

* Wed Apr 22 2015 Bastien Nocera <bnocera@redhat.com> 0.2.1-2
- Initial RHEL packaging
Resolves: #1184200

* Mon Aug 25 2014 Kalev Lember <kalevlember@gmail.com> - 0.2.1-1
- Initial Fedora packaging
