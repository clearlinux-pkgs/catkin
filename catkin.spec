#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : catkin
Version  : 0.8.8
Release  : 46
URL      : https://github.com/ros/catkin/archive/0.8.8/catkin-0.8.8.tar.gz
Source0  : https://github.com/ros/catkin/archive/0.8.8/catkin-0.8.8.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: catkin-bin = %{version}-%{release}
Requires: catkin-data = %{version}-%{release}
Requires: catkin-license = %{version}-%{release}
Requires: catkin-python = %{version}-%{release}
Requires: catkin-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : catkin-data
BuildRequires : catkin_pkg
BuildRequires : empy
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : python3

%description
.. image:: https://www.gravatar.com/avatar/ebfbbd6f16ce1f0dc30fc7c82c38d688
:width: 100px

%package bin
Summary: bin components for the catkin package.
Group: Binaries
Requires: catkin-data = %{version}-%{release}
Requires: catkin-license = %{version}-%{release}

%description bin
bin components for the catkin package.


%package data
Summary: data components for the catkin package.
Group: Data

%description data
data components for the catkin package.


%package dev
Summary: dev components for the catkin package.
Group: Development
Requires: catkin-bin = %{version}-%{release}
Requires: catkin-data = %{version}-%{release}
Provides: catkin-devel = %{version}-%{release}
Requires: catkin = %{version}-%{release}

%description dev
dev components for the catkin package.


%package license
Summary: license components for the catkin package.
Group: Default

%description license
license components for the catkin package.


%package python
Summary: python components for the catkin package.
Group: Default
Requires: catkin-python3 = %{version}-%{release}

%description python
python components for the catkin package.


%package python3
Summary: python3 components for the catkin package.
Group: Default
Requires: python3-core

%description python3
python3 components for the catkin package.


%prep
%setup -q -n catkin-0.8.8
cd %{_builddir}/catkin-0.8.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1595611492
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DCATKIN_BUILD_BINARY_PACKAGE=TRUE
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1595611492
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/catkin
cp %{_builddir}/catkin-0.8.8/LICENSE %{buildroot}/usr/share/package-licenses/catkin/8a5f2893445b1f334b6c2554e38bf39f4ab70913
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/catkin_find
/usr/bin/catkin_init_workspace
/usr/bin/catkin_make
/usr/bin/catkin_make_isolated
/usr/bin/catkin_test_results
/usr/bin/catkin_topological_order

