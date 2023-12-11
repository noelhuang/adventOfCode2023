from helpers.parsers import parse_txt_as_string

parsed = parse_txt_as_string('input.txt')
parsed = parsed.split("\n\n")
parsed = [parsed[i].split('\n') for i in range(len(parsed))]


# Make hashmaps where key = (source start, source end) and value = (destination start, destination end)
# Note that input is given in [destination, source, range]
seeds = parsed[0][0].split(':')[1].strip().split(' ')
seeds = [int(seeds[i]) for i in range(len(seeds))]
seeds_ranges = []
for i in range(0, len(seeds), 2):
    seeds_ranges.append((seeds[i], seeds[i] + seeds[i+1] - 1))
print('seeds ranges', seeds_ranges)


def parsed_to_arrays(parsed, j):
    rows = parsed[j][1:]
    rows = [rows[i].split(' ') for i in range(len(rows))]
    rows = [[int(row[i]) for i in range(len(row))] for row in rows]
    return rows


def array_to_map(my_array, my_map):
    for row in my_array:
        my_map[(row[1], row[1] + row[2] - 1)] = (row[0], row[0] + row[2] - 1)
    return my_map


seed_soils = parsed_to_arrays(parsed, 1)
soil_ferts = parsed_to_arrays(parsed, 2)
fert_waters = parsed_to_arrays(parsed, 3)
water_lights = parsed_to_arrays(parsed, 4)
light_temps = parsed_to_arrays(parsed, 5)
temp_humis = parsed_to_arrays(parsed, 6)
humi_locations = parsed_to_arrays(parsed, 7)

seed_soil_map = {}
soil_fert_map = {}
fert_water_map = {}
water_light_map = {}
light_temp_map = {}
temp_humi_map = {}
humi_location_map = {}

array_to_map(seed_soils, seed_soil_map)
array_to_map(soil_ferts, soil_fert_map)
array_to_map(fert_waters, fert_water_map)
array_to_map(water_lights, water_light_map)
array_to_map(light_temps, light_temp_map)
array_to_map(temp_humis, temp_humi_map)
array_to_map(humi_locations, humi_location_map)




def translate(number, my_map):
    for key, value in my_map.items():
        if key[1] >= number >= key[0]:
            offset = number - key[0]
            output = value[0] + offset
            return output
    return number


# This function needs to accept ranges of values, and then output ranges on values based on the my_map (dict)
def map_step(ranges, my_map):
    """

    :param ranges: array of tuples [(range start, range end), (start, end), ... etc]
    :param my_map: map that acts as 'sieve' for the array of tuples
    """
    output_ranges = []
    # for my_range in ranges():
    while len(ranges) > 0:
        my_range = ranges.pop()
        has_matched = False
        for source_range, destination_range in my_map.items():
            # If the given range is fully inside the source ranges, just translate the complete range
            if (source_range[0] <= my_range[0] <= source_range[1]) and (source_range[0] <= my_range[1] <= source_range[1]):
                output_ranges.append((translate(my_range[0], my_map), translate(my_range[1], my_map)))
                has_matched = True
            # If only the first part of the given range is inside the source range, slice the range and that partial
            elif (source_range[0] <= my_range[0] <= source_range[1]) and not (source_range[0] <= my_range[1] <= source_range[1]):
                output_ranges.append((translate(my_range[0], my_map), translate(source_range[1], my_map)))
                ranges.append((source_range[1] + 1, my_range[1]))
                has_matched = True
            # If only the second part of the given range is inside the source range, slice the range
            elif (source_range[0] <= my_range[1] <= source_range[1]) and not (source_range[0] <= my_range[0] <= source_range[1]):
                output_ranges.append((translate(source_range[0], my_map), translate(my_range[1], my_map)))
                ranges.append((my_range[0], source_range[0] - 1))
                has_matched = True
            # If my range is larger than the source range, translate only the middle part and push the left and right sides
            elif my_range[0] < source_range[0] and my_range[1] > source_range[1]:
                output_ranges.append((translate(source_range[0], my_map), translate(source_range[1], my_map)))
                ranges.append((my_range[0], source_range[0] - 1))  # append left side overshoot
                ranges.append((source_range[1] + 1, my_range[1]))  # append right side overshoot
                has_matched = True
        # If my range does not have any overlap with the source range, mark it as such so we can push it to the output as is at the end of all iterations
        if not has_matched:
            output_ranges.append((my_range[0], my_range[1]))
    # print(output_ranges)
    return output_ranges


def all_maps(seed_ranges):
    res = map_step(seed_ranges, seed_soil_map)
    res = map_step(res, soil_fert_map)
    res = map_step(res, fert_water_map)
    res = map_step(res, water_light_map)
    res = map_step(res, light_temp_map)
    res = map_step(res, temp_humi_map)
    res = map_step(res, humi_location_map)
    return res


# print(all_maps(seeds_ranges))
answer_array = all_maps(seeds_ranges)
print('answer array', answer_array)

my_locations = []
for location_range in answer_array:
    my_locations.append(location_range[0])
    my_locations.append(location_range[1])

# 30879028 is wrong
print('my_locs', my_locations)
print('test', min(my_locations))
