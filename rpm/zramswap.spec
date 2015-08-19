Name:		zramswap
Version:	1.1.1
Release:	1%{?dist}
Summary:	Sets up zram-based swap devices on boot
Group:		Applications/System
License:	GPL
URL:		https://github.com/mlehtima/zramswap
Source: %{name}-%{version}.tar.gz
Requires:	bash

%description
Zram-based swap (compressed RAM block devices). Based on Arch linux zramswap from https://aur.archlinux.org/packages/zramswap/.

%prep

%setup

%build

%install
  mkdir -p %{buildroot}/lib/systemd/system/multi-user.target.wants/
  mkdir -p %{buildroot}%{_sbindir}
  mkdir -p %{buildroot}/lib/systemd/system/
  cp -p zramctrl %{buildroot}%{_sbindir}/zramctrl
  cp -p zramswap.service %{buildroot}/lib/systemd/system/zramswap.service
  ln -s '../zramswap.service' '%{buildroot}/lib/systemd/system/multi-user.target.wants/zramswap.service'

%files
%defattr(0755, root,root)
%{_sbindir}/zramctrl
/lib/systemd/system/zramswap.service
/lib/systemd/system/multi-user.target.wants/zramswap.service
%changelog
