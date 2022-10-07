# There are n apples with known weights. Your task is to divide the
# apples into two groups so that the difference between the weights
# of the groups is minimal.


n = int(input())
lst = list(map(int,input().split()))
t = sum(lst)
ans=0
cnt=0
for i in range(0,1<<n):
    s=0
    for j in range(0,n):
        cnt+=1
        if (i & (1<<j)):
            s+=lst[j]
    if s<=t/2:
        ans=max(s,ans)
# print(cnt)
# print(ans)
print(t-2*ans)