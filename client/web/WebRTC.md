## 등장배경

---

### HTTP

<img width="826" alt="rtc1" src="https://github.com/zacinthepark/TIL/assets/86648892/596c9390-885f-48f7-bc77-7facf5c8f8bd">

- 브라우저 서버 간 통신
- HttpRequest and HttpResponse
- 서버가 브라우저의 요청에 응답하고 나면 브라우저-서버 간 통신은 끝남
    - 서버가 브라우저에 무엇인가를 보내는 것은 요청이 있을 때만

### WebSocket

<img width="862" alt="rtc2" src="https://github.com/zacinthepark/TIL/assets/86648892/b6041939-6283-4f18-ad60-075450e072af">

- Request-Response 개념이 아닌 커넥션의 Open-Close 여부
- 양방향 통신 및 Open
    - 브라우저와 서버 둘다 메세지를 보내고 받을 수 있음
    - 통신이 열려있는 동안
        - 서버는 요청을 기다릴 필요가 없음
        - 업데이트가 필요한 경우 서버는 정보를 보낼 수 있음
- 채팅방, 주식거래앱, 게임 등 리얼타임 경험
    - 채팅방에 입장하면 상대방과 연결된 것이 아닌 상대방과 동일한 웹소켓 서버에 연결된 것
- 문제점
    - 메모리 파워
        - 유저가 많을수록 메모리가 더 필요하고, 서버에 드는 비용 상승
    - 속도
        - 서버에 수많은 커넥션이 오고가고 있다면 딜레이가 생길 수 있고, 이는 좋지 않은 UX
    - 서버가 crash하면 서비스에 타격이 있을 수 있음

### WebRTC

<img width="859" alt="rtc3" src="https://github.com/zacinthepark/TIL/assets/86648892/fa95a984-fb75-448e-b87b-6ab08b12a6a5">

- Web Real-Time Communication
- 브라우저끼리 연결이 가능하도록 함
    - Peer to Peer communication
- 단순 텍스트 뿐만 아니라 영상, 오디오 등도 주고받을 수 있음
- 문제점
    - 비디오 채팅방에 1000명이 있다면
        - 나의 컴퓨터는 999개의 비디오, 오디오를 다운받고
        - 나의 비디오, 오디오를 999개의 컴퓨터에 업로드해야함

## WebRTC란?

---

별도의 플러그인 없이 실시간 소통이 가능하도록 만들어주는 기술로, 기존에는 스카이프, 구글 행아웃을 설치해야 했으나 WebRTC를 사용하면 크롬 등의 브라우저에서 바로 실시간 소통을 할 수 있음

### WebRTC 통신 방식

1. P2P (Peer to Peer): 두 단말이 서로 1:1 통신하는 방식

2. MCU, SFU: 대규모 서비스를 구축할 때 사용하는 방식, 중앙 서버를 두어 트래픽 중계하도록 함

### 실시간 소통을 위해 필요한 사항

1. 기기의 스트리밍 오디오, 비디오, 데이터를 가져올 수 있을 것
2. 소통하고자 하는 기기의 IP 주소와 포트 등 네트워크 데이터가 필요
3. 에러 보고, 세션 초기화를 위해 신호 통신을 관리해야함
4. 서로 소통할 수 있는 해상도인지, 코덱은 맞는지 capability 정보 교환
5. 실제 연결을 맺음
6. 이후 스트리밍 오디오, 비디오, 데이터를 주고 받을 수 있어야함

