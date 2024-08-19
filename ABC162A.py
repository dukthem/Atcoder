N = input()
a = 0
for i in range(0, 3):
   if N[i] == "7":
      a += 1
if a > 0:
   print("Yes")
else:
   print("No")