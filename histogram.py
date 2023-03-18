

import matplotlib.pyplot as plt
import numpy as np

wt = np.random.uniform(40.0, 90.0, 100) # kilogram
ht = np.random.randint(140, 200, 100) # centimeter
BMI = wt / (ht/100)**2 # calculate BMI

    
bin = [0,18.5,25.0,30.0,BMI.max()]
colors = ['r','g','b','violet']
labels = ['underweight','healthy','overweight','obses']

# create histogram for each BMI level
plt.hist(BMI, bins=bin, edgecolor='black')


plt.title('Student Distribution for Each BMI Level')
plt.xticks([0,18.5,25.0,30.0])
plt.xlabel('BMI')
plt.ylabel('Number of Students')

plt.legend()
plt.show()