import numpy as np
wt = np.random.uniform(40.0 ,90.0 ,100) # unit => kilogram
ht = np.random.randint(140,200,100) # unit => centimeter
BMI = wt / (ht/100)**2 # ht unit [centimeter => meter]
print(BMI)