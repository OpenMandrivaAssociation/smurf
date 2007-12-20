%define name	smurf
%define version	0.52.6
%define release	%mkrel 7

Summary: 	A GPL sound font editor
Name: 		%name
Version: 	%version
Release: 	%release
License: 	GPL
Group: 		Sound
URL: 		http://smurf.sourceforge.net
Source: 	%name-%version.tar.bz2
BuildRequires: audiofile-devel

%description
Smurf is a GTK based sound font editor. Sound font files are a collection of
audio samples and other data that describe instruments for the purpose of
composing music. Sound fonts do not describe the music itself, but rather the
sounds of the instruments. These instruments can be composed of any digitally
recordable or generated sound. This format provides a portable and flexible
sound synthesis environment that can be supported in hardware or software.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build

%configure

%make

%install

%makeinstall

(cd $RPM_BUILD_ROOT
mkdir -p ./usr/lib/menu
cat > ./usr/lib/menu/%{name} <<EOF
?package(%{name}):\
command="/usr/bin/smurf"\
title="Smurf"\
longtitle="GPL sound font editor"\
needs="x11"\
icon="sound_section.png"\
section="Multimedia/Sound"
EOF
)
 
%find_lang %name
 
%post
%update_menus
  
%postun
%clean_menus 

%clean
rm -rf $RPM_BUILD_ROOT 

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog HACKING INSTALL NEWS README
%_bindir/*
%_menudir/*

