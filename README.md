# Сервис мониторинга сеансов пользователей

## Тестовое задание

Разработать сервис, который выполняет мониторинг подключённых к системе пользователей по `ssh` каждые `30` секунд. При подключении внешнего пользователя по `ssh`, пользователю должно выводиться на экран уведомление (механизм `notify`) с именем пользователя, который подключился к системе удалённо.

## Создание RPM-пакета из сценария на языке Bash

```
[tecatech@10 ~]$ cd
[tecatech@10 ~]$ rpmdev-setuptree
[tecatech@10 ~]$ cd ~/rpmbuild/SOURCES/
[tecatech@10 SOURCES]$ mkdir session-monitoring-1.0/
[tecatech@10 SOURCES]$ cd session-monitoring-1.0/
[tecatech@10 session-monitoring-1.0]$ nano session-monitoring.service
[tecatech@10 session-monitoring-1.0]$ nano session-monitoring
[tecatech@10 session-monitoring-1.0]$ chmod +x nano session-monitoring
[tecatech@10 session-monitoring-1.0]$ nano session-monitoring-test
[tecatech@10 session-monitoring-1.0]$ chmod +x nano session-monitoring-test
[tecatech@10 session-monitoring-1.0]$ nano session-monitoring.8
[tecatech@10 session-monitoring-1.0]$ gzip -k session-monitoring.8
[tecatech@10 session-monitoring-1.0]$ chmod +x nano session-monitoring-test
[tecatech@10 session-monitoring-1.0]$ cd ~/rpmbuild/SOURCES/
[tecatech@10 SOURCES]$ tar -cvzf session-monitoring-1.0.tar.gz session-monitoring-1.0/
session-monitoring-1.0/
session-monitoring-1.0/session-monitoring.service
session-monitoring-1.0/session-monitoring
session-monitoring-1.0/session-monitoring-test
session-monitoring-1.0/session-monitoring.8
session-monitoring-1.0/session-monitoring.8.gz
[tecatech@10 SOURCES]$ cd ../SPECS/
[tecatech@10 SPECS]$ nano session-monitoring.spec
[tecatech@10 SPECS]$ rpmbuild -ba session-monitoring.spec
Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.5IEGAh
+ umask 022
+ cd /home/tecatech/rpmbuild/BUILD
+ cd /home/tecatech/rpmbuild/BUILD
+ rm -rf session-monitoring-1.0
+ /usr/bin/tar -xof -
+ /usr/bin/gzip -dc /home/tecatech/rpmbuild/SOURCES/session-monitoring-1.0.tar.gz
+ STATUS=0
+ '[' 0 -ne 0 ']'
+ cd session-monitoring-1.0
+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
+ exit 0
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.KTaJGh
+ umask 022
+ cd /home/tecatech/rpmbuild/BUILD
+ '[' /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64 '!=' / ']'
+ rm -rf /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64
++ dirname /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64
+ mkdir -p /home/tecatech/rpmbuild/BUILDROOT
+ mkdir /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64
+ cd session-monitoring-1.0
+ mkdir -p /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/bin
+ mkdir -p /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/etc/systemd/system
+ mkdir -p /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/man/man8
+ install -m 755 session-monitoring /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/bin
+ install -m 644 session-monitoring.service /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/etc/systemd/system
+ install -m 644 session-monitoring.8.gz /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/man/man8
+ install -d /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -d /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/devel/include/contrib
+ install -d /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/etc/selinux/targeted/contexts/users
+ install -m 644 /home/tecatech/rpmbuild/SOURCES/session_monitoring.pp /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -m 644 /home/tecatech/rpmbuild/SOURCES/session_monitoring.if /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/devel/include/contrib
+ install -m 644 /home/tecatech/rpmbuild/SOURCES/my-logger.pp /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -m 644 /home/tecatech/rpmbuild/SOURCES/my-notifysend.pp /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -m 644 /home/tecatech/rpmbuild/SOURCES/my-ps.pp /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -m 644 /home/tecatech/rpmbuild/SOURCES/my-session-monitoring.pp /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/packages
+ '[' noarch = noarch ']'
+ case "${QA_CHECK_RPATHS:-}" in
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/redhat/brp-ldconfig
/sbin/ldconfig: Warning: ignoring configuration file that cannot be opened: /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/etc/ld.so.conf: No such file or directory
+ /usr/lib/rpm/brp-compress
+ /usr/lib/rpm/brp-strip /usr/bin/strip
+ /usr/lib/rpm/brp-strip-comment-note /usr/bin/strip /usr/bin/objdump
+ /usr/lib/rpm/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/brp-python-bytecompile '' 1
+ /usr/lib/rpm/brp-python-hardlink
+ PYTHON3=/usr/libexec/platform-python
+ /usr/lib/rpm/redhat/brp-mangle-shebangs
Processing files: session-monitoring-1.0-1.el8.noarch
Provides: session-monitoring = 1.0-1.el8
Requires(interp): /bin/sh /bin/sh
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires(post): /bin/sh libselinux-utils policycoreutils selinux-policy-base >= 3.14.3-80 selinux-policy-targeted >= 3.14.3-80
Requires(postun): /bin/sh
Requires: /bin/bash
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64
Wrote: /home/tecatech/rpmbuild/SRPMS/session-monitoring-1.0-1.el8.src.rpm
Wrote: /home/tecatech/rpmbuild/RPMS/noarch/session-monitoring-1.0-1.el8.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.tEtCfk
+ umask 022
+ cd /home/tecatech/rpmbuild/BUILD
+ cd session-monitoring-1.0
+ /usr/bin/rm -rf /home/tecatech/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64
+ exit 0
```

