import numpy as np

score = np.array([28, 35, 26, 32, 28, 28, 35, 34, 46, 42, 37])
mean = np.mean(score) # mean
devi = np.std(score) # standard deviation

mean = round(mean,1)
devi = round(devi,1)

stdScore = []

for i in range(len(score)):
    z = (score[i] - mean) / devi
    z = round(z,2)
    stdScore.append(z)
    


print("The mean: " + str(mean))
print("The standard deviation: "+ str(devi))
print("The standard scores: "+ str(stdScore))

# Based on the lecture note, 
# those who received an F noted that the z-score 
# was less than -1 and highlighted in red.
# If stdScore < -1, a student stands out to receive a 'F'

F = []

for i in range(len(stdScore)):
    if(stdScore[i] < -1):
        F.append(score[i])

print("The students score that stand out to receive a 'F':", end = '')
print(F)

