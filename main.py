from func_cnpj import *

resp = input('Escolha uma opção: \n[1]VALIDAR CNPJ \n[2]GERAR CNPJ \n')
if resp == '2':
    gerar_cnpj()
else:
    cnpj = input('Informe o CNPJ: ')
    novo_cnpj = gerador_digitos(cnpj)
    result(cnpj, novo_cnpj)

