'''
입력
1
9
7 4 2 0 0 6 0 7 0

출력
#1 7
'''

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if lst[i] > lst[j]:
                cnt += 1
        if ans < cnt:
                ans = cnt
    print(f'#{test_case} {ans}')