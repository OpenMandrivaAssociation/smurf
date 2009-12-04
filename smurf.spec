%define name	smurf
%define version	0.52.6
%define release	%mkrel 10

Summary: 	A GPL sound font editor
Name: 		%name
Version: 	%version
Release: 	%release
License: 	GPL
Group: 		Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: 		http://smurf.sourceforge.net
Source: 	%name-%version.tar.bz2
Patch0:		smurf-0.52.6-gcc4.patch
BuildRequires: audiofile-devel gtk-devel sndfile-devel

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
%patch0 -p1

%build

%configure

%make

%install

%makeinstall

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=/usr/bin/smurf
Name=Smurf
Comment=GPL sound font editor
Icon=sound_section
Categories=Audio;
EOF
 
%find_lang %name
 
%if %mdkversion < 200900
%post
%update_menus
%endif
  
%if %mdkversion < 200900
%postun
%clean_menus 
%endif

%clean
rm -rf $RPM_BUILD_ROOT 

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog HACKING INSTALL NEWS README
%_bindir/*
%{_datadir}/applications/mandriva-*.desktop

