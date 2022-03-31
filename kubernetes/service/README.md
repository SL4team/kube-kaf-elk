# kubernetes 의 service 부분 입니다.

service 설정과 metallb 설치법이 있습니다.

쿠버네티스 클러스터에 존재하는 Pod 서비스를 외부로 노출시키기 위한 가장 원시적인 방법은 NodePort를 이용하는 것입니다. 

하지만 NodePort는 인스턴스의 IP가 변경되면 해당 서비스에도 이를 반영해야 합니다. 

따라서 Cloud 벤더에서는 LoadBalancer나 Ingress 타입을 통해 서비스를 노출할 수 있도록 지원합니다.
