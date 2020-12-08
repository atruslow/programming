from day_one_input import day_one_input
from typing import Optional, Tuple

set_of_inputs_unique = set(day_one_input)

"""
In your expense report, what is the product of the three entries that sum to 2020?
"""


def _find_entries_sum(sum_target: int = 2020) -> Optional[Tuple[int]]:

    for datum in day_one_input:

        search_num = sum_target - datum

        if search_num in set_of_inputs_unique:

            return (search_num, datum)


def _find_tri_product(sum_target: int = 2020) -> int:

    for datum in day_one_input:

        dual_sum_target = sum_target - datum

        if dual_entries_sum := _find_entries_sum(dual_sum_target):
            val_1, val_2 = dual_entries_sum
            return datum * val_1 * val_2


if __name__ == "__main__":

    print(_find_tri_product())
