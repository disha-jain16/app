import heapq

def a_star(graph, start, goal, heuristic):
    # Priority queue for exploring nodes (f, node)
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], start))  # (f, node)
    
    # Dictionaries to store the costs
    g_costs = {start: 0}  # g(n): Cost from start to node
    f_costs = {start: heuristic[start]}  # f(n) = g(n) + h(n)
    previous_nodes = {start: None}  # To reconstruct the path
    
    while open_list:
        # Pop the node with the lowest f(n) value
        current_f, current_node = heapq.heappop(open_list)
        
        # If we reach the goal, reconstruct the path
        if current_node == goal:
            return reconstruct_path(previous_nodes, start, goal)
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            tentative_g_cost = g_costs[current_node] + weight
            
            # If this path is better, update the costs and previous node
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_costs[neighbor] = tentative_g_cost + heuristic[neighbor]
                previous_nodes[neighbor] = current_node
                
                # Add the neighbor to the open list with the updated f(n)
                heapq.heappush(open_list, (f_costs[neighbor], neighbor))
    
    return None  # Return None if there is no path

def reconstruct_path(previous_nodes, start, goal):
    path = []
    current_node = goal
    while current_node is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    return path[::-1]  # Reverse the path to get the correct order

# Example graph and heuristic (Manhattan distance as an example heuristic)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Heuristic for each node (simple straight-line distance or estimated cost)
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 0
}

start_node = 'A'
goal_node = 'D'

# Run A* algorithm
path = a_star(graph, start_node, goal_node, heuristic)
print(f"Shortest path from {start_node} to {goal_node}: {path}")
