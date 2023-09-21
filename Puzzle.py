def solve_puzzle(board, source, destination):
    rows, cols = len(board), len(board[0])
    queue = [(source[0], source[1])]
    visited = set(queue)
    parent = {}  # To store parent pointers

    while queue:
        curr_x, curr_y = queue.pop(0)

        if (curr_x, curr_y) == destination:
            path = []
            direction = []
            while (curr_x, curr_y) in parent:
                path.insert(0, (curr_x, curr_y))
                # up 0 -> 1
                if curr_x < parent[(curr_x, curr_y)][0]:
                    direction.insert(0,'U')
                # down 1 -> 0
                if curr_x > parent[(curr_x, curr_y)][0]:
                    direction.insert(0,'D')
                # left
                if curr_y < parent[(curr_x, curr_y)][1]:
                    direction.insert(0,'L')
                # right
                if curr_y > parent[(curr_x, curr_y)][1]:
                    direction.insert(0,'R')
                curr_x, curr_y = parent[(curr_x, curr_y)]
            path.insert(0, source)
            direction = ''.join(direction)
            return path, direction

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = curr_x + dx, curr_y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and board[new_x][new_y] == '-' and (
            new_x, new_y) not in visited:
                queue.append((new_x, new_y))
                visited.add((new_x, new_y))
                parent[(new_x, new_y)] = (curr_x, curr_y)

    return None  # No path exists


# Example usage
board = [['-', '-', '-', '-', '-'],
         ['-', '-', '#', '-', '-'],
         ['-', '-', '-', '-', '-'],
         ['#', '-', '#', '#', '-'],
         ['-', '#', '-', '-', '-']]
source = (0, 2)
destination = (2, 2)
result = solve_puzzle(board, source, destination)
print(result)

source = (0,0)
destination = (4,4)
result = solve_puzzle(board, source, destination)
print(result)


