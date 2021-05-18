%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-mocap-optitrack
Version:        0.1.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS mocap_optitrack package

License:        BSD
URL:            http://ros.org/wiki/mocap_optitrack
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-noetic-dynamic-reconfigure
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-nav-msgs
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-tf
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-dynamic-reconfigure
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-nav-msgs
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslaunch
BuildRequires:  ros-noetic-roslint
BuildRequires:  ros-noetic-tf
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Streaming of OptiTrack mocap data to tf This package contains a node that
translates motion capture data from an OptiTrack rig to tf transforms, poses and
2D poses. The node receives packets that are streamed by a NatNet compliant
source, decodes them and broadcasts the poses of configured rigid bodies as tf
transforms, poses, and/or 2D poses. Currently, this node supports the NatNet
streaming protocol v3.0 Copyright (c) 2013, Clearpath Robotics Copyright (c)
2010, University of Bonn, Computer Science Institute VI All rights reserved.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue May 18 2021 Tony Baltovski <tony@baltovski.ca> - 0.1.3-1
- Autogenerated by Bloom

* Wed Mar 24 2021 Tony Baltovski <tony@baltovski.ca> - 0.1.2-1
- Autogenerated by Bloom

* Mon Mar 08 2021 Tony Baltovski <tony@baltovski.ca> - 0.1.1-1
- Autogenerated by Bloom

* Thu Feb 25 2021 Tony Baltovski <tony@baltovski.ca> - 0.1.0-1
- Autogenerated by Bloom

