n = int(input())
a = list(map(int, input().split()))
sum = 0
test = 0
for i in range(0, len(a)):
    if a[i] >= 0:
        sum += a[i]
    else:
        if sum + a[i] < 0:
            test = (a[i] + sum)*(-1)
            sum += test
            sum = sum + a[i]
        else:
            sum += a[i]
#for i in range(0, len(a)):
 #   test += a[i]
print(sum)