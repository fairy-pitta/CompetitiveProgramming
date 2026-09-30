import networkx as nx
def make_graph_from_grid(grid):
    def is_connectable(r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == '.'

    graph = {}
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if is_connectable(r, c):
                # Initialize the list of neighbors for this cell
                graph[(r, c)] = []
                # Check each of the four neighbors (up, down, left, right)
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if is_connectable(nr, nc):
                        graph[(r, c)].append((nr, nc))
    return graph
def solve_maze(grid, start, goal):
    # First, create the graph from the grid
    graph = make_graph_from_grid(grid)

    # Convert the graph to a NetworkX graph
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)

    # Find the shortest path
    path = nx.shortest_path(G, source=start, target=goal)
    return path

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

sy -= 1
sx -= 1
gy -= 1
gx -= 1

grid = [input() for _ in range(R)]

# The start and goal positions (0-indexed)
start = (sy, sx)  # Corresponds to (1,1) in 1-indexed format
goal = (gy, gx)   # Corresponds to (3,4) in 1-indexed format

# Solve the maze
path = solve_maze(grid, start, goal)
print(len(path)-1)
