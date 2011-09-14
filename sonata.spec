Summary: An elegant music client for MPD
Name: sonata
Version: 1.6.2.1
Release: 3
Epoch: 1
Source0: http://download.berlios.de/sonata/%{name}-%{version}.tar.bz2
Patch0:	sonata-fix_link.patch
License: GPLv2+
Group: Sound
Url: http://sonata.berlios.de/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl(XML::Parser)
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-devel
BuildRequires:	pygtk2.0-libglade

Requires:	dbus-python >= 0.80
Requires:	python-notify
Requires:	pygtk2
Requires:	python-celementtree
Requires:	python-soap
Requires:	python-tagpy
Requires:	python-mpd
Requires:	gnome-python-gnomevfs

%description
Sonata is an elegant GTK+ music client for the Music Player Daemon (MPD).

Features :

  * Expanded and collapsed views
  * Automatic remote and local album art
  * User-configurable columns
  * Automatic fetching of lyrics
  * Playlist and stream support
  * Support for editing song tags
  * Popup notification
  * Playlist queue support
  * Library and playlist searching
  * Audioscrobbler (last.fm) support
  * Multiple MPD profiles
  * Keyboard friendly
  * Support for multimedia keys
  * Commandline controlFeatures

%prep
%setup -q
%patch0 -p0


%build
%{__python} setup.py build

%install
rm -rf %buildroot

%{__python} setup.py install --no-compile --prefix %{buildroot}/usr

mkdir -p %{buildroot}/usr
mkdir -p %{buildroot}/%{_datadir}
mkdir -p %{buildroot}/%{_docdir}/%{name}
mkdir -p %{buildroot}/%{_mandir}
mv %{buildroot}/%{_datadir}/sonata/{CHANGELOG,README,TODO,TRANSLATORS} %{buildroot}/%{_docdir}/%{name}/

%find_lang %{name}

%clean
rm -rf %buildroot

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc CHANGELOG README TODO TRANSLATORS
%{_bindir}/%{name}
%{py_platsitedir}/*
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
