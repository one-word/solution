## 标记节点不可用

```
kubectl cordon <node-name>
```

## 删除所有pod

```
#!/bin/bash
kubectl get pods -A -o wide | grep <node_name> | awk -F ' ' '{print $2}' | while read -r pod; do
  kubectl delete pod "$pod" -n <namespace>
done
```

## 停止Kubernetes agent：停止该节点上运行的Kubernetes agent，这通常是kubelet

## 删除节点：从集群中删除该节点

```
kubectl delete node <node-name>
```
