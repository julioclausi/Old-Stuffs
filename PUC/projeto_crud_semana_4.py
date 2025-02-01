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
    print ('(5) Gerenciar Matrículas.')
    print ('(9) Sair.\n')

#Aqui estou criando a uma função que terá a utilidade apenas de imprimir o menu de operações
def imprimir_menu_operacoes():
    """Imprime o Menu de Operações"""
    print ('(1) Incluir')
    print ('(2) Listar')
    print ('(3) Atualizar')
    print ('(4) Excluir')
    print ('(9) Voltar ao menu principal.\n')

#Criando lista de estudantes
estudantes = []

#primeiro while, que funcionará com as funções do menu principal
while True:
    imprimir_menu_principal() #Mostrando o menu principal para o usuário

    selecao_usuario = input ('Por favor, selecione uma opção: ') #solicitando para que o usuário entre com uma opção

    if selecao_usuario.isdigit():
        #Método isdigit() retorna True se o usuário digitou apenas número e False caso contrário
        #preferi tratar dessa forma do que utilizar try e except

        #aqui abaixo será o menu de ESTUDANTES
        if int(selecao_usuario) == 1:
            while True:
                #Imprimo o menu de operações
                print (f'---- [ESTUDANTES] Menu de Operações ----')
                imprimir_menu_operacoes()

                #Peço para o usuário entrar com alguma opção
                selecao_acao = input('Agora entre com a ação desejada: ')

                #Novamente, verifico com isdigit se ele está entrando apenas com números
                if selecao_acao.isdigit():

                    #Aqui irá incluir estudante
                    if int(selecao_acao) == 1:
                        print ('\n-=-=-INCLUIR ESTUDANTE-=-=-')
                        nome_estudante = input('Digite o nome do estudante: ')
                        estudantes.append(nome_estudante)
                        input('Pressione ENTER para continuar.\n')
                    
                    #Aqui irá listar estudantes
                    elif int(selecao_acao) == 2:
                        print ('\n-=-=-LISTAR ESTUDANTES-=-=-')
                        if len(estudantes) > 0:
                            for estudante in estudantes:
                                print (f'- {estudante}')
                        else:
                            print ('Não há estudantes cadastrados.\n')
                        input('Pressione ENTER para continuar.\n')
                    
                    #Aqui irá atualizar estudantes
                    elif int(selecao_acao) == 3:
                        print ('\nEM DESENVOLVIMENTO.\n')

                    #Aqui irá excluir algum estudante
                    elif int(selecao_acao) == 4:
                        print ('\nEM DESENVOLVIMENTO.\n')
                    
                    #Aqui para voltar ao menu principal
                    elif int(selecao_acao) == 9:
                        print ('\nVoltando ao Menu Principal.\n')
                        break

                    #Aqui caso o usuário digitou algo que não existe operação
                    else:
                        print ('\nERRO: Opção digitada inválida.\n')
                
                #Aqui caso tenha digitado algo diferente de número inteiro
                else:
                    print ('\nERRO: Digite apenas números.\n') 

        #Aqui abaixo ainda em desenvolvimento serão os menus de Disciplinas, Professores, Turmas e Matrículas
        elif int(selecao_usuario) > 1 and int(selecao_usuario) <6:
            print('\nEM DESENVOLVIMENTO.\n')
        
        #Verifico se o usuário selecionou a opção 9 de Sair.
        elif int(selecao_usuario) == 9:
            print ('Saindo...\n')
            break #esse break sai do while principal

        #Aqui caso o usuário digitou algo que não tem operação associada
        else:
            print ('\nERRO: Opção digitada inválida.\n')
    
    #Aqui caso o usuário digitou letra ao invés de números
    else:
        print ('\nERRO: Digite apenas números.\n')

print ('\nFinalizando aplicação.\n')
#Fim da aplicação