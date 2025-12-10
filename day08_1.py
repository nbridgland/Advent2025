def find_distance(box_coordinate_1, box_coordinate_2):
    return ((box_coordinate_1[0] - box_coordinate_2[0])**2 + (box_coordinate_1[1] - box_coordinate_2[1])**2 + (box_coordinate_1[2] - box_coordinate_2[2])**2)**(1/2)

def combine_common_verticies(vertex_lists):
    i = 0
    while i < len(vertex_lists):
        j = i + 1
        while j < len(vertex_lists):
            for vertex in vertex_lists[i]:
                if vertex in vertex_lists[j]:
                    for vertex_0 in vertex_lists[j]:
                        if vertex_0 not in vertex_lists[i]:
                            vertex_lists[i].append(vertex_0)
                    vertex_lists.pop(j)
                    j = i
                    break
            j += 1
        i += 1


if __name__ == "__main__":
    with open("day08_input.txt") as f:
        data = f.read()
    box_coordinates = [[int(coordinate) for coordinate in entry.split(',')] for entry in data.split('\n')]
    distance_dictionary = {}
    for i in range(len(box_coordinates)):
        for j in range(i+1, len(box_coordinates)):
            distance = find_distance(box_coordinates[i], box_coordinates[j])
            if distance not in distance_dictionary:
                distance_dictionary[distance] = [(i, j)]
            else:
                print('This edge case occurred!') # it did not
                distance_dictionary[distance].append((i, j))
    connected_verticies = []
    for k in range(1000):  # change to 10 for test input; 1000 for actual input
        vertex1, vertex2 = distance_dictionary[min(distance_dictionary.keys())][0]
        distance_dictionary.pop(min(distance_dictionary.keys()))
        added = False
        for vertex_list in connected_verticies:
            if vertex1 in vertex_list or vertex2 in vertex_list:
                added = True
                if vertex1 not in vertex_list:
                    vertex_list.append(vertex1)
                if vertex2 not in vertex_list:
                    vertex_list.append(vertex2)
        if not added:
            connected_verticies.append([vertex1, vertex2])
        if k % 100 == 0:
            print(k)
    combine_common_verticies(connected_verticies)
    output = 1
    for k in range(3):
        max_length = 0
        max_index = 0
        for i in range(len(connected_verticies)):
            if len(connected_verticies[i]) > max_length:
                max_length = len(connected_verticies[i])
                max_index = i
        output *= max_length
        connected_verticies.pop(max_index)
    print(output)