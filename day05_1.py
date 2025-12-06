if __name__=='__main__':
    with open('day05_input.txt') as f:
        data = f.read()
    ranges, id_list = data.split('\n\n')
    ranges = [id_range.split('-') for id_range in ranges.split('\n')]
    id_list = id_list.split('\n')
    fresh_count = 0
    for item_id in id_list:
        for id_range in ranges:
            if int(id_range[0]) <= int(item_id) <= int(id_range[1]):
                fresh_count += 1
                break
    print(fresh_count)
