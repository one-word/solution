```
kubeadm config images list
```
```
#!/bin/bash
images=(
    kube-apiserver:v1.25.2
    kube-controller-manager:v1.25.2
    kube-scheduler:v1.25.2
    kube-proxy:v1.25.2
    pause:3.8
    etcd:3.5.4-0
    coredns/coredns:v1.9.3
)
for imageName in ${images[@]};
do
    docker pull registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName
	docker tag registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName k8s.gcr.io/$imageName
	docker rmi registry.cn-hangzhou.aliyuncs.com/google_containers/$imageName
done
```
