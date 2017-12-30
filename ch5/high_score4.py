result_f = open("results.txt")
score_hash = {}
score_array = []
for line in result_f:
    (name, score) = line.split() #集合
    score_hash[float(score)] = name
    score_array.append(float(score))
result_f.close()
#score_array.sort().reverse()--false
#score_array.sort()
#score_array.reverse()
score_array.sort(reverse = True)

print("V1--the highest score was:")
print(score_hash[score_array[0]] + ' had a score wth ' + str(score_array[0]))
print(score_hash[score_array[1]] + ' had a score wth ' + str(score_array[1]))
print(score_hash[score_array[2]] + ' had a score wth ' + str(score_array[2]))


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

print("V2--the highest score was:")
print(score_hash[str(score_array[0])] + ' had a score wth ' + str(score_array[0]))
print(score_hash[str(score_array[1])] + ' had a score wth ' + str(score_array[1]))
print(score_hash[str(score_array[2])] + ' had a score wth ' + str(score_array[2]))