sed -i 's/sandbox_image = "k8s.gcr.io\/pause:3.5"/sandbox_image = "registry.cn-hangzhou.aliyuncs.com\/google_containers\/pause:3.7"/' /etc/containerd/config.toml
systemctl daemon-reload
systemctl restart containerd
