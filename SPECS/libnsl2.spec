# Uncomment on initial build for soname bump.
#global bump_soname 1
%global sover 3

%if 0%{?bump_soname}
%global relsuffix ~sonamebump
%global old_sover %(echo $((%{sover}-1)))
%endif

Name:       libnsl2
Version:    2.0.0
Release:    1%{?relsuffix}%{?dist}
Summary:    Public client interface library for NIS(YP) and NIS+

License:    BSD and LGPLv2+
URL:        https://github.com/thkukuk/libnsl

Source0:    https://github.com/thkukuk/libnsl/archive/v%{version}.tar.gz

BuildRequires: autoconf, automake, gettext-devel, libtool, libtirpc-devel
BuildRequires: make
BuildRequires: gcc
%if 0%{?bump_soname}
BuildRequires: libnsl2 < %{version}
%endif

%description
This package contains the libnsl library. This library contains
the public client interface for NIS(YP).
This code was formerly part of glibc, but is now standalone to
be able to link against TI-RPC for IPv6 support.

%package devel
Summary: Development files for libnsl
Requires: %{name}%{?_isa} = %{version}-%{release}
Conflicts: glibc-devel < 2.26.9000-40

%description devel
Development files for libnsl2


%prep
%setup -q -n libnsl-%{version}

%build
autoreconf -fiv

%configure \
    --libdir=%{_libdir} \
    --includedir=%{_includedir}

%make_build


%install
%make_install

rm %{buildroot}%{_libdir}/libnsl.{a,la}

%if 0%{?bump_soname}
cp -p %{_libdir}/libnsl.so.%{old_sover}* %{buildroot}%{_libdir}
%endif

%files
%license COPYING
%{_libdir}/libnsl.so.%{sover}*
%if 0%{?bump_soname}
%{_libdir}/libnsl.so.%{old_sover}*
%endif

%files devel
%{_libdir}/libnsl.so
%{_includedir}/*
%{_libdir}/pkgconfig/libnsl.pc

%changelog
* Thu Jan 20 2022 Alexander Bokovoy <abokovoy@redhat.com> - 2.0.0-1
- Rebase to upstream 2.0.0 release
- Resolves: rhbz#2039220

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1.3.0-4
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.3.0-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 18 2020 Filip Janus <fjanus@redhat.com> - 1.3.0-1
- Upstreal released new version 1.3.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8.20180605git4a062cf
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7.20180605git4a062cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6.20180605git4a062cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5.20180605git4a062cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4.20180605git4a062cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Oct 29 2018 James Antill <james.antill@redhat.com>
- Remove ldconfig scriptlet, now done via. transfiletrigger in glibc (#1644073).

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3.20180605git4a062cf
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 05 2018 Matej Mužila <mmuzila@redhat.com> - 1.2.0-2.20181605git4a062cf
- Update to 1.2.0-2.20181605git4a062cf
  Resolves: rhbz#1573895

* Fri Feb 09 2018 Matej Mužila <mmuzila@reedhat.com> - 1.2.0-1
- Update to version 1.2.0
- Change libdir and includedir

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Oct 04 2017 Matej Mužila <mmuzila@redhat.com> 1.1.0-1
- Update to version 1.1.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Matej Mužila <mmuzila@redhat.com> 1.0.5-1
- Update to version 1.0.5
- Fix missing stdint.h

* Mon Apr 10 2017 Matej Mužila <mmuzila@redhat.com> 1.0.4-4
- Initial version for 1.0.4

