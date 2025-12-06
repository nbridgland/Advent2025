def compress_ranges(ranges):
    k = 0
    while k < len(ranges): # index on the length of the list so that I can change its entries
        j = k + 1
        while j < len(ranges): # compare against entries after
            # check for various kinds of overlap
            if ranges[k][0] <= ranges[j][0] <= ranges[k][1]:
                if ranges[k][1] <= ranges[j][1]:
                    ranges = ranges[:k] + [(ranges[k][0], ranges[j][1])] + ranges[k+1:j] + ranges[j+1:]
                    j -= 1
                else:
                    ranges = ranges[:k] + [(ranges[k][0], ranges[k][1])] + ranges[k+1:j] + ranges[j+1:]
                    j -= 1
            elif ranges[k][0] <= ranges[j][1] <= ranges[k][1]:
                if ranges[k][0] <= ranges[j][0]:
                    ranges = ranges[:k] + [(ranges[k][0], ranges[k][1])] + ranges[k+1:j] + ranges[j+1:]
                    j -= 1
                else:
                    ranges = ranges[:k] + [(ranges[j][0], ranges[k][1])] + ranges[k+1:j] + ranges[j+1:]
                    j -= 1
            elif ranges[j][0] <= ranges[k][0] <= ranges[j][1]:
                if ranges[j][1] <= ranges[k][1]:
                    ranges = ranges[:k] + [(ranges[j][0], ranges[k][1])] + ranges[k+1:j] + ranges[j+1:]
                    j -= 1
                else:
                    ranges = ranges[:k] + [(ranges[j][0], ranges[j][1])] + ranges[k+1:j] + ranges[j+1:]
                    j -= 1
            elif ranges[j][0] <= ranges[k][1] <= ranges[j][1]:
                if ranges[j][0] <= ranges[k][0]:
                    ranges = ranges[:k] + [(ranges[j][0], ranges[j][1])] + ranges[k+1:j] + ranges[j+1:]
                    j -= 1
                else:
                    ranges = ranges[:k] + [(ranges[k][0], ranges[j][1])] + ranges[k+1:j] + ranges[j+1:]
                    j -= 1
            j += 1
        k += 1
    return ranges



if __name__=='__main__':
    with open('day05_input.txt') as f:
        data = f.read()
    id_ranges, _ = data.split('\n\n')
    id_ranges = [id_range.split('-') for id_range in id_ranges.split('\n')]
    id_ranges = [(int(id_range[0]), int(id_range[1])) for id_range in id_ranges]
    current_length = len(id_ranges)
    id_ranges = compress_ranges(id_ranges)
    while len(id_ranges) < current_length:
        current_length = len(id_ranges)
        id_ranges = compress_ranges(id_ranges)
    count_fresh = 0
    for id_range in id_ranges:
        count_fresh += (max(id_range[1] - id_range[0], - 1) + 1)
    print(count_fresh)