from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
directions = []
map_dict = {}
number = 500
visited = [False] * number
locations = []

# Creating world graph
for i in range(0, number):
    nsew = world.rooms[i].get_exits()
    map_dict[i] = []
    for j in nsew:
        map_dict[i].append(f'{j} {world.rooms[i].get_room_in_direction(j).id}')
print(map_dict)

def rec_func(node):
    global locations
    locations += [node]
    # if len(map_dict[node]) == 0:
    #     return directions
    # else:
    visited[node] = True
    if node == 26:
        print(f'this is 26: {map_dict[node]}')
    for idx, i in enumerate(map_dict[node]):
        if visited[int(i.split(" ")[1])] == False:
            directions.append(i.split(" ")[0])
            if len(map_dict[node]) == 0:
                return directions
            map_dict[node].pop(idx)
            rec_func(int(i.split(" ")[1]))
    if len(map_dict[node]) == 0:
        return directions
    directions.append(map_dict[node][0].split(" ")[0])
    x = int(map_dict[node][0].split(" ")[1])
    map_dict[node].pop(0)
    rec_func(x)
traversal_path = rec_func(0)
print(f'traversal path: {traversal_path}')
print(len(traversal_path))
print(map_dict)
print(visited)
# for i in range(0, 500):
#     if i in locations:
#         print(f'{i} ---- {True}')


# traversal_path = ['n', 'n', 's', 's', 'e', 'e', 'w', 'w', 's', 's', 'w', 'w', 'n', 'n', 'e']
# traversal_path = []



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
