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
License:        GPL v2 or later
Group:          Development/Tools/Building
Summary:        This is a fake provides for ia32el, it inserts a file to /etc/ld.so.conf.d/
BuildRoot:	%{_tmppath}/%{name}-%{version}-build
Source1:        %{name}.conf
Source1001: packaging/tizen-accelerator.manifest 
BuildRequires:  -rpmlint-Factory -rpmlint-mini -post-build-checks tar
Requires(post):	/bin/chmod

%description
Needed for cross-build speedup
This is a fake provides for ia32el, it inserts a file to /etc/ld.so.conf.d/

%prep

%build
cp %{SOURCE1001} .

%install
mkdir -p %buildroot/emul/ia32-linux
mkdir -p %buildroot/emul/ia32-linux/etc
mkdir -p %buildroot/emul/ia32-linux/lib
mkdir -p %buildroot/emul/ia32-linux/usr
mkdir -p %buildroot/emul/ia32-linux/usr/lib
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
chmod 755 /emul/ia32-linux/usr
chmod 755 /emul/ia32-linux/usr/lib
cd /lib && ln -sf ../emul/ia32-linux/lib/ld-linux.so.2 ld-linux.so.2
#/emul/ia32-linux/sbin/ldconfig

%files
%manifest tizen-accelerator.manifest
%defattr(-,root,root)
/etc/ld.so.conf.d/*
/usr/share/%name/version
/emul