%files data
%defattr(-,root,root,-)
/usr/share/catkin/LICENSE
/usr/share/catkin/cmake/all.cmake
/usr/share/catkin/cmake/assert.cmake
/usr/share/catkin/cmake/atomic_configure_file.cmake
/usr/share/catkin/cmake/catkinConfig-version.cmake
/usr/share/catkin/cmake/catkinConfig.cmake
/usr/share/catkin/cmake/catkin_add_env_hooks.cmake
/usr/share/catkin/cmake/catkin_destinations.cmake
/usr/share/catkin/cmake/catkin_download.cmake
/usr/share/catkin/cmake/catkin_generate_environment.cmake
/usr/share/catkin/cmake/catkin_install_python.cmake
/usr/share/catkin/cmake/catkin_libraries.cmake
/usr/share/catkin/cmake/catkin_metapackage.cmake
/usr/share/catkin/cmake/catkin_package.cmake
/usr/share/catkin/cmake/catkin_package_xml.cmake
/usr/share/catkin/cmake/catkin_python_setup.cmake
/usr/share/catkin/cmake/catkin_symlink_install.cmake
/usr/share/catkin/cmake/catkin_workspace.cmake
/usr/share/catkin/cmake/custom_install.cmake
/usr/share/catkin/cmake/debug_message.cmake
/usr/share/catkin/cmake/em/order_packages.cmake.em
/usr/share/catkin/cmake/em/pkg.pc.em
/usr/share/catkin/cmake/em_expand.cmake
/usr/share/catkin/cmake/empy.cmake
/usr/share/catkin/cmake/env-hooks/05.catkin_make.bash
/usr/share/catkin/cmake/env-hooks/05.catkin_make_isolated.bash
/usr/share/catkin/cmake/find_program_required.cmake
/usr/share/catkin/cmake/interrogate_setup_dot_py.py
/usr/share/catkin/cmake/legacy.cmake
/usr/share/catkin/cmake/list_append_deduplicate.cmake
/usr/share/catkin/cmake/list_append_unique.cmake
/usr/share/catkin/cmake/list_insert_in_workspace_order.cmake
/usr/share/catkin/cmake/order_paths.py
/usr/share/catkin/cmake/parse_package_xml.py
/usr/share/catkin/cmake/platform/lsb.cmake
/usr/share/catkin/cmake/platform/ubuntu.cmake
/usr/share/catkin/cmake/platform/windows.cmake
/usr/share/catkin/cmake/python.cmake
/usr/share/catkin/cmake/safe_execute_process.cmake
/usr/share/catkin/cmake/shell.cmake
/usr/share/catkin/cmake/stamp.cmake
/usr/share/catkin/cmake/string_starts_with.cmake
/usr/share/catkin/cmake/symlink_install/catkin_install_logic.cmake
/usr/share/catkin/cmake/symlink_install/catkin_symlink_install.cmake.in
/usr/share/catkin/cmake/symlink_install/catkin_symlink_install_append_install_code.cmake
/usr/share/catkin/cmake/symlink_install/catkin_symlink_install_directory.cmake
/usr/share/catkin/cmake/symlink_install/catkin_symlink_install_files.cmake
/usr/share/catkin/cmake/symlink_install/catkin_symlink_install_programs.cmake
/usr/share/catkin/cmake/symlink_install/catkin_symlink_install_targets.cmake
/usr/share/catkin/cmake/symlink_install/install.cmake
/usr/share/catkin/cmake/templates/Doxyfile.in
/usr/share/catkin/cmake/templates/__init__.py.in
/usr/share/catkin/cmake/templates/_setup_util.py.in
/usr/share/catkin/cmake/templates/cfg-extras.context.py.in
/usr/share/catkin/cmake/templates/env-hook.context.py.in
/usr/share/catkin/cmake/templates/env.bat.in
/usr/share/catkin/cmake/templates/env.sh.in
/usr/share/catkin/cmake/templates/generate_cached_setup.py.in
/usr/share/catkin/cmake/templates/local_setup.bash.in
/usr/share/catkin/cmake/templates/local_setup.bat.in
/usr/share/catkin/cmake/templates/local_setup.sh.in
/usr/share/catkin/cmake/templates/local_setup.zsh.in
/usr/share/catkin/cmake/templates/order_packages.context.py.in
/usr/share/catkin/cmake/templates/pkg.context.pc.in
/usr/share/catkin/cmake/templates/pkgConfig-version.cmake.in
/usr/share/catkin/cmake/templates/pkgConfig.cmake.in
/usr/share/catkin/cmake/templates/python_distutils_install.bat.in
/usr/share/catkin/cmake/templates/python_distutils_install.sh.in
/usr/share/catkin/cmake/templates/python_win32_wrapper.cpp.in
/usr/share/catkin/cmake/templates/relay.py.in
/usr/share/catkin/cmake/templates/rosinstall.in
/usr/share/catkin/cmake/templates/safe_execute_install.cmake.in
/usr/share/catkin/cmake/templates/script.bash.in
/usr/share/catkin/cmake/templates/script.bat.in
/usr/share/catkin/cmake/templates/script.in
/usr/share/catkin/cmake/templates/script.py.in
/usr/share/catkin/cmake/templates/script.sh.in
/usr/share/catkin/cmake/templates/setup.bash.in
/usr/share/catkin/cmake/templates/setup.bat.in
/usr/share/catkin/cmake/templates/setup.sh.in
/usr/share/catkin/cmake/templates/setup.zsh.in
/usr/share/catkin/cmake/test/catkin_download_test_data.cmake
/usr/share/catkin/cmake/test/download_checkmd5.py
/usr/share/catkin/cmake/test/gtest.cmake
/usr/share/catkin/cmake/test/nosetests.cmake
/usr/share/catkin/cmake/test/remove_test_results.py
/usr/share/catkin/cmake/test/run_tests.py
/usr/share/catkin/cmake/test/tests.cmake
/usr/share/catkin/cmake/tools/bz2.cmake
/usr/share/catkin/cmake/tools/doxygen.cmake
/usr/share/catkin/cmake/tools/libraries.cmake
/usr/share/catkin/cmake/tools/rt.cmake
/usr/share/catkin/cmake/tools/threads.cmake
/usr/share/catkin/cmake/toplevel.cmake
/usr/share/catkin/package.xml

%files dev
%defattr(-,root,root,-)
/usr/lib64/pkgconfig/catkin.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/catkin/8a5f2893445b1f334b6c2554e38bf39f4ab70913

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
