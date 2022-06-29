k8s reset and flannel reset.
---
```
kubeadm reset
systemctl stop kubelet
systemctl stop docker

ifconfig cni0 down
ifconfig flannel.1 down
ifconfig del flannel.1
ifconfig del cni0

ip link del flannel.1
ip link del cni0

yum install -y bridge-utils
brctl delbr flannel.1
brctl delbr cni0
rm -rf /var/lib/cni/flannel/*
rm -rf /var/lib/cni/networks/cbr0/*
ip link delete cni0
rm -rf /var/lib/cni/network/cni0/*
rm -rf /etc/cni/net.d/*
rm -rf /run/flannel/*
```
