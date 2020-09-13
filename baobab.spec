Summary:	GNOME Disk Usage Analyzer
Summary(pl.UTF-8):	Analizator wykorzystania dysku dla GNOME
Name:		baobab
Version:	3.38.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/baobab/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	b69c1e9e4711d15367b894f63d2081e8
Patch0:		%{name}-desktop.patch
URL:		https://wiki.gnome.org/Apps/DiskUsageAnalyzer
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.44
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(find_lang) >= 1.35
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.38.0.11
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.44
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.44
Requires:	gtk+3 >= 3.20.0
Requires:	hicolor-icon-theme
Provides:	gnome-utils-baobab = 1:%{version}-%{release}
Obsoletes:	gnome-utils-baobab < 1:3.3.2-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Baobab is a simple application which can scan either specific folders
(local or remote) or volumes and give a graphical representation
including each directory size or percentage in the branch. It also
auto-detects any mounted/unmounted device.

%description -l pl.UTF-8
Baobab to prosta aplikacja, która potrafi przeszukać określone
katalogi (lokalne lub zdalne) lub wolumeny i podać graficzną
reprezentację rozmiaru każdego katalogu lub jego udziału procentowego
w gałęzi. Wykrywa także dowolne zamontowane/odmontowane urządzenia.

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
%doc AUTHORS NEWS README.md
%attr(755,root,root) %{_bindir}/baobab
%{_datadir}/dbus-1/services/org.gnome.baobab.service
%{_datadir}/glib-2.0/schemas/org.gnome.baobab.gschema.xml
%{_datadir}/metainfo/org.gnome.baobab.appdata.xml
%{_desktopdir}/org.gnome.baobab.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.baobab.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.baobab.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.baobab-symbolic.svg
%{_mandir}/man1/baobab.1*
