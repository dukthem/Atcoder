n =int(input())
fatigue = 0
last = 0
last2 = 0
cnt = 0
cnt2 = 0
for i in range(n):
    ab = list(map(str, input().split()))
    if ab[1] == "L": 
        cnt += 1
        num = int(ab[0])
        fatigue += abs(num - last)
        last = num
        if cnt == 1:
            fatigue -= num
    else:
        cnt2 += 1
        num2 = int(ab[0])
        fatigue += abs(num2 - last2)
        last2 = num2
        if cnt2 == 1:
            fatigue -= num2
print(fatigue)