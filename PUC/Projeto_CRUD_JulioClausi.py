#Projeto CRUD
#Desenvolvido por Julio Roberto Carneiro Clausi
#Para a disciplina de Raciocínio Computacional (11100010563_20231_06)
#Do curso Big Data e Inteligência Analítica EAD da PUC-PR
###########################################################################################
#Aqui irei importar a única biblioteca adicional que irei utilizar, a biblioteca JSON
#Que irá auxiliar nas leituras e salvamentos dos arquivos em .json
import json
###########################################################################################
#Criei essa constante que será o nome do arquivo de leitura e saída de dados
NOME_ARQUIVO_JSON = 'projeto_crud_julio_clausi.json'
###########################################################################################
#Função para salvar os dados num arquivo .json
def salvar_json():
    resultado = {
        'Estudantes':estudantes,
        'Professores':professores,
        'Disciplinas':disciplinas,
        'Turmas':turmas,
        'Matrículas':matriculas
    }
    with open (NOME_ARQUIVO_JSON, 'w') as arquivo:
        json.dump(resultado,arquivo,indent=4)
    arquivo.close()
###########################################################################################
#Função para ler os dados do arquivo .json
def carregar_json():
    try:
        with open(NOME_ARQUIVO_JSON, 'r') as arquivo:
            print('Carregando dados...')
            dados = json.load(arquivo)
            return dados
    except:
        dados = {
        'Estudantes':[],
        'Professores':[],
        'Disciplinas':[],
        'Turmas':[],
        'Matrículas':[]
        }
        return dados
###########################################################################################
#Função parar imprimir o menu principal
def imprimir_menu_principal():
    print ('\n---- MENU PRINCIPAL ----')
    print ('(1) Gerenciar Estudantes.')
    print ('(2) Gerenciar Professores.')
    print ('(3) Gerenciar Disciplinas.')
    print ('(4) Gerenciar Turmas.')
    print ('(5) Gerenciar Matrículas.')
    print ('(9) Sair.\n')
###########################################################################################
#Função para imprimir o menu secundário
def imprimir_menu_operacoes(assunto):
    print (f'\n---- [{assunto}] Menu de Operações ----')
    print ('(1) Incluir')
    print ('(2) Listar')
    print ('(3) Atualizar')
    print ('(4) Excluir')
    print ('(9) Voltar ao menu principal.\n')
###########################################################################################
#Função para imprimir as listas
def imprimir(lista,assunto):
    if lista_vazia(lista):
        print (f'[AVISO] Lista de {assunto} está vazia.')
        input ('Pressione ENTER para continuar.')
    else:
        print (f'Listando {assunto}')
        for item in lista:
            print (item)
    print()
###########################################################################################
#Como tanto os professores quanto os alunos terão 3 atributos (código, nome e cpf)
#Fiz uma função que irá pegar os dados deles da mesma forma
#O parâmetro dessa função recebe assunto que será ou ESTUDANTES ou PROFESSORES
#Facilitando a diminuição de códigos digitados
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
            input ('Pressione ENTER para continuar.')
###########################################################################################
#Essa função irá solicitar para o usuário os dados das disciplinas
#Que terão dois atributos: código e nome
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
            print (f'{disciplina} cadastrada.')
            return disciplina
        else:
            print (f'[AVISO] Código {codigo} já utilizado na lista de {assunto}. Tente novamente.')
            input ('Pressione ENTER para continuar.')
###########################################################################################
#Essa função irá criar uma turma
#Mas para que haja uma turma deverá haver professores cadastrados e disciplinas cadastradas
#Se o usuário não cadastrou ambos, ela informará para o usuário cadastrar professores e disciplinas
def dados_turma():
    if lista_vazia(professores) or lista_vazia(disciplinas):
        print ('[AVISO] Lista de professores ou de disciplinas não possuem nenhum registro.')
        print ('Cadastre professores e disciplinas antes de cadastrar turmas.')
        input ('Pressione ENTER para continuar.')
        return
    while True:

        try:
            codigo = int(input(f'Informe o código da turma: '))
        except:
            print ('[AVISO] Por favor, digite apenas números para o código.\n')
            continue
        if localizar_na_lista(turmas,codigo):
            print (f'[AVISO] Turma {codigo} já existe. Tente novamente.\n')
            input ('Pressione ENTER para continuar.')
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
                            input ('Voltaremos ao Menu de Operações. Pressione ENTER para continuar.')
                            return None
                else:
                    print(f'[AVISO] Professor com código {professor} não está cadastrado.')
                    input ('Voltaremos ao Menu de Operações. Pressione ENTER para continuar.')
                    return None
###########################################################################################
#Função que cria uma matrícula
#Para a criação há a necessidade que hajam turmas e estudantes
#Caso contrário o programa informa o usuário para cadastrar as turmas e estudantes antes.
def dados_matricula():
    if lista_vazia(turmas) or lista_vazia(estudantes):
        print ('[AVISO] Lista de turmas ou de estudantes não possuem nenhum registro.')
        print ('Cadastre turmas e estudantes antes de cadastrar matrículas.')
        input ('Pressione ENTER para continuar.')
        return
    while True:
        try:
            turma = int(input(f'Informe o código da turma: '))
        except:
            print ('[AVISO] Por favor, digite apenas números para o código da turma.\n')
            continue
        if localizar_na_lista(turmas,turma):
            print ('Turma Localizada.\n')
            while True:
                try:
                    estudante = int(input(f'Informe o código do estudante: '))
                except:
                    print ('[AVISO] Por favor, digite apenas números para o código da turma.\n')
                    continue
                if localizar_na_lista(estudantes,estudante):
                    print ('Estudante Localizado.\n')
                    matricula = {
                        'turma':turma,
                        'estudante':estudante
                    }
                    return matricula
                else:
                    print ('Estudante não localizado. Voltaremos ao menu de operações.')
                    input ('Pressione ENTER para continuar.')
                    return
        else:
            print ('Turma não localizada. Voltaremos ao menu de operações.')
            input ('Pressione ENTER para continuar.')
            return
