from typing import List, Tuple
import re

# debug:

# edge cases not being handled:


# sum: 5 [60, 62, 63, 65, 63, 66, 69, 71] is Safe distance after removing element 3 False
# sum: 17 [52, 51, 52, 49, 47, 45] is Safe distance after removing element 2 False
# sum: 62 [17, 15, 13, 12, 15, 10] is Safe distance after removing element 2 False
class PowerPlantHistorian:

    def __init__(self, plant_list: str):
        self.plant_list = plant_list
        self.parsed_list = self.parse_plant_list(plant_list=self.plant_list)
        self.is_list_safe = self.check_list_if_safe(input_list=self.parsed_list)
        self.dampened_parsed_list = [
            self.dampener(input_list=pl, original_list_ok=line_safe)
            for pl, line_safe in zip(self.parsed_list, self.is_list_safe)
        ]
        self.count_of_safe = sum(self.is_list_safe)
        self.is_dampened_list_safe = self.check_list_if_safe(
            input_list=self.dampened_parsed_list
        )
        self.count_of_safe_dampened = sum(self.is_dampened_list_safe)

    def parse_plant_list(self, plant_list: str) -> List[List[int]]:
        split_lines = plant_list.splitlines()
        number_sequence = []
        for line in split_lines:
            sequence_of_numbers = line.split()
            try:
                assert len(sequence_of_numbers) > 0
            except AssertionError as e:
                print("Line is not a sequence of integers: ", e)
                continue  # skip the line
            sequence_of_numbers_int = [int(x) for x in sequence_of_numbers]
            number_sequence.append(sequence_of_numbers_int)
        return number_sequence

    def list_increasing(self, input_list: List[int]) -> List[bool]:
        return [a > b for a, b in zip(input_list, input_list[1:])]

    def list_decreasing(self, input_list: List[int]) -> List[bool]:
        return [a < b for a, b in zip(input_list, input_list[1:])]

    def list_change_within_threshold(
        self, input_list: List[int], at_most: int = 3
    ) -> List[bool]:
        return [abs(a - b) <= at_most for a, b in zip(input_list, input_list[1:])]

    def dampener(self, input_list: List[int], original_list_ok: bool) -> List[int]:
        if original_list_ok:
            return input_list
        else:
            for i in range(len(input_list)):
                new_list = input_list.copy()
                new_list.pop(i)
                check_if_list_ok = self.check_list_if_safe(input_list=[new_list])
                if check_if_list_ok[0]:
                    return new_list
                else:
                    continue
            if check_if_list_ok[0]:
                return new_list
            else:
                return input_list

    def check_list_if_safe(self, input_list: List[List[int]]) -> List[bool]:
        safe_for_each_line = []
        for line in input_list:
            increasing_conditions = self.list_increasing(line)
            decreasing_conditions = self.list_decreasing(line)
            changed_within_threshold = self.list_change_within_threshold(line)

            total_increasing = sum(increasing_conditions)
            total_decreasing = sum(decreasing_conditions)

            if total_increasing >= total_decreasing:
                increasing_or_decreasing = increasing_conditions
            else:
                increasing_or_decreasing = decreasing_conditions
            is_line_safe = [
                i_d and t
                for i_d, t in zip(increasing_or_decreasing, changed_within_threshold)
            ]
            safe_for_each_line.append(all(is_line_safe))

        return safe_for_each_line
