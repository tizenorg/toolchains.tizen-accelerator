# spec file for cross-chroot accelerator
#
# Copyright (c) 2010  Jan-Simon Möller (jsmoeller@linuxfoundation.org)
#
Name:           tizen-accelerator
ExclusiveArch:  %arm
AutoReqProv:    0
AutoReqProv:    off
Provides:       ia32el
Provides:       fake-ia32el
Provides:       tizen-accelerator
Version:        1.0.1
Release:        1
VCS:            toolchains/tizen-accelerator#Z910F_PROTEX_0625-2-g7802012545f8d77ce4a0e172642f8304a6e9e64f
License:        GPL v2 or later
Group:          Development/Tools/Building
Summary:        This is a fake provides for ia32el, it inserts a file to /etc/ld.so.conf.d/
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Source1:        tizen-accelerator.conf
BuildRequires:  -rpmlint-Factory -rpmlint-mini -post-build-checks tar
Requires(post):	/bin/chmod

%description
Needed for cross-build speedup
This is a fake provides for ia32el, it inserts a file to /etc/ld.so.conf.d/

%prep

%build

%install
mkdir -p %buildroot/emul/ia32-linux
mkdir -p %buildroot/emul/ia32-linux/etc
mkdir -p %buildroot/emul/ia32-linux/lib
mkdir -p %buildroot/emul/ia32-linux/lib64
mkdir -p %buildroot/emul/ia32-linux/usr
mkdir -p %buildroot/emul/ia32-linux/usr/lib
mkdir -p %buildroot/emul/ia32-linux/usr/lib64
mkdir -p %buildroot/etc/ld.so.conf.d/
cp %{S:1} %buildroot/etc/ld.so.conf.d/
mkdir -p %buildroot/usr/share/%name/
echo "%{version}" > %buildroot/usr/share/%name/version

%clean
rm -rf $RPM_BUILD_ROOT

%post
chmod 755 /emul
chmod 755 /emul/ia32-linux
chmod 755 /emul/ia32-linux/etc
chmod 755 /emul/ia32-linux/lib
chmod 755 /emul/ia32-linux/lib64
chmod 755 /emul/ia32-linux/usr
chmod 755 /emul/ia32-linux/usr/lib
chmod 755 /emul/ia32-linux/usr/lib64
mkdir -p /lib && ln -sf ../emul/ia32-linux/lib/ld-linux.so.2 /lib/ld-linux.so.2
mkdir -p /lib64 && ln -sf ../emul/ia32-linux/lib64/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2
/emul/ia32-linux/sbin/ldconfig

%files
%defattr(-,root,root)
/etc/ld.so.conf.d/*
/usr/share/%name/version
/emul