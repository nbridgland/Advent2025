def make_map(map_rows):
    output = [[0 for _ in range(len(map_rows[0]))] for _ in range(len(map_rows))]
    for k in range(len(map_rows)):
        for j in range(len(map_rows[k])):
            if map_rows[k][j] == 'S':
                output[k][j] = 1
            if map_rows[k][j] == '^':
                output[k][j] = -1
    return output


if __name__ == '__main__':
    with open('day07_input.txt') as f:
        data = f.read()
    rows = data.split('\n')
    splitter_map = make_map(rows)
    for k in range(len(splitter_map)-1):
        for index in range(len(splitter_map[k])):
            if splitter_map[k][index] > 0:
                if splitter_map[k+1][index] == -1:
                    splitter_map[k+1][index-1] += splitter_map[k][index]
                    splitter_map[k+1][index+1] += splitter_map[k][index]
                else:
                    splitter_map[k+1][index] += splitter_map[k][index]
    for row in splitter_map:
        print(row)
    count_paths = 0
    for entry in splitter_map[-1]:
        if entry > 0:
            count_paths += entry
    print(count_paths)