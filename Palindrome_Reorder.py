# Given a string, your task is to reorder its letters in such a way
# that it becomes a palindrome (i.e., it reads the same forwards
# and backwards).


n = input().upper()
dic={}
cnt=0
st=""
left=""

for i in n:
    if i in dic:
        dic[i]+=1 
    else:
        dic[i]=1
        
for i in dic.values():
    if i%2!=0:
        cnt+=1
        
print(dic)

if cnt > 1:
    print("NO SOLUTION")
else:
    if cnt == 0:
        for i in dic:
            st+=i
        st += st[::-1] 
        print(st)
    else:
        for i in dic:
            if dic[i]%2==0:
                st+=i
            else:
                left=i
        st = st + left*dic[left] + st[::-1]
        print(st)
