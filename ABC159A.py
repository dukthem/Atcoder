N, M = map(int, input().split())
a = 0 
while N > 0:
    N = N - 1
    a = N + a
while M > 0:
    M = M - 1
    a = M + a
print(a)