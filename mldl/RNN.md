### RNN

#### RNN: Process Sequences

- 각 단어가 timesteps
- 시계열은 설정한 timesteps
- `W(hh) * h(t-1) + W(xh) * X(t) => (D X D) X (D X 1) + (D X m) X (m X 1) = (D X 1)`
- `W(hy) * h(t) => (m X D) X (D X 1)`
    - 원하는 출력값으로 형태로 변경

#### RNN: Applications

- 구조를 잘못 적용하면 성능이 떨어지므로 구조를 잘 잡는 것이 중요하다
- one to one
- one to many
- many to one
- many to many
