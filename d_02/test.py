"""Test for day 2!
"""

from power_plant_historian import PowerPlantHistorian


TEST_DATA = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


TEST_DATA_2 = """
60 62 63 65 63 66 69 71
52 51 52 49 47 45
17 15 13 12 15 10
"""

with open("d_02/challenge02.data", "r") as file:
    challenge02_data = file.read()


def main(data: str):
    historian = PowerPlantHistorian(plant_list=data)
    print("Parsed plant list: ", historian.parsed_list)
    print("Is list safe: ", historian.is_list_safe)
    print("The count of safe reports: ", historian.count_of_safe)
    print(
        "The dampener made it so these reports were safe: ",
        historian.count_of_safe_dampened,
    )

    # print("Is Dampened List Safe: ", historian.is_dampened_list_safe)


if __name__ == "__main__":
    main(data=TEST_DATA)
    main(data=challenge02_data)
