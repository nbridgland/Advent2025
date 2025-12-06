if __name__ == '__main__':
    with open('day06_input.txt') as f:
        data = f.read()
    rows = data.split('\n')
    rows = [row.split(' ') for row in rows]
    rows = [[entry for entry in row if entry != ''] for row in rows]
    grand_total = 0
    for k in range(len(rows[0])):
        if rows[-1][k] == '*':
            total = 1
            for i in range(len(rows)-1):
                total *= int(rows[i][k].strip())
            grand_total += total
        if rows[-1][k] == '+':
            for i in range(len(rows)-1):
                grand_total += int(rows[i][k].strip())
    print(grand_total)