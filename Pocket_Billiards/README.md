# Virtual Pocket Billiards Algorithm

```python
import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'SEOUL01_PARKJINWOO'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909

# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.
    
    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    # whiteBall_x = balls[0][0]
    # whiteBall_y = balls[0][1]
    
    # targetBall_x, targetBall_y: 목적구의 X, Y좌표를 나타내기 위해 사용한 변수
    # targetBall_x = balls[1][0]
    # targetBall_y = balls[1][1]

    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
    # width = abs(targetBall_x - whiteBall_x)
    # height = abs(targetBall_y - whiteBall_y)
    
    # radian: width와 height를 두 변으로 하는 직각삼각형의 각도를 구한 결과
    #   - 1radian = 180 / PI (도)
    #   - 1도 = PI / 180 (radian)
    # angle: 아크탄젠트로 얻은 각도 radian을 degree로 환산한 결과
    # radian = math.atan(width / height) if height > 0 else 0
    # angle = 180 / math.pi * radian
    
    # 목적구가 흰 공과 상하좌우로 일직선상에 위치했을 때 각도 입력
    # if whiteBall_x == targetBall_x:
    #     if whiteBall_y < targetBall_y:
    #         angle = 0
    #     else:
    #         angle = 180
    # elif whiteBall_y == targetBall_y:
    #     if whiteBall_x < targetBall_x:
    #         angle = 90
    #     else:
    #         angle = 270
    
    # 목적구가 흰 공을 중심으로 3사분면에 위치했을 때 각도를 재계산
    # if whiteBall_x > targetBall_x and whiteBall_y > targetBall_y:
    #     radian = math.atan(width / height)
    #     angle = (180 / math.pi * radian) + 180
    
    # 목적구가 흰 공을 중심으로 4사분면에 위치했을 때 각도를 재계산
    # elif whiteBall_x < targetBall_x and whiteBall_y > targetBall_y:
    #     radian = math.atan(height / width)
    #     angle = (180 / math.pi * radian) + 90
        
    # distance: 두 점(좌표) 사이의 거리를 계산
    # distance = math.sqrt(width**2 + height**2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    # power = distance * 0.5
    
    r = 5.73                        # 공의 반지름
    hole_distance = 10000000        # 홀까지의 거리 임의값 생성 (향후 타겟 홀을 정할 시 활용)
    
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]
    
    # 선공 플레이어 1, 3, 5 후공 플레이어 2, 4, 5
    player_one = [3, 1, 5]
    player_two = [2, 4, 5]
    
    # 선공 후공 여부 결정
    if order == 1:
        for i in player_one:
            if balls[i][0] > 0:            # 이미 좌표 밖으로 나간 공은 제외
                targetBall_x = balls[i][0]
                targetBall_y = balls[i][1]
                break
    elif order == 2:
        for i in player_two:
            if balls[i][1] > 0:            # 이미 좌표 밖으로 나간 공은 제외
                targetBall_x = balls[i][0]
                targetBall_y = balls[i][1]
                break
    
    # target_x와 target_y (최종적으로 히트할 지점)을 구하고, 해당 지점을 바탕으로 angle과 power 결정
    # 우선 목적구의 좌표로 초기화
    # 피타고라스의 정리 활용
    distance = math.sqrt((targetBall_x - whiteBall_x) ** 2 + (targetBall_y - whiteBall_y) ** 2)     # 목적구의 좌표와 흰공 간의 거리
    target_x = targetBall_x
    target_y = targetBall_y
    
    # 가까운 홀 선택
    for i in range(6):
        target_to_hole_distance = math.sqrt((targetBall_x - HOLES[i][0]) ** 2 + (targetBall_y - HOLES[i][1]) ** 2)
        if hole_distance > target_to_hole_distance:
            hole_distance = target_to_hole_distance
            hole_x = HOLES[i][0]
            hole_y = HOLES[i][1]
        
    # 목적구와 홀과의 각도 계산
    target_to_hole_width = abs(hole_x - targetBall_x)
    target_to_hole_height = abs(hole_y - targetBall_y)
    hole_radian = math.atan(target_to_hole_width / target_to_hole_height)   # 아크탄젠트를 활용하여 radian 각 생성
    
    # 홀로 갈 수 있는 타격지점 구하기
    # 우선 목적구의 좌표로 초기화
    hit_target_x = targetBall_x
    hit_target_y = targetBall_y
    
    # 목적구의 히트 지점 좌표 구하기
    # sin(높이 / 빗변), cos(밑변 / 빗변), 빗변은 r인 점을 착안하여 홀과 목적구의 각에 해당 목적구 히트지점 좌표를 구하기
    
    if targetBall_x > hole_x and targetBall_y > hole_y:
        hit_target_x += (r * math.cos(hole_radian))
        hit_target_y += (r * math.sin(hole_radian))
    elif targetBall_x > hole_x and targetBall_y < hole_y:
        hit_target_x += (r * math.cos(hole_radian))
        hit_target_y -= (r * math.sin(hole_radian))
    elif targetBall_x < hole_x and targetBall_y > hole_y:
        hit_target_x -= (r * math.cos(hole_radian))
        hit_target_y += (r * math.sin(hole_radian))
    elif targetBall_x < hole_x and targetBall_y < hole_y:
        hit_target_x -= (r * math.cos(hole_radian))
        hit_target_y -= (r * math.sin(hole_radian))
    
    # 해당 히트 지점에 대하여 흰공이 홀과 더 멀리 있는 경우에 히트
    # 흰공과 목적구 간의 거리보다 히트 지점과의 거리가 더 가까이 있어야함으로 조건 설정
    hit_target_distance = math.sqrt((hit_target_x - whiteBall_x) ** 2 + (hit_target_y - whiteBall_y) ** 2)
    if hit_target_distance < distance:
        # 최종 지점 설정
        target_x = hit_target_x
        target_y = hit_target_y
            
    # 히트 지점을 바탕으로 angle, power 생성
    width = abs(target_x - whiteBall_x)
    height = abs(target_y - whiteBall_y)
    angle_radian = math.atan(width / height) if width > 0 and height > 0 else 0
    angle = 180 / math.pi * angle_radian
    
    # 목적구가 흰공 기준 1, 2, 3, 4분면일 시 angle 재계산
    # 각도는 동경을 기준으로 얼마나 갔는가
    # 1사분면 (동일)
    if target_x > whiteBall_x and target_y > whiteBall_y:
        angle_radian = math.atan(width / height)
        angle = 180 / math.pi * angle_radian
    # 2사분면
    elif target_x < whiteBall_x and target_y > whiteBall_y:
        angle_radian = math.atan(width / height)
        angle = 360 - (180 / math.pi * angle_radian)
    # 3사분면
    elif target_x < whiteBall_x and target_y < whiteBall_y:
        angle_radian = math.atan(width / height)
        #angle = 270 - (180 / math.pi * angle_radian)
        angle = 180 + (180 / math.pi * angle_radian)
    # 4사분면
    elif target_x > whiteBall_x and target_y < whiteBall_y:
        angle_radian = math.atan(width / height)
        angle = 180 - (180 / math.pi * angle_radian)
        
    # 수평, 수직
    if whiteBall_x == targetBall_x:
        if whiteBall_y < targetBall_y:
            angle = 0
        else:
            angle = 180
    elif whiteBall_y == targetBall_y:
        if whiteBall_x < targetBall_x:
            angle = 90
        else:
            angle = 270
        
    distance = math.sqrt(width ** 2 + height ** 2)  # 히트 지점과 흰공 간의 거리
    power = (distance * 1 + hole_distance * 0.8) / 5

    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')
```

---

### 개선점
- 흰 공과 목적구 사이의 각이 예각, 직각, 둔각인 경우 나누어 구현
- 직선의 방정식, 점과 직선 사이의 거리와 r 간의 비교를 통한 경로 검사 구현
- angle 설정이 정교하지 않음 (1, 2, 3, 4분면에 대한 개념 불명확)
- 쿠션 구현

---