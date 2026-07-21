# Enter your code here. Read input from STDIN. Print output to STDOUT
y = input()
English = [int(y) for y in input().split()]
x = input()
French = [int(x) for x in input().split()]
English = set(English)
print(len(English.symmetric_difference(French)))
