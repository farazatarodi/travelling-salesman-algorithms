def reportGenerator(x, y, c, minCost, minRoute):
    points = [[x[i], y[i]]for i in range(len(x))]
    print('points: ', points)
    print('**********')

    print('costs:')
    for i in range(len(x)):
        print(c[i])
    print('**********')

    print('minimum route: ', minRoute)
    print('minimum cost: ', minCost)
