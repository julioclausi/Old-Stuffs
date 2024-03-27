class HashItem:
    def __init__ (self,chave,valor):
        self.chave = chave
        self.valor = valor

class HashTable:
    def __init__ (self):
        self.tamanho = 5
        self.slots = [None for i in range (self.tamanho)]
        self.count = 0
        self.MAXLOADFACTOR = 0.65

    def _hash (self,chave):
        multiplicador = 1
        valor_hash = 0
        for letra in chave:
            valor_hash += multiplicador * ord(letra)
            multiplicador +=1
        return valor_hash % self.tamanho

    def put (self,chave,valor):
        item = HashItem (chave,valor)
        posicao = self._hash(chave)
        # esse while é para verificar se houve colisão, se sim faz sondagem linear e incrementa 1
        while self.slots[posicao]:
            if self.slots[posicao].chave == chave:
                # verifica se o item já existe na hash table
                break
            posicao = (posicao + 1) % self.tamanho
            # dessa forma não preciso fazer um IF para verificar se passou de 255 e devo voltar a 0
        if self.slots[posicao] is None:
            self.count += 1
        self.slots[posicao] = item
        # self.checkgrowth()

    def show (self):
        posicao = 0
        print ('\nPos -> Chave -> Valor')
        for item in self.slots:
            if item:
                print (f"{posicao:^3} ->{item.chave:^7}->{item.valor:^7}")
            posicao +=1
        print ()

    def verifica_tamanho (self):
        loadfactor = self.count / self.tamanho
        if loadfactor > self.MAXLOADFACTOR:
            print (f'Fator carga: {loadfactor}, Tamanho {self.tamanho}')
            self.aumenta_tamanho()
            print (f'Fator carga após aumento: {self.count / self.tamanho}, Tamanho {self.tamanho}')
    
    def aumenta_tamanho (self):
        nova_hash_table = HashTable()
        nova_hash_table.tamanho = self.tamanho * 2
        nova_hash_table.slots = [None for i in range(nova_hash_table.tamanho)]
        for item in self.slots:
            if item:
                nova_hash_table.put (item.chave,item.valor)
        self.tamanho = nova_hash_table.tamanho
        self.slots = nova_hash_table.slots

    def localiza_chave (self,chave):
        posicao = self._hash(chave)
        contador = 0
        while self.slots[posicao]:
            if self.slots[posicao].chave == chave:
                print (f'Localizado na posicao {posicao}. {chave} = {self.slots[posicao].chave}')
                print (f'Chave ({chave}) : Valor ({self.slots[posicao].valor})')
                return
            posicao = (posicao + 1) % self.tamanho
            contador +=1
            if contador > self.count:
                break
        print(f'{chave} não localizado!')

hashtable = HashTable()
hashtable.put('abc','menu')
hashtable.put('def','texto')
hashtable.put('ghi','dado')
hashtable.put('ad','item')
hashtable.verifica_tamanho()
hashtable.put('ga','arquivo')
hashtable.put('awd','botao')
hashtable.put('add','link')
hashtable.verifica_tamanho()
hashtable.show()
hashtable.localiza_chave('abc')
hashtable.localiza_chave('xyz')