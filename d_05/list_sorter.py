from typing import List, Tuple


class ListSorter:

    def __init__(self, input_data: str):
        self.input_data = input_data
        self.sorting_instructions, self.pages_to_update = self.parse_input_data(
            input_data=self.input_data
        )

    def parse_input_data(
        self, input_data: str
    ) -> Tuple[List[List[int]], List[List[int]]]:
        sorting_instructions = []
        pages_to_update = []
        for line in input_data.split():
            if "|" in line:
                instruction = [int(x) for x in line.split("|")]
                sorting_instructions.append(instruction)
            elif line == "":
                continue
            else:
                pages = [int(x) for x in line.split(",")]
                pages_to_update.append(pages)

        return sorting_instructions, pages_to_update

    def check_instructions(self, line: List[int], instruction: List[int]):
        """
        Returns true if rules are followed
        Stops iteration early and returns False if rules broken
        """
        rule_1_pos = -1  # initialize the values
        rule_2_pos = -1  # initialize the values
        rule1, rule2 = instruction[0], instruction[1]
        for i, val in enumerate(line):
            if val == rule1:
                rule_1_pos = i
                if rule_2_pos != -1 and rule_1_pos > rule_2_pos:
                    return False
            elif val == rule2:
                rule_2_pos = i
                if rule_1_pos != -1 and rule_1_pos > rule_2_pos:
                    return False
        return True

    async def filter_bad_sorts(
        self, data: List[List[int]], instructions: List[List[int]]
    ):
        for line in data:
            for instruction in instructions:
                is_line_ok = self.check_instructions(line=line, instruction=instruction)
                if not is_line_ok:
                    break  # skip the line
            if not is_line_ok:
                continue
            yield line

    def find_middle_value(self, list: List[int]) -> int:
        middle_index = int((len(list) - 1) / 2)
        return list[middle_index]

    def reorder_list(self, line: List[int], instruction: List[int]):
        rule_1_pos = -1  # initialize the values
        rule_2_pos = -1  # initialize the values
        rule1, rule2 = instruction[0], instruction[1]
        reordered_list = line.copy()  # init a copy to reorder
        for i, val in enumerate(line):
            if val == rule1:
                rule_1_pos = i
            elif val == rule2:
                rule_2_pos = i
            if rule_2_pos != -1 and rule_1_pos > rule_2_pos:
                # something that should go earlier is later
                reordered_list[rule_2_pos] = rule1
                reordered_list[rule_1_pos] = rule2
                return (
                    reordered_list,
                    False,
                )  # this will tell us to keep going for sorts
        return reordered_list, True
