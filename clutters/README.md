# Filled with Clutters💡

- [Command Line Interface](#cli)
- [Various Cheat Sheets](#cheat-sheets)
- [Markdown](#markdown-1)
- [Git](#git)

---

# CLI

## CLI?

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

---

## CLI 명령어

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

---

# Cheat Sheets

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
- tag’\*’숫자
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

| 번호 | 도구의 기능          | 단축키             | 설명                                                                                                                                                   |
| ---- | -------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1    | Show Execution Point | `Alt + F10`        | 현재 실행 지점을 가리킴                                                                                                                                |
| 2    | Step Over            | `F8`               | 현재 실행 지점이 있는 경우 해당 함수(메서드) 또는 파일의 다음 줄까지 이동<br>함수를 만나면 함수 안으로 들어가지 않고 함수의 실행 결과 뒷줄로 바로 이동 |
| 3    | Step Into            | `F7`               | 디버거가 순차적으로 실행되다가 함수(메서드)를 만나면 해당 함수 내부로 들어감                                                                           |
| 4    | Step Into My Code    | `Alt + Shift + F7` | 라이브러리 소스 코드가 아닌 내가 작성한 코드의 라인만 디버거를 실행하고 싶은 경우                                                                      |
| 5    | Force Step Into      | `Alt + Shift + F7` |                                                                                                                                                        |
| 6    | Step Out             | `Shift + F8`       | 현재 함수(메서드) 바로 뒤에 실행되는 줄로 이동<br>함수 안으로 들어갔는데 해당 밖으로 밖으로 나오고 싶은 경우 사용                                      |
| 7    | Run to Cursor        | `Alt + F9`         | 현재 커서가 위치한 줄로 바로 이동<br>단, 중간에 다른 Breakpoint가 있는 경우 해당 위치에서 멈추게 됨                                                    |
| 8    | Evaluate Expression  | `Alt + F8`         |                                                                                                                                                        |

### 재실행 및 종료

- 디버거 세션의 재실행은 `ctrl + F5`
- 디버거 세션의 종료는 `ctrl + F2`

---

# Markdown

## Markdown

- 텍스트 기반의 가벼운 마크업(markup) 언어
- 마크업(markup): 태그(tag)를 이용해서 문서의 구조를 나타내는 것
- 문서의 구조와 내용을 같이 쉽고 빠르게 적고자 탄생 // 시초는 신문기사 등을 빠르게 적기 위해 탄생
- jupyter, notion, typora
  - Typora
    - [Markdown Cheat-sheet](https://www.markdownguide.org/cheat-sheet)
    - Heading
      - '#' + spacebar
      - 문서의 제목이나 소제목으로 사용
      - #의 개수에 따라 제목의 수준을 구별 (1~6)
      - 문서 구조의 기본
      - 단순히 글자 크기를 사용하지 마라
    - Ordered List
      - '1. 2. 3.' + spacebar
    - Unorderd List
      - '\*' + spacebar
    - Code Block
      - ` 키를 3번 눌러주고 엔터
    - Inline Code Block
      - ` 키로 감싸주면 됨
    - Link
      - '[string]' + (url)
      - string 부분에 보여지는 이름, url 부분에 링크 주소
    - Image
      - '![string]' + (img_url)
      - '![string]' + (filepath\image.jpg)
    - Text Emphasis
      - bold: 글씨 양 옆에 '\*' 2개씩
      - italic: 글씨 양 옆에 '\*' 1개씩
      - strikethrough: 글씨 양 옆에 '~' 2개씩
    - Horizontal Line
      - -(hyphen) 3개 + enter
      - hyphen 대신 \_ or \* 역시 가능

## Why Markdown?

- Github 문서의 시작과 끝이다!
- README.md
  - 오픈소스의 공식 문서 작성
  - 매일 학습한 내용 정리
  - 마크다운을 이용한 블로그 운영

---

## TIL (Today I Learned)

- 매일 내가 배운 것을 마크다운으로 정리해서 문서화하는 것
- 신입 개발자에게 필요한 소양
- Github 관리에 있어 첫걸음 및 장기 프로젝트
- SSAFY에서 제공하는 자료나 과제는 깃헙에 올리지 말 것

---

# GIT

## GIT 이란?

- 분산 버전 관리 프로그램
- 분산 버전 관리 프로그램
- 버전 관리 프로그램(VCS): 코드의 히스토리, 개발 과정 파악 가능
- 분산: Central VCS와 달리 여러 서버들에 분산하여 관리
  - Server Computer(클라우드) + 물리적 Computer A, B, C…
  - Github은 Git 기반 저장소를 제공해주는 서비스 / 진짜 버전 관리해주는 프로그램이 Git
  - Github, Gitlab, Bitbucket 등 다양한 저장소 제공 서비스
    - Github - MS / Gitlab - 저장하는 서버 자체를 마음대로 구축할 수 있음(유출 우려 저하)
  - Git ≠ Github
- Github을 사용하면 뭐가 좋을까?
  - Git을 활용한 버전 관리
  - 포트폴리오
    - 잔디 관리
    - 1일 1커밋
    - Junior Developer에게 보는 소양 1)성실함 2)커뮤니케이션 능력
  - Social Coding

---

## GIT 개념

### Repository

- 특정 디렉토리를 버전 관리하는 저장소
- git init 명령어로 로컬 저장소를 생성
- README.md 생성

### Commit

- ‘특정 버전으로 남긴다’ = ‘커밋(commit)한다’
- 커밋은 3가지 영역을 바탕으로 동작
  - Working Directory
    - 내가 작업하고 있는 실제 디렉토리
  - Staging Area
    - 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
  - Repository
    - 커밋들이 저장되는 곳

### Working Directory / Staging Area / Repository

- Working Directory: Modified
  - git add (Working Directory → Staging Area
- Staging Area: Staged
  - git commit (Staging Area → Repository)
- Repository: Committed
  - Reminder: 커밋은 변경사항을 기록한 것이다!

### Remote Repository 생성 및 Collaborators 추가

- remote repository 생성
- settings → collaborators → add people
- git clone {url}
- git push
- git pull

### Git 사용자 관리

- 컴퓨터 내에서 기본적으로 사용할 계정은 global로 설정
  - git config —global user.name
  - git config —global user.email
- 그 중 특정 폴더나 파일은 다른 계정으로 사용하고 싶다면 local로 따로 설정
  - git config —local user.name
  - git config —local user.email

## .gitignore

- 여기에 올라가있는 파일들은 git이 더이상 버전관리하지 않겠다는 것
- repo를 최초로 생성할 때 아무것도 안 적더라도 꼭 만들자

![git_1](https://user-images.githubusercontent.com/86648892/181916219-743d32ea-a42e-4f0a-a305-59e07fd86a30.png)

- vscode에서는 GUI 형식으로 커밋을 할 수 있다
  - 커밋 및 밀기는 commit과 push를 동시에 진행
  - CLI와 달리 커밋 1개에 여러 줄을 작성할 수 있다
    - 이 때 형식은
      - 첫 줄은 commit title
      - 한 줄 공백
      - commit 내용

![git_2](https://user-images.githubusercontent.com/86648892/181916240-b46696d8-3a05-45f5-a2d5-23c34e7ec48b.png)

- 가령 password.txt와 같이 github에 올라갔을 시 유출 위험이 있거나 프라이빗한 파일들의 경우 올리지 않고 싶을 수 있다
  - 그렇다면 그 파일만 스테이징을 하지 않으면 되지 않는가?
    - 맞지만, 너무 귀찮다
- 이럴 때 필요한 것이 .gitignore!!!
  - .gitignore에 등록된 파일은 tracking되지 않는다
  - 만약에 폴더를 무시하고 싶다면?
    - 가령 Ignore라는 이름의 폴더가 있다고 하자
      - .gitignore 폴더에서
        - ignore/
        - ignore/* (*은 ignore 폴더 이하의 모든 파일들이라는 뜻)
        - 둘 중에 하나를 작성해주면 해당 폴더 역시 tracking하지 않는다

![git_3](https://user-images.githubusercontent.com/86648892/181916230-c9190363-a763-4bab-8c33-1060f88778b2.png)

- 위와 같이 .gitignore 파일에 작성된 것들은 github에서 찾아볼 수 없다

![git_4](https://user-images.githubusercontent.com/86648892/181916232-a7d86384-c570-401a-b9d0-a2dfc1a62616.png)

- 위와 같이 .gitignore에 \*.txt라 선언하면 ‘확장자가 .txt인 파일들은 모두 깃 관리를 하지 않을거야’라는 뜻
- 그런데 위 예시에서 ignore 폴더처럼 안에 파일들이 모두 .gitignore에서 무시하겠다고 선언한 파일들인 경우 github은 알아서 ‘해당 폴더보니까 어차피 올릴 파일 없던데 폴더도 무시할게?’라고 하며 폴더도 올리지 않는다
  - 만약 ‘디렉토리 구조는 그대로 유지하고 싶다!’라면 해당 디렉토리에 .gitkeep 생성

![git_5](https://user-images.githubusercontent.com/86648892/181916234-1c237647-98a4-4a7c-9ba5-25604a812495.png)

![git_6](https://user-images.githubusercontent.com/86648892/181916236-f04fa5af-b0c8-43ba-8565-9853667fc355.png)

- .gitkeep 파일을 통해 디렉토리 구조가 잘 유지되어 있음을 확인할 수 있다

## gitignore.io

- 프로그램을 사용하다보면 다양한 부산물들이 생긴다
  - window, python, mac, django…등등
- 위와 같이 공유하지 않을 파일을 지정하는 경우 외에 이러한 부산물들 역시 tracking하지 않고싶을 때 우리는 gitignore.io에 공유된 .gitignore 파일을 사용할 수 있다

![git_7](https://user-images.githubusercontent.com/86648892/181916237-db26761c-07ce-49f8-a0b7-4932788b48f7.png)

![git_8](https://user-images.githubusercontent.com/86648892/181916239-fcfa1406-9ecf-4d0f-b6a5-bb02d9303e66.png)

- 이처럼 검색하고, 파일 전체선택(ctrl + a), 복사(ctrl + c), .gitignore에 붙여넣기(ctrl + v), 그리고 저장(ctrl + s)하면 끝이다
- 따로 지정해서 무시하고 싶은 파일의 경우 복사한 gitignore 파일 위에 적어놓는다

---

## Git 명령어

- git status
  - 현재 git 상태 알려줌
- git add
  - untracked → staged
  - git add .
    - 모든 파일 staging area로 옮김
      ![git_9](https://user-images.githubusercontent.com/86648892/181916331-683aaf4a-20c4-46a9-93fd-3ddadc8ce3d3.png)
  - 여러 줄의 commit message를 남길 수 있는 장점
  - 그러나 굳이?
  - :q로 나감
- git commit -m “message”
  - message라는 이름의 커밋 메세지를 남김
- git log
  - 커밋 기록 확인 가능
- git diff ab12 cd34
  - ab12, cd34는 git log에서 확인한 커밋값 앞 4자리
  - ab12에 비해서 cd34가 어떻게 변했는지 알려줌
- git remote add origin {remote_repo}
  - origin: remote_repo의 별명
  - remote_repo: remote repo의 주소
  - 하나의 로컬저장소가 여러개의 remote repo를 바라볼 수 있긴함 but 잘안씀
- git push origin master
  - local의 commit을 remote으로 올리는 것을 push라 함
    ![git_10](https://user-images.githubusercontent.com/86648892/181916328-96dd4a37-8132-4ab7-a340-a84d85cfd72a.png)
  - 최초 push의 경우 권한 인증 필요
- git push —set-upstream origin master
  - 이후 git push만 누르면 master로 푸쉬됨
  - git push -u origin master
- git clone {remote_repo}
  - 최초의 커밋을 깃헙이 찍은 상태로 만들어줌
  - cd desktop
  - git clone https://github.com/zacinthepark/clone_test.git
  - start . → 현재 위치 폴더 열어줌
- git pull

---

# Git Undoing

- Working Direcory 작업 단계
  - Working Directory에서 수정한 파일 내용을 이전 커밋 상태로 되돌리기
  - `git restore`
- Staging Area 작업 단계
  - Staging Area에 반영된 파일을 Working Directory로 되돌리기
  - `git rm --cached`
  - `git restore --staged`
- Repo 작업 단계
  - 커밋을 완료한 파일을 Staging Area로 되돌리기
  - `git commit --amend`

---

## Working Directory 작업 단계 되돌리기

### `git restore`

- Working Directory에서 수정한 파일을(modified) 수정 전(직전 커밋)으로 되돌리기
- 이미 버전 관리가 되고 있는 파일만 되돌리기 가능
- git restore를 통해 되돌리면, 해당 내용을 복원할 수 없으니 주의할 것
- `git restore {파일 이름}`
  - [참고] git 2.23.0 버전 이전에는 `git checkout -- {파일 이름}`

## Staging Area 작업 단계 되돌리기

- Staging Area에 반영된 파일을 Working Directory로 되돌리기
- root-commit 여부에 따라 2가지 명령어로 나뉨
  - root-commit이 없는 경우
    - `git rm --cached`
  - root-commit이 있는 겨우
    - `git restore --staged`

### `git rm --cached`

- “to unstage and remove paths only from the staging area”
- root-commit이 없는 경우 사용
  - Git 저장소에 커밋이 찍힌 적이 없는 경우
- `git rm --cached {파일 이름}`

### `git restore --staged`

- “the contents are restroed form HEAD”
- root-commit이 있는 경우 사용
  - Git 저장소에 1개 이상의 커밋이 있는 경우
- `git restore --staged {파일 이름}`
  - [참고] git 2.2.3.0 버전 이전에는 `git reset HEAD {파일 이름}`

## Repository 작업 단계 되돌리기

### `git commit --amend`

- 커밋을 완료한 파일을 Staging Area로 되돌리기
- 상황 별로 2가지 기능으로 나뉨
  - Staging Area에 새로 올라온 내용이 없다면, 직전 커밋의 메시지만 수정
  - Staging Area에 새로 올라온 내용이 있다면, 직전 커밋을 덮어쓰기
- amend(수정하다)
  - 즉, 이전 커밋을 수정해서 새 커밋으로 남김
  - 커밋 내용을 수정하거나 수정 사항을 새로 커밋에 추가하고 싶을 때 사용
  - 수정 사항을 반영하기 위해 새로운 커밋을 생성하지 않아도 됨

### [참고] vim 편집기 명령어

- `i`
  - 삽입 모드
- `esc`
  - 삽입 모드 종료
- `wq`
  - wrtie and quit
    - 저장하고 편집기 종료
- `vi {파일 이름}`
  - 해당 파일을 vim 편집기로 편집

---

# Git reset & revert

## Git reset

- 프로젝트를 특정 커밋(버전) 상태로 되돌림
- 특정 커밋으로 되돌아갔을 때, 해당 커밋 이후로 쌓았던 커밋들은 전부 사라짐
- `git reset --[옵션] {커밋 ID}`
  - 옵션은 soft, mixed, hard 중 하나를 작성
    - 기본 옵션은 mixed
  - 커밋 ID는 되돌아가고 싶은 시점의 커밋 ID를 작성
    - 앞 4자리 정도만 적어줘도 충분히 구분 가능

### git reset의 3가지 옵션

- `--soft`
  - 해당 커밋으로 되돌아가고
  - 되돌아간 커밋 이후의 파일들은 Staging Area로 돌려놓음
- `--mixed`
  - 해당 커밋으로 되돌아가고
  - 되돌아간 커밋 이후의 파일들은 Working Directory로 돌려놓음
- `--hard`
  - 해당 커밋으로 되돌아가고
  - 되돌아간 커밋 이후의 파일들은 모두 Working Directory에서 삭제
    - 사용 시 주의할 것!
  - 기존의 Untracked 파일은 사라지지 않고 Untracked로 남아있음

### [참고] git reflog

- git reset의 hard 옵션은 Working Directory 내용까지 삭제하므로 위험할 수 있음
- `git reflog` 명령어를 이용하면 reset하기 전의 과거 커밋 내역을 모두 조회 가능
- 이후 해당 커밋으로 reset하면 hard 옵션으로 삭제된 파일도 복구 가능

## Git revert

- 과거를 없었던 일로 만드는 행위로, 이전 커밋을 취소한다는 새로운 커밋을 생성함
- `git revert {커밋 ID}`
  - 커밋 ID는 취소하고싶은 커밋 ID를 작성
- 커밋 기록은 그대로 남은 채로
  - 해당 커밋의 행위는 취소하고
    - 취소했다는 사실을 새로운 커밋으로 남김

---

# Git Branch

- “Branch는 Commit을 가리키는 Pointer임”

### 장점

- 브랜치는 독립 공간을 형성하기 때문에 원본(master)에 대해 안전함
- 하나의 작업은 하나의 브랜치로 나누어 진행되므로 체계적인 개발이 가능함
- Git은 브랜치를 만드는 속도가 굉장히 빠르고, 적은 용량을 소모함

## git branch

- 브랜치의 조회, 생성, 삭제와 관련된 git 명령어
- 조회
  - `git branch`
    - 로컬 저장소의 브랜치 목록 확인
  - `git branch -r`
    - 원격 저장소의 브랜치 목록 확인
- 생성
  - `git branch {브랜치 이름}`
    - 새로운 브랜치 생성
      - 이름은 보통 `git branch feature/signup` 과 같이 작성
  - `git branch {브랜치 이름} {커밋 ID}`
    - 특정 커밋 기준으로 브랜치 생성
- 삭제
  - `git branch -d {브랜치 이름}`
    - 병합된 브랜치만 삭제 가능
  - `git branch -D {브랜치 이름}`
    - 강제 삭제

## git switch

- 현재 브랜치에서 다른 브랜치로 이동하는 명령어
- `git switch {브랜치 이름}`
  - 다른 브랜치로 이동
- `git switch -c {브랜치 이름}`
  - 브랜치를 새로 생성 및 이동
- `git switch -c {브랜치 이름} {커밋 ID}`
  - 특정 커밋 기준으로 브랜치 생성 및 이동
- switch하기 전에, 해당 브랜치의 변경 사항을 반드시 커밋해야함을 주의할 것!
  - 다른 브랜치에서 파일을 만들고 커밋하지 않은 상태에서 switch를 하면 브랜치를 이동했음에도 불구하고 해당 파일이 그대로 남아있게됨

## [참고] HEAD

- “This is a pointer to the local branch you’re currently on”
- HEAD는 현재 브랜치를 가리키고, 각 브랜치는 자신의 최신 커밋을 가리키므로 결국 HEAD가 현재 브랜치의 최신 커밋을 가리킨다고 할 수 있음
- `git log` 혹은 `cat .git/HEAD`를 통해서 현재 HEAD가 어떤 브랜치를 가리키는지 알 수 있음

## git merge

- 분기된 브랜치들을 하나로 합치는 명령어
- master 브랜치가 사용이므로, 주로 master 브랜치에 병합
- `git merge {합칠 브랜치 이름}`
  - 병합하기 전에 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야함
  - 병합에는 세 종류가 존재
    1. Fast-Forward
       - 해당 브랜치 작업 사항까지 master의 포인터를 당겨오기
       - 마치 빨리감기처럼 브랜치가 가리키는 커밋을 앞으로 이동시키는 방법
    2. 3-way
       - 브랜치와 master의 공통된 머지 커밋 생성
       - 각 브랜치의 커밋 두 개와 공통 조상 하나를 사용하여 병합하는 방법
    3. Merge Conflict
       - 충돌이 발생한 부분은 작성자가 직접 해결

---

# Git workflow

## Git 브랜치 전략

### Git-Flow

- [우아한 형제들 Git-Flow](https://techblog.woowahan.com/2553/)

![git_11](https://user-images.githubusercontent.com/86648892/198499446-c6f5694d-3f7b-460f-bfc1-523fc9ba1c0e.png)

### Github-Flow

![git_12](https://user-images.githubusercontent.com/86648892/198499450-1dd0f5d5-86e0-4aaf-a137-1a5ea9d22556.png)

### Gitlab-Flow

![git_13](https://user-images.githubusercontent.com/86648892/198499449-b0171796-50f9-4171-8745-51ac9d60745e.png)

### 정리

- 어떤 브랜치 전략을 사용할 것인지는 팀에서 정하는 문제
- git, github, gitlab 브랜치 전략이 아닌 우리 팀 고유의 브랜치 전략도 가능
- 브랜치를 자주 생성하는 것을 강력히 권장하며, main(master) 브랜치 하나로만 작업하는 형태는 지양해야함

---
