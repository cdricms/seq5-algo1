from data import scores
from copy import deepcopy

## A15
def reject_under(threshold, data: list):
    result = deepcopy(data)

    for col in range(len(data)):
        for row in range (len(data[col])):
            if data[col][row] < threshold:
                result[col][row] = -1

    return result


print(reject_under(531, scores))


## A16
def multiply_by(coef, data: list):
    result = deepcopy(data)
    for col in range(len(data)):
        for row in range(len(data[col])):
            result[col][row] *=  coef

    return result

print(multiply_by(1.5, scores))
