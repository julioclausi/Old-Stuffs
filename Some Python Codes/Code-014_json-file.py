import json

def escrever(data,arquivo):
    with open (arquivo,'w') as f:
        json.dump(data,f)
        f.close()

def ler(arquivo):
    dados = {}
    try:
        with open (arquivo,'r') as f:
            dados = json.load(f)
            f.close()
            return dados
    except FileNotFoundError:
        print ('Arquivo não encontrado')
dicionario = [{"Nome": "João", "Sobrenome": "Silva"},
              {"Nome": "Maria 1", "Sobrenome": "Ferreira"},
              {"Nome": "Maria 2", "Sobrenome": "Ferreira"},
              {"Nome": "Maria 3", "Sobrenome": "Ferreira"},
              {"Nome": "Maria 4", "Sobrenome": "Ferreira"},
              {"Nome": "Maria 5", "Sobrenome": "Ferreira"}]

for i in range(0,len(dicionario)):
    print (dicionario[i])
escrever (dicionario,"my_file_for_code_014.json")
dadosretornados = ler ("my_file_for_code_014.json")
print (dadosretornados)

print ('Maria 2 3 4 serão excluídas')
dadosretornados.pop(4)
dadosretornados.pop(3)
dadosretornados.pop(2)
print (dadosretornados)