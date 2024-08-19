v, t, s, d = map(int, input().split())
a = d/v
if a >= t and a <= s:
    print("No")
else:
    print("Yes")