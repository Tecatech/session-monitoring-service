# Сервис мониторинга сеансов пользователей

## Тестовое задание

Разработать сервис, который выполняет мониторинг подключённых к системе пользователей по `ssh` каждые `30` секунд. При подключении внешнего пользователя по `ssh`, пользователю должно выводиться на экран уведомление (механизм `notify`) с именем пользователя, который подключился к системе удалённо.

## Создание RPM-пакета из сценария на языке Bash

```bash
[tecatexas@10 ~]$ cd
[tecatexas@10 ~]$ rpmdev-setuptree
[tecatexas@10 ~]$ cd ~/rpmbuild/SOURCES/
[tecatexas@10 SOURCES]$ mkdir session-monitoring-1.0/
[tecatexas@10 SOURCES]$ cd session-monitoring-1.0/
[tecatexas@10 session-monitoring-1.0]$ nano session-monitoring.service
[tecatexas@10 session-monitoring-1.0]$ nano session-monitoring
[tecatexas@10 session-monitoring-1.0]$ chmod +x nano session-monitoring
[tecatexas@10 session-monitoring-1.0]$ nano session-monitoring-test
[tecatexas@10 session-monitoring-1.0]$ chmod +x nano session-monitoring-test
[tecatexas@10 session-monitoring-1.0]$ nano session-monitoring.8
[tecatexas@10 session-monitoring-1.0]$ gzip -k session-monitoring.8
[tecatexas@10 session-monitoring-1.0]$ chmod +x nano session-monitoring-test
[tecatexas@10 session-monitoring-1.0]$ cd ~/rpmbuild/SOURCES/
[tecatexas@10 SOURCES]$ tar -cvzf session-monitoring-1.0.tar.gz session-monitoring-1.0/
session-monitoring-1.0/
session-monitoring-1.0/session-monitoring.service
session-monitoring-1.0/session-monitoring
session-monitoring-1.0/session-monitoring-test
session-monitoring-1.0/session-monitoring.8
session-monitoring-1.0/session-monitoring.8.gz
[tecatexas@10 SOURCES]$ cd ../SPECS/
[tecatexas@10 SOURCES]$ nano session-monitoring.spec
[tecatexas@10 SPECS]$ rpmbuild -ba session-monitoring.spec
Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.5IEGAh
+ umask 022
+ cd /home/tecatexas/rpmbuild/BUILD
+ cd /home/tecatexas/rpmbuild/BUILD
+ rm -rf session-monitoring-1.0
+ /usr/bin/tar -xof -
+ /usr/bin/gzip -dc /home/tecatexas/rpmbuild/SOURCES/session-monitoring-1.0.tar.gz
+ STATUS=0
+ '[' 0 -ne 0 ']'
+ cd session-monitoring-1.0
+ /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
+ exit 0
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.KTaJGh
+ umask 022
+ cd /home/tecatexas/rpmbuild/BUILD
+ '[' /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64 '!=' / ']'
+ rm -rf /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64
++ dirname /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64
+ mkdir -p /home/tecatexas/rpmbuild/BUILDROOT
+ mkdir /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64
+ cd session-monitoring-1.0
+ mkdir -p /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/bin
+ mkdir -p /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/etc/systemd/system
+ mkdir -p /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/man/man8
+ install -m 755 session-monitoring /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/bin
+ install -m 644 session-monitoring.service /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/etc/systemd/system
+ install -m 644 session-monitoring.8.gz /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/man/man8
+ install -d /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -d /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/devel/include/contrib
+ install -d /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/etc/selinux/targeted/contexts/users
+ install -m 644 /home/tecatexas/rpmbuild/SOURCES/session_monitoring.pp /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -m 644 /home/tecatexas/rpmbuild/SOURCES/session_monitoring.if /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/devel/include/contrib
+ install -m 644 /home/tecatexas/rpmbuild/SOURCES/my-logger.pp /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -m 644 /home/tecatexas/rpmbuild/SOURCES/my-notifysend.pp /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -m 644 /home/tecatexas/rpmbuild/SOURCES/my-ps.pp /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -m 644 /home/tecatexas/rpmbuild/SOURCES/my-session-monitoring.pp /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/usr/share/selinux/packages
+ '[' noarch = noarch ']'
+ case "${QA_CHECK_RPATHS:-}" in
+ /usr/lib/rpm/check-buildroot
+ /usr/lib/rpm/redhat/brp-ldconfig
/sbin/ldconfig: Warning: ignoring configuration file that cannot be opened: /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64/etc/ld.so.conf: No such file or directory
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
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64
Wrote: /home/tecatexas/rpmbuild/SRPMS/session-monitoring-1.0-1.el8.src.rpm
Wrote: /home/tecatexas/rpmbuild/RPMS/noarch/session-monitoring-1.0-1.el8.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.tEtCfk
+ umask 022
+ cd /home/tecatexas/rpmbuild/BUILD
+ cd session-monitoring-1.0
+ /usr/bin/rm -rf /home/tecatexas/rpmbuild/BUILDROOT/session-monitoring-1.0-1.el8.x86_64
+ exit 0
```

