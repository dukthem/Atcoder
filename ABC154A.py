a = input()
b = a.split()
S = str(b[0])
T = str(b[1])
c = input()
d = c.split()
A = int(d[0])
B = int(d[1])
U = input()
if (U == S):
    print(A-1, "", B)
elif (T == U):
    print(A, "", B-1)