# Elasticsearch 

[ 역할 ]
엘라스틱 서치라는 이름에서 알 수 있듯이 전문(Full Text) 검색 기능을 제공하는 강력한 소프트웨어
단순 검색 엔진으로 끝나지 않고 다양한 프로그램들과 플랫폼을 구성하여 
빠른 검색에 사용하던 기술과 다른 프로그램들을 합쳐 대량의 데이터를 수집 저장 처리 분석하는데 활용하게 되었다.


● elasticsearch.yml

    [ 역할 ]
    elasticsearch 실행 환경에 대한 실제 설정을 작성하는 파일

    elasticsearch.yml 사진 파일 첨부

    ![elasticsearch yml](https://user-images.githubusercontent.com/97823665/161199639-da7055f8-fc53-48c8-8016-5befc8cdacb1.png)



● elasticsearch.txt

    [ 역할 ]
    이미지 빌드시 자동 생성되었던 /usr/share/elasticsearch/bin/elasticsearch 파일이 제대로 작동하지 않아서 다음과 같은 명령어를 추가함
    
    ![usr-share-elasticsearch-bin-elasticsearch](https://user-images.githubusercontent.com/97823665/161199670-08a88ab6-a684-44b5-92b6-51d658f5af04.png)


● elasticsearch.yaml : 엘라스틱서치 디플로이먼트 생성 파일

    [ 역할 ] 
    쿠버네티스안에 디플로이먼트 형태의 컨테이너 생성

    elasticsearch.yaml 사진 파일 첨부
    
    ![image](https://user-images.githubusercontent.com/97823665/161199866-4add87a5-265b-41ab-8113-b268bedacfae.png)
