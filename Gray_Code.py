# A Gray code is a list of all 2n bit strings of length n, where
# any two successive strings differ in exactly one bit (i.e., their
# Hamming distance is one).

# Your task is to create a Gray code for a given length n.


n = int(input())
for i in range(1<<n):
    val = (i^(i>>1))
    val = bin(val)[2::]
    val = val.zfill(n)
    print(val)
