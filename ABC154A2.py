S, T = input().split() # ['red', 'blue']
A, B = list(map(int, input().split())) # ['3', '4'] => [3, 4]
U = input()
if U == S:
    print(A - 1, "", B)
elif T == U:
    print(A, "", B - 1)