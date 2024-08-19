a = input()
b = a.split()
A = int(b[0])
B = int(b[1])
C = int(b[2])
if (A == B  and B == C):
    print("No")
elif (A != B and A != C and B != C):
    print("No")
else:
    print("Yes")