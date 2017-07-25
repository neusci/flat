def logistic(x, mu=4):
    return mu*x*(1-x)


def logistic_list(x, l=1, mu=4):
    lis = zeros(l)
    lis[0] = logistic(x)
    for i in range(1,l):
        lis[i] = logistic(lis[i-1])
    return lis
