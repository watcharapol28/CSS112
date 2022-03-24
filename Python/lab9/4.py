import numpy as np

x = np.array([[3,4],[5,12],[24,7]])
y = np.array([int((i[0]**2 + i[1]**2)**(1/2)) for i in x])
print(y)