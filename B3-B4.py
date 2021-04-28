from data import my_marks

## B3
def calcul_raw_avg(marks):
    sum = 0
    for mark in marks:
        sum += mark['result']

    return sum / len(marks)

print(calcul_raw_avg(my_marks))


def calcul_avg(marks):
    sum = 0
    total_coef = 0
    for mark in marks:
        sum += (mark['result'] * mark['coef'])
        total_coef += mark['coef']

    return round(sum / total_coef, 2)

print(calcul_avg(my_marks))
