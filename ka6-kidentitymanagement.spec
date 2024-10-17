#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	24.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kidentitymanagement
Summary:	kidentitymanagement
Name:		ka6-%{kaname}
Version:	24.08.2
Release:	2
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ce1e1f23544cfe59cdfc9f8a95c5f46b
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= 5.11.1
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Test-devel >= 5.9.0
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka6-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{kframever}
BuildRequires:	kf6-kcodecs-devel >= %{kframever}
BuildRequires:	kf6-kcompletion-devel >= %{kframever}
BuildRequires:	kf6-kconfig-devel >= %{kframever}
BuildRequires:	kf6-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf6-kiconthemes-devel >= %{kframever}
BuildRequires:	kf6-kio-devel >= %{kframever}
BuildRequires:	kf6-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf6-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Obsoletes:	ka5-%{kaname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KIdentity Management.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ka5-%{kaname}-devel < %{version}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libKPim6IdentityManagementCore.so.*.*
%ghost %{_libdir}/libKPim6IdentityManagementCore.so.6
%attr(755,root,root) %{_libdir}/libKPim6IdentityManagementQuick.so.*.*
%ghost %{_libdir}/libKPim6IdentityManagementQuick.so.6
%attr(755,root,root) %{_libdir}/libKPim6IdentityManagementWidgets.so.*.*
%ghost %{_libdir}/libKPim6IdentityManagementWidgets.so.6
%dir %{_libdir}/qt6/qml/org/kde/kidentitymanagement
%{_libdir}/qt6/qml/org/kde/kidentitymanagement/BasicIdentityEditorCard.qml
%{_libdir}/qt6/qml/org/kde/kidentitymanagement/CryptographyEditorCard.qml
%{_libdir}/qt6/qml/org/kde/kidentitymanagement/IdentityConfigurationForm.qml
%{_libdir}/qt6/qml/org/kde/kidentitymanagement/IdentityEditorPage.qml
%{_libdir}/qt6/qml/org/kde/kidentitymanagement/kde-qmlmodule.version
%{_libdir}/qt6/qml/org/kde/kidentitymanagement/kidentitymanagement_quick_plugin.qmltypes
%attr(755,root,root) %{_libdir}/qt6/qml/org/kde/kidentitymanagement/libkidentitymanagement_quick_plugin.so
%{_libdir}/qt6/qml/org/kde/kidentitymanagement/qmldir
%{_datadir}/dbus-1/interfaces/kf6_org.kde.pim.IdentityManager.xml
%{_datadir}/qlogging-categories6/kidentitymanagement.categories
%{_datadir}/qlogging-categories6/kidentitymanagement.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KPim6/KIdentityManagementCore
%{_includedir}/KPim6/KIdentityManagementQuick
%{_includedir}/KPim6/KIdentityManagementWidgets
%{_libdir}/cmake/KPim6IdentityManagementCore
%{_libdir}/cmake/KPim6IdentityManagementQuick
%{_libdir}/cmake/KPim6IdentityManagementWidgets
%{_libdir}/libKPim6IdentityManagementCore.so
%{_libdir}/libKPim6IdentityManagementQuick.so
%{_libdir}/libKPim6IdentityManagementWidgets.so
