Summary:	D-Bus support for AppArmor
Name:		apparmor-dbus
Version:	2.3
Epoch:		1
Release:	%mkrel 4
License:	GPL
Group:		System/Servers
URL:		http://forge.novell.com/modules/xfmod/project/?apparmor
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:  libdbus-devel
BuildRequires:  libaudit-devel
BuildRequires:  libapparmor-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
AppArmor is a security framework that proactively protects the operating system
and applications.

This package contains the D-Bus support for AppArmor.

%prep
%setup -q

%build
%serverbuild

export CFLAGS="$RPM_OPT_FLAGS"
%configure
%make 

%install
rm -rf %{buildroot}

%{makeinstall_std}


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS
%doc COPYING
%{_bindir}/apparmor-dbus
