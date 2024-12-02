from typing import List, Tuple
import re


class Historian:

    def __init__(self, text_list: str):
        self.text_list = text_list
        self.parsed_list1, self.parsed_list2 = self.parse_text_list()
        self.pairwise_distances = self.pairwise_distances_between_lists(
            list1=self.parsed_list1, list2=self.parsed_list2
        )
        self.total_distance = sum(self.pairwise_distances)
        self.similarity_scores = self.compute_similarity_scores(
            left_list=self.parsed_list1, right_list=self.parsed_list2
        )
        self.similarity_score = sum(self.similarity_scores)

    def parse_text_list(self) -> Tuple[List, List]:
        list1 = []
        list2 = []
        split_lines = self.text_list.splitlines()
        for line in split_lines:
            pair_of_numbers = re.findall(r"\d+", line)
            try:
                assert len(pair_of_numbers) == 2
            except AssertionError as e:
                print("Line Missing Pair of Digits, Skipping", e)
                continue  # next line
            pair_of_numbers_ints = [int(x) for x in pair_of_numbers]
            list1.append(pair_of_numbers_ints[0])
            list2.append(pair_of_numbers_ints[1])
        return list1, list2

    @staticmethod
    def _return_smallest_and_rest_of_list(
        input_list: List[int],
    ) -> Tuple[int, List[int]]:
        copy_of_input = input_list.copy()

        smallest = min(input_list)
        copy_of_input.remove(smallest)
        return smallest, copy_of_input

    def pairwise_distances_between_lists(
        self, list1: List[int], list2: List[int]
    ) -> List[int]:
        try:
            assert len(list1) == len(list2)
        except AssertionError as e:
            print("Lists are not of same length. ", e)
        distances = []
        while True:
            smallest1, list1 = self._return_smallest_and_rest_of_list(input_list=list1)
            smallest2, list2 = self._return_smallest_and_rest_of_list(input_list=list2)
            distance = abs(smallest1 - smallest2)
            distances.append(distance)
            if len(list1) == 0:
                break
        return distances

    def compute_similarity_scores(
        self, left_list: List[int], right_list: List[int]
    ) -> List[int]:
        similarity_scores = []
        for number in left_list:
            count_in_right_list = right_list.count(number)
            similarity_score = number * count_in_right_list
            similarity_scores.append(similarity_score)
        return similarity_scores
