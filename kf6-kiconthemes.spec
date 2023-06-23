%define libname %mklibname KF6IconThemes
%define devname %mklibname KF6IconThemes -d
%define widgetslibname %mklibname KF6IconWidgets
%define widgetsdevname %mklibname KF6IconWidgets -d
%define git 20230622

Name: kf6-kiconthemes
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kiconthemes/-/archive/master/kiconthemes-master.tar.bz2#/kiconthemes-%{git}.tar.bz2
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
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Archive)
# Just to avoid pulling in the KF5 version
BuildRequires: plasma6-xdg-desktop-portal-kde
Requires: %{libname} = %{EVRD}

%description
Icon GUI utilities

%package -n %{libname}
Summary: Icon GUI utilities
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Icon GUI utilities

%package -n %{widgetslibname}
Summary: Icon Widgets library
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{widgetslibname}
Icon Widgets library

%package -n %{libname}-designer
Summary: Qt Designer support for %{name} widgets
Group: System/Libraries
Requires: %{libname} = %{EVRD}
Supplements: qt6-qttools-designer

%description -n %{libname}-designer
Qt Designer support for %{name} widgets

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Icon GUI utilities

%package -n %{widgetsdevname}
Summary: Development files for KIconWidgets
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{widgetsdevname}
Development files (Headers etc.) for KIconWidgets

Icon GUI utilities

%prep
%autosetup -p1 -n kiconthemes-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kiconthemes.*
%{_bindir}/kiconfinder6

%files -n %{devname}
%{_includedir}/KF6/KIconThemes
%{_libdir}/cmake/KF6IconThemes
%{_qtdir}/mkspecs/modules/qt_KIconThemes.pri
%{_qtdir}/doc/KF6IconThemes.*

%files -n %{libname}
%{_libdir}/libKF6IconThemes.so*
%{_qtdir}/plugins/iconengines/KIconEnginePlugin.so
%{_qtdir}/qml/org/kde/iconthemes

%files -n %{widgetslibname}
%{_libdir}/libKF6IconWidgets.so*

%files -n %{widgetsdevname}
%{_includedir}/KF6/KIconWidgets
%{_qtdir}/mkspecs/modules/qt_KIconWidgets.pri
%{_qtdir}/doc/KF6IconWidgets.*

%files -n %{libname}-designer
%{_qtdir}/plugins/designer/kiconthemes6widgets.so
