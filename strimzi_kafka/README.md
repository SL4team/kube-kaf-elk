# strimzi kafka down
wget https://github.com/strimzi/strimzi-kafka-operator/releases/download/0.24.0/strimzi-0.24.0.tar.gz

# strimzi kafka cluser operator 관리용 ns
kubectl create ns kafka create ns kafka

# strimzi 설정 변경, OS에 따라 namespace가 다릅니다 (linux)
sed -i 's/namespace: .*/namespace: kafka/' install/cluster-operator/*RoleBinding*.yaml

# kafka cluster 관리용 ns
kubectl create ns my-kafka-project

# Deployment 설정 변경
vi 060-Deployment-strimzi-cluster-operator.yaml

![image](https://user-images.githubusercontent.com/97927143/161060991-c7b9136e-27dc-4814-b6b8-ab31de7ae73d.png)


  
# CRD 생성 명령어
kubectl apply -f install/cluster-operator/ -n kafka

# kafka와 my-kafka-project에 Rolebinding을 부여하는 명령어
kubectl create -f install/cluster-operator/020-RoleBinding-strimzi-cluster-operator.yaml -n my-kafka-project

kubectl create -f install/cluster-operator/031-RoleBinding-strimzi-cluster-operator-entity-operator-delegation.yaml -n my-kafka-project


모든 설정 후 전체 모습
![image](https://user-images.githubusercontent.com/97927143/161060001-7db5884c-2d9d-43c2-8ef7-517fc8f0f415.png)
![image](https://user-images.githubusercontent.com/97927143/161060022-ddc4815e-f3b2-4b6e-b13f-46314655032e.png)
![image](https://user-images.githubusercontent.com/97927143/161060081-46c023be-2022-4651-92ed-0aae3d443c82.png)
