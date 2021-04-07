import re
from random import randint


def remove_carac(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)


def itera(cnpj):
    novo_cnpj = remove_carac(cnpj[:-2])
    while len(novo_cnpj) != 14:
        mult = 5
        if len(novo_cnpj) == 13:
            mult = 6
        temp = []
        for p in novo_cnpj:
            temp.append(int(p) * mult)
            mult -= 1
            if mult == 1:
                mult = 9
        soma = sum(temp)
        temp.clear()
        novo_cnpj += str(digito(soma))
    return novo_cnpj


def digito(soma):
    s = 11 - (soma % 11)
    if s > 9:
        s = 0
    return s


def result(cnpj, novo_cnpj):
    cnpj = remove_carac(cnpj)
    sequencia = novo_cnpj == str(novo_cnpj[0]) * len(cnpj)
    if cnpj == novo_cnpj and not sequencia:
        print('O CNPJ é válido')
    else:
        print('O CNPJ é inválido')


def gera():
    primeiro_digito = randint(0, 9)
    segundo_digito = randint(0, 9)
    segundo_bloco = randint(100, 999)
    terceiro_bloco = randint(100, 999)
    quarto_bloco = '0001'

    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}' \
                  f'{terceiro_bloco}{quarto_bloco}00'

    novo_cnpj = remove_carac(inicio_cnpj[:-2])

    while len(novo_cnpj) != 14:
        novo_cnpj = itera(novo_cnpj)

    print(f'O CNPJ gerado é: {novo_cnpj[:2]}.{novo_cnpj[2:5]}.{novo_cnpj[5:8]}/'
          f'{novo_cnpj[8:12]}-{novo_cnpj[12:14]}')