![rtc4](https://github.com/zacinthepark/TIL/assets/86648892/5e1038a1-e94a-464a-920b-1e1fc657e241)

### WebRTC 통신과정

- WebRTC를 사용한 통신은 두 갈래로 설명할 수 있다
    - Signaling을 통해 통신할 peer 간 정보를 교환한다 (네트워크 정보, capability 정보, 세션 수립 등)
    - WebRTC를 사용해 연결을 맺고, peer 기기에서 데이터를 가져와 교환

### WebRTC APIs

- 위의 사항들을 위해 WebRTC는 다음 API를 제공함
    - `getUserMedia`
        - 사용자 단말기의 미디어 장치(마이크와 웹캠)를 액세스할 수 있는 방법을 제공한다. getUserMedia를 통해 미디어 장치를 액세스하게 되면 미디어 스트림 전체를 얻을 수 있으며 이를 PeerConnection에 전달하여 미디어 스트림을 전송하게 된다.
    - `PeerConnection`
        - 가장 중요한 API이면서 Peer 간의 화상과 음성 등을 교환하기 위한 거의 모든 작업을 수행하는 API이다. 기본적인 기능은 Signal Processing, Security, 비디오 encode 및 decode, 네트워크와 관련된 NAT Traversal, Packet send & receive, bandwidth estimation 등이 있다.
    - `DataChannel`
        - Peer 간에 텍스트나 파일을 주고받을 수 있는 메시징 API이다. 설정에 따라 SCTP 또는 RTP로 전송할 수 있다. DataChannel은 WebSocket과 같은 수준의 API를 제공하며 이는 Low Level API라 할 수 있다. 대용량 파일을 주고받기 위해서는 이 API를 활용한 어플리케이션 단의 테크닉이 필요하다.

### Signaling

- WebRTC는 브라우저 간 스트리밍 데이터를 교환하기 위해 `PeerConnection`을 사용한다. Signaling은 그 외 통신 조정 및 메시지를 컨트롤하는 메커니즘이다.
- 즉, 통신을 조율할 때 메시지를 주고 받는 일련의 과정을 의미한다.
- 시그널링의 역할
    1. `Session control messages`: 통신의 초기화, 종료, 그리고 에러 메시지
        - 네트워크 정보 교환, 미디어 정보 교환 외 작업
    2. `네트워크 정보 교환 (Network configuration)`: 외부에서 보는 내 컴퓨터의 IP 주소와 포트 정보
        - `ICE` 프레임워크를 사용해서 서로의 IP와 포트를 찾는 과정
        - `Candidate`에 서로를 추가
            - ICE?
                - Interactive Connectivity Establishment
                - STUN, TURN 서버를 이용해서 획득했던 IP 주소와 프로토콜, 포트의 조합으로 구성된 연결 가능한 네트워크 주소들을 `후보(candidate)`라 부른다. PeerConnection 객체를 생성하면 candidate를 얻을 수 있다.
                - 후보(candidate)들을 수집하면 일반적으로 3개의 주소를 얻게 된다.
                    - 자신의 사설 IP와 포트 넘버
                    - 자신의 공인 IP와 포트 넘버 (STUN, TURN 서버로부터 획득 가능)
                    - TURN 서버의 IP와 포트 넘버 (TURN 서버로부터 획득 가능)
                - 이 모든 과정은 ICE Framework 위에서 이루어진다. ICE는 두 개의 단말이 P2P 연결을 가능하게 하도록 최적의 경로를 찾아주는 프레임워크이다. ICE는 STUN과 TURN을 활용하여 여러 Candidate를 검출하고 이들 중 하나를 선택하여 Peer 간 연결을 수행한다.
    3. `미디어 정보 교환 (Media capabilities)`: 상호 두 단말의 브라우저에서 사용 가능한 코덱, 해상도
        - 미디어 정보 교환은 `offer와 answer` 로직으로 진행
        - 형식은 `SDP (Session Description Protocol)`
            - SDP?
                - SDP는 WebRTC에서 스트리밍 미디어의 해상도나 형식, 코덱 등의 멀티미디어 컨텐츠의 초기 인수를 설명하기 위해 채택한 프로토콜이다. 미디어에 대한 메타 데이터로, 사용할 수 있는 코덱은 무엇들이 있으며, 어떤 프로토콜을 사용하고, 비트레이트는 얼마이며, bandwidth(대역폭)은 얼마이다와 같은 데이터가 텍스트 형태로 명시되어 있다.
                - PeerConnection 객체를 생성하게 되면 해당 객체에서 offer SDP, answer SDP를 얻을 수 있다. 이처럼 `미디어와 관련된 초기 세팅 정보를 기술하는 SDP`는 발행 구독 모델(Pub, Sub)과 유사한 `제안 응답 모델(Offer, Answer)`을 갖고 있다.
- 위 작업은 스트리밍이 시작되기 전에 완료되어야 한다.
- 시그널링을 성공적으로 마치면, 실제 데이터(미디어, 영상, 음성)는 P2P 또는 중계서버를 거쳐서 통신하게 된다.

## 서버의 역할

---

![rtc5](https://github.com/zacinthepark/TIL/assets/86648892/4a727ef8-bc9c-4b7e-ad31-97d5cd93ec9c)

- WebRTC에서 서버가 필요한 경우는 다음과 같다.
    - Signaling 사용자 탐색과 통신
    - 방화벽과 NAT 트래버설
        - `STUN (Session Traversal Utilities for NAT) Server`
    - P2P 통신 중계서버
        - `TURN (Traversal Using Relays around NAT) Server`

### 방화벽과 NAT 트래버설

- 일반적인 컴퓨터에는 방화벽(Firewall), 여러 대의 컴퓨터가 하나의 공인 IP를 공유하는 NAT(Network Address Translation) 등에 의해 공인 IP가 할당되어 있지 않다.
- 그러므로 단순히 공인 IP만을 알아낸다고 해서, 특정 사용자를 가리킬 수 없다.
- 공인 IP 뿐만 아니라 해당 네트워크에 연결된 사설 IP 주소까지 알아내야 특정한 사용자를 지정할 수 있다.
- 일반적으로 라우터가 NAT 역할을 한다. 외부에서 접근하는 “공인 IP와 포트 번호”를 확인하여 현재 네트워크 내의 사설 IP들을 적절히 매핑시켜준다. 따라서 어떤 브라우저 두 개가 서로 직접 통신을 하려면, 각자 현재 연결된 라우터의 “공인 IP와 포트 번호”를 먼저 알아내야 한다.
- 하지만 어떤 라우터들은 특정 주소나 포트와의 연결을 차단하는 방화벽 설정이 되어있을 수도 있다. 이처럼 라우터를 통과해서 연결할 방법을 찾는 과정을 `NAT 트래버설 (NAT Traversal)`이라고 한다.

### STUN

![rtc6](https://github.com/zacinthepark/TIL/assets/86648892/fe452d64-3edc-454e-a13a-744f353e521a)

- NAT 트래버설 작업은 `STUN(Session Traversal Utilities for NAT)` 서버에 의해 이루어진다. STUN 방식은 단말이 자신의 “공인 IP 주소와 포트”를 확인하는 과정에 대한 프로토콜이다. 클라이언트가 STUN 서버에 요청을 보내면 공인 IP 주소와 함께 통신에 대한 필요한 정보들을 보내주는데, 클라이언트는 이를 이용해 다른 기기와 통신한다. 하지만 이러한 경우에도 통신이 되지 않는다면 TURN 서버로 넘기게 된다.

### TURN

![rtc7](https://github.com/zacinthepark/TIL/assets/86648892/1f41fa4a-9ba6-45d8-98fd-243ded274c11)

- STUN 서버를 이용하더라도 항상 자신의 정보를 알아낼 수 있는 것은 아니다. 어떤 라우터들은 방화벽 정책을 달리 할 수도 있고, 이전에 연결된 적이 있는 네트워크만 연결할 수 있게 제한을 걸기도 한다 (`Symmetric NAT`). 이 때문에 STUN 서버를 통해 자기 자신의 주소를 찾아내지 못했을 경우, `TURN(Traversal Using Relay NAT)` 서버를 대안으로 이용하게 된다.

- TURN(Traversal Using Relays around NAT)는 이러한 Symmetric NAT 제약조건을 우회하기 위해 만들어졌다. TURN 서버와 연결을 맺고, 이 서버에서 모든 교환 과정을 중계한다. 모든 기기는 TURN 서버로 패킷을 보내고, 서버가 이를 포워딩한다. 모든 작업을 한 서버에서 처리하는 만큼 오버헤드가 있다.

## WebRTC 구현 방식

---

![rtc8](https://github.com/zacinthepark/TIL/assets/86648892/994026b8-4e22-4073-b7b1-20eed89bdb58)

WebRTC는 기본적으로는 P2P, 두 단말이 서로 1:1 통신을 하게 되어있다. 따라서 대규모 방송 서비스를 구축하거나 컨텐츠 가공이 필요할 경우 중앙 미디어 서버를 구축할 필요성이 생긴다. 이런 목적에 따라 SFU, MCU 아키텍처를 고려해볼 수 있다.

### P2P

중앙 미디어 서버 없이 종단 간 직접 연결하므로, 비용 측면에서 이득이 있다. 다만 peer 수가 증가할수록 개별 기기의 높은 성능을 요구한다. 1:1, 최소한 소규모 미디어 교환에 적합하다.

### MCU (Multipoint Control Unit)

한쪽 Peer에 서버를 두고, 들어오는 트래픽을 서버에서 믹싱해서 다시 내보내는 방식이다. 클라이언트와 네트워크의 부담이 줄어드는 반면, 중앙서버의 컴퓨팅 파워가 많이 요구된다. 참고한 블로그에서는 낡은 기술이고 + 서버 운용 비용이 높아, WebRTC와 같은 실시간성 보장이 우선인 서비스인 경우 장점이 상쇄된다고 언급되어있다.

### SFU (Selective Forwarding Unit)

믹싱하지않고 트래픽을 선별적으로 배분해서 보내주는 방식. 각 peer 연결 할당과 encrypt, decrypt 역할을 서버가 담당한다. 1:N 스트리밍 구조에 적합하다고 한다.