## Настройка политики SELinux

```
[tecatech@10 SOURCES]$ sepolicy generate --init session-monitoring
Created the following files:
/home/tecatech/rpmbuild/session_monitoring.te # Type Enforcement file
/home/tecatech/rpmbuild/session_monitoring.if # Interface file
/home/tecatech/rpmbuild/session_monitoring.fc # File Contexts file
/home/tecatech/rpmbuild/session_monitoring_selinux.spec # Spec file
/home/tecatech/rpmbuild/session_monitoring.sh # Setup Script
[tecatech@10 SOURCES]$ sudo ./session_monitoring.sh
Building and Loading Policy
+ make -f /usr/share/selinux/devel/Makefile session_monitoring.pp
Compiling targeted session_monitoring module
Creating targeted session_monitoring.pp policy package
rm tmp/session_monitoring.mod tmp/session_monitoring.mod.fc
+ /usr/sbin/semodule -i session_monitoring.pp
+ sepolicy manpage -p . -d session_monitoring_t
./session_monitoring_selinux.8
+ /sbin/restorecon -F -R -v /home/tecatech/rpmbuild/SOURCES/session-monitoring
++ pwd
+ pwd=/home/tecatech/rpmbuild/SOURCES
+ rpmbuild --define '_sourcedir /home/tecatech/rpmbuild/SOURCES' --define '_specdir /home/tecatech/rpmbuild/SOURCES' --define '_builddir /home/tecatech/rpmbuild/SOURCES' --define '_srcrpmdir /home/tecatech/rpmbuild/SOURCES' --define '_rpmdir /home/tecatech/rpmbuild/SOURCES' --define '_buildrootdir /home/tecatech/rpmbuild/SOURCES/.build' -ba session_monitoring_selinux.spec
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.b1sW2E
+ umask 022
+ cd /home/tecatech/rpmbuild/SOURCES
+ '[' /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64 '!=' / ']'
+ rm -rf /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64
++ dirname /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64
+ mkdir -p /home/tecatech/rpmbuild/SOURCES/.build
+ mkdir /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64
+ install -d /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -m 644 /home/tecatech/rpmbuild/SOURCES/session_monitoring.pp /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -d /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/usr/share/selinux/devel/include/contrib
+ install -m 644 /home/tecatech/rpmbuild/SOURCES/session_monitoring.if /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/usr/share/selinux/devel/include/contrib/
+ install -d /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/usr/share/man/man8/
+ install -m 644 /home/tecatech/rpmbuild/SOURCES/session_monitoring_selinux.8 /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/usr/share/man/man8/session_monitoring_selinux.8
+ install -d /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/etc/selinux/targeted/contexts/users/
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/redhat/brp-ldconfig
/sbin/ldconfig: Warning: ignoring configuration file that cannot be opened: /etc/ld.so.conf: No such file or directory
+ /usr/lib/rpm/brp-compress
+ /usr/lib/rpm/brp-strip /usr/bin/strip
+ /usr/lib/rpm/brp-strip-comment-note /usr/bin/strip /usr/bin/objdump
+ /usr/lib/rpm/brp-strip-static-archive /usr/bin/strip
+ /usr/lib/rpm/brp-python-bytecompile '' 1
+ /usr/lib/rpm/brp-python-hardlink
+ PYTHON3=/usr/libexec/platform-python
+ /usr/lib/rpm/redhat/brp-mangle-shebangs
Processing files: session_monitoring_selinux-1.0-1.el8.noarch
Provides: session_monitoring_selinux = 1.0-1.el8
Requires(interp): /bin/sh /bin/sh
Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires(post): /bin/sh policycoreutils selinux-policy-base >= 3.14.3-80
Requires(postun): /bin/sh policycoreutils
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64
Wrote: /home/tecatech/rpmbuild/SOURCES/session_monitoring_selinux-1.0-1.el8.src.rpm
Wrote: /home/tecatech/rpmbuild/SOURCES/noarch/session_monitoring_selinux-1.0-1.el8.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.hgIzFG
+ umask 022
+ cd /home/tecatech/rpmbuild/SOURCES
+ /usr/bin/rm -rf /home/tecatech/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64
+ exit 0
[tecatech@10 SOURCES]$ sudo chcon -h system_u:object_r:session-monitoring_exec_t:s0 /usr/bin/session-monitoring
[tecatech@10 SOURCES]$ ps -eZ | grep session-monitor
system_u:object_r:session-monitoring_exec_t:s0 14134 ?  00:00:00 session-monitor
```

