from interface import *
from functions import *
from time import sleep

arq = 'database.txt'

if arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    criarArquivo(arq)

# Loop para tela de cadastro de produtos
while True:
    resposta = menu(['Ver Produtos Cadastrados', 'Cadastrar Novo Produto', 'Apagar produto', 'Começar as vendas', 'Sair do Sistema'])   
    if resposta == 1: 
        #opção de listar o conteudo do arquivo    
        lerArquivo(arq)

    elif resposta == 2:
        #opção de cadastrar um novo produto
        cabeçalho('NOVO CADASTRO')
        nome = leianome('Produto: ')
        quantidade = leiaint('Quantidade: ')
        preço = leiaPreço('Digite o valor: R$')
        cadastrar(arq, nome, quantidade, preço)

    elif resposta == 3:
        #apagar linha do produto
        apagar(arq)

    elif resposta == 4:
        print('Iniciar as vendas!')
        sleep(1)
        # Loop para tela de vendas
        while True:
            resposta = menu_de_venda(['Conferir estoque', 'Vender produto', 'Retornar ao menu principal'])
            if resposta == 1:
                lerArquivo(arq)

            elif resposta == 2:
                vender(arq)

            elif resposta == 3:
                print('Retornando para o menu principal.')
                break

    elif resposta == 5:
        #sair do sistema
        cabeçalho('Saindo do sistema ... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!') 
    sleep(1)
 