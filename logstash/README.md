# docker image를 사용한 elasticsearch 설치법.

kubectl apply -f logstash.yaml

kubectl expose deploy elastic --type LoadBalancer --name elastic

kubectl get pods

kubectl exec -it logstash-68469b57c4-x62fw /bin/bash

/usr/share/logstash/bin/logstash -f ./logstash-sample.conf


# logstash.conf
logstash가 kafka에서 data를 가져오는 consumer 일때의 코드 입니다.
