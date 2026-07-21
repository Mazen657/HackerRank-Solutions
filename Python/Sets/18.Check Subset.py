# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range (int(input())):
    y = input()
    A = [int(y) for y in input().split()]
    x = input()
    B = [int(x) for x in input().split()]
    A = set(A)
    B = set(B)
    print(A.issubset(B))
