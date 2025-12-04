def find_joltage(bank):
    max_first_entry = bank[0]
    max_first_entry_index = 0
    for i in range(1, len(bank)-1):
        if bank[i] > max_first_entry:
            max_first_entry = bank[i]
            max_first_entry_index = i
    max_second_entry= bank[max_first_entry_index+1]
    max_second_entry_index = max_first_entry_index+1
    for j in range(max_first_entry_index+1, len(bank)):
        if bank[j] > max_second_entry:
            max_second_entry = bank[j]
            max_second_entry_index = j
    return int(max_first_entry+max_second_entry)


if __name__ == "__main__":
    with open("day03_input.txt") as f:
        data = f.read()
        battery_banks = data.split('\n')
        output = 0
        for battery_bank in battery_banks:
            output+=find_joltage(battery_bank)
        print(output)