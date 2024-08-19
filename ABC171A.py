c = input()
A = "QWERTYUIOPASDFGHJKLZXCVBNM"
a = "qwertyuiopasdfghjklzxcvbnm"
U = 0
L = 0
for i in range (0, 25):
    if A[i] == c:
        U += 1
for v in range (0, 25):
    if a[i] == c:
        L += 1
if U > 0:
    print("A")
else:
    print("a")