

import matplotlib.pyplot as plt
import numpy as np

wt = np.random.uniform(40.0, 90.0, 100) # kilogram
ht = np.random.randint(140, 200, 100) # centimeter
BMI = wt / (ht/100)**2 # calculate BMI

a = 0
b = 0
c = 0
d = 0
for i in range(100):
    if(BMI[i] < 18.5):
        a += 1
    elif(BMI[i] < 25.0):
        b += 1
    elif(BMI[i] < 30.0):
        c += 1
    else:
        d += 1

ratio = [a,b,c,d]
langs = ['underweight', 'healthy', 'overweight', 'obses']
plt.pie(ratio, labels = langs, autopct = '%.2f%%')
plt.show()