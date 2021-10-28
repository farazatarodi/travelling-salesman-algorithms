import matplotlib.pyplot as plt
import numpy as np
import itertools as it
import time
from report import reportGenerator


# def heapGenerate(k, array):
#     if k == 1:
#         print(array)
#         yield array
#     else:
#         heapGenerate(k-1, array)
#         for i in range(k-1):
#             if (k-1) % 2 == 0:
#                 temp = array[i]
#                 array[i] = array[k-1]
#                 array[k-1] = temp
#             else:
#                 temp = array[0]
#                 array[0] = array[k-1]
#                 array[k-1] = temp
#             heapGenerate(k-1, array)


length = 5

startPoint = [0, 0]

x = [np.random.randint(1, 10) for i in range(length)]
y = [np.random.randint(1, 10) for i in range(length)]

x.insert(0, startPoint[0])
y.insert(0, startPoint[1])

c = [[0.0 for i in range(len(x))]for j in range(len(x))]

# calculating cost between points
for i in range(len(x)):
    for j in range(i+1, len(x)):
        c[i][j] = round(np.sqrt((x[i]-x[j]) ** 2+(y[i]-y[j])**2), 1)
        c[j][i] = c[i][j]

minCost = np.Inf

routes = it.permutations(range(1, len(x)))

for route in routes:
    totalCost = c[0][route[0]]+c[route[-1]][0]

    for i in range(len(route)-1):
        start = route[i]
        end = route[i+1]
        totalCost += c[start][end]

    if totalCost < minCost:
        minCost = totalCost
        minRoute = route

minX = [x[point] for point in minRoute]
minY = [y[point] for point in minRoute]

minX.insert(0, startPoint[0])
minY.insert(0, startPoint[1])
minX.insert(len(minX), startPoint[0])
minY.insert(len(minY), startPoint[1])

plt.xlim([0, 10])
plt.ylim([0, 10])

plt.scatter(x, y)

plt.plot(minX, minY)

reportGenerator(x, y, c, minCost, minRoute)

plt.show()