## Настройка политики SELinux

```bash
[tecatexas@10 SOURCES]$ sepolicy generate --init session-monitoring
Created the following files:
/home/tecatexas/rpmbuild/session_monitoring.te # Type Enforcement file
/home/tecatexas/rpmbuild/session_monitoring.if # Interface file
/home/tecatexas/rpmbuild/session_monitoring.fc # File Contexts file
/home/tecatexas/rpmbuild/session_monitoring_selinux.spec # Spec file
/home/tecatexas/rpmbuild/session_monitoring.sh # Setup Script
[tecatexas@10 SPECS]$ sudo ./session_monitoring.sh
Building and Loading Policy
+ make -f /usr/share/selinux/devel/Makefile session_monitoring.pp
Compiling targeted session_monitoring module
Creating targeted session_monitoring.pp policy package
rm tmp/session_monitoring.mod tmp/session_monitoring.mod.fc
+ /usr/sbin/semodule -i session_monitoring.pp
+ sepolicy manpage -p . -d session_monitoring_t
./session_monitoring_selinux.8
+ /sbin/restorecon -F -R -v /home/tecatexas/rpmbuild/SOURCES/session-monitoring
++ pwd
+ pwd=/home/tecatexas/rpmbuild/SOURCES
+ rpmbuild --define '_sourcedir /home/tecatexas/rpmbuild/SOURCES' --define '_specdir /home/tecatexas/rpmbuild/SOURCES' --define '_builddir /home/tecatexas/rpmbuild/SOURCES' --define '_srcrpmdir /home/tecatexas/rpmbuild/SOURCES' --define '_rpmdir /home/tecatexas/rpmbuild/SOURCES' --define '_buildrootdir /home/tecatexas/rpmbuild/SOURCES/.build' -ba session_monitoring_selinux.spec
Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.b1sW2E
+ umask 022
+ cd /home/tecatexas/rpmbuild/SOURCES
+ '[' /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64 '!=' / ']'
+ rm -rf /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64
++ dirname /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64
+ mkdir -p /home/tecatexas/rpmbuild/SOURCES/.build
+ mkdir /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64
+ install -d /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -m 644 /home/tecatexas/rpmbuild/SOURCES/session_monitoring.pp /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/usr/share/selinux/packages
+ install -d /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/usr/share/selinux/devel/include/contrib
+ install -m 644 /home/tecatexas/rpmbuild/SOURCES/session_monitoring.if /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/usr/share/selinux/devel/include/contrib/
+ install -d /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/usr/share/man/man8/
+ install -m 644 /home/tecatexas/rpmbuild/SOURCES/session_monitoring_selinux.8 /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/usr/share/man/man8/session_monitoring_selinux.8
+ install -d /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64/etc/selinux/targeted/contexts/users/
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
Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64
Wrote: /home/tecatexas/rpmbuild/SOURCES/session_monitoring_selinux-1.0-1.el8.src.rpm
Wrote: /home/tecatexas/rpmbuild/SOURCES/noarch/session_monitoring_selinux-1.0-1.el8.noarch.rpm
Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.hgIzFG
+ umask 022
+ cd /home/tecatexas/rpmbuild/SOURCES
+ /usr/bin/rm -rf /home/tecatexas/rpmbuild/SOURCES/.build/session_monitoring_selinux-1.0-1.el8.x86_64
+ exit 0
[tecatexas@10 SOURCES]$ sudo chcon -h system_u:object_r:session-monitoring_exec_t:s0 /usr/bin/session-monitoring
[tecatexas@10 SOURCES]$ ps -eZ | grep session-monitor
system_u:object_r:session-monitoring_exec_t:s0 14134 ?  00:00:00 session-monitor
```

