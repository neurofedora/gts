%global snapshot 121130

Name:           gts
Version:        0.7.6
Release:        26.20%{snapshot}%{?dist}
Summary:        GNU Triangulated Surface Library
Group:          Applications/Engineering
License:        LGPLv2+
URL:            http://gts.sourceforge.net/index.html
Source0:        http://gts.sourceforge.net/tarballs/gts-snapshot-%{snapshot}.tar.gz
Patch0:         0001-examples-rename-with-gts-prefix-and-install-set-and-.patch
BuildRequires:  git-core
BuildRequires:  autoconf automake libtool
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  netpbm-devel

%package devel
Summary:        Development files for gts
Group:          Applications/Engineering
Requires:       pkgconfig
Requires:       glib2-devel%{_isa}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description
GTS provides a set of useful functions to deal with 3D surfaces meshed
with interconnected triangles including collision detection,
multiresolution models, constrained Delaunay triangulations and robust
set operations (union, intersection, differences).

%description devel
This package contains the gts header files and libs.

%prep
%autosetup -n %{name}-snapshot-%{snapshot} -S git

# Fix broken permissions
chmod +x test/*/*.sh

%build
autoreconf -vfi
%configure --disable-static --disable-dependency-tracking
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%check
# Urgh, something is very broken with gts rsp. its testsuite
make check ||:

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%doc README AUTHORS THANKS
%{_bindir}/gtsdelaunay
%{_bindir}/gts2dxf
%{_bindir}/gts2oogl
%{_bindir}/gts2stl
%{_bindir}/gtscheck
%{_bindir}/gtscompare
%{_bindir}/gtstemplate
%{_bindir}/gtshapprox
%{_bindir}/stl2gts
%{_bindir}/gtstransform
%{_bindir}/gts2xyz
%{_libdir}/lib%{name}*.so.*
%{_mandir}/man1/gtsdelaunay.1*
%{_mandir}/man1/gts2dxf.1*
%{_mandir}/man1/gts2oogl.1*
%{_mandir}/man1/gts2stl.1*
%{_mandir}/man1/gtscheck.1*
%{_mandir}/man1/gtscompare.1*
%{_mandir}/man1/gtstemplate.1*
%{_mandir}/man1/gtshapprox.1*
%{_mandir}/man1/stl2gts.1*
%{_mandir}/man1/gtstransform.1*
# was noinst
%{_bindir}/gtsset
%{_bindir}/gtsrefine

%files devel
%doc examples/*.c
%{_bindir}/gts-config
%{_includedir}/%{name}*.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib%{name}*.so
%{_datadir}/aclocal/%{name}.m4
%{_mandir}/man1/gts-config.1*

%changelog
* Thu Nov 05 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.6-26.20121130
- Update to latest snapshot
- Small cleanups in spec
- Include some new examples

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-26.20111025
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-25.20111025
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-24.20111025
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-23.20111025
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-22.20111025
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-21.20111025
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-20.20111025
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 07 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.7.6-19.20111025
- Update to new upstream snapshot
- Rebase patches.
- Spec file cleanup.

* Wed Nov 16 2011 Jindrich Novy <jnovy@redhat.com> - 0.7.6-16
- rebuild against new netpbm

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jun  1 2010 Dan Horák <dan[at]danny.cz> - 0.7.6-14
- fix include path for pgm.h (#538971)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jul 30 2008 Ralf Corsépius <rc040203@freenet.de> - 0.7.6-11
- Let *-devel Require: glib2-devel (BZ: 457099).
- Pass LIBS=-lm to %%configure (avoid non-weak refs to libm).
- Add gts-0.7.6-hacks.diff (Various configuration fixes).
- Add gts-0.7.6-autotools.diff (regenerate autotool-generated files).
- Add %%check.

* Fri May 23 2008 Jon Stanley <jonstanley@gmail.com> - 0.7.6-10
- Fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.7.6-9
- Autorebuild for GCC 4.3

* Sun Oct 21 2007 Ralf Corsépius <rc040203@freenet.de> - 0.7.6-8
- Address BZ 341431:
  - Rework gts-config.
  - Rework gts.pc.
  - Regenerate gts-0.7.6-pkg_config.diff.

* Tue Aug 28 2007 Ed Hill <ed@eh3.com> - 0.7.6-7
- rebuild for BuildID

* Fri Sep  1 2006 Ed Hill <ed@eh3.com> - 0.7.6-6
- rebuild for imminent FC-6 release

* Mon May 22 2006 Ralf Corsépius <rc040203@freenet.de> - 0.7.6-5
- BR: netpbm-devel (Required to build happrox).
- Add --disable-dependency-tracking.

* Sun May 21 2006 Ed Hill <ed@eh3.com> - 0.7.6-4
- add gts-config patch

* Sun May 21 2006 Ed Hill <ed@eh3.com> - 0.7.6-3
- add Ralf's includedir patch

* Fri May 19 2006 Ed Hill <ed@eh3.com> - 0.7.6-2
- fix FE review items provided by Ralf Corsepius

* Thu May 18 2006 Ed Hill <ed@eh3.com> - 0.7.6-1
- initial package creation

