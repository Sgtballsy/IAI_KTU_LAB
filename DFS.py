print("pls enter the number of nodes: ")
n = int(input())

print("pls enter the start node: ")
start = input()

print("pls enter all the nodes: ")
nodes = input().split()

tree = {}
for i in range(n):
    print("pls enter the nodes connected to ", nodes[i], " : ")
    tree[nodes[i]] = input().split()



visited = []


def dfs(node,tree,visited):
    if node not in visited:
        print(node,end=" ")
        visited.append(node)
        for neighbour in tree[node]:
            dfs(neighbour,tree,visited)


dfs(start,tree,visited) 


