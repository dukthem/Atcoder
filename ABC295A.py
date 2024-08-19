x= int(input())
n = 0
a = list(map(str, input().split()))
for i in range (0, x):
    if a[i] == "and" or a[i] == "not" or a[i] == "that" or a[i] == "the" or a[i] == "you" :
        n += 1
if n >0:
    print("Yes")
else:
    print("No")
    