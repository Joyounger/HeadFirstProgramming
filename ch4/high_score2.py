highest_score = 0
result_f = open("results.txt")
for line in result_f:
    score_str = line[line.find(' ')+1]
    if float(score_str) > highest_score:
        highest_score = float(score_str)
result_f.close()
print("V1--the highest score was:")
print(highest_score)


result_f = open("results.txt")
for line in result_f:
    (name, score) = line.split() #集合
    if float(score) > highest_score:
        highest_score = float(score)
result_f.close()
print("V2--the highest score was:")
print(highest_score)