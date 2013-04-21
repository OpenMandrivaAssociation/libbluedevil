Name:		libbluedevil
Summary:	Qt-based library written in C++ to handle all Bluetooth functionality
Group:		Graphical desktop/KDE
Version:	1.9.3
Release:	1
License:	LGPLv2+
URL:		https://projects.kde.org/projects/playground/libs/libbluedevil
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	kde4-macros
BuildRequires:	qt4-devel

%description
Qt-based library written in C++ to handle all Bluetooth functionality

#------------------------------------------------

%define bluedevil_major 1
%define libbluedevil %mklibname bluedevil %{bluedevil_major}

%package -n %{libbluedevil}
Summary:	Bluedevil Runtime library
Group:		System/Libraries

%description -n %{libbluedevil}
Qt-based library written in C++ to handle all Bluetooth functionality

%files -n %{libbluedevil}
%{_kde_libdir}/libbluedevil.so.%{bluedevil_major}*

#------------------------------------------------

%package devel
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libbluedevil} = %{version}-%{release}

%description devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_kde_includedir}/bluedevil
%{_kde_libdir}/libbluedevil.so
%{_kde_libdir}/pkgconfig/bluedevil.pc

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Tue May 01 2012 Andrey Bondrov <abondrov@mandriva.org> 1.9.2-1mdv2012.0
+ Revision: 794727
- New version 1.9.2

* Wed Nov 23 2011 Andrey Bondrov <abondrov@mandriva.org> 1.9.1-1
+ Revision: 732775
- New version 1.9.1, spec cleanup

* Tue Oct 04 2011 Александр Казанцев <kazancas@mandriva.org> 1.9-1
+ Revision: 702790
- update ro version 1.9

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-2
+ Revision: 661452
- mass rebuild

* Fri Dec 03 2010 Funda Wang <fwang@mandriva.org> 1.8.1-1mdv2011.0
+ Revision: 606721
- update url
- new version 1.8-1

* Mon Sep 13 2010 Andrey Borzenkov <arvidjaar@mandriva.org> 1.8-1mdv2011.0
+ Revision: 578067
- new version; remove patch0 (upstream)

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Use my git patch sent upstream

* Fri Aug 06 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.7-2mdv2011.0
+ Revision: 566502
- Fix requires

* Thu Aug 05 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.7-1mdv2011.0
+ Revision: 566489
- Fix install of pkgconfig (P0)
- import libbluedevil


