n = int(input())
my_list = []
def printFunction (num):
    for i in range(1,num+1):
       my_list.append(i) 
    return print(*my_list, sep="" )
    

printFunction(n)
