"""Test for day 5!
"""

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


def main(data: str):
    sorter = ListSorter(input_data=data)
    print("Parsed sorting instructions: ", sorter.sorting_instructions)
    print("Parsed pages to update : ", sorter.pages_to_update)

    # print("Is Dampened List Safe: ", historian.is_dampened_list_safe)


if __name__ == "__main__":
    main(data=TEST_DATA)
    # main(data=challenge05_data)
