n = int(input())
x = []
for i in range(n):
    a = list(map(int, input().split()))
    x.append(a)
pst = x[0][0]
l = 0
for j in range(1, n):
    i = pst-1
    if i > j:
        pst = x[i][j]
    else:
        pst = x[j][i]
print(pst)