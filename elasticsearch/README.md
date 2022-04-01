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

### [ 역할 ]
엘라스틱 서치라는 이름에서 알 수 있듯이 전문(Full Text) 검색 기능을 제공하는 강력한 소프트웨어
단순 검색 엔진으로 끝나지 않고 다양한 프로그램들과 플랫폼을 구성하여 
빠른 검색에 사용하던 기술과 다른 프로그램들을 합쳐 대량의 데이터를 수집 저장 처리 분석하는데 활용하게 되었다.


● elasticsearch.yml

    [ 역할 ]
    elasticsearch 실행 환경에 대한 실제 설정을 작성하는 파일

    elasticsearch.yml 사진 파일 첨부



● elasticsearch.txt

    [ 역할 ]
    이미지 빌드시 자동 생성되었던 /usr/share/elasticsearch/bin/elasticsearch
    파일이 제대로 작동하지 않아서 다음과 같은 명령어를 개인적으로 추가함

    usr-share-elasticsearch-bin-elasticsearch 사진 첨부
![image](https://user-images.githubusercontent.com/97927143/161200773-1d906021-56a7-41ed-8e47-9ac7931fb1ec.png)


● elasticsearch.yaml : 엘라스틱서치 디플로이먼트 생성 파일

    [ 역할 ] 
    쿠버네티스안에 디플로이먼트 형태의 컨테이너 생성

    elasticsearch.yaml 사진 파일 첨부
