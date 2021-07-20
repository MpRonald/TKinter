# -*- coding: utf-8 -*-
"""
Uma docstring é uma string no início de uma função que explica a interface 
(“doc” é uma abreviação para “documentação”). Aqui está um exemplo:
"""
import turtle

def polyline(t, n, length, angle):
    """Desenha os seguimentos de reta com o comprimento dado e
    ângulo (em graus) entre eles. t é um turtle
    """
    
    for i in range(n):
        t.fd(length)
        t.lt(angle)


"""
Por convenção, todas as docstrings têm aspas triplas, também conhecidas como 
strings multilinha porque as aspas triplas permitem que a string se estenda 
por mais de uma linha. É conciso, mas contém a informação essencial que alguém 
precisaria para usar esta função. Explica sucintamente o que a função faz 
(sem entrar nos detalhes de como o faz). Explica que efeito cada parâmetro tem 
sobre o comportamento da função e o tipo que cada parâmetro deve ser 
(se não for óbvio). Escrever este tipo de documentação é uma parte importante 
do projeto da interface. Uma interface bem projetada deve ser simples de 
explicar; se não for assim, talvez a interface possa ser melhorada.
"""