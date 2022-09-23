# Your task is to count for k=1,2,…,n the number of ways two
# knights can be placed on a k×k chessboard so that they do not
# attack each other.

n = int(input())
org = 0
flt = 0
for i in range(1,n+1):
    org = ((i**2)*(i**2-1))/2
    flt = 4*(i-1)*(i-2)
    print(int(org-flt))