"""Test for day 5!
"""

import asyncio
from list_sorter import ListSorter


TEST_DATA = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


with open("d_05/challenge05.data", "r") as file:
    challenge05_data = file.read()


async def main(data: str):
    sorter = ListSorter(input_data=data)
    print("Parsed sorting instructions: ", sorter.sorting_instructions)
    print("Parsed pages to update : ", sorter.pages_to_update)
    ok_lines = []
    async for ok_line in sorter.filter_bad_sorts(
        data=sorter.pages_to_update, instructions=sorter.sorting_instructions
    ):
        ok_lines.append(ok_line)
    print(f"Lines that meet the sorting criteria: {ok_lines}")
    print(f"Total good lines: {len(ok_lines)}")
    ok_middles = [sorter.find_middle_value(list=x) for x in ok_lines]
    print(f"The sum of the OK lines: {sum(ok_middles)}")
    # pt2
    not_ok_lines = [x for x in sorter.pages_to_update if x not in ok_lines]
    reordered_not_ok_lines = []

    for not_ok in not_ok_lines:
        keep_sorting = True
        while keep_sorting is True:
            line_ok_checks = []
            for instruction in sorter.sorting_instructions:
                not_ok, line_ok = sorter.reorder_list(
                    line=not_ok, instruction=instruction
                )  # mutate rule-by-rule
                line_ok_checks.append(line_ok)
            keep_sorting = not all(line_ok_checks)
        reordered_not_ok_lines.append(not_ok)
    print("Sorted not ok lists: ", reordered_not_ok_lines)
    fixed_middles = [sorter.find_middle_value(list=x) for x in reordered_not_ok_lines]
    print("Sum of the fixed line middle values: ", sum(fixed_middles))


if __name__ == "__main__":
    asyncio.run(main(data=TEST_DATA))
    asyncio.run(main(data=challenge05_data))
    print("done!")
