import re

def fileInput(destination):
    f = open(destination,'r')
    intext = f.read()
    tree = {}
    intext = intext.split('\n')
    n = int(intext[0])

    start = intext[1]
    nodes = intext[2].split()
    for i in range(n):
        tree[nodes[i]] = intext[3+i].split()
    return start,tree