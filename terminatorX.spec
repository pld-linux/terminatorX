# TODO:
# - place docs correctly (maybe ;)
# - pl desc
# - check BR and R
#
Summary:	Realtime audio synthesizer
Summary(pl):	Syntezator audio czasu rzeczywistego
Name:		terminatorX
Version:	3.80
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://terminatorx.cx/dist/%{name}-%{version}.tar.gz
# Source0-md5:	04ad737a0b555ea869c27960088a7872
Patch0:		%{name}-fixes.patch
Patch1:		%{name}-desktop.patch
URL:		http://terminatorx.cx/
BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel
BuildRequires:	gtk+2-devel
BuildRequires:	ladspa-devel
BuildRequires:	libglade2-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	mad-devel
Requires:	mpg123
Requires:	sox
Requires:	vorbis-tools
Requires(post,postun):	scrollkeeper
Requires(post,postun):	/sbin/ldconfig
Requires(post):	GConf2 >= 2.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
terminatorX is a realtime audio synthesizer that allows you to
"scratch" on digitally sampled audio data (*.wav, *.au, *.ogg, *.mp3,
etc.) the way hiphop-DJs scratch on vinyl records. It features
multiple turntables, realtime effects (buit-in as well as LADSPA
plugin effects), a sequencer and MIDI interface - all accessible
through an easy-to-use gtk+ GUI.

%description -l pl
termintorX to syntezatro audio pracuj±cy w czasie rzeczywistym
pozwalaj±cy skreczowaæ cyfrowo spróbkowane dane audio (*.wav, *.au,
*.ogg, *.mp3, etc.) tak jak to robi± dj hiphop'owi na p³ytach 
winylowych. Jego opcje to zwielokrotniony ???, efekty w czasie
rzeczywistym (jak równierz wbudowane jako wtyczki efekty LADSPA),
sequencer oraz interfejs MIDI - wszystko dostêpne poprzez ³atwe
w u¿yciu GUI napisane w gtk+.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-docdir=%{_datadir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_desktopdir} \
	gnomedir=%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
scrollkeeper-update

%postun
/sbin/ldconfig
scrollkeeper-update

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS NEWS THANKS TODO README.GNOME README.PERFORMANCE
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_mandir}/man1/*
%{_datadir}/mime-info/*
%{_datadir}/%{name}
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*