## Электронная цифровая подпись RPM-пакета

```
[tecatech@10 rpmbuild]$ gpg2 --gen-key
[tecatech@10 rpmbuild]$ gpg2 --export -a 'Rodionov Dmitriy' > ~/rpmbuild/RPM-GPG-KEY-Rodionov-Dmitriy
[tecatech@10 rpmbuild]$ nano ~/.rpmmacros
[tecatech@10 rpmbuild]$ rpm --addsign ~/rpmbuild/RPMS/*/*.rpm
/home/tecatech/rpmbuild/RPMS/noarch/session-monitoring-1.0-1.el8.noarch.rpm:
```

## Создание RPM-репозитория

```
[tecatech@10 rpmbuild]$ sudo mkdir -p /var/www/html/session-monitoring-repo/
[tecatech@10 rpmbuild]$ sudo cp ~/rpmbuild/RPMS/*/*.rpm /var/www/html/session-monitoring-repo/
[tecatech@10 rpmbuild]$ sudo cp ~/rpmbuild/RPM-GPG-KEY-Rodionov-Dmitriy /var/www/html/session-monitoring-repo/
[tecatech@10 rpmbuild]$ sudo createrepo -v /var/www/html/session-monitoring-repo/
07:09:27: Version: 0.17.2 (Features: DeltaRPM LegacyWeakdeps )
07:09:27: Signal handler setup
07:09:27: Thread pool ready
Directory walk started
07:09:27: Adding pkg: /var/www/html/session-monitoring-repo/session-monitoring-1.0-1.el8.noarch.rpm
07:09:27: Dir to scan: /var/www/html/session-monitoring-repo/.repodata
07:09:27: Package count: 1
Directory walk done - 1 packages
Temporary output repo path: /var/www/html/session-monitoring-repo/.repodata/
07:09:27: Creating .xml.gz files
07:09:27: Setting number of packages
Preparing sqlite DBs
07:09:27: Creating databases
07:09:27: Thread pool user data ready
Pool started (with 5 workers)
Pool finished
07:09:27: Generating repomd.xml
07:09:27: Old repodata doesn't exists: Cannot rename /var/www/html/session-monitoring-repo/repodata/ -> /var/www/html/session-monitoring-repo/repodata.old.14000.20220522070927.936138: No such file or directory
07:09:27: Renamed /var/www/html/session-monitoring-repo/.repodata/ -> /var/www/html/session-monitoring-repo/repodata/
07:09:27: Memory cleanup
07:09:27: All done
[tecatech@10 rpmbuild]$ sudo systemctl enable httpd.service
[tecatech@10 rpmbuild]$ sudo systemctl start httpd.service
[tecatech@10 rpmbuild]$ sudo systemctl start httpd.service
[tecatech@10 rpmbuild]$ sudo yum install session-monitoring
Package session-monitoring-1.0-1.el8.noarch is already installed.
Dependencies resolved.
Nothing to do.
Complete!
[tecatech@10 rpmbuild]$ sudo systemctl start session-monitoring
[tecatech@10 rpmbuild]$ sudo systemctl status session-monitoring
● session-monitoring.service - Session monitoring service
   Loaded: loaded (/etc/systemd/system/session-monitoring.service; enabled; vendor preset: disabled)
   Active: active (running) since Fri 2022-05-20 07:10:00 EDT; 5s ago
     Docs: man:session-monitoring(8)
 Main PID: 14134 (session-monitor)
    Tasks: 2 (limit: 11263)
   Memory: 576.0K
   CGroup: /system.slice/session-monitoring.service
           ├─14134 /bin/bash /usr/bin/session-monitoring
           └─14155 sleep 30
```

