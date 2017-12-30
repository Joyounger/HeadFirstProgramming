result_f = open("results.txt")
score_hash = {}
score_array = []
for line in result_f:
    (name, score) = line.split() #集合
    score_hash[score] = name
    score_array.append(float(score))
result_f.close()
#score_array.sort().reverse()--false
#score_array.sort()
#score_array.reverse()
score_array.sort(reverse = True)

print("V1--the highest score was:")
for each_score in sorted(score_hash.keys(), reverse = True):
    print(score_hash[each_score] + ' had a score wth ' + each_score)

