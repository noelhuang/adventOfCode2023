from helpers.parsers import parse_txt_as_string
import re
# Parse txt file
input_string = parse_txt_as_string('01/input.txt')

word_num_map = {
    'one' : '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

raw_arr = input_string.split()
num_arr = []


# Part one
for item in raw_arr:
    matches = []
    for match in re.finditer(r'one|two|three|four|five|six|seven|eight|nine', item, re.IGNORECASE):
        matches.append(match)
    first_word = matches[0].start()
    last_word = matches[-1].start()
    print(first_word)
    print(last_word)
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