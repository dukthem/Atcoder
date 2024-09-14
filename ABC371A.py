ab, ac, bc = list(map(str, input().split()))
if ab == ac and ac == bc and bc == ">":
    print("B")
elif ab == ac and ac == bc and bc == "<":
    print("B")
elif ab == ac and ac != bc:
    if ac == "<":
        print("C")
    else:
        print("C")
elif ab == bc and bc != ac:
    if bc == "<":
        print("A")
    else:
        print("A")
elif ac == bc and ac != ab:
    if ac == "<":
        print("A")
    else:
        print("A")
# a = 0
# b = 0
# c = 0
# if ab == "<":
#     b = 10
#     a = 5