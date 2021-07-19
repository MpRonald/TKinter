# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Tue Dec 15 11:11:57 2020
# 
# Curso de Python -> vlidação de dados no padrão Nacional (Brasil)
# """
# 
# # =============================================================================
# # # PARTE I -> VALIDAÇÃO DE CPF E ACESSANDO PYPI
# # =============================================================================
# 
# cpf = 12345678912
# tamanho_cpf = len(str(cpf))
# print(tamanho_cpf)
# 
# class Cpf:
#     def __init__(self, documento):
#         documento = str(documento)
#         if self.cpf_eh_valido(documento):
#             self.cpf = documento
#         else:
#             raise ValueError("Cpf Inválido!")
#             
#             
#     def __str__(self):
#         return self.format_cpf()
# 
#     def cpf_eh_valido(self, cpf):
#         if len(cpf) == 11:
#             validador = CPF()
#             return validador.validate(cpf)
#         else:
#             raise ValueError("Quantidade de Dígitos Inválida!")
#         
#     
#     def format_cpf(self):
#         mascara = CPF
#         return mascara.mask(self.cpf)
#             
#     
# 
# cpf = "11550042726"
# objeto_cpf = Cpf(cpf)
# print(objeto_cpf)
# 
# # fatiando strings
# 
# # logica de validação de cpf;
# 
# from validate_docbr import CPF
# 
# cpf = CPF()
# print(cpf.validate("11550042726"))
# 
# cpf_um = Cpf("11550042726")
# print(cpf_um)
# 
# 
# 
# 
# # =============================================================================
# # VALIDANDO CNPJ
# # =============================================================================
# 
# 
# from validate_docbr import CNPJ
# 
# exemplo_cnpj = "04952717000194"
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
# 
# 
# 
# class Cnpj:
#     
#     def __init__(self, documento, tipo_doc):
#         self.tipo_doc = tipo_doc
#         documento = str(documento)
#         if tipo_doc == "cpf":
#             if self.cnpj_eh_valido(documento):
#                 self.cnpj = documento
#             else:
#                 raise ValueError("Cpf Inválido!")
#         else:
#             self.tipo_doc == "cnpj"
#             
#     def __str__(self):
#         return self.format_cnpj()
# 
#     def cnpj_eh_valido(self, cnpj):
#         if len(c) == 14:
#             validador_cnpj = CNPJ()
#             return validador_cnpj.validate(cnpj)
#         else:
#             raise ValueError("Quantidade de Dígitos Inválida!")
#         
#     def format_cpf(self):
#         mascara = cnpj
#         return mascara.mask(self.cnpj)
# 
# 
# 
# exemplo_cnpj = "04952717000194"
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))
# 
# 
# =============================================================================

# =============================================================================
# REFATORANDO CÓDIGO:
# =============================================================================
from validate_docbr import CNPJ
from validate_docbr import CPF
 
class documento:
    
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Documento Inválido!")
   

class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Cpf Inválido!")
            
    def __str__(self):
        return self.format()
    
    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Cpf Inválido!")
            
    def __str__(self):
        return self.format()
    
    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    
    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)



cpf_um = "11550042726"
doc_cpf = documento.cria_documento(cpf_um)
print(doc_cpf)

cpf_err = "22654475148"
doc_cpf = documento.cria_documento(cpf_err)
print(doc_cpf)

cnpj_test = "04952717000194"
doc_cnpj = documento.cria_documento(cnpj_test)
print(doc_cnpj)


# =============================================================================
# PARTE III
# VALIDANDO TELEFONES E EMAILS COM EXPRESSOES REGULARES
# =============================================================================

import re
padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao, texto)
print(resposta.group())

# criando padrao para email;
padrao2 = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto2 = "luciene@yahoo.com.br"


resposta2 = re.search(padrao2, texto2)
print(resposta2.group())



# definindo padrao para telefones;

telefone = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "eu gosto do numero 2127431678 e gosto tbm do 2126429494"
resposta_tel = re.findall(telefone, texto)
print(resposta_tel)
# o re.search() -> retorna só o primeiro elemento;
# o re.findall() -> retorna todos os elementos encontrados;

class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
           self.numero = telefone
        else:
            raise ValueError("Número Incorreto!")
    
    
    def valida_telefone(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, texto)
        if resposta:
            return True
        else:
            return False
        
    def __str__(self):
        return self.format_numero()
        
    def format_numero(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, telefone)
        numero_formatado = f"+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"
        return numero_formatado
                            


telefone = "26420971"
telefone_obj = TelefonesBr(telefone)

telefone2 = "2121205531"
telefone_obj2 = TelefonesBr(telefone2)

telefone3 = "552121205531"
telefone_obj3 = TelefonesBr(telefone3)
print(telefone_obj3)



# criando mascara para numero de telefone;

telefone = "552126429464"
telefone_obj1 = TelefonesBr(telefone)
print(telefone_obj1)


# TRABALHANDO COM DATAS;

from datetime import datetime, timedelta
print(datetime.today())

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
        
    def __str__(self):
        return self.format_data()
        
    def mes_cadastro(self):
        meses_do_ano = ["janeiro","fevereiro", "março", "abril",
                        "maio", "junho", "julho", "agosto",
                        "setembro", "outubro", "novembro", "dezembro"]
       
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]
    
    def dia_semana(self):
        dia_semana_lista = ["segunda", "terça", "quarta", "quinta",
                      "sexta", "sabado", "domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
    
    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() + timedelta(days=30) - self.momento_cadastro
        return tempo_cadastro
    

cadastro = DatasBr()
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())


# FORMATANDO datetime para padrao brasileiro;
hoje = datetime.today()
hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M")
print(hoje_formatado)


cadastro = DatasBr()
print(cadastro)

# =============================================================================
# TRABALHANDO COM CEP E ACESSANDO UMA API
# =============================================================================
import requests
class BuscaEndereco:
    
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_e_valido(cep):
            self.cep = cep
        else:
            raise ValueError("Cep não existe!")
            
    def __str__(self):
        return self.format_cep()
    
    def cep_e_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
        
    def format_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])
    
    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return(
            dados['bairro'],
            dados['localidade'],
            dados['uf']
            )





cep = 25955040
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

import requests

r = requests.get("http://viacep.com.br/ws/01001000/json/")
print(r.text)

a = objeto_cep.acessa_via_cep()
print(dir(a))

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)




























































































