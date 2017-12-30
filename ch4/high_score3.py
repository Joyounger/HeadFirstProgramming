result_f = open("results.txt")
score_array = []
for line in result_f:
    (name, score) = line.split() #集合
    score_array.append(float(score))
result_f.close()
#score_array.sort().reverse()--false
#score_array.sort()
#score_array.reverse()
score_array.sort(reverse = True)
print("V2--the highest score was:")
print(score_array[0],score_array[1],score_array[2])