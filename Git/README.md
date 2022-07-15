# Git

## STARTUP

- Git이란?
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

        

## GIT?

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

## Working Directory / Staging Area / Repository

- Working Directory: Modified
    - git add (Working Directory → Staging Area
- Staging Area: Staged
    - git commit (Staging Area → Repository)
- Repository: Committed
    - Reminder: 커밋은 변경사항을 기록한 것이다!

## Git 명령어

- git status
    - 현재 git 상태 알려줌
- git add
    - untracked → staged
    - git add .
        - 모든 파일 staging area로 옮김

- git commit -m “blahblah”
    - blahblah라는 이름의 커밋 메세지를 남김
- git log
    - 커밋 기록 확인 가능
- git diff ab12 cd34
    - ab12, cd34는 git log에서 확인한 커밋값 앞 4자리
    - ab12에 비해서 cd34가 어떻게 변했는지 알려줌

## Remote Repository

- git remote add origin {remote_repo}
    - origin: remote_repo의 별명
    - remote_repo: remote repo의 주소
    - 하나의 로컬저장소가 여러개의 remote repo를 바라볼 수 있긴함 but 잘안씀
- git push origin master
    - local의 commit을 remote으로 올리는 것을 push라 함
    - 최초 push의 경우 권한 인증 필요
- git push —set-upstream origin master
    - 이후 git push만 누르면 master로 푸쉬됨
    - git push -u origin master
- git clone {remote_repo}
    - 최초의 커밋을 깃헙이 찍은 상태로 만들어줌
    - cd desktop
    - git clone {remote_repo}
    - start . → 현재 위치 폴더 열어줌
- git pull
    - remote repo가 더 최신인 경우
    - conflict이 발생할 경우 <<<>>> 부분을 알맞게 수정