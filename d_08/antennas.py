from typing import List, Tuple, Dict
import asyncio
import itertools


TEST_DATA = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
with open("d_08/challenge08.data", "r") as file:
    challenge08_data = file.read()


def get_unique_frequencies(data: str) -> List[str]:
    output = []
    results = [line for line in data.splitlines() if line != ""]
    for line in results:
        if line == "":
            continue
        characters = [*line]
        characters_filtered = [x for x in characters if x != "."]
        if characters_filtered != []:
            output.extend(characters_filtered)
    return list(set(output))


def get_antinode(node_one: List[List[int]], node_two: List[List[int]]) -> List[int]:
    run = node_one[1] - node_two[1]
    rise = node_one[0] - node_two[0]
    antinode_location = [rise + node_one[0], run + node_one[1]]
    return antinode_location


def get_antinode_multiple(
    node_one: List[List[int]], node_two: List[List[int]], max_x: int, max_y: int
) -> List[List[int]]:
    antinode_locations = []
    run = node_one[1] - node_two[1]
    rise = node_one[0] - node_two[0]
    antinode_location = [rise + node_one[0], run + node_one[1]]
    antinode_locations.append(node_two)
    antinode_locations.append(antinode_location)
    while (
        antinode_location[0] > -1
        and antinode_location[1] > -1
        and antinode_location[0] <= max_y
        and antinode_location[1] <= max_x
    ):
        antinode_location = [rise + antinode_location[0], run + antinode_location[1]]
        antinode_locations.append(antinode_location)
    return antinode_locations


async def get_and_iterate_over_freq_combos(antenna_map: Dict[str, List[int]]):
    for frequency in antenna_map.keys():
        antennas = antenna_map[frequency]
        for antenna_one in antennas:
            for antenna_two in antennas:
                if antenna_one == antenna_two:
                    continue
                yield get_antinode(node_one=antenna_one, node_two=antenna_two)


async def get_and_iterate_over_freq_combos_multiple(
    antenna_map: Dict[str, List[int]], max_x: int, max_y: int
):
    for frequency in antenna_map.keys():
        antennas = antenna_map[frequency]
        for antenna_one in antennas:
            for antenna_two in antennas:
                if antenna_one == antenna_two:
                    continue
                yield get_antinode_multiple(
                    node_one=antenna_one, node_two=antenna_two, max_x=max_x, max_y=max_y
                )


def parse_data(data: str) -> Dict[str, List[int]]:
    unique_frequencies = get_unique_frequencies(data)
    antenna_map = {freq: [] for freq in unique_frequencies}
    data_filtered = data.splitlines()
    data_filtered = [x for x in data.splitlines() if x != ""]
    for freq in unique_frequencies:
        for i, line in enumerate(data_filtered):
            for j, char in enumerate([*line]):
                if char == freq:
                    antenna_map[freq].append([i, j])
    return antenna_map, i, j  # max bounds for later


async def main(data: str):
    parsed_data, max_y, max_x = parse_data(data)
    print("Parsed data: ", parsed_data)
    anti_node_unfiltered = []
    async for anti_node in get_and_iterate_over_freq_combos(antenna_map=parsed_data):
        if anti_node[0] <= max_y and anti_node[1] <= max_x:
            if anti_node[0] > -1 and anti_node[1] > -1:
                anti_node_unfiltered.append(anti_node)
    print("Unfiltered anti node locations :", anti_node_unfiltered)
    unique_set_of_anti_nodes = set(str(x) for x in anti_node_unfiltered)
    print("Unique antinode locations: ", unique_set_of_anti_nodes)
    print("Total anti-nodes: ", len(unique_set_of_anti_nodes))

    anti_node_unfiltered2 = []
    async for list_of_antinodes in get_and_iterate_over_freq_combos_multiple(
        antenna_map=parsed_data, max_x=max_x, max_y=max_y
    ):
        filtered_antinodes = [
            x
            for x in list_of_antinodes
            if x[0] > -1 and x[1] > -1 and x[0] <= max_y and x[1] <= max_x
        ]
        anti_node_unfiltered2.extend(filtered_antinodes)

        unique_set_of_anti_nodes2 = set(str(x) for x in anti_node_unfiltered2)
        print("Unique antinode locations: ", unique_set_of_anti_nodes2)
        print("Total anti-nodes: ", len(unique_set_of_anti_nodes2))


if __name__ == "__main__":
    asyncio.run(main(data=TEST_DATA))
    asyncio.run(main(data=challenge08_data))
