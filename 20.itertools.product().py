# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
A = [int(y) for y in input().split()]
B = [int(x) for x in input().split()]
APoductB = list(itertools.product(A, B))
print(*APoductB, sep=" " )
