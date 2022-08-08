lst = list(map(int, input()))
cnts = [0] * 12
ans = 0
#cnts 배열에 빈도수 표기
for n in lst:
    cnts[n] += 1
#tri, run 찾기
i = 0
while i < 10:
    if cnts[i] >= 3:
        ans += 1
        cnts[i] -= 3
    elif cnts[i] >= 1 and cnts[i+1] >= 1 and cnts[i+2] >=2:
        ans += 1
        cnts[i] -= 1
        cnts[i+1] -= 1
        cnts[i+2] -= 1
    else:
        i += 1
print(ans//2)



'''
방법 1
cnts = [0] * 10
ans = 0
#cnts 배열에 빈도수 표기
for n in lst:
    cnts[n] += 1
#tri 찾기
i = 0
while i < 10:
    if cnts[i] >= 3:
        ans += 1
        cnts[i] -= 3
    else:
        i += 1
#run 찾기
i = 0
while i < 8:
    if cnts[i] >= 1 and cnts[i+1] >= 1 and cnts[i+2] >=2:
        ans += 1
        cnts[i] -= 1
        cnts[i+1] -= 1
        cnts[i+2] -= 1
    else:
        i += 1
'''
'''
방법 2
cnts = [0] * 12
ans = 0
#cnts 배열에 빈도수 표기
for n in lst:
    cnts[n] += 1
#tri, run 찾기
i = 0
while i < 10:
    if cnts[i] >= 3:
        ans += 1
        cnts[i] -= 3
        continue

    if cnts[i] >= 1 and cnts[i+1] >= 1 and cnts[i+2] >=2:
        ans += 1
        cnts[i] -= 1
        cnts[i+1] -= 1
        cnts[i+2] -= 1
        continue
    i += 1
'''


#print(f'{testcase} {ans//2}')