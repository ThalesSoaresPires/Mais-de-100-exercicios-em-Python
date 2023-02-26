def aumentar(n, porc, formato=False):
    res = n + (n * (porc/100))
    return res if not formato else moeda(res)


def diminuir(n, porc, formato=False):
    res = n - (n * (porc/100))
    return res if not formato else moeda(res)


def dobro(n, formato=False):
    res = n + n
    return res if not formato else moeda(res)


def metade(n, formato=False):
    res = n / 2
    return res if not formato else moeda(res)


def moeda(res, moeda='R$'):
    return '{}{:.2f}'.format(moeda, res).replace('.', ',')
