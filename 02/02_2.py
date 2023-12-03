from helpers.parsers import parse_txt_as_string

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
    max_cubes = {
        'red': [0],
        'green': [0],
        'blue': [0]
    }
    for j, subgame in enumerate(game): # for every subgame
        subgame_split = subgame.strip().split(', ')
        for k, amountcolor in enumerate(subgame_split):
            amount, color = amountcolor.split(' ')
            print(color)
            max_cubes[color].append(int(amount))
    # after all subgames in a game, look for the max number of cubes in each color of the game and multiply them
    total += max(max_cubes['red']) * max(max_cubes['green']) * max(max_cubes['blue'])

print(total)