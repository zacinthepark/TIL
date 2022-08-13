# CHEAT SHEET

## WINDOW

- window + 방향키
    - 화면 분할
- window + shift + S
    - 부분 캡쳐

---

## MARKDOWN

- tab
    - 들여쓰기
- shift + tab
    - 내어쓰기

---

## CLI (GIT BASH)

- 위아래 화살표 누르기
    - 이전에 내렸던 명령 히스토리들이 뜸
- code .
    - 현재 위치에서 vscode 열기
- python del.py
    - del.py 파일 실행
    - python은 ~~~~pyhton.exe에 대한 환경변수
- CLI에서 파일 수정
    - vi 파일명
    - i → 수정 → esc → :wq

---

## VSCODE

- 새로운 파일 생성
    - 왼쪽 위 아이콘 클릭
    - ctrl + n → ctrl + s
- 전체선택
    - ctrl + a
- 주석처리
    - ctrl + /
- 전체 주석처리
    - ctrl + a → ctrl + /
- 커서를 위아래 여러 줄로 확장
    - alt + ctrl + 위아래 화살표
- 줄 바꿈
    - alt + 위아래 화살표
- 줄 복사
    - alt + shift + 위아래 화살표
- 특정 단어 replace
    - ctrl + d
- 파일 settings
    - ctrl + ,
- 전체 settings
    - ctrl + shift + p
- 터미널 열기
    - ctrl + shift + `
- 시작화면
    - ctrl + k → f

---

## HTML / CSS

- [Emmet Documentation](https://docs.emmet.io/cheat-sheet/)
- ‘!’ + tab
    - html document 구조 생성
- tag’*’숫자
    - 숫자만큼 태그 생성
- tag1‘>’tag2
    - tag1 아래 하위 tag2 생성
- ctrl + ‘/’
    - 주석 처리
- shift + 스크롤
    - 옆으로 스크롤

---

## PyCharm

### 디버거 실행
- `shift + F9`

### Stepping Tools
- 디버깅을 수행할 때 유용한 다양한 도구

![aps_31](https://user-images.githubusercontent.com/86648892/184479545-17d7412e-a520-45d9-8c67-9998c689dfbd.png)

|번호   |도구의 기능   |단축키   |설명   |
|---|---|---|---|
|1   |Show Execution Point   |`Alt + F10`   |현재 실행 지점을 가리킴   |
|2  |Step Over   |`F8`   |현재 실행 지점이 있는 경우 해당 함수(메서드) 또는 파일의 다음 줄까지 이동<br>함수를 만나면 함수 안으로 들어가지 않고 함수의 실행 결과 뒷줄로 바로 이동   |
|3   |Step Into   |`F7`   |디버거가 순차적으로 실행되다가 함수(메서드)를 만나면 해당 함수 내부로 들어감   |
|4   |Step Into My Code   |`Alt + Shift + F7`   |라이브러리 소스 코드가 아닌 내가 작성한 코드의 라인만 디버거를 실행하고 싶은 경우   |
|5   |Force Step Into   |`Alt + Shift + F7`   |   |
|6   |Step Out   |`Shift + F8`   |현재 함수(메서드) 바로 뒤에 실행되는 줄로 이동<br>함수 안으로 들어갔는데 해당 밖으로 밖으로 나오고 싶은 경우 사용   |
|7   |Run to Cursor   |`Alt + F9`   |현재 커서가 위치한 줄로 바로 이동<br>단, 중간에 다른 Breakpoint가 있는 경우 해당 위치에서 멈추게 됨   |
|8   |Evaluate Expression   |`Alt + F8`   |   |

### 재실행 및 종료

- 디버거 세션의 재실행은 `ctrl + F5`
- 디버거 세션의 종료는 `ctrl + F2`