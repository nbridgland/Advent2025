def check_pattern(input_string):
    return input_string[:len(input_string)//2] == input_string[len(input_string)//2:]

if __name__ == '__main__':
    with open('day2_input.txt') as f:
        data = f.read()
        id_ranges = data.split(',')
        sum_invalid = 0
        count_invalid = 0
        for id_range in id_ranges:
            id_min, id_max = id_range.split('-')
            current_id = int(id_min)
            while current_id <= int(id_max):
                if check_pattern(str(current_id)):
                    sum_invalid += current_id
                current_id += 1
        print(f"Sum: {sum_invalid}\n")