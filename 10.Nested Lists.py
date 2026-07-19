records = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    l = []
    for i in range(len(records)):
        l.append(records[i][1]) 
        
    s = set(l)
    l = sorted(s)
    n = []
    for i in range(len(records)):
        if records[i][1] == l[1]:
            n.append(records[i][0])
    n.sort()        
    print(*n, sep="\n")
    
