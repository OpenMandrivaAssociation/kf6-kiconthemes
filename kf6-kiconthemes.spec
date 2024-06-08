%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6IconThemes
%define devname %mklibname KF6IconThemes -d
%define widgetslibname %mklibname KF6IconWidgets
#define git 20240217

Name: kf6-kiconthemes
Version: 6.3.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kiconthemes/-/archive/master/kiconthemes-master.tar.bz2#/kiconthemes-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{major}/kiconthemes-%{version}.tar.xz
%endif
Summary: Icon GUI utilities
URL: https://invent.kde.org/frameworks/kiconthemes
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: gettext
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6BreezeIcons)
# FIXME ^^^ is also provided by kf6-breeze-icons-devel
BuildRequires: %mklibname -d KF6BreezeIcons
Requires: %{libname} = %{EVRD}
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Icon GUI utilities.

%package -n %{libname}
Summary: Icon GUI utilities
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Icon GUI utilities.

%package -n %{widgetslibname}
Summary: Icon Widgets library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{widgetslibname}
Icon Widgets library.

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
%rename %{mklibname KF6IconWidgets -d}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Icon GUI utilities.

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kiconthemes.*
%{_bindir}/kiconfinder6

%files -n %{devname}
%{_includedir}/KF6/KIconThemes
%{_libdir}/cmake/KF6IconThemes
%{_qtdir}/doc/KF6IconThemes.*
%{_includedir}/KF6/KIconWidgets
%{_qtdir}/doc/KF6IconWidgets.*

%files -n %{libname}
%{_libdir}/libKF6IconThemes.so*
%{_qtdir}/qml/org/kde/iconthemes
%{_qtdir}/plugins/kiconthemes6/iconengines/KIconEnginePlugin.so

%files -n %{widgetslibname}
%{_libdir}/libKF6IconWidgets.so*

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/kiconthemes6widgets.so
