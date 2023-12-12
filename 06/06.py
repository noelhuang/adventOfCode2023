import math
from functools import reduce

from helpers.parsers import parse_txt_as_string

parsed = parse_txt_as_string('input.txt')
parsed = parsed.split('\n')
parsed = [parsed[i].split() for i in range(len(parsed))]
times = [int(parsed[0][i]) for i in range(1, len(parsed[0]))]
distances = [int(parsed[1][i]) for i in range(1, len(parsed[1]))]

print(times)
print(distances)

number_of_ways = []

for i in range(len(times)):
    t_total = times[i]
    distance = distances[i] + 0.0000000001
    t_charge_1 = math.ceil((-1*t_total + (t_total**2 - 4 * -1 * -1*distance)**0.5) / (2*-1))
    t_charge_2 = math.floor(((-1*t_total - (t_total**2 - 4 * -1 * -1*distance)**0.5) / (2*-1)))
    print(t_charge_1, t_charge_2)
    number_of_ways.append(t_charge_2 - t_charge_1 + 1)

print(number_of_ways)

print('res', reduce((lambda x, y: x * y), number_of_ways))