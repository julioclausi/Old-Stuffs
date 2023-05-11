#Projeto CRUD
#Desenvolvido por Julio Roberto Carneiro Clausi
#Para a disciplina de Raciocínio Computacional (11100010563_20231_06)
#Do curso Big Data e Inteligência Analítica EAD da PUC-PR

#Etapas da semana 1:
#•	Apresentar ao usuário um menu de navegação contendo as 5 opções de dados cadastrais (além de uma opção “Sair”), que chamaremos de menu principal.
# 1.	Estudantes
# 2.	Disciplinas
# 3.	Professores
# 4.	Turmas
# 5.	Matrículas
#•	Realizar a leitura da opção desejada pelo usuário (pode ser através de um número inteiro ou texto).
#•	Apresentar ao usuário qual foi a opção escolhida com o apoio de estrutura condicional.
#•	Apresentar ao usuário um menu de navegação contendo as 4 operações possíveis (além de uma opção “Voltar ao menu principal”), que chamaremos de menu de operações.
# 1.	Incluir
# 2.	Listar
# 3.	Atualizar
# 4.	Excluir
#•	Realizar a leitura da opção desejada pelo usuário (pode ser através de um número inteiro ou texto).
#•	Apresentar ao usuário qual foi a opção escolhida com o apoio de estrutura condicional.
#•	Fim da aplicação. 
#Observação: O sistema deve obrigatoriamente fechar sempre que o usuário selecionar a opção cadastral e a funcionalidade. As opções “Sair” e “Voltar ao menu principal” ficarão sem funcionalidade por enquanto.

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

#Aqui estou criando uma lista das categorias e das ações
categorias = ['Estudantes','Disciplinas','Professores','Turmas','Matrículas']
acoes = ['Incluir', 'Listar', 'Atualizar', 'Excluir', 'Voltar ao menu principal']

imprimir_menu_principal() #Mostrando o menu principal para o usuário

selecao_usuario = input ('Por favor, selecione uma opção: ') #solicitando para que o usuário entre com uma opção

if selecao_usuario.isdigit():
    #Método isdigit() retorna True se o usuário digitou apenas número e False caso contrário
    if int(selecao_usuario) < 6 and int(selecao_usuario) > 0:
    #Neste if verifico se o usuário digitou 1, 2, 3, 4 ou 5
        categoria_selecionada = categorias[int(selecao_usuario)-1] #salvo na variável categoria_selecionada a opção da lista de categorias referente à seleção do usuário
        print (f'Você selecionou a opção de gerenciamento de {categoria_selecionada}\n') #um \n adicionou para ficar visualmente melhor
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
            else:
                print ('Opção digitada inválida.')
        else:
            print ('Digite apenas números.')        
    elif int(selecao_usuario) == 9:
        #Aqui será a opção sair, mas não fará nada por enquanto
        ...
    else:
        print ('Opção digitada inválida.')
else:
    print ('Digite apenas números.')
