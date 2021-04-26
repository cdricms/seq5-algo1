from data import scores


## A4
def get_high_score(data):
    highest = 0
    for col in range(len(data)):
        for row in range(len(data[col])):
            if data[col][row] > highest:
                highest = data[col][row]

    return highest

print(get_high_score(scores))


## A5
def get_high_index(data):

    highest = 0
    result = [-1, 1]
    for col in range(len(data)):
        for row in range(len(data[col])):
            if data[col][row] > highest:
                result = [col, row]

    return result


print(get_high_index(scores))


## A6
def players_high_score(data):
    result = []
    for col in range(len(data)):
        highest = 0
        for row in range(len(data[col])):
            if data[col][row] > highest:
                highest = data[col][row]

        result.append(highest)

    return result

print(players_high_score(scores))


## A7
def players_high_score_plus(data):

    result = []
    for col in range(len(data)):
        highest = 0
        indices = None
        for row in range(len(data[col])):
            if data[col][row] > highest:
                highest = data[col][row]
                indices = (row, data[col][row])

        result.append(indices)

    return result


print(players_high_score_plus(scores))


## A8

#######################################################
#   petit problème, quand highest est dans les premiers
#   indices, latest ne peut pas être mis à jour car le 
#   plus gros chiffre a déjà était trouvé. 
#   Je reglerai ça la prochaine fois.
#######################################################

def players_nbests_scores(nbests, data):
    result = []
    for col in range(len(data)):
        latest = 0
        highest = 0
        score = None
        for row in range(len(data[col])):
            if data[col][row] > highest:
                latest = highest
                highest = data[col][row]
                score = (highest, latest)

        result.append(score)

    return result


print(players_nbests_scores(0, scores))


## A9
def rounds_high_score(data):
    result = []
    for col in range(len(data)):
        highest = 0
        for row in range(len(data[col])):
            if data[col][row] > highest:
                highest = data[col][row]

        result.append(highest)

    return result

print(rounds_high_score(scores))


## A10
def rounds_high_score_plus(data):
    result = []
    for col in range(len(data)):
        highest = 0
        indices = None
        for row in range(len(data[col])):
            if data[col][row] > highest:
                highest = data[col][row]
                indices = (col, highest)

        result.append(indices)

    return result


print(rounds_high_score_plus(scores))