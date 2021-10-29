def reportGenerator(x, y, c, minCost, minRoute, iterations):
    points = [[x[i], y[i]]for i in range(len(x))]
    print('number of points: ', len(x))
    print('points: ', points)
    print('**********')

    print('number of iterations: ', iterations)
    print('**********')

    print('costs:')
    for i in range(len(x)):
        print(c[i])
    print('**********')

    print('minimum route: ', minRoute)
    print('minimum cost: ', minCost)
    print('**********')
