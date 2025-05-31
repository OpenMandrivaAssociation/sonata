Summary:	An elegant music client for MPD
Name:		sonata
Version:	1.7.1
Release:	1
License:	GPLv2+
Group:		Sound
Url:		https://www.nongnu.org/sonata/
Source0:	https://github.com/multani/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires: gettext

Requires:	mpd
Requires:	python-dbus
Requires:	python3dist(pygobject)
Requires:	python-mpd2

Recommends:	python-tagpy

BuildArch:	noarch

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

%files -f %{name}.lang
%license COPYING
%doc CHANGELOG README.rst TODO TRANSLATORS PLUGINS.rst
%{_bindir}/%{name}
%{python3_sitelib}/*
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

#install -Dm 0755 %{buildroot}%{_prefix}
#install -Dm 0755 %{buildroot}%{_datadir}
#install -Dm 0755 %{buildroot}%{_docdir}/%{name}
#install -Dm 0755 %{buildroot}%{_mandir}

# icon
install -dm 0755 %{buildroot}%{_datadir}/pixmaps
install -pm 0644 sonata/pixmaps/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

# remove docs
rm -f %{buildroot}%{_datadir}/%{name}/{CHANGELOG,README.rst,TODO,TRANSLATORS}

# locales
%find_lang %{name}

