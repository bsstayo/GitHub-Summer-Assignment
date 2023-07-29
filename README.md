# Git-Summer-Assignment Week 2
**가사 출력 shell script 만들기**

## 설명

### 자동으로 SuperShy 가사를 생성해드립니다!

- main 브랜치 protection 적용
- git lfs를 이용하여 jpg파일은 lfs에 추가
- tools폴더의 sh 파일이 자동으로 가사를 생성
- 가사 생성과 동시에 가사 한줄마다 자동으로 커밋
- merge confilct 발생시 해결
- tag & release 적용

## 사용방법

```bash
    git clone https://github.com/bsstayo/GitHub-Summer-Assignment.git
```
```bash
   ./tools/pre-generate-lyric.sh
   ./tools/post-generate-lyric.sh 
```


## Contributors

- @bsstayo
- @jcy0308

# Git-Summer-Assigment Week 1 
**복권 번호 조회기**

![main_image](https://play-lh.googleusercontent.com/eUVpXzvy-5cGRnp025XcAnXN7HS2QFftJBcDW7EdAoH4OPD50sq2LaI0bVffDFyduQ)

## 설명

- 궁금하신 회차의 로또 당첨번호를 알려드립니다!

### 사용 방법

```bash
    git clone https://github.com/bsstayo/GitHub-Summer-Assignment.git
```
```bash
    cd GitHub-Summer-Assignment
    cd test
```
```bash
    ./main.py
```

## Contributors
 - 김도훈 @bsstayo
 - 정찬영 @jcy0308

## Link

동행 복권에 대해 더 자세히 알고 싶으시다면 아래의 링크를 참고해주세요!

- [동행 복권 홈페이지](https://dhlottery.co.kr/common.do?method=main)
- [로또 6/45 소개 페이지](https://dhlottery.co.kr/gameInfo.do?method=gameMethod&wiselog=H_B_1_1)

사용된 Requests library에 대해 더 자세히 알고 싶으시다면 아래의 링크를 참고해주세요!

- [Requests: HTTP for Humans](https://requests.readthedocs.io/en/latest/)
