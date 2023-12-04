from helpers.parsers import parse_txt_as_string

# Maximum cube amounts
max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# General parsing
parsed_input = parse_txt_as_string('input.txt')
parsed_input = parsed_input.strip()
parsed_input = parsed_input.split('\n')

# Remove the 'Game: ' substring
for i in range(len(parsed_input)):
    if 'Game' in parsed_input[i]:
        parsed_input[i] = parsed_input[i].split(': ')[1]

# Split the subgames within one game
parsed_input = [parsed_input[i].split(';') for i in range(len(parsed_input))]

total = 0

# Loop over every subgame, check if it violates any max_cubes. If no violations, we can add the GameID to the total.
for i, game in enumerate(parsed_input): # for every game
    is_possible = True
    for j, subgame in enumerate(game): # for every subgame
        subgame_split = subgame.strip().split(', ')
        for k, amountcolor in enumerate(subgame_split):
            amount, color = amountcolor.split(' ')
            if int(amount) > max_cubes[color]: # if amount > max_cubes, the game is no longer possible
                is_possible = False
    # if every subgame is possible, add the game ID to the sum
    if is_possible:
        total += i + 1

print(total)