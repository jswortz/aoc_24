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


def main(data: str):
    puzzler = Puzzler(input_data=data, sequence_to_find="MAS")
    print("Parsed input: ", puzzler.lines_with_sublist)
    print("Sequence to find: ", puzzler.sequence_to_find)
    # print(
    #     f"""Solutions found: {puzzler.solutions}

    #     Number of Solutions: {len(puzzler.solutions)}"""
    # )
    print(
        f"""Xmases found: {puzzler.set_of_xmas_points}, 
        
        A total of {len(puzzler.set_of_xmas_points)}"""
    )


if __name__ == "__main__":
    # main(data=TEST_DATA)
    main(data=TEST_DATA2)
    main(data=challenge03_data)
