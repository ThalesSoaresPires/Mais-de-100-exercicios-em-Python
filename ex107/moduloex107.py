def aumentar(n, porc):
    res = n + (n * (porc/100))
    return res


def diminuir(n, porc):
    res = n - (n * (porc/100))
    return res


def dobro(n):
    res = n + n
    return res


def metade(n):
    res = n / 2
    return res


def moeda(res):
    var = 'R${}'.format(res)
    return var
