#For git snapshots, set to 0 to use release instead:
%global usesnapshot 0
%if 0%{?usesnapshot}
%global commit0 da0dff96a563fb8b09f2a2a78a0aa97b8af47ff2
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global snapshottag .git%{shortcommit0}
%endif
%global pname   MP4Tools
%global wxsvg_ver 1.5.22

Name:           mp4tools
%if 0%{?usesnapshot}
Version:        3.8
Release:        8.beta3%{?snapshottag}%{?dist}
%else
Version:        3.8
Release:        5%{?dist}
%endif
Summary:        A free cross-platform tool to manipulate MP4 files
License:        GPLv2
URL:            http://www.mp4joiner.org

# checkout instructions
# git clone git://git.code.sf.net/p/mp4joiner/git mp4tools
# cd mp4tools
# git rev-parse --short HEAD
# git archive --format=tar --prefix=mp4tools/ %%{shortcommit0} \
#   -o mp4tools-%%{shortcommit0}.tar
# bzip2 mp4tools-%%{shortcommit0}.tar

%if 0%{?usesnapshot}
Source0:        %{name}-%{shortcommit0}.tar.bz2
%else
Source0:        https://sourceforge.net/projects/mp4joiner/files/%{pname}/%{version}/%{pname}-%{version}.tar.bz2
%endif
# fedora specific patch
Patch0:         %{name}-wx-config.patch
BuildRequires:  gcc gcc-c++
BuildRequires:  wxGTK3-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ffmpeg
BuildRequires:  ffmpeg-devel
BuildRequires:  gettext-devel
BuildRequires:  gpac
BuildRequires:  wxsvg-devel >= %{wxsvg_ver}
Requires:       wxsvg >= %{wxsvg_ver}
Requires:       ffmpeg
Requires:       gpac

%description
MP4Tools is a collection of cross-platform free tools to manipulate MP4 files.
It contains following applications:
⦁ MP4Joiner is a free application that allows join multiple MP4 files into one
⦁ MP4Splitter is a free application that allows split a MP4 file in multiple
files

%prep
%if 0%{?usesnapshot}
%setup -q -n %{name}
%else
%setup -q -n %{pname}-%{version}
%endif

%build

if [ ! -f configure ]; then
NOCONFIGURE=1 ./autogen.sh
fi
%configure
%make_build

%install
%make_install

#menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mp4joiner.desktop <<EOF
[Desktop Entry]
Name=MP4Joiner
Comment=Join multiple MP4 files.
Exec=mp4joiner
Icon=mp4joiner
Type=Application
Terminal=false
Categories=Video;
EOF

cat > %{buildroot}%{_datadir}/applications/mp4splitter.desktop <<EOF
[Desktop Entry]
Name=MP4Splitter
Comment=Split MP4 files.
Exec=mp4splitter
Icon=mp4splitter
Type=Application
Terminal=false
Categories=Video;
EOF

#icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 644 resources/mp4joiner.png \
%{buildroot}%{_datadir}/pixmaps/mp4joiner.png

install -m 644 resources/mp4splitter.png \
%{buildroot}%{_datadir}/pixmaps/mp4splitter.png
# remove not relevant file
rm -f %{buildroot}%{_docdir}/%{name}/INSTALL
rm -f %{buildroot}%{_pkgdocdir}/COPYING

%find_lang %name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/mp4joiner.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/mp4splitter.desktop

%files -f %{name}.lang
%doc README ChangeLog AUTHORS
%license COPYING
%{_bindir}/mp4joiner
%{_bindir}/mp4splitter
%{_datadir}/applications/mp4joiner.desktop
%{_datadir}/applications/mp4splitter.desktop
%{_datadir}/pixmaps/mp4joiner.png
%{_datadir}/pixmaps/mp4splitter.png

%changelog
* Fri Nov 12 2021 Leigh Scott <leigh123linux@gmail.com> - 3.8-5
- Rebuilt for new ffmpeg snapshot

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.8.1-1
- Update to 3.8.1

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Feb 10 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.7.1-5
- Add RR wxsvg-1.5.16 fixes (rfbz#5166).

* Tue Jan 29 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.7.1-4
- Rebuilt for wxsvg-1.5.16

* Mon Jan 28 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.7.1-3
- Rebuilt for wxsvg-1.5.16

* Tue Jan 22 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.7.1-2
- Rebuilt

* Wed Dec 26 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.7.1-1
- Update to 3.7.1
- Add BR gcc gcc-c++
- Add BR wxGTK3-devel for Fedora >= 30

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.6.1-2
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.6.1-1
- Update to 3.6.1

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 08 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 3.5-7
- Rebuilt for new ffmpeg snapshot

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 3.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 3.5-5
- Rebuilt for ffmpeg-3.5 git

* Tue Jan 09 2018 Martin Gansser <martinkg@fedoraproject.org> - 3.5-4
- Add RR gpac

* Thu Oct 12 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.5-3
- COPYING file does not report a GPLv3 license, use GPLv2
- Do not use %%license and %%{_pkgdocdir} together

* Sat Sep 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.5-2
- remove scriptlets now longer needed

* Fri Sep 01 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.5-1
- Update to 3.5
- Add %%{name}-wx-config.patch

* Fri Sep 01 2017 Martin Gansser <martinkg@fedoraproject.org> - 3.4-1
- initial build
