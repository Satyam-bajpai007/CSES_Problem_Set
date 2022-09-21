#A number spiral is an infinite grid whose upper-left square has
# number 1. Here are the first five layers of the spiral:
                  # [1,2,9,9,10,25]
                  # [4,3,8,11,24]
                  # [5,6,7,12,23]
                  # [16,15,14,13,22]
                  # [17,18,19,20,21]


spiral = [[1,2,9,9,10,25],[4,3,8,11,24],[5,6,7,12,23],[16,15,14,13,22],[17,18,19,20,21]]
n = int(input())
lst=[]
for i in range(n):
    a,b = map(int, input().split())
    x = spiral[a-1][b-1]
    lst.append(x)
for i  in range(n):
    print(lst[i])