1.shutdown selinux
```
vi /etc/sysconfig/selinux
  SELinux=disabled
```
2.install utils
```
yum install epel-release net-tools vim unzip zip wget ftp -y
yum install qemu-kvm libvirt virt-install bridge-utils -y
systemctl start libvirtd
systemctl enable libvirtd
```
3.modify network
```
cp -rf /etc/sysconfig/network-scripts /etc/sysconfig/network-scripts-bak
```
```
vi /etc/sysconfig/network-scripts/ifcfg-br0
  TYPE=Bridge
  PROXY_METHOD=none
  BROWSER_ONLY=no
  BOOTPROTO=static
  DEFROUTE=yes
  IPV4_FAILURE_FATAL=no
  IPV6INIT=yes
  IPV6_AUTOCONF=yes
  IPV6_DEFROUTE=yes
  IPV6_FAILURE_FATAL=no
  IPV6_ADDR_GEN_MODE=stable-privacy
  NAME=br0
  #UUID=31b1b957-bf54-4262-9c4c-067e1b34bcea
  DEVICE=br0
  ONBOOT=yes
  IPADDR=10.10.11.240
  PREFIX=24
  GATEWAY=10.10.11.254
  DNS1=103.16.125.251
  DNS2=223.6.6.6
```
```
vi /etc/sysconfig/network-scripts/ifcfg-eno1s
  TYPE="Ethernet"
  PROXY_METHOD="none"
  BROWSER_ONLY="no"
  BOOTPROTO="static"
  DEFROUTE="yes"
  IPV4_FAILURE_FATAL="YES"
  IPV6INIT="yes"
  IPV6_AUTOCONF="yes"
  IPV6_DEFROUTE="yes"
  IPV6_FAILURE_FATAL="no"
  IPV6_ADDR_GEN_MODE="stable-privacy"
  NAME="eno1"
  UUID="bb40d726-8d67-4187-90c3-eb61e1b42d61"
  DEVICE="eno1"
  ONBOOT="yes"
  IPADDR="192.168.1.130"
  NETAMSK=255.255.255.0
  GATEWAY="192.168.1.254"
  DNS1="221.6.4.66"
  IPV6_PRIVACY="no"
  BRIDGE=br0
```
```
systemctl restart network
```
