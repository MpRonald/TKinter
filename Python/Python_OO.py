# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 17:30:19 2020

Curso Python OO - Parte II
"""

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    def __str__(self):
        return f''

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0
    
    def __str__(self):
        return(f'{self._nome} - {self.ano} - {self.duracao} - {self._likes} likes.')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0
        
    def __str__(self):
        return(f'{self._nome} - {self.ano} - {self.temporadas} - {self._likes} likes.')



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_likes()
cabana = Filme('A Cabana', 2018, 135)
cabana.dar_likes()
cabana.dar_likes()
cabana.dar_likes()
community = Serie('Community', 2009, 6)
community.dar_likes()
community.dar_likes()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()
atlanta.dar_likes()

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
        
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
       return len(self._programas)

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano}')
  

filmes_e_series = [vingadores, atlanta, cabana, community]
playlist_fds = Playlist('Fim de Semana', filmes_e_series)

len(playlist_fds)

for programa in playlist_fds.listagem:
    print(programa)

print(f'Tamanho do playlist: {len(playlist_fds)}')

print(playlist_fds[0])

# =============================================================================
# Aula 5   
# =============================================================================

class Funcionario:
    def __init__(self, nome):
        self.nome = nome
    
    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostra_tarefas(self):
        print('Fez muita coisa...')
        
class Caelum(Funcionario):
    def mostra_tarefas(self):
        print('Fez muita coisa, Caelumer')
        
    def busca_curso_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando curso desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')
        
    def busca_pergunta_sem_resposta(self):
        print('Mostrando perguntas não respondidas no fórum.')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass


class Senior(Alura, Caelum, Hipster):
    pass
    


jose = Junior()
jose.busca_pergunta_sem_resposta()

luan = Pleno()
luan.busca_pergunta_sem_resposta()
luan.busca_curso_mes

luan.mostrar_tarefas()

luan = Senior('Luan')
print(luan)





























