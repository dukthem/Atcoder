n = int(input())
a = list(map(int, input().split()))
G = []
for i in range(1, n):
    b = list(map(int, input().split()))  
    G.append(b)
cnt = 0
while max(a) != a[n-1]:
    for i in range(0,n):
        if a[i] == max(a):
            cnt = i+1
    if a[cnt-1] <= G[cnt-1][0]:
        a[cnt-1] -= G[cnt-1][0]
        a[cnt] += G[cnt-1][1]
    else:
        print(max(a))
        break
print(a[n-1])
        