# Jupyter Notebook
## 설치

---

- pip install notebook

![jp_1](https://user-images.githubusercontent.com/86648892/181916735-d01bb42d-b747-4e52-b93d-7ab3f4158e6e.png)

- 성공적으로 설치했다는 메세지를 확인 (경고 메세지가 있다면 무시)

![jp_2](https://user-images.githubusercontent.com/86648892/181916731-f5c45b1f-2070-4ea1-95c8-a1f1bc882f82.png)

---

## 실행

- 주의: 주피터 노트북이 실행 중인 git bash를 종료하지 않도록 주의
- jupyter notebook (실행 명령어)

<img width="716" alt="jp_3" src="https://user-images.githubusercontent.com/86648892/181916732-639a9774-2ca3-4c54-b40f-5b8819c21083.png">

- 실행 화면

<img width="1000" alt="jp_4" src="https://user-images.githubusercontent.com/86648892/181916730-db22643a-ba6f-4170-aa58-a7171d250123.png">

---

## 종료

1. jupyter 화면에서 종료하는 경우
    - 우측상단 Quit 클릭

<img width="1000" alt="jp_5" src="https://user-images.githubusercontent.com/86648892/181916729-982efc32-5d40-4e6d-8be1-36771baabaef.png">

1. 터미널에서 종료하는 경우
    - 아래 화면(jupyter 서버가 켜진 상태)에서 ctrl + c 누르기 (2~3번 정도 연속 입력)
    - 되도록 위 방법으로 진행하는 것을 권장

<img width="575" alt="jp_6" src="https://user-images.githubusercontent.com/86648892/181916727-1883ccd5-1129-416a-8631-9a074761546e.png">

---

## 확장 프로그램 설치

### 설치

1. nbextensions
    - pip install jupyter_contrib_nbextensions

![jp_7](https://user-images.githubusercontent.com/86648892/181916726-6ba668b4-2afd-4670-8cd6-29b95abd0737.png)

![jp_8](https://user-images.githubusercontent.com/86648892/181916725-a9c64f1b-5fe3-49dd-8e6f-90ae6db7de82.png)

1. css, js files
    - jupyter contrib nbextension install —user

![jp_9](https://user-images.githubusercontent.com/86648892/181916724-41e04439-b1e8-425a-8451-006b03a182ab.png)

### 설치완료 확인

![jp_10](https://user-images.githubusercontent.com/86648892/181916720-5fb853af-c9e8-411b-9eea-a11c8c2f4391.png)

### 확장프로그램 활성화

- 확장프로그램 명: Table Of Contents
    - 노트북 메인 페이지 → NBextensions 선택
    - disable configuration 체크박스 해제
    - table 검색 → Table Of Contents 선택
    - 확장프로그램 사용하기

---

## 기본 사용 가이드

### Cell Mode

- 파란색 == Command Mode
    - 셀에 입력할 수 없으며 특정 명령어를 통해 수행하는 상태
- 초록색 == Edit Mode
    - 셀에 데이터를 입력하는 상태

### Cheat Sheet
- 단축키 목록 출력
    - `H`
- 상단 셀 생성
    - `A`
- 하단 셀 생성
    - `B`
- Edit Mode로 전환
    - `클릭` or `enter`
- Command Mode로 전환
    - `esc`
- 셀 삭제
    - `가위 아이콘` or `X`
- 현재 셀 실행
    - `ctrl` + `enter`
- 실행 + 다음 셀 선택 (없다면 생성)
    - `shift` + `enter`
- 실행 + 다음 셀 생성
    - `alt` + `enter`'
- 마크다운 셀로 변경
    - `M`
- 코드 셀로 변경
    - `Y`
- 저장
    - `ctrl` + `s` or `S`
- 셀 삭제
    - `D` + `D`
- 셀 삭제 되돌리기
    - `Z`
- 삭제 취소
    - Edit → Undo Delete Cells or Z
- `In[3]`
    - In안의 숫자 == 셀의 실행 순서(카운트)
- 재시작 및 초기화(쥬피터 노트북에 문제가 생긴다면 대부분 이 형식으로 해결됨)
    - Kernel → Restart and Clear All Output

---

## Alias 등록

### `jupyter notebook` 명령어를 `jp`로 변경하기 (mac OS는 ~/.bashrc가 아닌 ~/.zshrc에서 진행)

- 순서대로 실행

![jp_11](https://user-images.githubusercontent.com/86648892/181916715-4cf6a4bd-6e4e-4212-ba66-707468316638.png)


<img width="297" alt="jp_12" src="https://user-images.githubusercontent.com/86648892/181916740-b9284678-0d6f-40ac-9946-a417d5db4417.png">

<img width="483" alt="jp_13" src="https://user-images.githubusercontent.com/86648892/181916739-b8117a6a-06ca-48a2-a2c5-a13a595f42ba.png">


- notebook 실행 확인

<img width="483" alt="jp_14" src="https://user-images.githubusercontent.com/86648892/181916738-dae4fca4-e202-4d8b-9827-939eb3c913c4.png">

---

## 설치 이슈

- 노트북 실행 시 `jupyter command not found` 가 출력되는 경우
    - python package 전체 삭제 후 재설치
        - pip freeze | xargs pip uninstall -y
        - pip install notebook
    - 그 외 아나콘다 등 제대로 삭제되지 않는 다른 패키지 및 라이브러리의 영향일 경우 파이썬 재설치 권장
---