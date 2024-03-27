class HashItem:
    def __init__ (self,chave,valor):
        self.chave = chave
        self.valor = valor

# Vou criar uma tabela hash com tamanho fixo de 256, então não irei tratar colisões no momento
# A fórmula para calcular a posição será transformar cada letra em valor ordinal com a função ord() e multiplicar pela posição começando em 1
# H -> 72
# e -> 202
# l -> 324
# l -> 432
# o -> 555
#   -> 192
# W -> 609
# o -> 888
# r -> 1026
# l -> 1080
# d -> 1100
# Aí somar todos os resultados pegar o resto da divisão por 256 (que é o tamanho da lista)
# Dessa forma já resolvo alguns conflitos como "Hello World" ser diferente de "World Hello"
class HashTable:
    def __init__ (self):
        self.tamanho = 256
        self.slots = [None for i in range (self.tamanho)]
        # slots vai de 0 a 255
        self.count = 0

    def _hash (self,chave):
        multiplicador = 1
        valor_hash = 0
        for letra in chave:
            valor_hash += multiplicador * ord(letra)
            multiplicador +=1
        return valor_hash % self.tamanho

hashtable = HashTable()
