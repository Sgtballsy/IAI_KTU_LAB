cost = {}
parent = {}
n = int(input("enter no. of nodes: "))
print("enter nodes:(separated by spaces) ")
key = input().split()
for i in range(n):
    cost[key[i]] = float('inf')

graph = {}
gcost = {}

for i in key:
    graph[i] = []
    gcost[i] = {}
    x = int(input("enter no. of nodes connected to " + i + ": "))
    if(x==0):continue
    print("enter nodes and cost:(node,cost node,cost) ")
    le = input()
    le = le.split()
    for j in range(0, len(le)):
        ve = le[j].split(',')
        graph[i].append(ve[0])
        gcost[i][ve[0]] = int(ve[1])

start = input("enter start node: ")
cost[start] = 0
parent[start] = None
def dijkstras(node,bcost):
    for i in graph[node]:
        c = bcost+gcost[node][i]
        if c<cost[i]:
            parent[i] = node
            cost[i] = c
            dijkstras(i,c)
dijkstras(start,0)

path = {}

print(' ')
for i in key:
    path[i] = i
    t = i
    while parent[t] != None:
        path[i] = parent[t] + '->'+path[i]
        t = parent[t]
print(' ')

for i in key:
    print("Shortest Path to "+i+" = "+path[i])
    print("Lowest Cost to "+i+" = "+ str(cost[i]))