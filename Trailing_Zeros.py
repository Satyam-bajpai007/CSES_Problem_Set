# Your task is to calculate the number of trailing zeros in the
# factorial n!.

# For example, 20!=2432902008176640000 and it has 4 trailing zeros.

import math
n = int(input())
cnt = 0
n = math.factorial(n)
while n%10 == 0:
    if n%10 == 0:
        cnt+=1
        n = n/10
print(cnt)