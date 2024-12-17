"""Test for day 6!
"""

import asyncio
from guard_maze import Guard
from typing import Tuple, List

TEST_DATA = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


with open("d_06/challenge06.data", "r") as file:
    challenge06_data = file.read()


async def get_guard_path_based_on_obstacle(
    data: str, obstacle_locs: List[Tuple[int, int]]
):
    for obstacle_placed in obstacle_locs:
        guard_with_obstacle = Guard(init_data=data, add_obstacle=obstacle_placed)
        if guard_with_obstacle.still_on_map:
            yield guard_with_obstacle


async def main(data: str):
    guard = Guard(init_data=data)
    print("Parsed maze instructions: ", guard.parsed_input_data)
    print("init_guard_location: ", guard.init_guard_location)
    # still_on_map = True
    # guard_telemetry = []
    # guard_orientation = guard.guard_orientation
    # guard_position = guard.init_guard_location
    # guard_telemetry.append(guard_position)
    # while still_on_map:
    #     next_location_info = guard.find_guard_next_pos(
    #         guard_pos=guard_position, guard_orientation=guard_orientation
    #     )
    #     still_on_map = next_location_info["still_on_map"]
    #     if not still_on_map:
    #         break
    #     guard_telemetry.append(next_location_info["new_position"])
    #     guard_position = next_location_info["new_position"]
    #     guard_orientation = next_location_info["new_orientation"]
    print("Guard coords until left map: ", guard.guard_path)
    print("No. of distinct positions the guard walked: ", len(set(guard.guard_path)))
    obstacle_list = []
    for y in range(guard.max_y):
        for x in range(guard.max_x):
            obstacle_list.append((y, x))
    guards = []
    async for guard in get_guard_path_based_on_obstacle(
        data=data, obstacle_locs=obstacle_list
    ):
        guards.append(guard)
    distinct_obstacle_locations = set([guard.add_obstacle for guard in guards])
    # guards_stuck_in_loop = [guard for guard in guards if guard.still_on_map]
    print("Number of guards stuck in a loop: ", len(guards))
    print(
        "Number of distinct locations w/ stuck in a loop: ",
        len(distinct_obstacle_locations),
    )


if __name__ == "__main__":
    asyncio.run(main(data=TEST_DATA))
    asyncio.run(main(data=challenge06_data))
    print("done!")
