# Given a string, your task is to generate all different strings
# that can be created using its characters.


from itertools import permutations
n = input()
lst = sorted(["".join(i) for i in list(set(permutations(n)))])
# print(lst)
for i in lst:
    print(i)