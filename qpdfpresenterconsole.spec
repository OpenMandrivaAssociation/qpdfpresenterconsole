%define sfname qpdfpresenter
%define fullname QPdfPresenterConsole

Summary:        Beamer-targeted presentation tool
Name:           qpdfpresenterconsole
Version:        2.5.13
Release:        2
License:        MIT
Source0:        http://sourceforge.net/projects/%{sfname}/files/sources/%{name}-v%{version}.tar.bz2
Group:          Graphical desktop/Other
Url:		http://gitorious.org/qpdfpresenterconsole
BuildRequires:	cmake
BuildRequires:	asciidoc
BuildRequires:	docbook-xsl
BuildRequires:	docbook-dtd45-xml
BuildRequires:	xsltproc
BuildRequires:	libxml2-utils
BuildRequires:	libpoppler-qt4-devel
BuildRequires:	pkgconfig(Qt3Support)
BuildRequires:	pkgconfig(libvlc)

%description
Presentation console software, similar to what is provided by LibreOffice
Impress' plug-in or Apple Keynote, targeting PDF presentations and especially
those written in LaTeX with the Beamer package. It provides a presentation
console on the main speaker's screen which contains:
 - the current slide if it's a simple pdf presentation, with notes below if
   there is a text file provided that contains slide notes
 - the current notes slide if it contains Beamer notes (left/right notes
   supported)
 - current date and time, current slide number
 - countdown from the start of the presentation
 - timer alarm to notify when the end of your slot is approaching
Slides are pre-rendered in background (current, next, previous) so that
changing slide is smooth and fast. Beamer-embedded (at least using movie15
package) videos are supported through LibVLC and one can provide separate text
file containing notes too. It's also heavily inspired from Pdf Presenter
Console, main differences are background pre-rendering of slides, videos
support, beamer and text file notes support. It should work nice on any
XRandR-capable system.

%prep
%setup -q -n %{name}-v%{version}

%build
%cmake_qt4
%make

%install
make -C build DESTDIR=%buildroot install

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{fullname}.png
%{_datadir}/applications/%{fullname}.desktop


%changelog
* Sun Mar 25 2012 Alexandre Lissy <alissy@mandriva.com> 2.5.13-1
+ Revision: 786667
- added dependency against docbook-dtd45-xml (needed by asciidoc)
- fix (remove) invalid vendor field
- Imported QPdfPresenterConsole
- Created package structure for 'qpdfpresenterconsole'.

