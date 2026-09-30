
def caculate_score(data, result):
    score = 0
    for i in range(len(result)):
        a, b, c, d = result[i]
        area = (c-a) * (d-b)

        score += 1-(1-min(area, data[i][2])/max(area, data[i][2]))**2
    
    return score 

