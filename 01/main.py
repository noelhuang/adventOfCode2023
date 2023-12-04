from helpers.parsers import parse_txt_as_string
import re
# Parse txt file
input_string = parse_txt_as_string('input.txt')

word_num_map = {
    'one': 'o1ne',
    'two': 't2wo',
    'three': 't3hree',
    'four': 'f4our',
    'five': 'f5ive',
    'six': 's6ix',
    'seven': 's7even',
    'eight': 'e8ight',
    'nine': 'n9ine',
}

for key, value in word_num_map.items():
    input_string = input_string.replace(key, value)

raw_arr = input_string.split()
num_arr = []


# Part one
for item in raw_arr:
    # matches = []
    # for match in re.finditer(r'one|two|three|four|five|six|seven|eight|nine', item, re.IGNORECASE):
    #     matches.append(match)
    # if len(matches) > 1:
    #     last_word_start = matches[-1].start()
    #     last_word_end = matches[-1].end()
    #     item = item[0:last_word_start] + word_num_map[matches[-1][0]] + item[last_word_end:]
    # if len(matches) > 0:
    #     first_word_start = matches[0].start()
    #     first_word_end = matches[0].end()
    #     item = item[0:first_word_start] + word_num_map[matches[0][0]] + item[first_word_end:]
    print(item)
    # initialize variables
    first_digit = 0
    second_digit = 0
    for i in range(len(item)):
        if '0' <= item[i] <= '9':
            first_digit = item[i]
            break
    for i in range(len(item)-1, -1, -1):
        if '0' <= item[i] <= '9':
            second_digit = item[i]
            break
    combined_number = int(first_digit + second_digit)
    num_arr.append(combined_number)

print(sum(num_arr))