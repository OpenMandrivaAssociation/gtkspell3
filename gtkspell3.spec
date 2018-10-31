Name:           gtkspell3
Version:        3.0.8
Release:        2
Summary:        On-the-fly spell checking for GtkTextView widgets

License:        GPLv2+
Group:		System/Libraries
URL:            http://gtkspell.sourceforge.net/
Source0:        http://downloads.sourceforge.net/gtkspell/gtkspell3-%{version}.tar.gz

BuildRequires:  pkgconfig(enchant)
BuildRequires:  gettext
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  intltool
BuildRequires:  vala-devel
BuildRequires:  vala-tools

%description
GtkSpell provides word-processor-style highlighting and replacement of
misspelled words in a GtkTextView widget as you type. Right-clicking a
misspelled word pops up a menu of suggested replacements.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Group:		Development/C

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use GtkSpell API version 3.0.

%prep
%setup -q

%build
%configure2_5x --disable-static --enable-vala --prefix=%{_prefix} --libdir=%{_libdir}
%make V=1

%install
%makeinstall_std

find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang gtkspell3

%files -f gtkspell3.lang
%doc AUTHORS COPYING README
%{_libdir}/girepository-1.0/GtkSpell-3.0.typelib
%{_libdir}/libgtkspell3-3.so.*

%files devel
%doc %{_datadir}/gtk-doc/
%{_includedir}/gtkspell-3.0/
%{_libdir}/libgtkspell3-3.so
%{_libdir}/pkgconfig/gtkspell3-3.0.pc
%{_datadir}/gir-1.0/GtkSpell-3.0.gir
%{_datadir}/vala/vapi/gtkspell3-3.0.vapi
%{_datadir}/vala/vapi/gtkspell3-3.0.deps

