 
goal = [] 
openList = [] 
closeList = [] 
path = [] 
graph = {} 
 
size = int(input(f"Enter Size of the Graph: ")) 
for i in range(size): 
    node = input(f"Enter name of the node {i+1} : ").upper() 
    children = input(f"Enter Children of {node} (separate them by spaces): ").upper().split() 
    graph[node] = children 
first = input(f"Enter Initial State: ").upper() 
goal = input(f"Enter Goal State (separate Them with spaces): ").upper().split() 
if first not in graph: 
    print(f"{first} not in the graph") 
openList.append([first,None]) 
print(f"The Structure of the graph is:\n {graph}") 
 
def is_in_both(value,list): 
    return  any(data[0 == value for data in list) 
 
def GoalTest(): 
    if not openList: 
        return print(f"Goal {goal} not found") 
    TestNode = openList.pop(0 
    if TestNode[0 in goal: 
        closeList.append(TestNode) 
        our_path = TestNode[0 
        while our_path is not None: 
            path.append(our_path) 
            for get_nodes in closeList: 
                if get_nodes[0 == our_path: 
                    our_path = get_nodes[1 
                    break 
        print(f"Goal State TestNode[0 Found") 
        path.reverse() 
        print("Shortest Path:", "→".join(path)) 
        return 
 
 
    else: 
        closeList.append(TestNode) 
        for children in graph[TestNode[0]: 
            if not is_in_both(children,closeList) and not is_in_both(children,openList): 
                openList.append([children,TestNode[0]) 
        return GoalTest() 
 
GoalTest() 
print("Traversal Path:","→".join(list_traversal for list_traversal,_ in closeList)) 
