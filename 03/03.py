from helpers.parsers import parse_txt_as_string
import re

parsed = parse_txt_as_string('input.txt')
parsed = parsed.strip()
parsed = parsed.split('\n')


def check_surroundings(i, j, input_grid):
    '''
    return true if any of the surrounding characters is a symbol
    :param i:
    :param j:
    :param input_grid:
    :return:
    '''
    max_i = len(input_grid) - 1
    max_j = len(input_grid[0]) - 1
    offsets = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]  # col, row offsets
    for offset in offsets:
        col_offset = offset[0]
        row_offset = offset[1]
        if 0 <= i + row_offset <= max_i and 0 <= j + col_offset <= max_j:
            scanned_char = input_grid[i + row_offset][j + col_offset]
            if scanned_char not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
                # we found a symbol
                return True
    return False


# print(check_surroundings(4, 2, input_grid=parsed))

# iterate over each char, if it is a number first finish building the complete number, then for each complete number check its surroundings
# if the complete number is next to a symbol, add it to the sum
total = 0
for i, row in enumerate(parsed):
    matches = re.finditer(r"\d+", row)
    for match in matches:
        is_complete_number_next_to_symbol = False
        for j in range(match.span()[0], match.span()[1]):  # for every col in the match
            is_char_next_to_symbol = check_surroundings(i, j, parsed)
            if is_char_next_to_symbol:
                is_complete_number_next_to_symbol = True
        if is_complete_number_next_to_symbol:
            total += int(match.group(0))
print(total)
