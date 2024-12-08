"""Who is he? The puzzler.
"""

from typing import List, Tuple

from enum import Enum


class Direction(Enum):
    "Using Compass Standard"
    WEST = 1
    SOUTHWEST = 2
    SOUTH = 3
    SOUTHEAST = 4
    EAST = 5
    NORTHEAST = 6
    NORTH = 7
    NORTHWEST = 8


class Puzzler:
    def __init__(self, input_data: str, sequence_to_find: str):
        self.input_data = input_data
        self.sequence_to_find = sequence_to_find
        self.lines_with_sublist = [
            list(line) for line in self.input_data.split()
        ]  # breaks characters to list for indexing

    async def convolve_left_to_right(
        self,
        input_lines: List[List[str]],
        sequence_to_find: str,
    ) -> Tuple[Tuple[int, int], Direction]:

        DIRECTIONS_TO_CHECK = [
            Direction.WEST,
            Direction.SOUTHWEST,
            Direction.SOUTH,
            Direction.SOUTHEAST,
            Direction.EAST,
            Direction.NORTHEAST,
            Direction.NORTH,
            Direction.NORTHWEST,
        ]
        matched_sequences = []

        for i in range(len(input_lines)):
            for j in range(len(input_lines[0])):
                position = (i, j)
                for direction in DIRECTIONS_TO_CHECK:
                    circled_word = self.get_sequence_by_direction(
                        input_lines=input_lines,
                        position=position,
                        direction=direction,
                        sequence_to_find=self.sequence_to_find,
                    )
                    if circled_word == sequence_to_find:
                        matched_sequences.append((position, direction))
        yield matched_sequences

    def get_sequence_by_direction(
        self,
        input_lines: List[List[str]],
        position: Tuple[int, int],
        direction: Direction,
        sequence_to_find: str,
    ):
        len_of_seq_to_find = len(sequence_to_find)
        row, col = position
        try:
            circled_word = ""
            if direction is Direction.WEST:
                for i in range(len_of_seq_to_find):
                    if col - i < 0:
                        raise IndexError("Index out of bounds stopping search")
                    circled_word += input_lines[row][col - i]
            if direction is Direction.SOUTHWEST:
                for i in range(len_of_seq_to_find):
                    if col - i < 0:
                        raise IndexError("Index out of bounds stopping search")
                    circled_word += input_lines[row + i][col - i]
            if direction is Direction.SOUTH:
                for i in range(len_of_seq_to_find):
                    circled_word += input_lines[row + i][col]
            if direction is Direction.SOUTHEAST:
                for i in range(len_of_seq_to_find):
                    circled_word += input_lines[row + i][col + i]
            if direction is Direction.EAST:
                for i in range(len_of_seq_to_find):
                    circled_word += input_lines[row][col + i]
            if direction is Direction.NORTHEAST:
                for i in range(len_of_seq_to_find):
                    if row - i < 0:
                        raise IndexError("Index out of bounds stopping search")
                    circled_word += input_lines[row - i][col + i]
            if direction is Direction.NORTH:
                for i in range(len_of_seq_to_find):
                    if row - i < 0:
                        raise IndexError("Index out of bounds stopping search")
                    circled_word += input_lines[row - i][col]
            if direction is Direction.NORTHWEST:
                for i in range(len_of_seq_to_find):
                    if col - i < 0:
                        raise IndexError("Index out of bounds stopping search")
                    if row - i < 0:
                        raise IndexError("Index out of bounds stopping search")
                    circled_word += input_lines[row - i][col - i]

        except IndexError as e:
            print("Index out of bounds stopping search :", e)
            return "OUT_OF_BOUNDS"

        return circled_word

    async def check_for_xmas(
        self, solutions: List[Tuple[Tuple[int, int], Direction]]
    ) -> List[Tuple[int, int]]:
        # crosses = []
        solutions = solutions
        for coords, direction in solutions:
            y, x = coords  # reversed if we think x = horizontal and y = vertical
            if direction is Direction.SOUTHWEST:
                for x_solution_coords, x_solution_dir in solutions:
                    if x_solution_dir is Direction.NORTHWEST and x_solution_coords == (
                        y + 2,
                        x,
                    ):
                        yield (y + 1, x - 1)
                    if x_solution_dir is Direction.SOUTHEAST and x_solution_coords == (
                        y,
                        x - 2,
                    ):
                        yield (y + 1, x - 1)
            if direction is Direction.SOUTHEAST:
                for x_solution_coords, x_solution_dir in solutions:
                    if x_solution_dir is Direction.NORTHEAST and x_solution_coords == (
                        y + 2,
                        x,
                    ):
                        yield (y + 1, x + 1)
                    if x_solution_dir is Direction.SOUTHWEST and x_solution_coords == (
                        y,
                        x + 2,
                    ):
                        yield (y + 1, x + 1)
            if direction is Direction.NORTHWEST:
                for x_solution_coords, x_solution_dir in solutions:
                    if x_solution_dir is Direction.NORTHEAST and x_solution_coords == (
                        y,
                        x - 2,
                    ):
                        yield (y - 1, x - 1)
                    if x_solution_dir is Direction.SOUTHWEST and x_solution_coords == (
                        y - 2,
                        x,
                    ):
                        yield (y - 1, x - 1)
            if direction is Direction.NORTHEAST:
                for x_solution_coords, x_solution_dir in solutions:
                    if x_solution_dir is Direction.NORTHWEST and x_solution_coords == (
                        y,
                        x + 2,
                    ):
                        yield (y - 1, x + 1)
                    if x_solution_dir is Direction.SOUTHEAST and x_solution_coords == (
                        y - 2,
                        x,
                    ):
                        yield (y - 1, x + 1)

        # set_of_solutions = set([xmas for xmas in crosses])
        # return list(set_of_solutions)
