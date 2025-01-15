import numpy as np
import matplotlib.pyplot as plt
import random

x = []
y = []
for i in range(0,100):
    r = random.random()
    x.append(r)
    r2 = random.random()
    y.append(-5 * (r + (r2/1.5)) + 50)

plt.scatter(x, y)

X = np.vstack([np.ones(len(x)), x]).T

coefficients, _, _, _ = np.linalg.lstsq(X, y, rcond=None) # run linear regression

slope = coefficients[1]
intercept = coefficients[0]


line_x = np.linspace(0, 1, 100) 
line_y = slope * line_x + intercept
plt.plot(line_x, line_y, color='red', linewidth=2)

plt.title('Linear Regression')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

