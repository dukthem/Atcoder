S = input()
T = input()
i = 0
a = 0
while i != len(S):
    if (S[i] != T[i]):
        a = a + 1
    i = i + 1
if (a > 0):
    print("No")
else:
    print("Yes")