# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:46:19 2020

CURSO ALURA PYTHON COLECTIONS == CONJUNTOS E DICIONÁRIOS
"""

# =============================================================================
# Trabalhando com Conjuntos, os SETS
# =============================================================================

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = []
assistiram.extend(usuarios_data_science) 
# extend recebe uma coleção e passa por cada dado da lista;
assistiram # aqui foi feito uma cópia da lista usuarios_data_science


# usando o shalow copy;
assistiram = usuarios_data_science.copy() # realizando copia 
assistiram.extend(usuarios_machine_learning) # extendendo a lista 
assistiram

# observando, quando a copia e extensão foram feitas, alguns
# elementos foram repetidos;

# Tranformando uma lista num conjunto ==> set()
# o set() não repete valores;
set(assistiram)  # criando um conjunto;

# podemos iterar com sets
for usuario in set(assistiram):
    print(usuario)

# =============================================================================
# FAZENDO OPERÇÕES COM CONJUNTOS
# =============================================================================

# verificando os itens repetidos nos dois cnjuntos
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

usuarios_data_science & usuarios_machine_learning

# chamando itens que estão em data_science que não estão em machine;
usuarios_data_science - usuarios_machine_learning

for usuario in usuarios_data_science & usuarios_machine_learning:
    print(usuario)

# chamando apenas usuarios que esta em apenas um set;
usuarios_data_science ^ usuarios_machine_learning

# modificando os sets;
usuarios = {1, 5, 76, 34, 52, 13, 17}
len(usuarios)

# incluindo dados ao set;
usuarios.add(765)
usuarios

# tornando o set imutavel;
usuarios = frozenset(usuarios)
type(usuarios)

usuarios.add(199)  # quando modificamos para frozenset, o set fica congelado;
usuarios

# utilizando sets com strings;
meu_texto = "Toddy Toddy guaraná Toddy o melhor Toddy guaraná toddy guaraná"
set(meu_texto.split())

# =============================================================================
# #TRABALHANDO COM DICIONARIO
# =============================================================================

# criando um dicionario;
aparicoes = dict(Ronald=1, Luciene=2, Toddy=3)
aparicoes


# adicionando elementos;
aparicoes["Flamengo"] = 4
aparicoes

# substituindo elementos pela chave;
aparicoes["Ronald"] = 5
aparicoes

# removendo elementos;
del aparicoes["Flamengo"]
aparicoes

# verificando elementos;
"Toddy" in aparicoes

# iterando dicionarios;
for elemento in aparicoes:
    print(elemento)

# na iteração será retornado a chave do dicionário;
# =============================================================================
# =============================================================================

# iterando através das chaves;
for elemento in aparicoes.keys():
    print(elemento)

# iterando através das valores;
for elemento in aparicoes.values():
    print(elemento)

# iterando com chave-valor -> forma 01
for elemento in aparicoes.keys():
    print(elemento, aparicoes[elemento])

# iterando com chave-valor -> forma 02
for elemento in aparicoes.items():
    print(elemento)
# neste formato será retornado como tupla;

# desempacotando forma 02;
for chave, valor in aparicoes.items():
    print(chave, "=", valor)

# =============================================================================
# =============================================================================

meu_texto = "Toddy Toddy guaraná Toddy o melhor Toddy guaraná toddy guaraná"

# contando quantidade de repetições;
meu_texto = meu_texto.lower()
meu_texto

meu_texto.split()

aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

aparicoes

# utilizando o dafultdict para contar itens do dicionario;
from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
    ate_agora = aparicoes[palavra]
    aparicoes[palavra] = ate_agora + 1

aparicoes

class Conta:
    def __init__(self):
        print("Criando conta")


contas = defaultdict(Conta)
contas[15]
contas[16]

# utilizando o counter;
from collections import Counter

aparicoes = Counter()
for palavra in meu_texto.split():
    aparicoes[palavra] += 1
    
aparicoes

# refatorando codigo acima;
aparicoes = Counter(meu_texto.split())
aparicoes

# =============================================================================
# =============================================================================
from collections import defaultdict
from collections import Counter
# testando o uso de diversas coleções;

texto1 = """A treinadora Pia Sundhage convocou nesta segunda-feira 23 
jogadoras para um período de treinos entre 5 e 20 de janeiro em Viamão, no
Rio Grande do Sul. A meia Marta, cortada os amistosos contra o Equador por 
ter testado positivo para Covid-19, está de volta ao grupo, assim como a 
atacante Bia Zaneratto, uma das jogadoras mais convocadas pela técnica do 
Brasil. Quatro jogadoras foram chamadas pela primeira vez pela treinadora 
sueca: as goleiras Viviane e Nicole e as meias Ingryd e Kerolin, que está sem 
clube após cumprir dois anos de suspensão por doping. Na entrevista coletiva 
após anunciar a lista, Pia afirmou que a lista para Tóquio ainda está aberta 
a possíveis novidades.Eu espero que alguém nos surpreenda, sim, uma nova 
jogadora. Eu fico sempre muito empolgada com as convocações, e sempre 
existe a chance (de novidades). Sim, temos as nossas jogadoras principais, 
mas se a gente olhar ao redor, eu teria aí oito, nove jogadoras, e eu quero 
criar uma competitividade entre elas e quero sentir que elas têm sim uma 
chance - declarou a treinadora."""

texto2 = """Desta forma, médicos e preparadores físicos do grupo profissional 
passarão a atuar também no sub-20 em jogos e treinos, através de uma 
programação estipulada previamente. Em alguns dias eles estarão nos juniores 
e, em outros, no profissional.O processo será conduzido por Marcio Tannure, 
gerente do Departamento de Saúde e Alto Rendimento do Flamengo, e foi 
aprovado pelo vice-presidente de futebol, Marcos Braz, e pelo diretor de 
futebol, Bruno Spindel. Em alguns casos, a integração já começou. Um exemplo 
é o atacante Guilherme Bala, do sub-20, que teve uma lesão muscular na 
coxa direita e vem se tratando com fisioterapeutas do profissional."""

Counter(texto1.lower())
# contando a quantidade de letras;

def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))
  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print("{} => {:.2f}%".format(caractere, proporcao * 100))

analisa_frequencia_de_letras(texto1)

analisa_frequencia_de_letras(texto2)



















































































































