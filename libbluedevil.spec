%define major	1
%define libname	%mklibname bluedevil %{major}
%define devname	%mklibname bluedevil -d

Summary:	Qt-based library written in C++ to handle all Bluetooth functionality
Name:		libbluedevil
Group:		Graphical desktop/KDE
Version:	1.9.4
Release:	5
License:	LGPLv2+
Url:		https://projects.kde.org/projects/playground/libs/libname
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	kde4-macros
BuildRequires:	qt4-devel

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
%setup -qn %{name}-v%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_kde_libdir}/libbluedevil.so.%{major}*

%files -n %{devname}
%{_kde_includedir}/bluedevil
%{_kde_libdir}/libbluedevil.so
%{_kde_libdir}/pkgconfig/bluedevil.pc

