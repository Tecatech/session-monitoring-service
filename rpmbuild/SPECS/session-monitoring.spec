%define relabel_files() restorecon -R -v /usr/bin & restorecon -R -v /usr/lib/systemd/system

%define selinux_policy_version 3.14.3-80

Name:           session-monitoring
Version:        1.0
Release:        1%{?dist}
Summary:        Session Monitoring Service
Group:          Testing
License:        GPL
URL:            https://github.com/Tecatech/session-monitoring-service
Source0:        %{name}-%{version}.tar.gz
Source1:        session_monitoring.pp
Source2:        session_monitoring.if
Source3:        my-logger.pp
Source4:        my-notifysend.pp
Source5:        my-ps.pp
Source6:        my-session-monitoring.pp
BuildRequires:  /bin/cp, /bin/mkdir, /bin/rm, /bin/sudo, libnotify-devel, selinux-policy-devel, systemd
Requires:       /bin/bash, /usr/bin/awk, /usr/bin/cut, /usr/bin/echo, /usr/bin/grep, /usr/bin/logger, /usr/bin/ps, /usr/bin/tr
Requires(post): libselinux-utils, policycoreutils, selinux-policy-base >= %{selinux_policy_version}, selinux-policy-targeted >= %{selinux_policy_version}
BuildArch:      noarch

%description
Session Monitoring Service

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/systemd/system
mkdir -p %{buildroot}%{_mandir}/man8
install -m 755 session-monitoring %{buildroot}%{_bindir}
install -m 644 session-monitoring.service %{buildroot}/etc/systemd/system
install -m 644 session-monitoring.8.gz %{buildroot}%{_mandir}/man8
install -d %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -d %{buildroot}/etc/selinux/targeted/contexts/users
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE4} %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE5} %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE6} %{buildroot}%{_datadir}/selinux/packages

%post
semodule -n -i %{_datadir}/selinux/packages/session_monitoring.pp
if /usr/sbin/selinuxenabled; then
    /usr/sbin/load_policy
    %relabel_files
fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r session-monitoring
    if /usr/sbin/selinuxenabled; then
       /usr/sbin/load_policy
       %relabel_files
    fi;
fi;
exit 0

%files
%{_bindir}/session-monitoring
/etc/systemd/system/session-monitoring.service
%{_mandir}/man8/session-monitoring.8.gz
%defattr(-, root, root, 0755)
%attr(0600, root, root)
%{_datadir}/selinux/packages/session_monitoring.pp
%{_datadir}/selinux/devel/include/contrib/session_monitoring.if
%{_datadir}/selinux/packages/my-logger.pp
%{_datadir}/selinux/packages/my-notifysend.pp
%{_datadir}/selinux/packages/my-ps.pp
%{_datadir}/selinux/packages/my-session-monitoring.pp

%changelog
* Fri May 20 2022 <tecatech>
- Added %{_bindir}/session-monitoring.spec