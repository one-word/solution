```
rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org
rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-2.el7.elrepo.noarch.rpm
yum --disablerepo="*" --enablerepo="elrepo-kernel" list available
yum --enablerepo=elrepo-kernel install kernel-lt -y
vi /etc/default/grub
  GRUB_DEFAULT=0
grub2-mkconfig -o /boot/grub2/grub.cfg
reboot
```
