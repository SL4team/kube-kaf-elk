[스파크 설치, 설정 과정]

1. kubernetes 에서 도커 파일 읽어오기
  vi dockerfile	

2. 이미지 빌드
  docker build -t [name:tag]	.[경로]

3. docker images로 확인
  docker images

4. 이미지 푸시
  docker push [ name:tag  ] 

5. yaml 파일 만들기
	role.yaml
	service.yaml
	config.yaml
		마스터 아이피 확인
		컨테이너 이미지 경로 확인
	spark_job.yaml
		arg 명령어 작성 : spark-submit 작동, 파이썬 파일 실행 명령어 작성
		컨테이너 이미지 경로 확인
		메모리 용량 설정
		mount path 설정

6. yaml apply
  kubectl apply -f [ 이름 ] 

7. 파드 확인
  kubectl get pods
  kubectl get svc
  kubectl get role
  kubectl get configmap

8. running 이면 로그 확인
  kubectl logs -f [ 스파크 파드 이름 ] 


-------------------------------------------------------------------------------------------------------------------------------------------------------------------
[설정 파일 목록]

dockerfile_imagebuild : 우분투 기반 스파크 환경 구성된 도커 이미지 빌드 파일

config.yaml : 스파크 환경에 대한 기본 설정 파일

role.yaml : 해당 디플로이먼트에 대한 configmap을 읽어들일 수 있게 해주고 명령어를 실행할 수 있도록 권한 부여하는 역할 설정 파일

service.yaml : 스파크 디플로이먼트의 서비스에 대한 설정 파일

spark_job.yaml : 스파크 디플로이먼트에 대한 정보 파일
