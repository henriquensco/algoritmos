def regressao(i):
    if i <= 0:
        return
    else:
        print(i)
        regressao(i-1)


def regressao_loop(i):
    while i != 0:
        i -= 1
        print(i + 1)

#regressao(5)
regressao_loop(5)