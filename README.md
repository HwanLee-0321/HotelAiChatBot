# 지능형 호텔 챗봇

이 프로젝트는 호텔 정보를 기반으로 대화하는 지능형 챗봇입니다. 자연어 처리(NLP) 및 임베딩 기술을 활용하여 호텔 데이터를 효율적으로 처리하고 검색할 수 있도록 설계되었습니다.

## 주요 기능
- 호텔 데이터 로드 및 처리
- 텍스트 임베딩을 통한 의미론적 검색
- 관련 호텔 정보 검색
- 호텔 데이터 기반의 대화형 응답 제공
- 비정형 텍스트 데이터를 구조화된 CSV 형식으로 변환

## 프로젝트 구조
```
chatbot/
│── app.py                  # 메인 애플리케이션 실행 파일
│── data.txt                # 원본 호텔 데이터 파일
│── embeddings.csv          # 사전 처리된 텍스트 임베딩 데이터
│── scraped.csv             # 스크래핑한 호텔 데이터
│── search.py               # 검색 기능 구현 코드
│── text_embedding.py       # 텍스트 임베딩 로직
│── text_to_csv_converter.py # 데이터 변환 유틸리티
```

## 설치 방법
### 1. 저장소 클론
```sh
git clone https://github.com/your-repo/chatbot.git
cd chatbot
```

### 2. 필수 패키지 설치
Python 3.8 이상이 필요합니다. 
```sh
pip install -r requirements.txt
```


## 실행 방법
### 1. 데이터 준비
`data.txt` 파일에 필요한 호텔 정보를 포함하고 있어야 합니다. 만약 비정형 데이터라면 `text_to_csv_converter.py`를 실행하여 CSV 형식으로 변환할 수 있습니다.
```sh
python text_to_csv_converter.py
```
이 과정이 완료되면 `scraped.csv` 파일이 생성되며, 이후 처리에 사용됩니다.

### 2. 임베딩 생성
다음 명령어를 실행하여 호텔 정보에 대한 텍스트 임베딩을 생성하세요:
```sh
python text_embedding.py
```
이 과정이 완료되면 `embeddings.csv` 파일이 생성되며, 호텔 데이터의 벡터 표현이 저장됩니다.

### 3. 챗봇 애플리케이션 실행
```sh
python app.py
```
이 명령어를 실행하면 챗봇이 실행되어 호텔 관련 정보를 대화형으로 검색할 수 있습니다.

### 4. 호텔 정보 검색
특정 호텔 정보를 검색하려면 다음 명령어를 실행하세요:
```sh
python search.py "검색할 문장"
```
`"검색할 문장"` 부분을 원하는 검색어로 변경하여 실행하세요.

## 사용 예시
1. 챗봇 실행: `python app.py`
2. 예제 질문 입력:
   - "파리의 5성급 호텔을 찾아줘."
   - "호텔 XYZ의 편의시설이 뭐야?"
   - "공항 근처에서 이용 가능한 호텔은?"
3. 챗봇이 처리된 데이터 기반으로 적절한 응답을 제공합니다.

## 향후 개선 사항
- 고급 AI 모델을 활용하여 NLP 기능 강화
- 실시간 호텔 예약 API와의 통합
- 웹 인터페이스 개발을 통한 사용자 경험 개선

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.



