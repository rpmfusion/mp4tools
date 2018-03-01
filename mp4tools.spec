%global pname   MP4Tools

Name:           mp4tools
Version:        3.5
Release:        6%{?dist}
Summary:        A free cross-platform tool to manipulate MP4 files
License:        GPLv2
URL:            http://www.mp4joiner.org
Source0:        http://app.oldfoss.com:81/download/MP4Joiner/%{pname}-%{version}.tar.bz2
# fedora specific patch
Patch0:         %{name}-wx-config.patch

BuildRequires:  compat-wxGTK3-gtk2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ffmpeg
BuildRequires:  ffmpeg-devel
BuildRequires:  gettext-devel
BuildRequires:  gpac
BuildRequires:  wxsvg-devel
Requires:       ffmpeg
Requires:       gpac


%description
MP4Tools is a collection of cross-platform free tools to manipulate MP4 files.
It contains following applications:
⦁ MP4Joiner is a free application that allows join multiple MP4 files into one
⦁ MP4Splitter is a free application that allows split a MP4 file in multiple
files


%prep
%autosetup -n %{pname}-%{version}

%build

%configure \
%if (0%{?fedora} && 0%{?fedora} < 28)
 --with-wx-config=%{_bindir}/wx-config-3.0-gtk2
%endif

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
