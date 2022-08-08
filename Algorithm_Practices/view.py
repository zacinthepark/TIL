N = int(input())
tc = list(map(int, input().split()))

ans = 0
for i in range(2, N-2):
    if tc[i] > tc[i-2] and tc[i] > tc[i-1] and tc[i] > tc[i+1] and tc[i] > tc[i+2]:
        if tc[i-2] >= tc[i-1] and tc[i-2] >= tc[i+1] and tc[i-2] >= tc[i+2]:
            ans += tc[i] - tc[i-2]
        elif tc[i-1] >= tc[i-2] and tc[i-1] >= tc[i+1] and tc[i-1] >= tc[i+2]:
            ans += tc[i] - tc[i-1]
        elif tc[i+1] >= tc[i-2] and tc[i+1] >= tc[i-1] and tc[i+1] >= tc[i+2]:
            ans += tc[i] - tc[i+1]
        elif tc[i+2] >= tc[i-2] and tc[i+2] >= tc[i-1] and tc[i+2] >= tc[i+1]:
            ans += tc[i] - tc[i+2]

print(ans)