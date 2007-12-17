%define name sonata
%define version 1.3
%define release %mkrel 2

Summary: An elegant music client for MPD
Name: %{name}
Version: %{version}
Release: %{release}
Epoch: 1
Source0: http://download.berlios.de/sonata/%{name}-%{version}.tar.bz2
License: GPL
Group: Sound
Url: http://sonata.berlios.de/index.html
BuildRequires:	perl(XML::Parser)
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-devel
BuildRequires:	pygtk2.0-libglade

Requires:	dbus-python >= 0.80
Requires:	python-notify
Requires:	pygtk2
Requires:       python-celementtree
Requires:       python-soap
Requires:       python-tagpy

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


%build
%{__python} setup.py build

%install
rm -rf %buildroot

%{__python} setup.py install --no-compile --prefix %{buildroot}/usr

mkdir -p %{buildroot}/usr
mkdir -p %{buildroot}/%{_datadir}
mkdir -p %{buildroot}/%{_docdir}/%{name}
mkdir -p %{buildroot}/%{_mandir}
mv %{buildroot}/usr/man/* %{buildroot}/%{_mandir}
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
