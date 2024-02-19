## plotly 활용

---

- Plotly의 graph_objects 패키지
    - graph_objects 패키지를 이용하면 섬세하게 그래프를 그릴 수 있음
    - `Figure`: 객체 생성
    - `add_traces`: 그래프 생성
    - `update_layout`: 레이아웃 설정

### graph_objects

- graph_objects는 Plotly의 인기 있는 데이터 시각화 모듈로, 3D 형태의 그래프를 포함한 다양한 그래프를 그릴 수 있음
- go라는 별칭 이용하여 호출

### go 그리는 방법

- `fig=go.Figure()`: Figure 객체 생성
- `fig.add_traces(그래프)`: add_traces로 원하는 유형의 그래프 추가 (go의 그래프 유형 설정)
- `fig.update_layout(옵션)`: 레이아웃 설정
    - 대표적인 옵션: title, yaxis_title 등
