a = input()
b = a.split()
x = int(b[0])
y = int(b[1])
count = 0
while x > 0:
    x = x - y
    count = count + 1
print(count)