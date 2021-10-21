import matplotlib.pyplot as plt
import numpy as np

length = 2

points = [[np.random.randint(1, 10), np.random.randint(1, 10)]
          for i in range(length)]

start = [0, 0]

points.insert(0, start)

c = [[0.0 for i in range(len(points))]for j in range(len(points))]

print('points:', points)

# calculating cost between points
for i in range(len(points)):
    for j in range(i+1, len(points)):
        c[i][j] = round(np.sqrt((points[i][0]-points[j][0]) **
                        2+(points[i][1]-points[j][1])**2), 1)
        c[j][i] = c[i][j]
    print(c[i])


plt.xlim([0, 10])
plt.ylim([0, 10])

plt.plot(points, 'bo')
plt.show()
