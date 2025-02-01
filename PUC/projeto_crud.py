#Projeto CRUD
#Desenvolvido por Julio Roberto Carneiro Clausi
#Para a disciplina de Raciocínio Computacional (11100010563_20231_06)
#Do curso Big Data e Inteligência Analítica EAD da PUC-PR

#Aqui estou criando a uma função que terá a utilidade apenas de imprimir o menu principal
def imprimir_menu_principal():
    """Imprime o Menu Principal"""
    print ('---- MENU PRINCIPAL ----')
    print ('(1) Gerenciar Estudantes.')
    print ('(2) Gerenciar Disciplinas.')
    print ('(3) Gerenciar Professores.')
    print ('(4) Gerenciar Turmas.')
    print ('(5) Gerear Matrículas.')
    print ('(9) Sair.\n')

#Aqui estou criando a uma função que terá a utilidade apenas de imprimir o menu de operações
def imprimir_menu_operacoes():
    """Imprime o Menu de Operações"""
    print ('(1) Incluir')
    print ('(2) Listar')
    print ('(3) Atualizar')
    print ('(4) Excluir')
    print ('(9) Voltar ao menu principal.\n')

#Aqui estou criando uma lista das categorias e das ações
categorias = ['Estudantes','Disciplinas','Professores','Turmas','Matrículas']
acoes = ['Incluir', 'Listar', 'Atualizar', 'Excluir', 'Voltar ao menu principal']

#primeiro while, que funcionará com as funções do menu principal
while True:
    imprimir_menu_principal() #Mostrando o menu principal para o usuário
    selecao_usuario = input ('Por favor, selecione uma opção: ') #solicitando para que o usuário entre com uma opção
    if selecao_usuario.isdigit():
        #Método isdigit() retorna True se o usuário digitou apenas número e False caso contrário
        #preferi tratar dessa forma do que utilizar try e except
        if int(selecao_usuario) < 6 and int(selecao_usuario) > 0:
        #Neste if verifico se o usuário digitou 1, 2, 3, 4 ou 5
            #segundo while, que funcionará com as opções do menu de operações
            while True:
                categoria_selecionada = categorias[int(selecao_usuario)-1] #salvo na variável categoria_selecionada a opção da lista de categorias referente à seleção do usuário
                print (f'Você está dentro da opção de gerenciamento de {categoria_selecionada}\n') #um \n adicionou para ficar visualmente melhor
                print (f'---- [{categoria_selecionada}] Menu de Operações ----') 
                imprimir_menu_operacoes() #imprimindo o menu de operações
                #agora vamos verificar a ação do usuário
                selecao_acao = input('Agora entre com a ação desejada: ')
                if selecao_acao.isdigit():
                    if int(selecao_acao) <5 and int(selecao_acao) >0:
                        acao_selecionada = acoes[int(selecao_acao)-1]
                        print (f'Você selecionou a opção de [{acao_selecionada}] na categoria [{categoria_selecionada}]\n')
                    elif int(selecao_acao) == 9:
                        print ('Você selecionou a opção de voltar ao menu principal.\n')
                        break
                    else:
                        print ('\nERRO: Opção digitada inválida.\n')
                else:
                    print ('\nERRO: Digite apenas números.\n')        
        elif int(selecao_usuario) == 9:
            print ('Saindo...\n')
            break
        else:
            print ('\nERRO: Opção digitada inválida.\n')
    else:
        print ('\nERRO: Digite apenas números.\n')

print ('\nFinalizando aplicação.\n')
