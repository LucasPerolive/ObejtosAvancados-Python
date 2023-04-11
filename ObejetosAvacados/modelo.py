# Criando a classe mãe chamada PROGRAMA
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes
    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

# Todo objeto tem que saber se auto imprimir
    def __str__(self):
        return f' {self._nome} - {self.ano} - {self._likes} Likes'

# Criando o objeto FILME
# "super" chama a classe mãe
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

# Todo objeto tem que saber se auto imprimir
    def __str__(self):
        return f' {self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

# Criando o objeto PROGRAMA
# "super" chama a classe mãe
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

#Todo objeto tem que saber se auto imprimir
    def __str__(self):
        return f' {self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

# Cria a Playlist 
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

# Faz com que o objeto seja interável - Faz com que deixe eu usar o FOR IN, IN, pegar um item específico com o índice, etc. 
    def __getitem__(self, item):
        return self._programas[item]

# Faz com que eu possa olhar seu tamanho devido ao comportamento
    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas
    
    @property
    def tamanho(self):
        return len(self._programas)









# Adiconando valores aos objetos
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100) 
demolidor = Serie('Demolidor', 2016, 2)

# Dar like nos filme e nos programas
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
demolidor.dar_like()
demolidor.dar_like()

# Adciona os filmes e programas na playlist
filmes_e_series = [vingadores, atlanta, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

# Mostra o tamanho da playlist (quantidade de programas e filmes juntos)
print(f'Tamanho do playlist: {len(playlist_fim_de_semana )}')

len(playlist_fim_de_semana)

# Mostra o catalago da playlist
for programa in playlist_fim_de_semana:
    print(programa)