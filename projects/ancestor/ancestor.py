def earliest_ancestor(ancestors, starting_node):
    counter = 0
    depths = []
    test = [item for item in ancestors if item[1] == starting_node]
    if test == []:
        return -1
    def rec_function(input):
        nonlocal counter
        nonlocal depths
        for i in ancestors:
            if input == i[1]:
                counter += 1
                rec_function(i[0])
        depths += [(input, counter)]
        counter -= 1
    rec_function(starting_node)
    earliest = (0,0)
    for i in depths:
        if i[1] == earliest[1] and i[0] <= earliest[0]:
            earliest = (i[0], i[1])
        elif i[1] > earliest[1]:
            earliest = (i[0], i[1])
    # print(depths)
    # print(earliest[0])
    return earliest[0]

x = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
earliest_ancestor(x, 6)