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
  IPADDR=10.10.10.10
  PREFIX=24
  GATEWAY=10.10.10.255
  DNS1=103.16.124.211
  DNS2=223.6.3.5
```
```
vi /etc/sysconfig/network-scripts/ifcfg-eno1s
  TYPE=Ethernet
  PROXY_METHOD=none
  BROWSER_ONLY=no
  BOOTPROTO=none
  DEFROUTE=yes
  IPV4_FAILURE_FATAL=no
  IPV6INIT=yes
  IPV6_AUTOCONF=yes
  IPV6_DEFROUTE=yes
  IPV6_FAILURE_FATAL=no
  IPV6_ADDR_GEN_MODE=stable-privacy
  NAME=ens11f0
  UUID=31b1b957-bf54-4262-9c4c-067e1b34bcea
  DEVICE=ens11f0
  ONBOOT=yes
  BRIDGE=br0
```
```
systemctl restart network
```
