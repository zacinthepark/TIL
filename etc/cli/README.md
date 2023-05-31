## CLI?

---

- Command Line Interface
  - 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식
- ↔ GUI (Graphic User Interface)
  - 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식
- CLI / GUI 모두 컴퓨터에 명령을 내리는 것
  - WHY CLI?
  - 컴퓨터의 리소스 절약
  - 할 수 있는게 더 많음
  - 수많은 서버 / 개발 시스템이 CLI를 통한 조작 환경을 제공
- 절대경로? 상대경로?
  - 절대경로
    - C:/Users/ssafy/Desktop
    - 루트 디렉토리부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것
  - 상대경로
    - 현재 작업하고 있는 디렉토리를 기준으로 계산된 상대적 위치를 작성한 것
    - 현재 작업하고 있는 디렉토리가 C:/Users일 때 윈도우 바탕화면으로의 상대 경로는 ssafy/Desktop
    - ./ : 현재 작업하고 있는 폴더
    - ../ : 현재 작업하고 있는 폴더의 부모 폴더
    - start . : 내가 있는 위치에서 window를 열어달라는 것, 이 역시도 상대경로
  - 절대경로 상대경로 설정을 잘못하여 에러가 나는 경우도 있다
- ~: 현재 작업 중인 위치 중 자주 접근하는 곳! 홈 디렉토리 부분 C: / Users / username
  ![CLI_1](https://user-images.githubusercontent.com/86648892/181915858-4843a73f-843a-4a1f-b1f6-7989c5be5227.png)
  - 바탕화면도 폴더이다
  - desktop.ini 같은 것은 숨겨져 있는 것
    ![CLI_2](https://user-images.githubusercontent.com/86648892/181915871-bd5912ab-6db4-465c-8cb2-6555d554bdaa.png)
  - CLI의 근본은 Linux / Unix에서 나옴
    - mac OS는 이 명령어를 그대로 차용
      - OS 자체가 터미널 친화적
    - window는 명령어 체계가 다름
      - PowerShell은 이러한 명령어 체계를 사용할 수 있도록 패치하여 만든 것

## CLI 명령어

---

- touch: 파일을 생성하는 명령어
- mkdir: 새 폴더를 생성하는 명령어
- ls: 현재 작업 중인 디렉토리의 폴더 / 파일 목록을 보여주는 명령어
- cd: change directory / 현재 작업 중인 디렉토리를 변경하는 명령어
  - cd 경로이름 치다가 tab 누르면 ls에서 검색한 목록 중 가장 근접한 것으로 자동완성
  - cd .. 은 하나 상위 폴더로 이동
- start / open: 폴더 / 파일을 여는 명령어 / window는 start, mac은 open
  - 폴더 path가 너무 길 경우 GUI로 바로 짠 열어줄 수 있음
  - start . : 현재 위치를 열어줌
  - start : CLI 환경 열어줌
- rm: 파일을 삭제하는 명령어 / -r 옵션을 주면 폴더 삭제 가능
  - rm 파일명 일부 + tab 2번 치면 해당 명칭이 포함된 것들 보여줌 → 이 중 골라서 삭제
  - -r 옵션의 의미는 recursive
- clear: 화면 지우기
