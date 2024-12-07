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
