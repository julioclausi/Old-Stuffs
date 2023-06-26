#Projeto CRUD
#Desenvolvido por Julio Roberto Carneiro Clausi
#Para a disciplina de Raciocínio Computacional (11100010563_20231_06)
#Do curso Big Data e Inteligência Analítica EAD da PUC-PR

import json

NOME_ARQUIVO_JSON = 'projeto_crud_julio_clausi.json'

def salvar_json():
    resultado = {
        'Estudantes':estudantes,
        'Professores':professores,
        'Disciplinas':disciplinas,
        'Turmas':turmas
    }
    with open (NOME_ARQUIVO_JSON, 'w') as arquivo:
        json.dump(resultado,arquivo,indent=4)
    arquivo.close()

def carregar_json():
    try:
        with open(NOME_ARQUIVO_JSON, 'r') as arquivo:
            print('Carregando dados...')
            dados = json.load(arquivo)
            return dados
    except:
        return []

def imprimir_menu_principal():
    print ('---- MENU PRINCIPAL ----')
    print ('(1) Gerenciar Estudantes.')
    print ('(2) Gerenciar Professores.')
    print ('(3) Gerenciar Disciplinas.')
    print ('(4) Gerenciar Turmas.')
    print ('(5) Gerenciar Matrículas.')
    print ('(9) Sair.\n')

def imprimir_menu_operacoes():
    print ('(1) Incluir')
    print ('(2) Listar')
    print ('(3) Atualizar')
    print ('(4) Excluir')
    print ('(9) Voltar ao menu principal.\n')

def imprimir(lista,assunto):
    if lista_vazia(lista):
        print (f'[AVISO] Lista de {assunto} está vazia.')
    else:
        print (f'Listando {assunto}')
        for item in lista:
            print (item)
    print()

def dados_pessoa(lista,assunto):
    while True:
        try:
            codigo = int(input(f'Informe o código da pessoa que será cadastrada na lista de {assunto}: '))
        except:
            print ('[AVISO] Por favor, digite apenas números para o código.\n')
            continue
        if localizar_na_lista(lista,codigo) == False:
            nome = input('Informe o nome da pessoa: ')
            cpf = input(f'Informe o CPF de {nome}: ')
            pessoa = {
                'codigo':codigo,
                'nome':nome,
                'cpf':cpf
            }
            print (f'{pessoa} cadastrada.')
            return pessoa
        else:
            print (f'[AVISO] Código {codigo} já utilizado na lista de {assunto}. Tente novamente.')

def dados_disciplina(lista):
    while True:
        try:
            codigo = int(input(f'Informe o código da disciplina: '))
        except:
            print ('[AVISO] Por favor, digite apenas números para o código.\n')
            continue
        if localizar_na_lista(lista,codigo) == False:
            nome = input('Informe o nome da disciplina: ')
            disciplina = {
                'codigo':codigo,
                'nome':nome,
            }
            return disciplina
        else:
            print (f'[AVISO] Código {codigo} já utilizado na lista de {assunto}. Tente novamente.')

def dados_turma():
    while True:
        if lista_vazia(professores) or lista_vazia(disciplinas):
            print ('[AVISO] Lista de professores ou de disciplinas não possuem nenhum registro.')
            print ('Cadastre professores e disciplinas antes de cadastrar turmas.')
            return
        try:
            codigo = int(input(f'Informe o código da turma: '))
        except:
            print ('[AVISO] Por favor, digite apenas números para o código.\n')
            continue
        if localizar_na_lista(turmas,codigo):
            print (f'[AVISO] Turma {codigo} já existe. Tente novamente.')
        else:
            while True:
                try:
                    professor = int(input(f'Informe o código do professor: '))
                except:
                    print ('[AVISO] Por favor, digite apenas números para o código.\n')
                    continue
                if localizar_na_lista(professores,professor):
                    print(f'[OK] Professor com código {professor} está cadastrado.\n')
                    while True:
                        try:
                            disciplina = int(input(f'Informe o código da disciplina: '))
                        except:
                            print ('[AVISO] Por favor, digite apenas números para o código.\n')
                            continue
                        if localizar_na_lista(disciplinas,disciplina):
                            print(f'[OK] Disciplina com código {disciplina} está cadastrada.\n')
                            turma = {
                                'codigo':codigo,
                                'professor':professor,
                                'disciplina':disciplina
                            }
                            print (f'Turma {turma} cadastrada.')
                            return turma
                        else:
                            print(f'[AVISO] Disciplina com código {disciplina} não está cadastrada.')
                            return None
                else:
                    print(f'[AVISO] Professor com código {professor} não está cadastrado.')
                    return None

def lista_vazia(lista):
    if len(lista) == 0:
        return True
    return False

def incluir_na_lista(lista,item):
    lista.append(item)
    salvar_json()

def localizar_na_lista(lista,codigo):
    count = 1
    if lista_vazia(lista):
        return False
    for item in lista:
        if codigo == item['codigo']:
            return count
        count +=1
    return False

def excluir_da_lista(lista,assunto):
    if lista_vazia(lista):
        print (f'Lista de {assunto} vazia, sem itens para excluir.')
        return
    try:
        codigo = int(input('Digite o código que deseja excluir: '))
    except:
        print ('[AVISO] Digite apenas números para a entrada do código.\n')
        return
    indice = localizar_na_lista(lista,codigo)
    if indice:
        print (f'[AVISO] {lista[indice-1]} removido com sucesso.')
        del lista[indice-1]
    else:
        print (f'[AVISO] Código {codigo} não localizado na lista de {assunto}.')
    salvar_json()

