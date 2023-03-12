# SolvedACRandomDefence

[Solved.ac](https://solved.ac/)사이트를 사용하여 원하는 난이도의 문제를 랜덤한 순서로 뽑아주는 코드

## Usage
#### 1. [Chrome Driver](https://chromedriver.chromium.org/downloads) 다운로드
Chrome 브라우저의 버전을 확인하고 그에 맞는 드라이버를 다운로드 받아 프로젝트 폴더에 넣는다

#### 2. 라이브러리 설치
```
cd [프로젝트 폴더 경로]
pip install -r requirements.txt
```

#### 3. 실행
```
python main.py
Input Users
[참여하는 인원들의 BOJ 핸들을 띄어쓰기로 구분해서 입력]
Input Levels
[문제들의 난이도를 띄어쓰기로 구분해서 입력(중복 가능) (ex) g2 g2 s5)]
Input Min and Max
[문제를 푼 사람의 최소 수와 최대 수를 띄어쓰기로 구분해서 입력]
```

#### 4. etc
- 조건에 해당하는 문제가 없으면, 에러를 발생시키고 종료된다
- 크롬창을 띄우지 않고 실행시킬 수 있는데(기본값), 이 때 콘솔창에 cookie에 대한 에러 문구가 뜰 수 있다. 실행에는 문제가 없다
- main.py 에서 chrome driver의 위치를 하드코딩 할 수 있다
- 지속적인 에러가 발생할 때, main.py 에서 delay를 조정하여 해결할 수 있다
  - 보통 컴퓨터나 네트워크의 속도가 느릴 때 발생
