1.turn off the firewall
```
systemctl stop firewalld
systemctl disable firewalld
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux 
setenforce 0
```
2.replace mirror source
```
yum install -y epel-release
yum install -y wget
mv /etc/yum.repos.d /etc/yum.repos.d.backup
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo
yum clean all
yum makecache
```
3.add kubenetes mirron source
```
cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg https://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF
```
4.install kubernetes' utils
```
yum install -y kubelet kubeadm kubectl --disableexcludes=kubernetes
systemctl enable --now kubelet
```
5.add hosts
```
cat <<EOF >>/etc/hosts 
10.10.11.241 master
EOF
```
6.install docker
```
yum install -y yum-utils device-mapper-persistent-data lvm2
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo 
yum makecache fast
yum -y install docker-ce
systemctl start docker
systemctl enable docker
tee /etc/docker/daemon.json <<-'EOF' 
{ 
  "registry-mirrors": ["your repo addr"],
  "exec-opts": ["native.cgroupdriver=systemd"]
}
EOF

systemctl daemon-reload
systemctl restart docker
```
7.install cri-docker
https://github.com/Mirantis/cri-dockerd
```
rpm -ivh https://github.com/Mirantis/cri-dockerd/releases/download/v0.2.6/cri-dockerd-0.2.6-3.el7.x86_64.rpm
vi /lib/systemd/system/cri-docker.service
  ExecStart=/usr/bin/cri-dockerd --container-runtime-endpoint fd:// --pod-infra-container-image registry.cn-hangzhou.aliyuncs.com/google_containers/pause:3.8
systemctl daemon-reload
systemctl restart cri-docker
systemctl enable cri-docker
```
8.shutdown swap
```
swapoff -a
```
9.iptables 1
```
echo 1 > /proc/sys/net/bridge/bridge-nf-call-iptables
echo 1 > /proc/sys/net/bridge/bridge-nf-call-ip6tables
iptables -F
```
