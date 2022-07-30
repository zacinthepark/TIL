# Git

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

- 위와 같이 .gitignore에 *.txt라 선언하면 ‘확장자가 .txt인 파일들은 모두 깃 관리를 하지 않을거야’라는 뜻
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