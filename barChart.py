import matplotlib.pyplot as plt
import numpy as np

wt = np.random.uniform(40.0 ,90.0 ,100) # unit => kilogram
ht = np.random.randint(140,200,100) # unit => centimeter

BMI = wt / (ht/100)**2 # ht unit [centimeter => meter]

a = 0 
b = 0 
c = 0 
d = 0 # a->underweight,b->Healthy,c->Overweight,d->obses

for i in range(100):
    if(BMI[i] < 18.5):
        a += 1
    elif(BMI[i] < 25.0):
        b += 1
    elif(BMI[i] < 30.0):
        c += 1
    else:
        d += 1 


x = np.arange(4)
status = ['Underweight', 'Healthy', 'Overweight', 'Obses']
values = [a,b,c,d]
colors = ['r','g','b','violet']

plt.bar(x, values, color = colors)
plt.xticks(x, status)
plt.show() 
