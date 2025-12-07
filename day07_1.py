if __name__ == '__main__':
    with open('day07_input.txt') as f:
        data = f.read()
    rows = data.split('\n')
    count_splits = 0
    for k in range(len(rows)-1):
        for index in range(len(rows[k])):
            if rows[k][index] == 'S':
                if rows[k+1][index] == '^':
                    rows[k+1] = rows[k+1][:index-1] + 'S^S' + rows[k+1][index+2:]
                    count_splits += 1
                else:
                    rows[k+1] = rows[k+1][:index] + 'S' + rows[k+1][index+1:]
    for row in rows:
        print(row)
    print(count_splits)