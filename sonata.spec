Summary: An elegant music client for MPD
Name: sonata
Version: 1.7.0
Release: 1
Epoch: 1
License: GPLv2+
Group: Sound
Url:		http://www.nongnu.org/sonata/
Source0:	https://github.com/multani/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
Requires:	mpd
Requires: python-dbus
Requires: python3dist(pygobject)
Requires: python-mpd2
Recommends: python-tagpy


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
%py_build

%install
%py_install

mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_mandir}
install -m644 sonata/pixmaps/%{name}.png -D %{buildroot}%{_datadir}/pixmaps/%{name}.png
rm -f %{buildroot}%{_datadir}/%{name}/{CHANGELOG,README.rst,TODO,TRANSLATORS}

%find_lang %{name}

%files -f %{name}.lang
%doc CHANGELOG README.rst TODO TRANSLATORS PLUGINS.rst
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/*
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*

%changelog
* Wed Sep 14 2011 Matthew Dawkins <mattydaw@mandriva.org> 1:1.6.2.1-3
+ Revision: 699787
- added sonata-fix_link.patch to fix build error taken from mga
  Sonata needs gnome-python-gnomevfs to start.
- rebuild

* Mon Nov 01 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1:1.6.2.1-2mdv2011.0
+ Revision: 591516
- rebuild for python-2.7

* Wed Sep 23 2009 Eugeni Dodonov <eugeni@mandriva.com> 1:1.6.2.1-1mdv2010.0
+ Revision: 447798
- Updated to 1.6.2.1

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 1:1.6.2-3mdv2010.0
+ Revision: 445163
- rebuild

* Tue Apr 21 2009 Eugeni Dodonov <eugeni@mandriva.com> 1:1.6.2-2mdv2009.1
+ Revision: 368542
- Updated to 1.6.2.

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1:1.5.3-2mdv2009.1
+ Revision: 326007
- rebuild

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 1:1.5.3-1mdv2009.1
+ Revision: 291815
- New version 1.5.3

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1:1.5.2-2mdv2009.0
+ Revision: 269342
- rebuild early 2009.0 package (before pixel changes)

* Fri Jun 06 2008 Jérôme Soyer <saispo@mandriva.org> 1:1.5.2-1mdv2009.0
+ Revision: 216417
- New release 1.5.2

* Mon May 05 2008 Funda Wang <fwang@mandriva.org> 1:1.5.1-2mdv2009.0
+ Revision: 201237
- requires python-mpd (bug#40560)

* Sun May 04 2008 Funda Wang <fwang@mandriva.org> 1:1.5.1-1mdv2009.0
+ Revision: 200847
- New version 1.5.1

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 1:1.5-1mdv2009.0
+ Revision: 200620
- New version 1.5

* Sat Feb 09 2008 Funda Wang <fwang@mandriva.org> 1:1.4.2-1mdv2008.1
+ Revision: 164570
- New version 1.4.2

* Sun Feb 03 2008 Funda Wang <fwang@mandriva.org> 1:1.4.1-1mdv2008.1
+ Revision: 161643
- New version 1.4.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 23 2007 Jérôme Soyer <saispo@mandriva.org> 1:1.3-2mdv2008.1
+ Revision: 111686
- Fix Requires mistake

* Fri Nov 23 2007 Jérôme Soyer <saispo@mandriva.org> 1:1.3-1mdv2008.1
+ Revision: 111591
- import sonata