## Демонстрация работы сервиса

```
[tecatech@10 rpmbuild]$ pstree
systemd─┬─ModemManager───2*[{ModemManager}]
        ├─NetworkManager───2*[{NetworkManager}]
        ├─accounts-daemon───2*[{accounts-daemon}]
        ├─alsactl
        ├─atd
        ├─auditd─┬─sedispatch
        │        └─2*[{auditd}]
        ├─avahi-daemon───avahi-daemon
        ├─chronyd
        ├─colord───2*[{colord}]
        ├─crond
        ├─cupsd
        ├─dbus-daemon
        ├─dnsmasq───dnsmasq
        ├─firewalld───{firewalld}
        ├─fprintd───4*[{fprintd}]
        ├─gdm─┬─gdm-session-wor─┬─gdm-wayland-ses─┬─gnome-session-b─┬─gnome-she+
        │     │                 │                 │                 ├─gnome-sof+
        │     │                 │                 │                 ├─gsd-a11y-+
        │     │                 │                 │                 ├─gsd-accou+
        │     │                 │                 │                 ├─gsd-clipb+
        │     │                 │                 │                 ├─gsd-color+++
        │     │                 │                 │                 ├─gsd-datet+
        │     │                 │                 │                 ├─gsd-disk-+
        │     │                 │                 │                 ├─gsd-house+
        │     │                 │                 │                 ├─gsd-keybo+
        │     │                 │                 │                 ├─gsd-media+
        │     │                 │                 │                 ├─gsd-mouse+++
        │     │                 │                 │                 ├─gsd-power+++
        │     │                 │                 │                 ├─gsd-print+
        │     │                 │                 │                 ├─gsd-rfkil+
        │     │                 │                 │                 ├─gsd-scree+
        │     │                 │                 │                 ├─gsd-shari+
        │     │                 │                 │                 ├─gsd-smart+
        │     │                 │                 │                 ├─gsd-sound+++
        │     │                 │                 │                 ├─gsd-wacom+++
        │     │                 │                 │                 ├─gsd-xsett+
        │     │                 │                 │                 ├─tracker-m+
        │     │                 │                 │                 ├─tracker-m+
        │     │                 │                 │                 └─3*[{gnome+
        │     │                 │                 └─2*[{gdm-wayland-ses}]
        │     │                 └─3*[{gdm-session-wor}]
        │     └─2*[{gdm}]
        ├─geoclue───2*[{geoclue}]
        ├─gnome-keyring-d───3*[{gnome-keyring-d}]
        ├─3*[gpg-agent]
        ├─gsd-printer───3*[{gsd-printer}]
        ├─gssproxy───5*[{gssproxy}]
        ├─httpd─┬─httpd
        │       ├─2*[httpd───64*[{httpd}]]
        │       └─httpd───80*[{httpd}]
        ├─ibus-x11───6*[{ibus-x11}]
        ├─ksmtuned───sleep
        ├─lsmd
        ├─mcelog
        ├─nm-dispatcher───2*[{nm-dispatcher}]
        ├─packagekitd───2*[{packagekitd}]
        ├─polkitd───5*[{polkitd}]
        ├─rhsmcertd
        ├─rpcbind
        ├─rsyslogd───2*[{rsyslogd}]
        ├─rtkit-daemon───2*[{rtkit-daemon}]
        ├─session-monitor───sleep
        ├─smartd
        ├─sshd
        ├─sssd─┬─sssd_be
        │      └─sssd_nss
        ├─sssd_kcm
        ├─systemd─┬─(sd-pam)
        │         ├─at-spi-bus-laun─┬─dbus-daemon
        │         │                 └─3*[{at-spi-bus-laun}]
        │         ├─at-spi2-registr───2*[{at-spi2-registr}]
        │         ├─dbus-daemon
        │         ├─dconf-service───2*[{dconf-service}]
        │         ├─evolution-addre─┬─evolution-addre───5*[{evolution-addre}]
        │         │                 └─4*[{evolution-addre}]
        │         ├─evolution-calen─┬─evolution-calen───8*[{evolution-calen}]
        │         │                 └─4*[{evolution-calen}]
        │         ├─evolution-sourc───3*[{evolution-sourc}]
        │         ├─gnome-shell-cal───5*[{gnome-shell-cal}]
        │         │
        │         ├─gnome-terminal-─┬─bash───pstree
        │         │                 └─3*[{gnome-terminal-}]
        │         ├─goa-daemon───3*[{goa-daemon}]
        │         ├─goa-identity-se───3*[{goa-identity-se}]
        │         ├─gpg-agent
        │         ├─gvfs-afc-volume───3*[{gvfs-afc-volume}]
        │         ├─gvfs-goa-volume───2*[{gvfs-goa-volume}]
        │         ├─gvfs-gphoto2-vo───2*[{gvfs-gphoto2-vo}]
        │         ├─gvfs-mtp-volume───2*[{gvfs-mtp-volume}]
        │         ├─gvfs-udisks2-vo───3*[{gvfs-udisks2-vo}]
        │         ├─gvfsd─┬─gvfsd-dnssd───2*[{gvfsd-dnssd}]
        │         │       ├─gvfsd-network───3*[{gvfsd-network}]
        │         │       ├─gvfsd-trash───2*[{gvfsd-trash}]
        │         │       └─2*[{gvfsd}]
        │         ├─gvfsd-fuse───5*[{gvfsd-fuse}]
        │         ├─gvfsd-metadata───2*[{gvfsd-metadata}]
        │         ├─ibus-portal───2*[{ibus-portal}]
        │         ├─nautilus───4*[{nautilus}]
        │         ├─pulseaudio───2*[{pulseaudio}]
        │         ├─tracker-store───4*[{tracker-store}]
        │         └─xdg-permission-───2*[{xdg-permission-}]
        ├─systemd-journal
        ├─systemd-logind
        ├─systemd-machine
        ├─systemd-udevd
        ├─tuned───4*[{tuned}]
        ├─udisksd───4*[{udisksd}]
        ├─upowerd───2*[{upowerd}]
        └─wpa_supplicant
[tecatech@10 rpmbuild]$ journalctl -f -u session-monitoring
-- Logs begin at Fri 2022-05-20 05:45:34 EDT. --
May 20 06:38:36 10.0.2.15 systemd[1]: Stopped Session monitoring service.
May 20 06:39:52 10.0.2.15 systemd[1]: Started Session monitoring service.
May 20 06:58:20 10.0.2.15 systemd[1]: Stopping Session monitoring service...
May 20 06:58:20 10.0.2.15 systemd[1]: session-monitoring.service: Succeeded.
May 20 06:58:20 10.0.2.15 systemd[1]: Stopped Session monitoring service.
May 20 06:58:32 10.0.2.15 systemd[1]: Started Session monitoring service.
May 20 07:09:42 10.0.2.15 systemd[1]: Stopping Session monitoring service...
May 20 07:09:42 10.0.2.15 systemd[1]: session-monitoring.service: Succeeded.
May 20 07:09:42 10.0.2.15 systemd[1]: Stopped Session monitoring service.
May 20 07:10:01 10.0.2.15 systemd[1]: Started Session monitoring service.
[tecatech@10 rpmbuild]$ sudo cat /var/log/messages | grep session-monitoring
May 20 06:58:20 10 systemd[1]: session-monitoring.service: Succeeded.
May 20 07:09:42 10 systemd[1]: session-monitoring.service: Succeeded.
[tecatech@10 rpmbuild]$ sudo kill -SIGUSR1 14134
[tecatech@10 rpmbuild]$ sudo systemctl status session-monitoring
● session-monitoring.service - Session monitoring service
   Loaded: loaded (/etc/systemd/system/session-monitoring.service; enabled; vendor preset: disabled)
   Active: active (running) since Fri 2022-05-20 07:10:00 EDT; 1h 21min ago
     Docs: man:session-monitoring(8)
 Main PID: 14134 (session-monitor)
    Tasks: 2 (limit: 11263)
   Memory: 3.4M
   CGroup: /system.slice/session-monitoring.service
           ├─14134 /bin/bash /usr/bin/session-monitoring
           └─24293 sleep 30

May 20 07:10:01 10.0.2.15 systemd[1]: Started Session monitoring service.
May 20 08:24:37 10.0.2.15 root: SSH service catched USR1 signal
May 20 08:24:37 10.0.2.15 systemd[1]: session-monitoring.service: main process exited, code=killed, status=10/USR1
[tecatech@10 rpmbuild]$ cd SOURCES/session-monitoring-1.0/
[tecatech@10 session-monitoring-1.0]$ ./session-monitoring-test
new_user@127.0.0.1's password:
new_user@127.0.0.1's password:
Service works correctly
[tecatech@10 session-monitoring-1.0]$ man session-monitoring
SESSION-MONITOR(8)        SESSION MONITORING SERVICE        SESSION-MONITOR(8)

NAME
       session-monitoring

DESCRIPTION
       session-monitoring  -  monitors users connected to system via ssh every
       30 seconds. When an external user  connects  via  ssh,  a  notification
       (notify  mechanism)  should  be displayed to user with name of the user
       who has connected to the system remotely.

AUTHORS
       Dmitriy Rodionov

SESSION-MONITOR 1.0               20 MAY 2022               SESSION-MONITOR(8)
```