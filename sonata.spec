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


