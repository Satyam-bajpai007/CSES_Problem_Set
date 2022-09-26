# The Tower of Hanoi game consists of three stacks (left, middle 
# and right) and n round disks of different sizes. Initially, the
# left stack has all the disks, in increasing order of size from
# top to bottom.

# The goal is to move all the disks to the right stack using the
# middle stack. On each move you can move the uppermost disk from
# a stack to another stack. In addition, it is not allowed to place
# a larger disk on a smaller disk.

# Your task is to find a solution that minimizes the number of moves.


n = int(input())
total = 2*n-1
mid = int((total+1)/2)
print(total)
for i in range(1,total+1):
    if i < mid:
        print("1  2")
    elif i == mid:
        print("1  3")
    else:
        print("2  3")