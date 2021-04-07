from func_cnpj import *

resp = input('Escolha uma opção: \n[1]VALIDAR CNPJ \n[2]GERAR CNPJ \n')
if resp == '2':
    gera()
else:
    cnpj = input('Informe o CNPJ: ')
    novo_cnpj = itera(cnpj)
    result(cnpj, novo_cnpj)

