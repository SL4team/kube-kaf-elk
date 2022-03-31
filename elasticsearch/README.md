# docker image를 사용한 elasticsearch 설치법.

kubectl apply -f elasticsearch.yaml

kubectl expose deploy elastic --type LoadBalancer --name elastic

kubectl get pods

kubectl exec -it [ 파드이름 ] /bin/bash

sudo sysctl -w vm.max_map_count=262144 ( 할당된 노드에서 )

vi /usr/share/elasticsearch/bin/elasticsearch

export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64  → 추가
export PATH=$JAVA_HOME/bin:$PATH  → 추가
 
service elasticsearch start
