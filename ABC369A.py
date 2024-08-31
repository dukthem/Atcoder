a , b = list(map(int, input().split()))
x1 = (2*b) - a
x2 = (b+a) / 2
x3  = (2*a) - b
a = str(x2)
s = {x1, x2, x3}
# if a == b:
#     print(1)
# else:
#     if x2 % 1 == 0.0:
#         print(3)
#     else:
#         print(2)
if x2 % 1 != 0.0:
    print(len(s)-1)
else:
    print(len(s))