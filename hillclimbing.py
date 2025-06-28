graph = {} 
path = [] 
heuristic = {} 
traversal = [] 
cost_of_traversal = 0 
is_maximization = False 
size = int(input("Enter Size of the Graph: ")) 
user_input = input("Enter True if the problem is a Maximization Problem: ").strip().lower() 
is_maximization = user_input == 'true' 
for i in range(size): 
    node = input(f"Enter name of node {i+1}: ").upper() 
    number = int(input(f"Enter Heuristic Value for node {node}: ")) 
    heuristic[node] = number 
    children = input(f"Enter Children of {node} (separate by spaces): ").upper().split() 
    graph[node] = children 
source = input("Enter Initial State: ").upper() 
def steepest_hill_climbing(source, heuristic): 
    global cost_of_traversal, path, traversal 
    path.clear() 
    traversal.clear() 
    cost_of_traversal = 0 
    current = source 
    path.append(current) 
    traversal.append(current) 
    cost_of_traversal += heuristic[current] 
    while True: 
        neighbors = graph.get(current, []) 
        if not neighbors: 
            break 
        if is_maximization: 
            next_node = max(neighbors, key=lambda node: heuristic[node], default=None) 
        else: 
            next_node = min(neighbors, key=lambda node: heuristic[node], default=None) 
        if next_node is None: 
            break 
        current_heuristic = heuristic[current] 
        next_heuristic = heuristic[next_node] 
        if is_maximization: 
            if next_heuristic <= current_heuristic: 
                break 
        else: 
            if next_heuristic >= current_heuristic: 
                break 
        current = next_node 
        path.append(current) 
traversal.append(current) 
cost_of_traversal += next_heuristic 
return "Reached local optimum!" 
result = steepest_hill_climbing(source, heuristic) 
print(result) 
print("Path taken:", " → ".join(path)) 
print("Traversal of the graph:", " → ".join(traversal)) 
print(f"Total traversal cost: {cost_of_traversal}") 