def atualizar_na_lista(lista,assunto):
    if lista_vazia(lista):
        print (f'Lista de {assunto} vazia, não há o que atualizar.')
        return
    else:
        try:
            codigo = int(input('Digite o código que deseja atualizar: '))
        except:
            print ('[AVISO] Digite apenas números para a entrada do código.\n')
            return
    indice = localizar_na_lista(lista,codigo)
    del lista[indice-1]
    if indice:
        if assunto == 'ESTUDANTES' or assunto == 'PROFESSORES':
            item = dados_pessoa(lista,assunto)
        elif assunto == 'DISCIPLINAS':
            item = dados_disciplina(lista)
        elif assunto == 'TURMAS':
            item = dados_turma()
        lista.append(item)
    else:
        print (f'[AVISO] Código {codigo} não localizado na lista de {assunto}.')
    salvar_json()

estudantes = []
professores = []
disciplinas = []
turmas = []

dados = carregar_json()
if len(dados)>0:
    estudantes = dados['Estudantes']
    professores = dados['Professores']
    disciplinas = dados['Disciplinas']
    turmas = dados['Turmas']

while True:
    imprimir_menu_principal()
    try:
        opcao_principal = int(input('Por favor, selecione uma opção: '))
    except:
        print ('[AVISO] Por gentileza, digite apenas números para as opções\n')
        continue
    
    if opcao_principal == 1:
        assunto = 'ESTUDANTES'
        while True:
            print (f'---- [{assunto}] Menu de Operações ----')
            imprimir_menu_operacoes()
            try:
                opcao_secundaria = int(input('Por favor, selecione uma opção: '))
            except:
                print('[AVISO] Por gentileza, digite apenas números para as opções\n')
                continue
            if opcao_secundaria == 1:
                #INSERIR
                estudante = dados_pessoa(estudantes,assunto)
                incluir_na_lista(estudantes,estudante)
            elif opcao_secundaria == 2:
                #LISTAR
                imprimir(estudantes,assunto)
            elif opcao_secundaria == 3:
                #ATUALIZAR
                atualizar_na_lista(estudantes,assunto)
            elif opcao_secundaria == 4:
                #EXCLUIR
                excluir_da_lista(estudantes,assunto)
            elif opcao_secundaria == 9:
                print ('Voltando ao menu principal\n')
                break
            else:
                print ('Opção inválida.')
                continue

    elif opcao_principal == 2:
        assunto = 'PROFESSORES'
        while True:
            print (f'---- [{assunto}] Menu de Operações ----')
            imprimir_menu_operacoes()
            try:
                opcao_secundaria = int(input('Por favor, selecione uma opção: '))
            except:
                print('[AVISO] Por gentileza, digite apenas números para as opções\n')
                continue
            if opcao_secundaria == 1:
                #INSERIR
                professor = dados_pessoa(professores,assunto)
                incluir_na_lista(professores,professor)
            elif opcao_secundaria == 2:
                #LISTAR
                imprimir(professores,assunto)
            elif opcao_secundaria == 3:
                #ATUALIZAR
                atualizar_na_lista(professores,assunto)
            elif opcao_secundaria == 4:
                #EXCLUIR
                excluir_da_lista(professores,assunto)
            elif opcao_secundaria == 9:
                print ('Voltando ao menu principal')
                break
            else:
                print ('Opção inválida.')
                continue

    elif opcao_principal == 3:
        assunto = 'DISCIPLINAS'
        while True:
            print (f'---- [{assunto}] Menu de Operações ----')
            imprimir_menu_operacoes()
            try:
                opcao_secundaria = int(input('Por favor, selecione uma opção: '))
            except:
                print('[AVISO] Por gentileza, digite apenas números para as opções\n')
                continue
            if opcao_secundaria == 1:
                #INSERIR
                disciplina = dados_disciplina(disciplinas)
                incluir_na_lista(disciplinas,disciplina)
            elif opcao_secundaria == 2:
                #LISTAR
                imprimir(disciplinas,assunto)
            elif opcao_secundaria == 3:
                #ATUALIZAR
                atualizar_na_lista(disciplinas,assunto)
            elif opcao_secundaria == 4:
                #EXCLUIR
                excluir_da_lista(disciplinas,assunto)
            elif opcao_secundaria == 9:
                print ('Voltando ao menu principal')
                break
            else:
                print ('Opção inválida.')
                continue
            
    elif opcao_principal == 4:
        assunto = 'TURMAS'
        while True:
            print (f'---- [{assunto}] Menu de Operações ----')
            imprimir_menu_operacoes()
            try:
                opcao_secundaria = int(input('Por favor, selecione uma opção: '))
            except:
                print('[AVISO] Por gentileza, digite apenas números para as opções\n')
                continue
            if opcao_secundaria == 1:
                #INSERIR
                turma = dados_turma()
                if turma != None:
                    incluir_na_lista(turmas,turma)
            elif opcao_secundaria == 2:
                #LISTAR
                imprimir(turmas,assunto)
            elif opcao_secundaria == 3:
                #ATUALIZAR
                atualizar_na_lista(turmas,assunto)
            elif opcao_secundaria == 4:
                #EXCLUIR
                excluir_da_lista(turmas,assunto)
            elif opcao_secundaria == 9:
                print ('Voltando ao menu principal.')
                break
            else:
                print ('Opção inválida.')
                continue
            
    elif opcao_principal == 5:
        assunto = 'MATRÍCULAS'
            
    elif opcao_principal == 9:
        print('Sair')
        break

    else:
        print('Opção inválida')

