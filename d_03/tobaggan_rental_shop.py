from typing import List, Tuple
import re


class RentalShop:

    def __init__(self, input_list: str):
        self.input_list = input_list
        self.clean_input = self.parse_input(self.input_list)
        self.mul_score = self.get_parsed_list_score(self.clean_input)
        self.input_with_clean_dos = self.filter_donts(self.input_list)
        self.clean_input_dos = self.parse_input(self.input_with_clean_dos)
        self.mul_score_dos = self.get_parsed_list_score(self.clean_input_dos)
        self.split_clean_input = self.filter_by_splitting(self.input_list)
        self.clean_split_inputs_dos = self.parse_input(self.split_clean_input)
        self.mul_score_split_dos = self.get_parsed_list_score(
            self.clean_split_inputs_dos
        )

    def parse_input(self, text_lines: str) -> List[List[List[int]]]:
        split_lines = text_lines.splitlines()
        output_lines = []
        for line in split_lines:
            mul_matches = re.findall(r"mul\(\d+,\d+\)", line)
            mul_pairs = [re.findall(r"\d+,\d+", x) for x in mul_matches]
            clean_mul_paris = [[int(y) for y in x[0].split(",")] for x in mul_pairs]
            output_lines.append(clean_mul_paris)
        return output_lines

    def get_parsed_list_score(self, parsed_list: List[List[List[int]]]) -> List[int]:
        line_score = []
        line_sum = 0
        for parsed_input_line in parsed_list:
            for mul_pair in parsed_input_line:
                assert len(mul_pair) == 2
                multiplications = mul_pair[0] * mul_pair[1]
                line_sum += multiplications
            line_score.append(line_sum)
        return line_sum

    def filter_by_splitting(self, input_list: str) -> str:
        split_dos = input_list.split("do()")
        split_donts = [do.split("don't()")[0] for do in split_dos]
        return "".join(split_donts)

    def filter_donts(self, input_list: str) -> str:
        REGEX = r"don\'t\(\)(.+?)do\(\)"
        REGEX_EOL = (
            r"don\t\(\)(.+?)$"  # grabs all if don't is enabled through end of line
        )
        new_list = re.sub(REGEX, "", input_list)
        new_list = re.sub(REGEX_EOL, "", new_list)
        return new_list
        # bad_muls = re.findall(REGEX, input_list)
        # bad_muls_eol = re.findall(REGEX_EOL, input_list)
        # new_output = input_list
        # if len(bad_muls) == 0 and len(bad_muls_eol) == 0:
        #     return input_list
        # else:
        #     if len(bad_muls) > 0:
        #         for bm in bad_muls:
        #             new_output = new_output.replace(bm, "")

        #     if len(bad_muls_eol) > 0:
        #         for bm in bad_muls_eol:
        #             new_output = new_output.replace(bm, "")

        #     return new_output
