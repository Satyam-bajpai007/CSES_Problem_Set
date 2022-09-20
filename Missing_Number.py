# You are given all numbers between 1,2,…,n except one.
# Your task is to find the missing number.

# Method 1
n = int(input())
lst = list(map(int,input().split()))
lst.sort()
# print(lst)
for i in range(1,n-1):
    if lst[i]-lst[i-1]!=1:
        print(lst[i]-1)
        
# Method 2
n = int(input())
lst = list(map(int,input().split()))
sm = sum(lst)
org_sm = (n*(n+1))/2
print(int(org_sm-sm))