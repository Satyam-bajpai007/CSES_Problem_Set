# You are given a DNA sequence: a string consisting of characters A,
# C, G, and T. Your task is to find the longest repetition in the
# sequence. This is a maximum-length substring containing only one
# type of character.

# Method 1
n = input()
mxm = 0  
for i in range(len(n)):
    cnt = 0
    for j in range(i,len(n)):
        if n[i] == n[j]:
            cnt+=1
    if cnt>mxm:
        mxm = cnt
print(mxm)

# Method 2
n = input()
cnt = 0
mxm = 0  
for i in range(len(n)-1):
    if n[i+1]==n[i]:
        cnt+=1
        if cnt>mxm:
            mxm=cnt
    else:
        cnt=0
print(mxm)