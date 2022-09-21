# You are given an array of n integers. You want to modify the
# array so that it is increasing, i.e., every element is at
# least as large as the previous element.

# On each move, you may increase the value of any element by one.
# What is the minimum number of moves required?

n =int(input())
cnt=0
lst = [int(i) for i in input().split()]
for i in range(len(lst)-1):
    if lst[i+1]<lst[i]:
        cnt += lst[i] - lst[i+1]
        lst[i+1]=lst[i]
print(cnt)