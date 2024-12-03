"""Test for day 3!
"""

from tobaggan_rental_shop import RentalShop


TEST_DATA = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
TEST_DATA2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

with open("d_03/challenge03.data", "r") as file:
    challenge03_data = file.read()


def main(data: str):
    toboggan = RentalShop(input_list=data)
    print("Parsed list: ", toboggan.input_list)
    print("Clean inputs: ", toboggan.clean_input)
    print("Score:", toboggan.mul_score)
    print("Score after removing bad instructions: ", toboggan.mul_score_dos)
    print("Using the splitting method for score: ", toboggan.mul_score_split_dos)


if __name__ == "__main__":
    main(data=TEST_DATA2)
    main(data=challenge03_data)
