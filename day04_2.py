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

class PaperMap():
    def __init__(self, input_map):
        self.input_map = input_map
        self.removed = 0

    def remove_accessible(self):
        for row in range(len(self.input_map)):
            for column in range(len(self.input_map[row])):
                if self.input_map[row][column] == '@' and is_accessible(row, column, self.input_map):
                    self.input_map[row] = self.input_map[row][:column] + '.' + self.input_map[row][column+1:]
                    self.removed += 1

if __name__=="__main__":
    with open("day04_input.txt") as f:
        data = f.read()
    rows = data.split('\n')
    paper_map = PaperMap(rows)
    removed = -1 #something that will satisfy while condition initially.
    while removed < paper_map.removed:
        removed = paper_map.removed
        paper_map.remove_accessible()
    print(removed)