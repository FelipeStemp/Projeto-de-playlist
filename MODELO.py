class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self.ano = ano
        self._like = 0

    @property  # usando para indicar  metodos GET
    def like(self):
        return self._like  # retornando __like para os demais

    def dar_like(self):
        self._like += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter  # setando novo nome
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self): # metodo especial qu faz a representação textual do obj
        return f'{self._nome} - {self.ano} - {self._like}'


# classes filhas
class Filme(Programa): # class clase_filha(classe_mae) mostrando como herdar classes
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # utilizado para metodo de herança puxando atributos da classe mae
        self.duracao = duracao
    def __str__(self): # metodo especial qu faz a representação textual do obj
        return f'{self._nome} - {self.ano} - {self.duracao} - {self._like}'

class Serie(Programa):
    def __init__(self, nome, ano, temp):
        super().__init__(nome, ano)
        self.temp = temp

    def __str__(self): # metodo especial qu faz a representação textual do obj
        return f'{self._nome} - {self.ano} - {self.temp} - {self._like}'

class Playlist: # herdando class list
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item): # metodo para utilizar itens de uma class \\ python data mode
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self): #metodo para informar que a listagem interna pode ter o len()
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
witcher = Serie('witcher', 2018, 2)
tmep = Filme('todo em p', 1999, 100)
demolidor = Serie('demolidor', 2019, 5)

tmep.dar_like()
demolidor.dar_like()
vingadores.dar_like()
witcher.dar_like()
witcher.dar_like()

serie_filme = [vingadores, witcher, tmep, demolidor] # lista
fim_de_semana = Playlist('fim de semana', serie_filme)

print(f'tamanho da playlist : {len(fim_de_semana)}')

for Programa in fim_de_semana: # consigo rodar desta maneira pois possuo o metodo __getitem__ para informar que o obj é interavel
    print(Programa) # consigo printar o programa com a função __str__

print(demolidor in fim_de_semana) # demolidor esta na lista fim de semana?