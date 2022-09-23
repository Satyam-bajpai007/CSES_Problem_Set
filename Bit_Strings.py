# Your task is to calculate the number of bit strings of length n.

# For example, if n=3, the correct answer is 8, because the possible
# bit strings are 000, 001, 010, 011, 100, 101, 110, and 111.

# Method 1
n = int(input())
print(2**n)

# Method 2
n = int(input())
m=1
for i in range(n):
    m<<=1
print(m)