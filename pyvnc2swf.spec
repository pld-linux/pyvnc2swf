Summary:	Cross-platform screen recording tool
Summary(pl.UTF-8):	Wieloplatformowe narzędzie do nagrywania ekranu
Name:		pyvnc2swf
Version:	0.9.5
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://www.unixuser.org/~euske/vnc2swf/%{name}-%{version}.tar.gz
# Source0-md5:	af9737400d605b16f7283b4d2615f207
URL:		http://www.unixuser.org/~euske/vnc2swf/
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
# for recordwin
Requires:	awk
Requires:	x11vnc
Requires:	xorg-app-xwininfo
# not exactly, but functionally - this projects is a continuation of vnc2swf/edit_vnc2swf
Obsoletes:	edit_vnc2swf
Obsoletes:	vnc2swf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyvnc2swf is a cross-platform screen recording tool. It captures
screen motion through VNC protocol and generates a Shockwave Flash
(SWF) movie.

%description -l pl.UTF-8
Pyvnc2swf to wieloplatformowe narzędzie do nagrywania ekranu.
Przechwytuje ruch na ekranie poprzez protokół VNC i generuje film w
formacie Shockwave Flash (SWF).

%prep
%setup -q

%{__sed} -i -e '1s,#!/usr/bin/env python,#!/usr/bin/python,' pyvnc2swf/*.py
%{__sed} -i -e 's,^VNC2SWF=pyvnc2swf/vnc2swf.py,VNC2SWF=pyvnc2swf,' bin/recordwin.sh

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{py_sitescriptdir}/pyvnc2swf}

install bin/recordwin.sh $RPM_BUILD_ROOT%{_bindir}/recordwin
cp -p pyvnc2swf/*.py $RPM_BUILD_ROOT%{py_sitescriptdir}/pyvnc2swf

ln -sf %{py_sitescriptdir}/pyvnc2swf/vnc2swf.py $RPM_BUILD_ROOT%{_bindir}/pyvnc2swf
ln -sf %{py_sitescriptdir}/pyvnc2swf/edit.py $RPM_BUILD_ROOT%{_bindir}/pyvnc2swf_edit
ln -sf %{py_sitescriptdir}/pyvnc2swf/play.py $RPM_BUILD_ROOT%{_bindir}/pyvnc2swf_play

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}/pyvnc2swf
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}/pyvnc2swf
# clean up these, keep the rest of *.py
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/pyvnc2swf/{__init__,d3des,html_templates,image,movie,mp3,output,rfb,swf}.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt docs/{changes,index,pyvnc2swf,recordwin}.html
%lang(ja) %doc docs/{index-j,pyvnc2swf-j}.html
%attr(755,root,root) %{_bindir}/pyvnc2swf
%attr(755,root,root) %{_bindir}/pyvnc2swf_edit
%attr(755,root,root) %{_bindir}/pyvnc2swf_play
%attr(755,root,root) %{_bindir}/recordwin
%dir %{py_sitescriptdir}/pyvnc2swf
%{py_sitescriptdir}/pyvnc2swf/*.py[co]
%attr(755,root,root) %{py_sitescriptdir}/pyvnc2swf/edit.py
%attr(755,root,root) %{py_sitescriptdir}/pyvnc2swf/play.py
%attr(755,root,root) %{py_sitescriptdir}/pyvnc2swf/record_sound.py
%attr(755,root,root) %{py_sitescriptdir}/pyvnc2swf/vnc2swf.py
