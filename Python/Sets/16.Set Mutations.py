def createMutations (operations, A):
    n = operations[1]
    if operations[0] == "update":
        update = [int(n) for n in input().split()]
        A.update(update)
    elif operations[0] == "intersection_update":
        intersection_update = [int(n) for n in input().split()]
        A.intersection_update(intersection_update)
    elif operations[0] == "symmetric_difference_update":
        symmetric_difference_update = [int(n) for n in input().split()]
        A.symmetric_difference_update(symmetric_difference_update)
    elif operations[0] == "difference_update":
        difference_update = [int(n) for n in input().split()]
        A.difference_update(difference_update)

y = input()
A = [int(y) for y in input().split()]
A = set(A)

for i in range(int(input())):
    x=list(input().split())
    createMutations(x, A)
print(sum(A))
