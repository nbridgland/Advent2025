def rotate_data(input_rows):
    output_list = [{'operation': '',
                    'numbers': []} for _ in range(len(input_rows[-1].strip()))]
    output_entry = -1
    for i in range(len(input_rows[0])):
        if input_rows[-1][i] != ' ':
            output_entry += 1
            output_list[output_entry]['operation'] = input_rows[-1][i]
        number_string = ''
        for j in range(len(input_rows)-1):
            number_string += input_rows[j][i]
        if number_string.strip() != '':
            output_list[output_entry]['numbers'].append(int(number_string.strip()))
    return output_list

if __name__ == '__main__':
    with open('day06_input.txt') as f:
        data = f.read()
    rows = data.split('\n')
    max_length = max([len(row) for row in rows])
    for k in range(len(rows)):
        while len(rows[k]) < max_length:
            rows[k] = rows[k] + ' '
    rotated_rows = rotate_data(rows)
    grand_total = 0
    for entry in rotated_rows:
        if entry['operation'] == '*':
            total = 1
            for i in entry['numbers']:
                total *= i
            grand_total += total
        if entry['operation'] == '+':
            for i in entry['numbers']:
                grand_total += i
    print(grand_total)