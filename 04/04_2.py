from helpers.parsers import parse_txt_as_string

parsed = parse_txt_as_string('input.txt')
parsed = parsed.strip().split('\n')
parsed = [parsed[i].split(': ')[1] for i in range(len(parsed))]

total_points = 0
winning_counts = []
for i, row in enumerate(parsed):
    winning_numbers = row.split('|')[0].split()
    my_numbers = row.split('|')[1].split()
    winning_numbers = [int(winning_numbers[i]) for i in range(len(winning_numbers))]
    my_numbers = [int(my_numbers[i]) for i in range(len(my_numbers))]

    number_map = {}  # key,value is winning_num, my_num
    for num in winning_numbers:
        number_map[num] = None
    for num in my_numbers:
        if num in number_map:
            number_map[num] = num
    winning_count = 0
    for key, value in number_map.items():
        if value is not None:
            winning_count += 1
    winning_counts.append(winning_count)


winning_counts = [[1, winning_counts[i]] for i in range(len(winning_counts))]

print(winning_counts)
total = 0
for i, row in enumerate(winning_counts):
    total += row[0]
    for j in range(i + 1, i + 1 + row[1]):
        winning_counts[j] = [winning_counts[j][0] + winning_counts[i][0], winning_counts[j][1]]
print(total)