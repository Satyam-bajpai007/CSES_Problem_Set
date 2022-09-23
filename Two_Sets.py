# Your task is to divide the numbers 1,2,…,n into two sets of equal sum.

n = int(input())
tar = 0
lst1 = [int(i) for i in range(1,n+1)]
lst2 = []
# print(lst1)
if (n*(n+1))%4 != 0:
    print("No")
else:
    print("Yes")
    tar = int((n*(n+1))/4)
    while tar != 0:
        if tar>lst1[-1]:
            tar=tar-lst1[-1]
            lst2.append(lst1[-1])
            lst1.remove(lst1[-1])
        else:
            lst2.append(tar)
            lst1.remove(tar)
            tar=0
print(len(lst1))
print(*lst1)
print(len(lst2))
print(*lst2)