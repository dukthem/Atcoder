n , k = list(map(int, input().split()))
s = input()
cnt = 0
ans = 0
l = 0
cand = 0
i = 0
while i <= n - k:
        a = s[i:i+k]
        if a == ('O'*k):
            cnt += 1
            i = i+k
        else: 
            i += 1
print(cnt)




#         if s[i] == 'O':
#             cnt += 1
#         else:
#             cnt = 0
#         if cnt == k:
#             cand += 1
#             l = i + 1
#             break
#         if i == n-1:
#             ans = cand
# print(ans)