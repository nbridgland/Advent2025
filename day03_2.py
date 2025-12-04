def find_joltage(bank):
    output_string = ''
    last_index = -1
    for k in range(12):
        max_entry = '0'
        for i in range(last_index+1, len(bank)-(12-k-1)):
            if bank[i] > max_entry:
                max_entry = bank[i]
                last_index = i
        output_string += str(max_entry)
    return int(output_string)


if __name__ == "__main__":
    with open("day03_input.txt") as f:
        data = f.read()
        battery_banks = data.split('\n')
        output = 0
        for battery_bank in battery_banks:
            output+=find_joltage(battery_bank)
        print(output)