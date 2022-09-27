import math
import numpy as np
from Map import Map_Obj

map_obj1 = Map_Obj(task=1)
map_obj1.read_map("Samfundet_map_1.csv")
# map_obj1.show_map()

int_map, str_map = map_obj1.get_maps()


def euclidian_distance(node1, node2):
    d1 = node1[0] - node2[0]
    d2 = node1[1] - node2[1]
    return math.sqrt(d1 ** 2 + d2 ** 2)


def a_star(map_obj, heuristic_function):
    map_size_x = len(map_obj.get_maps()[0])
    map_size_y = len(map_obj.get_maps()[0][0])
    print(map_size_x, map_size_y)
    start_node = tuple(map_obj.get_start_pos())
    goal_node = tuple(map_obj.get_goal_pos())

    print("Start node: ", start_node)
    print("Goal node: ", goal_node)

    open_list = [start_node]
    closed_list = []
    cost = {start_node: 0}
    previous_node = {start_node: None}

    while open_list:
        print("Open list: ", open_list)
        current_node = min(
            open_list, key=lambda x: cost[x] + heuristic_function(x, goal_node)
        )
        print("Current node: ", current_node)

        open_list.remove(current_node)

        if current_node == goal_node:
            print("found!")
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous_node[current_node]
            return path[::-1]

        # Up
        if current_node[0] - 1 >= 0:
            new_node = (current_node[0] - 1, current_node[1])
            node_value = map_obj.get_cell_value(list(new_node))
            if new_node not in closed_list and node_value != -1:
                if new_node not in open_list:
                    open_list.append(new_node)
                    cost[new_node] = cost[current_node] + 1
                    previous_node[new_node] = current_node
                else:
                    if cost[new_node] > cost[current_node] + 1:
                        cost[new_node] = cost[current_node] + 1
                        previous_node[new_node] = current_node

        # Down
        if current_node[0] + 1 < map_size_y:
            new_node = (current_node[0] + 1, current_node[1])
            node_value = map_obj.get_cell_value(list(new_node))
            if new_node not in closed_list and node_value != -1:
                if new_node not in open_list:
                    open_list.append(new_node)
                    cost[new_node] = cost[current_node] + 1
                    previous_node[new_node] = current_node
                else:
                    if cost[new_node] > cost[current_node] + 1:
                        cost[new_node] = cost[current_node] + 1
                        previous_node[new_node] = current_node

        # Left
        if current_node[1] - 1 >= 0:
            new_node = (current_node[0], current_node[1] - 1)
            node_value = map_obj.get_cell_value(list(new_node))
            if new_node not in closed_list and node_value != -1:
                if new_node not in open_list:
                    open_list.append(new_node)
                    cost[new_node] = cost[current_node] + 1
                    previous_node[new_node] = current_node
                else:
                    if cost[new_node] > cost[current_node] + 1:
                        cost[new_node] = cost[current_node] + 1
                        previous_node[new_node] = current_node

        # Right
        if current_node[1] + 1 < map_size_x:
            new_node = (current_node[0], current_node[1] + 1)
            node_value = map_obj.get_cell_value(list(new_node))
            if new_node not in closed_list and node_value != -1:
                if new_node not in open_list:
                    open_list.append(new_node)
                    cost[new_node] = cost[current_node] + 1
                    previous_node[new_node] = current_node
                else:
                    if cost[new_node] > cost[current_node] + 1:
                        cost[new_node] = cost[current_node] + 1
                        previous_node[new_node] = current_node

        closed_list.append(current_node)

    print(open_list)


print(a_star(map_obj1, euclidian_distance))
