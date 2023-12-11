from helpers.parsers import parse_txt_as_string

parsed = parse_txt_as_string('input.txt')
parsed = parsed.split("\n\n")
parsed = [parsed[i].split('\n') for i in range(len(parsed))]
print(parsed)

# Make hashmaps where key = (source start, source end) and value = (destination start, source end)
# Note that input is given in [destination, source, range]
seeds = parsed[0][0].split(':')[1].strip().split(' ')
seeds = [int(seeds[i]) for i in range(len(seeds))]


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

print(seed_soil_map)


def map_step(number, my_map):
    for key, value in my_map.items():
        if key[1] >= number >= key[0]:
            offset = number - key[0]
            output = value[0] + offset
            return output
    return number

print(map_step(2053199047, seed_soil_map))