from typing import List, Tuple, Dict, Set
import asyncio
import itertools
from tqdm import tqdm  # poetry add tqdm

TEST_DATA = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


with open("d_07/challenge07.data", "r") as file:
    challenge07_data = file.read()


class Calibration:

    def __init__(self, data: str):
        self.data = data
        self.parsed_data = self._parse_data(self.data)

    async def assess_operator_combo(
        self, operator_combo: List[str], input_data: List[int], answer: int
    ):
        output_data = input_data
        while len(output_data) > 1:
            for operator in operator_combo:
                if operator == "add":
                    output_data = self.add(output_data)
                if operator == "mul":
                    output_data = self.mul(output_data)
                if operator == "||":
                    output_data = self.cat(output_data)
            if len(output_data) == 1:
                final_value = output_data[0]
                is_final_value_an_answer = final_value == answer
                # print(
                #     f"Final Value: ",
                #     final_value,
                #     "\nTrue Answer: ",
                #     final_value,
                #     is_final_value_an_answer,
                # )
                yield is_final_value_an_answer

    def _parse_data(self, data: str) -> List[Tuple[int, List[int]]]:
        output = []
        for line in data.splitlines():
            if line == "":
                continue
            k_v = line.split(":")
            k = int(k_v[0])
            v = [int(v) for v in k_v[1].split(" ") if v != ""]
            output.append((k, v))
        return output

    async def get_all_operator_combos_per_line(
        self, line: List[int]
    ) -> List[Tuple[str]]:
        operators = ["add", "mul", "||"]
        # combinations = []
        n_operators = len(line) - 1
        operator_cartesian_prod = [operators for _ in range(n_operators)]
        for combination in itertools.product(*operator_cartesian_prod):
            yield combination
        #     combinations.append(combination)
        # return combinations  # get a list of all permutations

    def add(self, data: List[int]) -> List[int]:
        LHS = data.pop(0)
        data[0] += LHS
        return data

    def mul(self, data: List[int]) -> List[int]:
        LHS = data.pop(0)
        data[0] *= LHS
        return data

    def cat(self, data: List[int]) -> List[int]:
        LHS = data.pop(0)
        data[0] = int(str(LHS) + str(data[0]))
        return data


async def main(data: str):
    print("Initializing Calibration")
    calibration = Calibration(data=data)
    operator_combos = []
    calibration_result = 0
    for answer, line in tqdm(calibration.parsed_data):
        valid_combos = []
        bool_results = []
        async for op_combo in calibration.get_all_operator_combos_per_line(line):
            # find valid operator combos
            line_copy = line.copy()
            async for op_combo_valid_check in calibration.assess_operator_combo(
                op_combo, line_copy, answer
            ):
                bool_results.append(op_combo_valid_check)
                if op_combo_valid_check:
                    valid_combos.append(f"({operator_combos}, {line}, {answer}")
                    break
        is_line_valid = any(bool_results)
        if is_line_valid:
            calibration_result += answer
    print(f"Valid Combos: {valid_combos} \nCalibration Result: {calibration_result}")
    print("done!")


if __name__ == "__main__":
    asyncio.run(main(data=TEST_DATA))
    asyncio.run(main(data=challenge07_data))
