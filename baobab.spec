Summary:	Graphical directory tree analyzer
Summary(pl.UTF-8):	Graficzny analizator drzew katalogów
Name:		baobab
Version:	3.30.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/baobab/3.30/%{name}-%{version}.tar.xz
# Source0-md5:	a0ef355b575b6c63e95dfe75ee3c39f9
Patch0:		%{name}-desktop.patch
URL:		https://wiki.gnome.org/Apps/Baobab
BuildRequires:	appstream-glib-devel
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.39.90
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	vala >= 2:0.38.0.11
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.39.90
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.39.90
Requires:	gtk+3 >= 3.20.0
Requires:	hicolor-icon-theme
Provides:	gnome-utils-baobab = 1:%{version}-%{release}
Obsoletes:	gnome-utils-baobab < 1:3.3.2-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
baobab is a graphical directory tree analyzer.

%description -l pl.UTF-8
baobab jest graficznym analizatorem drzew katalogów.

%prep
%setup -q
%patch0 -p1

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/baobab
%{_desktopdir}/org.gnome.baobab.desktop
%{_iconsdir}/hicolor/*x*/apps/baobab.png
%{_iconsdir}/hicolor/symbolic/apps/baobab-symbolic.svg
%{_datadir}/dbus-1/services/org.gnome.baobab.service
%{_datadir}/glib-2.0/schemas/org.gnome.baobab.gschema.xml
%{_mandir}/man1/baobab.1*
%{_datadir}/metainfo/org.gnome.baobab.appdata.xml
