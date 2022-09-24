routers = ['AB', 'AH', 'AG', 'AF',
          'GF', 'GA', 'GL', 'GK', 'GJ', 'GI', 'GH',
          'BA', 'BH', 'BI', 'BC']

router = 'AGF'


for i in range(len(router) - 1):
    r = router[i: i + 2]
    if i >= 1:
        if router[i - 1] == router[i + 1]:
            print(0)
            break
    if r not in routers:
        print(0)
        break  