###########################################################################################
#Função que verifica se a lista está vazia
def lista_vazia(lista):
    if len(lista) == 0:
        return True
    return False
###########################################################################################
#Função que inclui um item na lista Estudantes, Professores, Disciplinas ou Turmas
def incluir_na_lista(lista,item):
    lista.append(item)
    salvar_json()
###########################################################################################
#Função que localiza se código está na lista Estudantes, Professores, Disciplinas ou Turmas
def localizar_na_lista(lista,codigo):
    count = 1
    if lista_vazia(lista):
        return False
    for item in lista:
        if codigo == item['codigo']:
            return count
        count +=1
    return False
###########################################################################################
#Função que irá excluir das listas Estudantes, Professores, Disciplinas ou Turmas
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
        input ('Pressione ENTER para continuar.')
    else:
        print (f'[AVISO] Código {codigo} não localizado na lista de {assunto}.')
        input ('Pressione ENTER para continuar.')
    salvar_json()
###########################################################################################
#Função que verifica se a matrícula já está cadastrada na lista de matrículas
def matricula_ja_existe(matricula):
    count = 1
    if not lista_vazia(matriculas):
        for item in matriculas:
            if matricula == item:
                return count
            count +=1
    return False
###########################################################################################
#Função que edita matrícula
#Aqui optei por editar no mesmo índice
def editar_matricula():
    if lista_vazia(matriculas):
        print (f'Lista de {assunto} vazia, sem itens para excluir.')
        return
    matricula = dados_matricula()
    indice = matricula_ja_existe(matricula)
    if indice:
        print ('Matrícula localizada, agora insira os novos dados para alteração.\n')
        matricula_nova = dados_matricula()
        if matricula_nova != None:
            if matricula_ja_existe(matricula_nova):
                print (f'{matricula_nova} já foi cadastrada anteriormente.')
            else:
                matriculas[indice-1] = matricula_nova
                print (f'{matricula_nova} cadastrada com sucesso.')
    else:
        print ('Matrícula não localizada.')
    salvar_json()
###########################################################################################
#Função que exclui matrícula
def excluir_matricula():
    if lista_vazia(matriculas):
        print (f'Lista de {assunto} vazia, sem itens para excluir.')
        return
    matricula = dados_matricula()
    indice = matricula_ja_existe(matricula)
    if indice:
        del matriculas[indice-1]
    else:
        print ('Matrícula não localizada.')
    salvar_json()
###########################################################################################
#Função que atualiza dados de Estudantes, Professores, Disciplinas ou Turmas
#Aqui optei por deletar o antigo e inserir um novo
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
        input ('Pressione ENTER para continuar.')
    salvar_json()
###########################################################################################
#Início do programa
dados = carregar_json() #lendo arquivo json
estudantes = dados['Estudantes'] #salvando os dados nas listas correspondentes
professores = dados['Professores']
disciplinas = dados['Disciplinas']
turmas = dados['Turmas']
matriculas = dados['Matrículas']
###########################################################################################
#Começando
while True:
    imprimir_menu_principal()
    try:
        opcao_principal = int(input('Por favor, selecione uma opção: '))
    except:
        print ('[AVISO] Por gentileza, digite apenas números para as opções\n')
        continue
###########################################################################################
# BLOCO DOS ESTUDANTES    
    if opcao_principal == 1:
        assunto = 'ESTUDANTES'
        while True:
            imprimir_menu_operacoes(assunto)
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
###########################################################################################
# BLOCO DOS PROFESSORES
    elif opcao_principal == 2:
        assunto = 'PROFESSORES'
        while True:
            imprimir_menu_operacoes(assunto)
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
###########################################################################################
# BLOCO DAS DISCIPLINAS
    elif opcao_principal == 3:
        assunto = 'DISCIPLINAS'
        while True:
            imprimir_menu_operacoes(assunto)
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
###########################################################################################
# BLOCO DAS TURMAS            
    elif opcao_principal == 4:
        assunto = 'TURMAS'
        while True:
            imprimir_menu_operacoes(assunto)
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
###########################################################################################
# BLOCO DAS MATRÍCULAS
    elif opcao_principal == 5:
        assunto = 'MATRÍCULAS'
        while True:
            imprimir_menu_operacoes(assunto)
            try:
                opcao_secundaria = int(input('Por favor, selecione uma opção: '))
            except:
                print('[AVISO] Por gentileza, digite apenas números para as opções\n')
                continue
            if opcao_secundaria == 1:
                #INSERIR
                matricula = dados_matricula()
                if matricula != None:
                    if matricula_ja_existe(matricula):
                        print (f'{matricula} já foi cadastrada anteriormente.')
                    else:
                        incluir_na_lista(matriculas,matricula)
                        print (f'{matricula} cadastrada com sucesso.')
            elif opcao_secundaria == 2:
                #LISTAR
                imprimir(matriculas,assunto)
            elif opcao_secundaria == 3:
                #ATUALIZAR
                editar_matricula()
            elif opcao_secundaria == 4:
                #EXCLUIR
                excluir_matricula()
            elif opcao_secundaria == 9:
                print ('Voltando ao menu principal.')
                break
            else:
                print ('Opção inválida.')
                continue
###########################################################################################            
    elif opcao_principal == 9:
        print('Sair')
        break
###########################################################################################
    else:
        print('Opção inválida')

salvar_json() #sempre salva ao encerrar para garantir que nada ficou sem ser salvo