%define major	5
%define libname	%mklibname bluedevil %{major}
%define devname	%mklibname bluedevil -d

Summary:	Qt-based library written in C++ to handle all Bluetooth functionality
Name:		libbluedevil
Group:		Graphical desktop/KDE
Version:	5.2.2
Release:	2
License:	LGPLv2+
Url:		https://invent.kde.org/unmaintained/libbluedevil
Source0:	https://invent.kde.org/unmaintained/libbluedevil/-/archive/v%{version}/libbluedevil-v%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)

%description
Qt-based library written in C++ to handle all Bluetooth functionality

%package -n %{libname}
Summary:	Bluedevil Runtime library
Group:		System/Libraries

%description -n %{libname}
Qt-based library written in C++ to handle all Bluetooth functionality

%package -n %{devname}
Summary:	Devel stuff for %{name}
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	libbluedevil-devel < 1.9.3-2

%description -n %{devname}
This package contains header files needed if you wish to build applications
based on %{name}.

%prep
%autosetup -p1 -n %{name}-v%{version}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libbluedevil.so.%{major}*

%files -n %{devname}
%{_includedir}/bluedevil
%{_libdir}/libbluedevil.so
%{_libdir}/pkgconfig/bluedevil.pc

