## Elasticsearch

▷ 역할
 
 엘라스틱 서치라는 이름에서 알 수 있듯이 전문 검색 기능을 제공하는 강력한 소프트웨어 단순 검색 엔진으로 끝나지 않고 
 다양한 프로그램들과 플랫폼을 구성하여 빠른 검색에 사용하던 기술과 다른 프로그램들을 합쳐 대량의 데이터를 수집 저장 처리 분석하는데 활용하게 되었다.

● elasticsearch.yml

▷ 역할

elasticsearch 실행 환경에 대한 실제 설정을 작성하는 파일

    
![image](https://user-images.githubusercontent.com/97927143/161200811-e50e3994-ff24-4ff3-b41a-8de2d7fddd1d.png)




● elasticsearch.txt

▷ 역할

이미지 빌드시 자동 생성되었던 /usr/share/elasticsearch/bin/elasticsearch 
파일이 제대로 작동하지 않아서 다음과 같은 명령어를 추가
    
![image](https://user-images.githubusercontent.com/97927143/161200829-e1c26303-8534-4986-ba28-503d42eac69c.png)



● elasticsearch.yaml : 엘라스틱서치 디플로이먼트 생성 파일

▷ 역할 

쿠버네티스안에 디플로이먼트 형태의 컨테이너 생성

![image](https://user-images.githubusercontent.com/97927143/161200861-6ef8d2cf-f111-4f34-b2bf-667c052974be.png)
