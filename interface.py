def leianome(msg):
    while True:
        try:
            linha()
            produtos = [
                'Frango Assado',
                'Costela Recheada',
                'Costela no Bafo',
                'Maminha Assada',
                'Fraldinha Assada']
            linha()
            for i, item in enumerate(produtos):
                print(f'\033[36m{i+1}\033[m - \033[33m{item}\033[m')
            nome = int(input(msg))
            indice = nome -1
            if 0 <= indice < len(produtos):
                nome = produtos[indice]
            else:
                print('Opção inválida')
                continue

        except(ValueError, TypeError):
            print('\033[0;31mERRO! digite um nome inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return nome
        
def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! digite um número inteiro válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:   
            return num 

def leiaPreço(msg):
    while True:
        try:
            num = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! digite um número preço válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:   
            return num 
        
def linha(tam = 42):
    return '-'*tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

      
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m -\033[34m {item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc

def menu_de_venda(lista):
    cabeçalho('MENU DE VENDAS')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m -\033[34m {item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('Sua opção: ')
    return opc
