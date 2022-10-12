```
kubeadm init --apiserver-advertise-address=10.10.11.241 --kubernetes-version v1.25.2 --service-cidr=10.96.0.0/16 --pod-network-cidr=10.244.0.0/16 --image-repository=registry.aliyuncs.com/google_containers --cri-socket unix:///var/run/cri-dockerd.sock --control-plane-endpoint="master"
```
