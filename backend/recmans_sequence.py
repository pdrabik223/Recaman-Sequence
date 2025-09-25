# Recamán's sequence
# Non visited hash table approach
# create a table where all non visited numbers are stored
# and second one for the known numbers
# when moving to the "next number" first check if number is in known not visited numbers than remove it from the list or add all numbers between self and next step


# problems: 1. big numbers that do not fit in ram
#           2. A lot of numbers in array -> we can store rages of numbers instead of


# memory: 520KB

# 10^230

# we can reset whenever we cover a

import json


def naive_approach(cut_out: int):
    result_sequence = []

    current_value = 0
    for step in range(cut_out):

        if current_value - step > 0 and (current_value - step) not in result_sequence:
            current_value = current_value - step
        else:
            current_value += step

        result_sequence.append(current_value)
    return result_sequence


if __name__ == "__main__":
    with open("res.json", mode="w") as f:
        f.writelines(json.dumps(naive_approach(80)))
