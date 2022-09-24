# You have two coin piles containing a and b coins. On each move,
# you can either remove one coin from the left pile and two coins
# from the right pile, or two coins from the left pile and one coin
# from the right pile.

# Your task is to efficiently find out if you can empty both the piles.


n = int(input())
lst = ["Yes" for i in range(n)]
for i in range(n):
    a,b =map(int,input().split())
    if (a+b)%3!=0:
        lst[i] = "No"
for i in range(n):
    print(lst[i])
