```
mkdir -p /data/kvm-images
virt-install --virt-type=kvm --name=njkvm07 --vcpus=4 --memory=6000 --location=/data/iso/CentOS-7-x86-64-DVD-1708.iso --disk path=/data/kvm-images/njkvm07.qcow2,size=200,format=qcow2 --network bridge=br0 --graphics none --extra-args='console=ttyS0' --force
```
