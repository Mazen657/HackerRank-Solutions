# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = input()
K = list(input().split())

counts = Counter(K)

for key, value in counts.items():
    if value == 1:
        print(key)
