# TODO решите задачу

import json
j = open('input.json')

def task() -> float:
    data = json.load(j)
    gen_result = 0

    for count in data :
        result = count["score"] * count["weight"]
        gen_result += result

    float_result = (f"{gen_result:.3f}")
    return float_result



print(task())
