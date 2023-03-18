import matplotlib.pyplot as plt
import numpy as np

wt = np.random.uniform(40.0, 90.0, 100) # kilogram
ht = np.random.randint(140, 200, 100) # centimeter
BMI = wt / (ht/100)**2 

colors = []
labels = []
for i in range(100):
    if(BMI[i] < 18.5):
        colors.append('r')
        labels.append('Underweight')
    elif(BMI[i] < 25.0):
        colors.append('g')
        labels.append('Normal')
    elif(BMI[i] < 30.0):
        colors.append('b')
        labels.append('Overweight')
    else:
        colors.append('violet')
        labels.append('Obese')


plt.scatter(ht[BMI<18.5], wt[BMI<18.5], color='r', label='Underweight')
plt.scatter(ht[(BMI>=18.5) & (BMI<25)], wt[(BMI>=18.5) & (BMI<25)], color='g', label='Normal')
plt.scatter(ht[(BMI>=25) & (BMI<30)], wt[(BMI>=25) & (BMI<30)], color='b', label='Overweight')
plt.scatter(ht[BMI>=30], wt[BMI>=30], color='violet', label='Obese')

plt.xlabel('height')
plt.ylabel('weight')
plt.title('Scatter plot')
plt.legend()
plt.show()


