# n, q = map(int, input().split())
# s = input()

# def count_abc(s):
#     count = 0
#     i = 0
#     while i < len(s) - 2:
#         if s[i:i+3] == "ABC":
#             count += 1
#             i += 3  
#         else:
#             i += 1
#     return count

# abc_count = count_abc(s)

# for _ in range(q):
#     a, c = input().split()
#     x = int(a)
#     x -= 1 

#     if s[x] != c:
#         if x > 1 and s[x-2:x+1] == "AB" and c == "C":
#             abc_count -= 1
#         if x > 0 and s[x-1:x+2] == "BC" and c == "A":
#             abc_count -= 1
#         if s[x-1:x+2] == "AB" and c == "C":
#             abc_count += 1
#         if s[x:x+3] == "ABC" and c == "A":
#             abc_count -= 1        
#         s = s[:x] + c + s[x+1:]

#         if x < n - 2 and s[x:x+3] == "ABC":
#             abc_count += 1
        
#     print(abc_count)

n , q = list(map(int, input().split()))
s = input()
for i in range(q):
    a, c = list(map(str, input().split()))
    x = int(a)
    s = s[ : x-1] + c + s[x :]
    ans = 0
    l = 0
    cnt = 0
    while ans == 0:
        for j in range(l,n-2):
                if s[j] == "A":
                    if s[j+1] == "B":
                        if s[j+2] == "C":
                            # print(j, end="")
                            # print(s[j:j+3])
                            cnt += 1
                            l += 3
                            break
        if l >= n-1:
             ans = 1
             break
    print(cnt)
        # cnt1 = 0
    # cnt = 0
    # l = 0
    # while(cnt1!=len(s)):
    #     for i in range(l, len(s)):
    #         if(len(s)-cnt1 >=3 and s[i]=="A" and s[i+1]=="B" and s[i+2]=="C"):
    #             l=i+3
    #             cnt1+=3
    #             cnt += 1
    #             break
    #         else:
    #             cnt1 += 1
    # print(cnt)
    #         nStr = s
    # pattern = 'ABC'
    # count = 0
    # flag = True
    # start = 0
    # while flag:
    #     g = nStr.find(pattern, start) 
    #     if g == -1:
    #         flag = False
    #     else:               
    #         count += 1        
    #         start = g + 1
    # print(count)
    # # print(s)