## Электронная цифровая подпись RPM-пакета

```bash
[tecatexas@10 rpmbuild]$ gpg2 --gen-key
[tecatexas@10 rpmbuild]$ gpg2 --export -a 'Rodionov Dmitriy' > ~/rpmbuild/RPM-GPG-KEY-Rodionov-Dmitriy
[tecatexas@10 rpmbuild]$ nano ~/.rpmmacros
[tecatexas@10 rpmbuild]$ rpm --addsign ~/rpmbuild/RPMS/*/*.rpm
/home/tecatexas/rpmbuild/RPMS/noarch/session-monitoring-1.0-1.el8.noarch.rpm:
```

## Создание RPM-репозитория

```bash
[tecatexas@10 rpmbuild]$ sudo mkdir -p /var/www/html/session-monitoring-repo/
[tecatexas@10 rpmbuild]$ sudo cp ~/rpmbuild/RPMS/*/*.rpm /var/www/html/session-monitoring-repo/
[tecatexas@10 rpmbuild]$ sudo cp ~/rpmbuild/RPM-GPG-KEY-Rodionov-Dmitriy /var/www/html/session-monitoring-repo/
[tecatexas@10 rpmbuild]$ sudo createrepo -v /var/www/html/session-monitoring-repo/
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
[tecatexas@10 rpmbuild]$ sudo systemctl enable httpd.service
[tecatexas@10 rpmbuild]$ sudo systemctl start httpd.service
[tecatexas@10 rpmbuild]$ sudo systemctl start httpd.service
[tecatexas@10 rpmbuild]$ sudo yum install session-monitoring
Package session-monitoring-1.0-1.el8.noarch is already installed.
Dependencies resolved.
Nothing to do.
Complete!
[tecatexas@10 rpmbuild]$ sudo systemctl start session-monitoring
[tecatexas@10 rpmbuild]$ sudo systemctl status session-monitoring
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

```bash
[tecatexas@10 rpmbuild]$ journalctl -f -u session-monitoring
-- Logs begin at Sun 2022-05-20 05:45:34 EDT. --
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
[tecatexas@10 rpmbuild]$ sudo cat /var/log/messages | grep session-monitoring
May 20 06:58:20 10 systemd[1]: session-monitoring.service: Succeeded.
May 20 07:09:42 10 systemd[1]: session-monitoring.service: Succeeded.
[tecatexas@10 rpmbuild]$ sudo kill -SIGUSR1 14134
[tecatexas@10 rpmbuild]$ sudo systemctl status session-monitoring
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
[tecatexas@10 rpmbuild]$ cd SOURCES/session-monitoring-1.0/
[tecatexas@10 session-monitoring-1.0]$ ./session-monitoring-test
new_user@127.0.0.1's password:
new_user@127.0.0.1's password:
Service works correctly
[tecatexas@10 session-monitoring-1.0]$ man session-monitoring
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