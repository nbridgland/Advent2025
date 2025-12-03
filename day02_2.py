def check_pattern_length(input_string, length):
    pattern = input_string[:length]
    k = 1
    while k < len(input_string) / length:
        if input_string[length * k:length * (k + 1)] != pattern:
            return False
        k += 1
    return True

def find_repeated_patterns(input_string):
    for i in range(1, len(input_string)):
        if len(input_string) % i == 0:
            if check_pattern_length(input_string, i):
                return True
    return False

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
                if find_repeated_patterns(str(current_id)):
                    sum_invalid += current_id
                current_id += 1
        print(f"Sum: {sum_invalid}\n")