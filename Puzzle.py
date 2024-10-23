class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.visited = set()
        self.stack = []

    def get_neighbors(self, state):
        neighbors = []
        zero_index = state.index(0)
        row, col = divmod(zero_index, 3)

        moves = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_index = new_row * 3 + new_col
                new_state = list(state)
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                neighbors.append(tuple(new_state))

        return neighbors

    def dfs(self):
        self.stack.append((self.start, []))
        while self.stack:
            current_state, path = self.stack.pop()
            if current_state == self.goal:
                return path + [current_state]
            if current_state not in self.visited:
                self.visited.add(current_state)
                for neighbor in self.get_neighbors(current_state):
                    self.stack.append((neighbor, path + [current_state]))
        return None

def main():
    start = tuple(map(int, input("Enter the start state (9 numbers separated by space, use 0 for the blank): ").split()))
    goal = tuple(map(int, input("Enter the goal state (9 numbers separated by space, use 0 for the blank): ").split()))

    puzzle = Puzzle(start, goal)
    solution = puzzle.dfs()

    if solution:
        print("Solution found:")
        for state in solution:
            for i in range(0, 9, 3):
                print(state[i:i+3])
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()