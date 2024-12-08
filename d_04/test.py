"""Test for day 4!
"""

from the_puzzler import Puzzler
import asyncio

TEST_DATA = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

TEST_DATA2 = """
.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
"""


with open("d_04/challenge04.data", "r") as file:
    challenge03_data = file.read()


async def main(data: str):
    puzzler = Puzzler(input_data=data, sequence_to_find="MAS")
    print("Parsed input: ", puzzler.lines_with_sublist)
    print("Sequence to find: ", puzzler.sequence_to_find)

    solutions = []
    async for solution in puzzler.convolve_left_to_right(
        input_lines=puzzler.lines_with_sublist,
        sequence_to_find=puzzler.sequence_to_find,
    ):
        solutions.extend(solution)

    xmas_points = []
    async for xmas_point in puzzler.check_for_xmas(solutions):
        xmas_points.append(xmas_point)
    set_of_xmas_points = set(xmas_points)
    print(
        f"""Xmases found: {set_of_xmas_points}, 
        
        A total of {len(set_of_xmas_points)}"""
    )


if __name__ == "__main__":
    # main(data=TEST_DATA)
    asyncio.run(main(data=TEST_DATA2))
    asyncio.run(main(data=challenge03_data))
    print("done!")
