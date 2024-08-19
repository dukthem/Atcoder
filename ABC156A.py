a = input()
b = a.split()
N = int(b[0])
R = int(b[1])
S = R + 100*(10-N)
if (N >= 10):
    print(R)
else:
    print(S)
