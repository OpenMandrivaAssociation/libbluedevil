Name:          libbluedevil
Summary:       Qt-based library written in C++ to handle all Bluetooth functionality
Group:         Graphical desktop/KDE
Version:       1.8
Release:       %mkrel 1
License:       GPL
URL:           http://www.kde.org
Source0:       %name-%version.tar.bz2
BuildRequires: cmake
BuildRequires: kde4-macros
BuildRequires: qt4-devel
BuildRoot: %_tmppath/%name-%version-%release-root

%description 
Qt-based library written in C++ to handle all Bluetooth functionality

#------------------------------------------------

%define bluedevil_major 1
%define libbluedevil %mklibname bluedevil %bluedevil_major

%package -n %libbluedevil
Summary: KDE 4 core library
Group: System/Libraries
Conflicts: konqueror <  1:4.0.82-5

%description -n %libbluedevil
Qt-based library written in C++ to handle all Bluetooth functionality

%files -n %libbluedevil
%defattr(-,root,root)
%_kde_libdir/libbluedevil.so.%{bluedevil_major}*

#------------------------------------------------

%package devel
Summary: Devel stuff for %name
Group: Development/KDE and Qt
Requires: %libbluedevil = %version-%release

%description  devel
This package contains header files needed if you wish to build applications
based on %{name} .

%files devel
%defattr(-,root,root)
%_kde_includedir/bluedevil
%_kde_libdir/libbluedevil.so
%_kde_libdir/pkgconfig/bluedevil.pc

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%install
rm -rf %buildroot

%makeinstall_std -C build

%clean
rm -fr %buildroot
