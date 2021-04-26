from data import scores


## A11
def calcul_sum(data):
    sum = 0
    for col in range(len(data)):
        for row in range(len(data[col])):
            sum += data[col][row]

    return sum

print(calcul_sum(scores))


## A12
def calcul_average(data):
    average = []

    for col in range(len(data)):
        d = len(data[col])
        sum = 0
        for row in range(len(data[col])):
            sum += data[col][row]

        average.append(sum / d)

    sum = 0
    for num in average:
        sum += num

    return sum / len(average)


print(calcul_average(scores))


## A13
def calcul_players_average(data):
    average = []
    for col in range(len(data)):
        a = 0
        for row in range(len(data[col])):
            a += data[col][row]

        average.append(a / len(data[col]))

    return average


print(calcul_players_average(scores))


## A14
def calcul_rounds_average(data):

    rounds = []

    for col in range(len(data)):
        for row in range(len(data[col])):
            try:
                rounds[row] += [data[col][row]]
            except IndexError:
                rounds.insert(row, [data[col][row]])

    average = []

    for col in range(len(rounds)):
        result = 0
        for row in range(len(rounds[col])):
            result += rounds[col][row]

        average.append(result / len(rounds[col]))

    return average


print(calcul_rounds_average(scores))