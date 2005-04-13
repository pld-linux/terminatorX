# Conditional build
%bcond_without	gnome		# for non-gnomers
#
Summary:	Realtime audio synthesizer
Summary(pl):	Syntezator d¼wiêku czasu rzeczywistego
Name:		terminatorX
Version:	3.82
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://terminatorx.cx/dist/%{name}-%{version}.tar.gz
# Source0-md5:	6faa4598f55d8727175576ce09bd1fac
Patch0:		%{name}-fixes.patch
Patch1:		%{name}-desktop.patch
URL:		http://terminatorx.cx/
BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel
BuildRequires:	jack-audio-connection-kit-devel >= 0.66
BuildRequires:	ladspa-devel
BuildRequires:	libglade2-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libmad-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	rpmbuild(macros) >= 1.197
%{?with_gnome:Requires(post,postun):	desktop-file-utils}
Requires(post,postun):	scrollkeeper
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
terminatorX is a realtime audio synthesizer that allows you to
"scratch" on digitally sampled audio data (*.wav, *.au, *.ogg, *.mp3,
etc.) the way hiphop-DJs scratch on vinyl records. It features
multiple turntables, realtime effects (buit-in as well as LADSPA
plugin effects), a sequencer and MIDI interface - all accessible
through an easy-to-use GTK+ GUI.

%description -l pl
termintorX to syntezator d¼wiêku pracuj±cy w czasie rzeczywistym,
pozwalaj±cy skreczowaæ na cyfrowo spróbkowanych danych d¼wiêkowych
(*.wav, *.au, *.ogg, *.mp3, etc.) tak jak to robi± DJ-e hiphopowi na
p³ytach winylowych. Jego mo¿liwo¶ci to wiele talerzy, efekty w czasie
rzeczywistym (wbudowane, jak równie¿ wtyczki efekty LADSPA), sequencer
oraz interfejs MIDI - wszystko dostêpne poprzez ³atwe w u¿yciu GUI
napisane w GTK+.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv gnome-support/terminatorX-mime.png \
	gnome-support/gnome-mime-application-x-terminatorX.png
	
%build
%{__aclocal}
%{__autoconf}
%{__automake}

# Due to possible security risk build by default without capabilities
%configure \
	--with-docdir=%{_datadir} \
	--disable-capabilities

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopdir=%{_desktopdir} \
	pixmapdir=%{_pixmapsdir} \
	icondir=%{_iconsdir}/gnome/48x48/mimetypes

rm -rf $RPM_BUILD_ROOT%{_datadir}/mime-info/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%scrollkeeper_update_post
%{?with_gnome:%update_desktop_database_post}
%banner %{name} -e << EOF
Suggested packages for use with terminatorX:
- mpg123
- sox
- vorbis-tools
EOF

%postun
/sbin/ldconfig
%scrollkeeper_update_postun
%{?with_gnome:%update_desktop_database_postun}

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS NEWS THANKS TODO README.PERFORMANCE
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{?with_gnome:%{_iconsdir}/gnome/48x48/mimetypes/*.png}
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
%{_pixmapsdir}/*
