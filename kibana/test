# docker image를 사용한 kibana 설치법.

kubectl apply -f kibana.yaml

kubectl expose deploy kibana --type LoadBalancer --name kibana

kubectl get pods

kubectl exec -it [ 파드이름 ] /bin/bash

service kibana start

sudo sysctl -w vm.max_map_count=262144 ( 할당된 노드에서 )
