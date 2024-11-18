MAX, MIN = float('inf'), -float('inf')

def minimax(depth , nodeindex,maximizingPlayer,values,alpha,beta):
    if depth == maxDepth:
        return values[nodeindex]
    if maximizingPlayer:
        best = MIN
        for i in range(0,2):
            val = minimax(depth+1,nodeindex*2+i,False,values,alpha,beta)
            best = max(best,val)
            alpha = max(alpha,best)
            print("Level: ", depth)
            print("Alpha: ",alpha)
            print("Beta: ",beta)
            print("\n")
            if beta<=alpha:
                print("PRUNING IS DONE\n")
                break
        return best
    else:
        best = MAX
        for i in range(0,2):
            val = minimax(depth+1,nodeindex*2+i,True,values,alpha,beta)
            best = min(best,val)
            beta = min(beta,best)
            if beta<=alpha:
                print("PRUNING IS DONE\n")
                break
        return best

maxDepth = int(input("Enter the depth of treeL "))
values = []
for i in range(2**maxDepth):
    value = int(input(f"Enter the value at index {i+1}: "))
    values.append(value)
print("The optimal value is : ",minimax(0,0,True,values,MIN,MAX))