import math
from Map import Map_Obj

TASK_NUMBER = 1
USE_EUCLIDIAN_DISTANCE = False

map_obj1 = Map_Obj(task=TASK_NUMBER)
map_obj1.read_map("Samfundet_map_1.csv")
map_obj1.show_map()

def euclidian_distance(node1, node2):
    d1 = node1[0] - node2[0]
    d2 = node1[1] - node2[1]
    return math.sqrt(d1 ** 2 + d2 ** 2)


def manhattan_distance(node1, node2):
    d1 = abs(node1[0] - node2[0])
    d2 = abs(node1[1] - node2[1])
    return d1 + d2


def a_star(map_obj, heuristic_function):
    map_size_x = len(map_obj.get_maps()[0])
    map_size_y = len(map_obj.get_maps()[0][0])

    start_node = tuple(map_obj.get_start_pos())
    goal_node = tuple(map_obj.get_goal_pos())

    print("Start node: ", start_node)
    print("Goal node: ", goal_node)

    open_list = [start_node]
    closed_list = []
    cost = {start_node: 0}
    previous_node = {start_node: None}

    while open_list:
        current_node = min(
            open_list, key=lambda x: cost[x] + heuristic_function(x, goal_node)
        )

        open_list.remove(current_node)

        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node)
                map_obj.set_cell_value(current_node, " P ")
                current_node = previous_node[current_node]
            map_obj.set_cell_value(start_node, " S ")
            map_obj.set_cell_value(goal_node, " G ")
            map_obj.show_map()
            return path[::-1]

        def expand_node(new_node):
            node_value = map_obj.get_cell_value(list(new_node))
            if new_node not in closed_list and node_value != -1:
                if new_node not in open_list:
                    open_list.append(new_node)
                    cost[new_node] = cost[current_node] + node_value
                    previous_node[new_node] = current_node
                else:
                    if cost[new_node] > cost[current_node] + 1:
                        cost[new_node] = cost[current_node] + node_value
                        previous_node[new_node] = current_node

        # Up
        if current_node[0] - 1 >= 0:
            expand_node((current_node[0] - 1, current_node[1]))

        # Down
        if current_node[0] + 1 < map_size_x:
            expand_node((current_node[0] + 1, current_node[1]))

        # Left
        if current_node[1] - 1 >= 0:
            expand_node((current_node[0], current_node[1] - 1))

        # Right
        if current_node[1] + 1 < map_size_y:
            expand_node((current_node[0], current_node[1] + 1))

        closed_list.append(current_node)
        map_obj.set_cell_value(list(current_node), " E ")

    print(open_list)


print(
    a_star(
        map_obj1, euclidian_distance if USE_EUCLIDIAN_DISTANCE else manhattan_distance
    )
)
