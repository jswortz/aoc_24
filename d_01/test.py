"""Test for day 1!
"""

from d_01.historian import Historian


TEST_DATA = """
3   4
4   3
2   5
1   3
3   9
3   3
"""

with open("d_01/challenge01.data", "r") as file:
    challenge01_data = file.read()


def main(data: str):
    historian = Historian(text_list=data)
    print("Fist parsed list: ", historian.parsed_list1)
    print("Second parsed list: ", historian.parsed_list2)
    print("Distances sorted by minimum first: ", historian.pairwise_distances)
    print("Total Distance Between Lists: ", historian.total_distance)
    print("Similarity Score From Left to Right List: ", historian.similarity_score)


if __name__ == "__main__":
    main(data=TEST_DATA)
    main(data=challenge01_data)
