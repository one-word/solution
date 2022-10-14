```
kubectl create secret docker-registry  --dry-run=client  <name>  --docker-server=<addr> --docker-username=aaa --docker-password=123 --namespace=<ns>  -o yaml > docker-secret.yaml
```
