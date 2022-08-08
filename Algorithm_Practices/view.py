for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    ans = 0
    # 양쪽 2씩 건물이 없으므로 인덱스 범위는 2에서 N-3
    for i in range(2, N - 2):
        # 가운데 빌딩이 가장 큰 경우에만 조망권 세대 존재
        if buildings[i] > buildings[i - 1] and buildings[i] > buildings[i - 2] and buildings[i] > buildings[i + 1] and buildings[i] > buildings[i + 2]:
            # 양옆 건물들 중 가장 높은 건물과의 차이가 조망권 세대 수
            d1 = buildings[i] - buildings[i - 1]
            d2 = buildings[i] - buildings[i - 2]
            d3 = buildings[i] - buildings[i + 1]
            d4 = buildings[i] - buildings[i + 2]
            min_d = d1
            for j in [d1, d2, d3, d4]:
                if j < min_d:
                    min_d = j
            ans += min_d
    print(f'#{test_case} {ans}')