from interface import *

def arquivoExiste(produto):
    try:
        arquivo = open(produto, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(produto):
    try:
        arquivo = open(produto, 'wt+')#essa funçao cria um txt automático
        arquivo.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {produto} criado com sucesso!')

def lerArquivo(produto):
    try:
        arquivo = open(produto, 'rt')
    except:
        print('ERRO ao ler o arquivo')
    else:
        cabeçalho('PRODUTOS CADASTRADOS')
        print(f'{"Produto":<17}{"Quantidade":^12}{"Preço Un.":>13}')
        print()
        for linha in arquivo:
            dado = linha.strip().split(';')
            print(f'{str(dado[0]):<17};{int(dado[1]):^10};{float(dado[2]):>12.2f}')
    finally:
        arquivo.close()

def cadastrar(arq, produto='desconhecido', quantidade=0, preço=0):
    try:
        arquivo = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura  do arquivo')
    else:
        try:
            arquivo.write(f'{produto};{quantidade};{preço}\n')
        except:
            print('Houve um ERRO na hgora de escrever os dados')
        else:
            print(f'Novo registro de {produto} adicionado.')
            arquivo.close()

def apagar(arq): # Função para deletar um item da lista
    try:
        with open(arq, 'r') as arquivo:
            linhas = arquivo.readlines()
        for i, linha in enumerate(linhas):
            print(f'{i+1} - {linha.strip()}')        
        opc = leiaint('Qual produto deseja excluir? ')
        indice = opc - 1
        if 0 <= indice < len(linhas):
            removido = linhas.pop(indice)
            print(f'Removido: {removido.strip()}')
        else:
            print('Índice inválido!')

        with open(arq, 'w') as arquivo:
            for linha in linhas:
                arquivo.write(linha)
    except:
        print('Houve um erro ao tentar apagar o produto.')
    else:
        print('Produto apagado com sucesso')

def vender(arq):
    try:
        with open(arq, 'r') as arquivo:
            linhas = arquivo.readlines()
        for i, linha in enumerate(linhas):
            dado = linha.strip().split(';')
            nome = dado[0]
            quantidade = int(dado[1])
            preco = float(dado[2])
            print(f'\033[32m{i+1}\033[m - \033[35m{nome:<20}\033[m | Qtd: {quantidade:^3}') 
           
        opc = leiaint('Qual produto quer vender:  ')
        indice = opc - 1

        if not (0 <= indice < len(linhas)):
            print('Índice inválido!')
            return
        dado = linhas[indice].strip().split(';')
        nome = dado[0]
        quantidade = int(dado[1])
        preço = float(dado[2])
        vendido = leiaint('Quantidade vendida: ')   

        if vendido > quantidade:
            print(f'Estoque insuficiente!')
            return
        total = vendido * preço
        print (f'Total da venda: R${total:.2f}')

        confirmar = input('Confirmar venda? [s/n]: ').lower()
        if confirmar != 's':
            print('Venda cancelada!')
            return
        
        quantidade -= vendido
        linhas[indice] = f'{nome};{quantidade};{preço}\n'
      
        with open(arq, 'w') as arquivo:
            for linha in linhas:
                arquivo.write(linha)
    except:
        print('Houve um erro ao tentar vender o produto.')
    else:
        print('Produto vendido com sussesso')
