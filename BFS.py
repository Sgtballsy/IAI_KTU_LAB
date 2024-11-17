n = int(input("pls enter the number of nodes: "))

start = input("pls enter the start node: ")

nodes = input("pls enter all the nodes: ").split()

tree = {}

for i in range(n):
    tree[nodes[i]] = input(f"pls enter the nodes connected to  {nodes[i]} ").split()

def bfs(tree, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = tree[node]
            for neighbour in neighbours:
                queue.append(neighbour)
    return visited

def prettyPrint(visited):
    for i in visited:
        print(i, end=" ")

myBFS = bfs(tree,start)
print(myBFS)



