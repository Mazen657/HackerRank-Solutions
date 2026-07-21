# Enter your code here. Read input from STDIN. Print output to STDOUT
A = list(input().split())
A = set(A)
l=[]
for n in range (int(input())):
    B = set(input().split())
    if A == B:
        l.append(False)
    else:
        l.append(A.issuperset(B))

if False in l:
    print(False)
else:
    print(True)
