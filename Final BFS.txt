from collections import deque

# Function to perform BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Add neighbors that haven't been visited
            queue.extend(graph[node])
    
    return order

# Main program
if __name__ == "__main__":
    graph = {}

    # Input number of locations
    n = int(input("Enter number of locations: "))

    # Input locations
    print("Enter location names (e.g., A B C ...):")
    locations = input().split()

    # Initialize adjacency list
    for loc in locations:
        graph[loc] = []

    # Input number of routes
    m = int(input("Enter number of routes: "))

    print("Enter routes as pairs (e.g., A B means route between A and B):")
    for _ in range(m):
        u, v = input().split()
        graph[u].append(v)
        graph[v].append(u)  # assuming undirected graph
    
    print (graph)
    # Input starting location
    start = input("Enter starting location: ")

    # Perform BFS
    bfs_order = bfs(graph, start)

    # Print visiting sequence
    print("BFS visiting sequence:", " -> ".join(bfs_order))
