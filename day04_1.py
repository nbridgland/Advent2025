def get_adjacent_cells(row, column, input_map):
    if row == 0 and (column == 0 or column == len(input_map[0])-1):
        return [] # because only 3 adjacent spots, so don't actually have to check
    if row == len(input_map)-1 and (column == 0 or column == len(input_map[0])-1):
        return [] # same as above
    if row == 0:
        return [(row, column-1), (row, column+1), (row+1, column-1), (row+1, column), (row+1, column+1)]
    if row == len(input_map)-1:
        return [(row-1, column-1), (row-1, column), (row-1, column+1), (row, column-1), (row, column+1)]
    if column == 0:
        return [(row-1, column), (row-1, column+1), (row, column+1), (row+1, column), (row+1, column+1)]
    if column == len(input_map[0])-1:
        return [(row-1, column-1), (row-1, column), (row, column-1), (row+1, column), (row+1, column-1)]
    else:
        return [(row-1, column-1), (row-1, column), (row-1, column+1),
                (row, column - 1), (row, column + 1),
                (row+1, column-1), (row+1, column), (row+1, column+1)]

def is_accessible(row, column, input_map):
    position_list = get_adjacent_cells(row, column, input_map)
    count_occupied = 0
    for position in position_list:
        if input_map[position[0]][position[1]] == '@':
            count_occupied += 1
    return count_occupied < 4


if __name__=="__main__":
    with open("day04_input.txt") as f:
        data = f.read()
    rows = data.split('\n')
    count_accessible = 0
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if rows[i][j] == '@':
                count_accessible+=is_accessible(i, j, rows)
    print(count_accessible)
