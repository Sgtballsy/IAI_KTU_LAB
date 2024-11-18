INF = float('inf')
    
def alpha_beta(depth, node_index, is_maximising, values, alpha, beta, level=0, path="0", pruned_paths=None):
    # Initialize pruned paths list if it's the first call
    if pruned_paths is None:
        pruned_paths = []
    
    # Base case: if depth is 0 or reached beyond leaf nodes
    if depth == 0 or node_index >= len(values):
        leaf_value = values[node_index] if node_index < len(values) else None
        print(f"{' ' * level}Leaf node value: {leaf_value} at path {path}")
        return leaf_value

    if is_maximising:
        max_eval = -INF
        print(f"{' ' * level}Maximising node at depth {level}, alpha {alpha}, beta {beta}, path {path}")
        
        for i in range(2):
            new_path = path + f"->{node_index * 2 + i}"
            eval = alpha_beta(depth - 1, node_index * 2 + i, False, values, alpha, beta, level + 1, new_path, pruned_paths)
            if eval is not None:
                max_eval = max(eval, max_eval)
                alpha = max(eval, alpha)
            
            # Alpha-beta pruning
            if alpha >= beta:
                print(f"{' ' * level}Pruned at depth {level}, alpha {alpha}, beta {beta}, path {new_path}")
                pruned_paths.append(new_path)  # Record the pruned path
                break
            
            print(f"{' ' * level}Maximising node returned {max_eval} at path {path}")
        
        # Print pruned paths at the root level
        if level == 0:
            print("\nPruned paths:", pruned_paths)
        return max_eval
    
    else:
        min_eval = INF
        print(f"{' ' * level}Minimising node at depth {level}, alpha {alpha}, beta {beta}, path {path}")
        
        for i in range(2):
            new_path = path + f"->{node_index * 2 + i}"
            eval = alpha_beta(depth - 1, node_index * 2 + i, True, values, alpha, beta, level + 1, new_path, pruned_paths)
            if eval is not None:
                min_eval = min(eval, min_eval)
                beta = min(eval, beta)
            
            # Alpha-beta pruning
            if alpha >= beta:
                print(f"{' ' * level}Pruned at depth {level}, alpha {alpha}, beta {beta}, path {new_path}")
                pruned_paths.append(new_path)  # Record the pruned path
                break
            
            print(f"{' ' * level}Minimising node returned {min_eval} at path {path}")
        
        # Print pruned paths at the root level
        if level == 0:
            print("\nPruned paths:", pruned_paths)
        return min_eval

# Input section with validation for leaf nodes
n = int(input("Enter the number of leaf nodes: "))
depth = int(input("Enter the depth: "))
req_leaf = 2 ** depth
if n != req_leaf:
    print(f"Error: Depth {depth} requires {req_leaf} leaf nodes, but {n} were provided.")
else:
    values = []
    for i in range(n):
        v = int(input(f"Enter the leaf node at index {i+1}: "))
        values.append(v)
    
    alpha = -INF
    beta = INF
    optimal = alpha_beta(depth, 0, True, values, alpha, beta, path="0")
    print(f"\nOptimal value: {optimal}")