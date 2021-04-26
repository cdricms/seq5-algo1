from data import scores


## A1
def score_exist(fscore, data):
    for col in range(len(data)):
        for row in range(len(data[col])):
            if data[col][row] == fscore:
                return True

    return False
            
print(score_exist(533, scores))



## A2
def score_index(fscore, data):

    indices = [-1, 1]

    for col in range(len(data)):
        for row in range(len(data[col])):
            if data[col][row] == fscore:
                indices = [col, row]
                break

    return indices


print(score_index(533, scores))

## A3
def score_count(fscore, data):
    count = 0
    for col in range(len(data)):
        for row in range(len(data[col])):
            if data[col][row] == fscore:
                count += 1
    
    return count


print(score_count(533, scores))

