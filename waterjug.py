goal = []
openList = []
closeList = []
path = []
graph = {}

rules = {
    1: "Fill 4-gallon jug",
    2: "Fill 3-gallon jug",
    3: "Empty 4-gallon jug",
    4: "Empty 3-gallon jug",
    5: "Pour 3-gallon into 4-gallon",
    6: "Pour 4-gallon into 3-gallon"
}

def get_children(state):
    a, b = state
    children = []

    children.append(((4, b), 1))  # Fill 4
    children.append(((a, 3), 2))  # Fill 3
    children.append(((0, b), 3))  # Empty 4
    children.append(((a, 0), 4))  # Empty 3

    total = a + b
    # Pour 3 into 4
    new_a = min(4, total)
    new_b = total - new_a
    children.append(((new_a, new_b), 5))

    # Pour 4 into 3
    new_b = min(3, total)
    new_a = total - new_b
    children.append(((new_a, new_b), 6))

    return children

goal_input = input("Enter Goal State (e.g., 2 0): ")
goal = [tuple(map(int, goal_input.replace(",", " ").split()))]

openList.append([(0, 0), None, None])
print(f"The Structure of the State Space is explored using rules.\n")

def is_in_both(value, list_):
    return any(data[0] == value for data in list_)

def GoalTest():
    if not openList:
        return print(f"Goal {goal} not found")

    TestNode = openList.pop(0)

    if TestNode[0] in goal:
        closeList.append(TestNode)
        our_path = TestNode[0]
        rule_path = TestNode[2]
        while our_path is not None:
            path.append((our_path, rule_path))
            for node in closeList:
                if node[0] == our_path:
                    our_path = node[1]
                    rule_path = node[2]
                    break
        path.reverse()
        for state, rule in path:
            print("------------------------")
            print(f"Current State: {state}")
            if rule:
                print(f"Rule Applied: {rules[rule]}")
        print("\nGoal State Reached!")
        print("→".join(str(state) for state, _ in path))
        return

    else:
        closeList.append(TestNode)
        for child, rule in get_children(TestNode[0]):
            if not is_in_both(child, closeList) and not is_in_both(child, openList):
                openList.append([child, TestNode[0], rule])
        return GoalTest()

GoalTest()
print("\nTraversal Path:", "→".join(str(state) for state, _, _ in closeList))
