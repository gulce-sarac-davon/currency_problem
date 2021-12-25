from numpy import inf
total={}
cost={}
def findAndReturn( ):
   
    file1 = open('input.txt', 'r')
    Lines = file1.readlines()
 

# Strips the newline character
    for line in Lines:

        splitted=line.strip().split("->")
        
        fromCur=splitted[0]
        
        splitted1=splitted[1].split("=")
       
        toCurr=splitted1[0]
        multip=float(splitted1[1])
        total.setdefault(fromCur, {})[toCurr] = multip
        total.setdefault(toCurr, {})[fromCur] = 1/multip
        cost[fromCur]=inf
        cost[toCurr]=inf
        """total[fromCur][toCurr]=multip
        total[toCurr][fromCur]=1/multip"""

findAndReturn( )
print(total)

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

result=find_path(total, "a", "x", path=[])      
print(result)
def calc(price ,path):
    for i in range(0,len(path)-1):
        price=price*total[path[i]][path[i+1]]
    return price
print(calc(10,result))




























