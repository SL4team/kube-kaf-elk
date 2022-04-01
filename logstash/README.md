## Logstash

▷ 역할

다양한 입력 소스로부터 입력받는 여러 종류의 데이터를 분석하기 쉬운 형태의 데이터로 정제하여 수집하는 프로그램

실시간 파이프라인 기능을 가진 오픈소스 데이터 수집 엔진, 수집된 데이터를 정규화하여 목적지로 전송하는 역할

● logstash.conf

▷ 역할

로그스태시를 기동할 때에 실행할 데이터 파이프라인에 대한 설정을 미리 작성하는 파일


![logstash conf](https://user-images.githubusercontent.com/97823665/161202109-ea99b11c-bec5-4281-8fe2-f8841590c288.PNG)

※ kafka에서 값을 받아와서 elasticsearch로 전달하는 과정을 작성한 파일이고 따로 filter는 없음

