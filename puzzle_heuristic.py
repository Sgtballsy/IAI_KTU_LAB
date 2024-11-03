import heapq

class Puzzle:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.visited = set()
        self.pq = []

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

    def manhattan_distance(self, state):
        distance = 0
        for i in range(9):
            if state[i] != 0:
                goal_index = self.goal.index(state[i])
                goal_row, goal_col = divmod(goal_index, 3)
                curr_row, curr_col = divmod(i, 3)
                distance += abs(goal_row - curr_row) + abs(goal_col - curr_col)
        return distance

    def a_star_search(self):
        heapq.heappush(self.pq, (self.manhattan_distance(self.start), 0, self.start, []))
        while self.pq:
            _, cost, current_state, path = heapq.heappop(self.pq)
            if current_state == self.goal:
                return path + [current_state], cost
            if current_state not in self.visited:
                self.visited.add(current_state)
                for neighbor in self.get_neighbors(current_state):
                    new_cost = cost + 1
                    heapq.heappush(self.pq, (new_cost + self.manhattan_distance(neighbor), new_cost, neighbor, path + [current_state]))
        return None, None

def main():
    start = tuple(map(int, input("Enter the start state (9 numbers separated by space, use 0 for the blank): ").split()))
    goal = tuple(map(int, input("Enter the goal state (9 numbers separated by space, use 0 for the blank): ").split()))

    puzzle = Puzzle(start, goal)
    solution,cost = puzzle.a_star_search()

    if solution:
        print("Solution found with cost:",cost)
        for state in solution:
            for i in range(0, 9, 3):
                print(state[i:i+3])
            print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()