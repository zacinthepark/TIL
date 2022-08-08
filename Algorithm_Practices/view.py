# test case 10번
for i in range(0, 10):
    # 가로 길이
    N = int(input())
    # 각 건물 높이들을 원소로 하는 리스트 생성
    tc = list(map(int, input().split()))
    # 조망권 확보 세대 수
    ans = 0
    # 양쪽 끝 2칸씩은 건물이 없으므로 인덱스 범위는 range(2, N-2)
    for j in range(2, N-2):
        # 조망권 확보 세대가 있는 경우는 해당 인덱스 건물(i) 양쪽 2칸씩까지의 건물(인덱스 i-2, i-1, i+1, i+2)보다 값이 큰 경우
        if tc[j] > tc[j-2] and tc[j] > tc[j-1] and tc[j] > tc[j+1] and tc[j] > tc[j+2]:
            # 조망권 확보 세대가 있음이 확보되었다면 양쪽 2칸씩까지의 건물 중 가장 높은 건물을 파악
            # 해당 건물에서 양쪽 2칸까지의 건물 중 가장 큰 건물의 높이를 뺀 것이 조망권 확보 세대의 수
            # 내장함수 max()를 사용하지 않음
            # if문을 활용하여 가장 큰 값을 일일이 검증
            if tc[j-2] >= tc[j-1] and tc[j-2] >= tc[j+1] and tc[j-2] >= tc[j+2]:
                ans += tc[j] - tc[j-2]
            elif tc[j-1] >= tc[j-2] and tc[j-1] >= tc[j+1] and tc[j-1] >= tc[j+2]:
                ans += tc[j] - tc[j-1]
            elif tc[j+1] >= tc[j-2] and tc[j+1] >= tc[j-1] and tc[j+1] >= tc[j+2]:
                ans += tc[j] - tc[j+1]
            elif tc[j+2] >= tc[j-2] and tc[j+2] >= tc[j-1] and tc[j+2] >= tc[j+1]:
                ans += tc[j] - tc[j+2]
print(f'#{i} {ans}')