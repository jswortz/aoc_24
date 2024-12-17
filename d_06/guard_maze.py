from typing import List, Tuple, Dict


class Guard:
    # If there is something directly in front of you, turn right 90 degrees.
    # Otherwise, take a step forward.
    def __init__(self, init_data: str, add_obstacle: Tuple[int, int] = None):
        self.init_data = init_data
        self.add_obstacle = add_obstacle
        self.parsed_input_data = self.parse_input_data(input_data=self.init_data)
        self.init_guard_location = self.find_guard_init_pos(
            parsed_input_data=self.parsed_input_data
        )
        if add_obstacle is not None and add_obstacle != self.init_guard_location:
            self.parsed_input_data = self.add_obstacle_to_data(
                data=self.parsed_input_data, location=self.add_obstacle
            )
        self.guard_orientation = "North"  # North, South, East, West
        self.max_y = len(self.parsed_input_data)
        self.max_x = len(self.parsed_input_data[0])

        self.guard_path, self.still_on_map = self.get_path()

    def parse_input_data(self, input_data: str) -> List[List[str]]:
        return [[*x] for x in input_data.split()]

    def find_guard_init_pos(
        self, parsed_input_data: List[List[str]]
    ) -> Tuple[int, int]:
        for y, horizontal_line in enumerate(parsed_input_data):
            for x, vertical_char in enumerate(horizontal_line):
                if vertical_char == "^":  # found him!
                    return x, y

    def find_guard_next_pos(
        self,
        guard_pos: Tuple[int, int],
        guard_orientation: str,
        # parsed_input_data: List[List[str]],
        barrier_chars: List[str] = ["#"],
    ) -> Dict:
        still_on_map = True
        x_guard, y_guard = guard_pos
        if guard_orientation == "North":
            maybe_new_x, maybe_new_y = (x_guard, y_guard - 1)
            if y_guard - 1 < 0:
                still_on_map = False
        elif guard_orientation == "South":
            maybe_new_x, maybe_new_y = (x_guard, y_guard + 1)
        elif guard_orientation == "East":
            maybe_new_x, maybe_new_y = (x_guard + 1, y_guard)
        elif guard_orientation == "West":
            maybe_new_x, maybe_new_y = (x_guard - 1, y_guard)
            if x_guard - 1 < 0:
                still_on_map = False
        else:
            maybe_new_x, maybe_new_y = (x_guard, y_guard - 1)
        try:  # try to catch list index exception to know when guard has left the maze
            if (
                self.parsed_input_data[maybe_new_y][maybe_new_x] in barrier_chars
            ):  # turn right!
                if guard_orientation == "North":
                    guard_orientation = "East"
                    maybe_new_x, maybe_new_y = (x_guard + 1, y_guard)
                elif guard_orientation == "South":
                    guard_orientation = "West"
                    maybe_new_x, maybe_new_y = (x_guard - 1, y_guard)
                    if (
                        x_guard - 1 < 0
                    ):  # take care of subtractions for negatives (we don't want the end of the list)
                        still_on_map = False
                elif guard_orientation == "East":
                    guard_orientation = "South"
                    maybe_new_x, maybe_new_y = (x_guard, y_guard + 1)
                elif guard_orientation == "West":
                    guard_orientation = "North"
                    maybe_new_x, maybe_new_y = (x_guard, y_guard - 1)
                    if y_guard - 1 < 0:
                        still_on_map = False
        except IndexError as e:
            print("That's it, he's off the map!", e)
            still_on_map = False
        return {
            "new_position": (maybe_new_x, maybe_new_y),
            "new_orientation": guard_orientation,
            "still_on_map": still_on_map,
        }

    def get_path(self, max_iter: int = 400) -> Tuple[Dict, bool]:
        i = 0
        still_on_map = True
        guard_telemetry = []
        guard_orientation = self.guard_orientation
        guard_position = self.init_guard_location
        guard_telemetry.append(guard_position)
        while still_on_map:
            i += 1
            next_location_info = self.find_guard_next_pos(
                guard_pos=guard_position, guard_orientation=guard_orientation
            )
            still_on_map = next_location_info["still_on_map"]
            if not still_on_map or i > max_iter:
                break
            guard_telemetry.append(next_location_info["new_position"])
            guard_position = next_location_info["new_position"]
            guard_orientation = next_location_info["new_orientation"]
            if (
                guard_position == self.init_guard_location
                and guard_orientation == self.guard_orientation
            ):
                break
        return guard_telemetry, still_on_map

    def add_obstacle_to_data(self, data, location: Tuple[int, int]):
        input_data = data
        y, x = location
        input_data[y][x] = "#"
        return input_data
