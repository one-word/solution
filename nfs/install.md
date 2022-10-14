```
yum install -y nfs-utils -y
systemctl enable rpcbind
systemctl enable nfs
systemctl start rpcbind
systemctl start nfs
vi /etc/exports
  /data/ 192.168.0.0/24(rw,sync,no_root_squash,no_all_squash)
```
