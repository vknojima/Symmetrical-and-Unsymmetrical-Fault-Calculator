import ast
import numpy as np

################################################################### INSERINDO TODOS OS ELEMENTOS DO SISTEMA ###################################################################

barras_Sistema = [] # Armazanando as barras do sistema
ele_Sistema = [] # Armazenando os elementos do sistema

num_barras = 4

# num_barras = int(input("Quantas barras o Sistema de Potencia tem: "))
# num_maquinas = int(input("Quantas maquinas o Sistema de Potencia tem: "))
# num_LT = int(input("Quantas linhas o sistema de Potencia tem: "))
# num_trafos = int(input("Quantos transformadores o sistema de Potencia tem: "))
# print("\n")

class Barras():
    def __init__(self, nome: str, Vb: float):
        self.nome = "B" + nome
        self.Vb = Vb

# for i in range(num_barras):
#     print("Barra:")
#     nome_barra = input("Numeracao da barra (e.g. 1, 2, etc) ")
#     tensao_base_barra = float(input("Tensao base na barra em kV: "))
#     barra = Barras(nome_barra, tensao_base_barra)
#     barras_Sistema.append(barra)
#     print("\n")

class Maquina():
    def __init__(self, nome: str, Vn: float, Sn: int, x_pos: complex, x_zero: complex, conex_ger: str, x_aterramento: complex, barras_conectadas: list): # Construtor (Criando o objeto e atribuindo dados a ele)
        self.nome = "M" + nome
        self.Vn = Vn
        self.Sn = Sn
        self.x_pos = x_pos
        self.xneg = x_pos
        self.x_zero = x_zero
        self.conex_ger = conex_ger # Na hora de montar a matriz de sequência zero, vamos considerar primeiro a variável "conex_ger". Se essas variável corresponder a um "Y aterrado", vamos utilizar a variável "x_aterramento", caso contrário "x_aterramento" será complementar descartado.
        self.x_aterramento = x_aterramento
        self.barras_conectadas = [0] * num_barras
        for i in range(len(barras_conectadas)):
            if barras_conectadas[i] > num_barras:
                print("Número da barra é maior que a quantidade totais de barras.")
                break 
            loc_SelfBarras_Conectadas = barras_conectadas[i]-1
            self.barras_conectadas[loc_SelfBarras_Conectadas] = self.barras_conectadas[loc_SelfBarras_Conectadas] + 1

class LinhaTransmissao():
    def __init__(self, nome: str, Sn: int, x_pos: complex, x_zero: complex, barras_conectadas: list):
        self.nome = "LT" + nome
        self.Sn = Sn
        self.x_pos = x_pos # reatância subtransitória em PU e na base do sistema
        self.xneg = x_pos
        self.x_zero = x_zero
        self.barras_conectadas = [0] * num_barras
        for i in range(len(barras_conectadas)):
            if barras_conectadas[i] > num_barras:
                print("Número da barra é maior que a quantidade totais de barras.")
                break 
            loc_SelfBarras_Conectadas = barras_conectadas[i]-1
            self.barras_conectadas[loc_SelfBarras_Conectadas] = self.barras_conectadas[loc_SelfBarras_Conectadas] + 1

class Transformador():
    def __init__(self, nome: str, Sn: int, x_pos: complex, x_zero: complex, barras_conectadas: list, conex_trafo: list):
        self.nome = "TRAFO" + nome
        self.Sn = Sn
        self.x_pos = x_pos # reatância subtransitória em PU e na base do sistema
        self.xneg = x_pos
        self.x_zero = x_zero
        self.barras_conectadas = [0] * num_barras
        self.conex_trafo = conex_trafo # O primário corresponde a barra na primeira posição da lista "barras_conectadas" e o secundário a barra da segunda posição.
        for i in range(len(barras_conectadas)):
            if barras_conectadas[i] > num_barras:
                print("Número da barra é maior que a quantidade totais de barras.")
                break 
            loc_SelfBarras_Conectadas = barras_conectadas[i]-1
            self.barras_conectadas[loc_SelfBarras_Conectadas] = self.barras_conectadas[loc_SelfBarras_Conectadas] + 1

# print("Inserir todas as maquinas do sistema:")

# for _ in range(num_maquinas):
#     nome_maquina = input("Numero da maquina no Sistema: ")
#     tensao_nominal_maquina = float(input("Tensao nominal da maquina em kV: "))
#     potencia_nominal_maquina = int(input("Potencia nominal da maquina em MVA: "))
#     reatancia_positiva_maquina = complex(input("Reatancia positiva subtransitoria da maquina: "))
#     reatancia_zero_maquina = complex(input("Reatancia zero subtransitoria da maquina: "))
#     barra_conectada_maquina = list(map(int, ast.literal_eval(input("Barra conectada com a máquina (inserir como uma lista, ex: [1, 2, 3]): "))))
#     maquina = Maquina(nome_maquina, tensao_nominal_maquina, potencia_nominal_maquina, reatancia_positiva_maquina, reatancia_zero_maquina, barra_conectada_maquina)
#     ele_Sistema.append(maquina)
#     print("\n")

# print("Inserir todas as linhas de transmissoes do sistema: ")
# for _ in range(num_LT):
#     nome_linha = input("Nome da LT no sistema: ")
#     potencia_nominal_linha = int(input("Potencia nominal da linha em MVA: "))
#     reatancia_positiva_linha = complex(input("Reatancia positiva subtransitoria da linha: "))
#     reatancia_zero_linha = complex(input("Reatancia zero subtransitoria da linha: "))
#     barra_conectada_linha = list(map(int, ast.literal_eval(input("Barras conectadas com a linha (inserir como uma lista, ex: [1, 2]): "))))
#     linha = LinhaTransmissao(nome_linha, potencia_nominal_linha, reatancia_positiva_linha, barra_conectada_linha)
#     ele_Sistema.append(linha)
#     print("\n")

# print("Inserir todos os transformadores do sistema: ")
# for _ in range(num_trafos):
#     nome_trafo = input("Número do transformador no sistema: ")
#     potencia_nominal_trafo = int(input("Potencia nominal do transformador em MVA: "))
#     reatancia_positiva_trafo = complex(input("Reatancia positiva subtransitoria do transformador: "))
#     reatancia_zero_trafo = complex(input("Reatancia zero subtransitoria do transformador: "))
#     barra_conectada_trafo = list(map(int, ast.literal_eval(input("Barras conectadas com o transformador (inserir como uma lista, ex: [1, 2]): "))))
#     trafo = Transformador(nome_trafo, potencia_nominal_trafo, reatancia_positiva_trafo, barra_conectada_trafo)
#     ele_Sistema.append(trafo)
#     print("\n")

################################################################### FUNÇÕES AUXILIARES ###################################################################

def print_elements():
    for i in range(len(ele_Sistema)):
        if ele_Sistema[i].nome[0] == "M":
            print(ele_Sistema[i].nome, ele_Sistema[i].Vn, ele_Sistema[i].Sn, ele_Sistema[i].x_pos, ele_Sistema[i].barras_conectadas)
        elif ele_Sistema[i].nome[0] == "L":
            print(ele_Sistema[i].nome, ele_Sistema[i].Sn, ele_Sistema[i].x_pos, ele_Sistema[i].barras_conectadas)
        else:
            print(ele_Sistema[i].nome, ele_Sistema[i].Sn, ele_Sistema[i].x_pos, ele_Sistema[i].barras_conectadas)

def admitancia(impedancia):
    return 1/impedancia

def round_3(valor):
    return np.round(valor, 3)

################################################################### CALCULANDO YBARRA E ZBARRA DE SEQ. POS., NEG. E ZERO ###################################################################

def Ybarra_pos_neg():
    Ybarra = np.zeros((num_barras, num_barras), dtype=complex)  # Initialize Ybarra as a complex matrix
    for i in range(len(ele_Sistema)):
        if sum(ele_Sistema[i].barras_conectadas) == 1: 
            for j in range(len(ele_Sistema[i].barras_conectadas)):
                if ele_Sistema[i].barras_conectadas[j] == 1:
                    Ybarra[j,j] += round_3(admitancia(ele_Sistema[i].x_pos))
                    break
        elif sum(ele_Sistema[i].barras_conectadas) == 2:
            pos_EntreBarras = []
            for j in range(len(ele_Sistema[i].barras_conectadas)):
                if ele_Sistema[i].barras_conectadas[j] == 1:
                    pos_EntreBarras.append(j)
                    Ybarra[j,j] += round_3(admitancia(ele_Sistema[i].x_pos))
            Ybarra[pos_EntreBarras[0],pos_EntreBarras[1]] += round_3(-admitancia(ele_Sistema[i].x_pos))
            Ybarra[pos_EntreBarras[1],pos_EntreBarras[0]] += round_3(-admitancia(ele_Sistema[i].x_pos))
    return Ybarra

def Zbarra_pos_neg(Ybarra):
   return np.round(np.linalg.inv(Ybarra), 3)

# print(Ybarra)
# print("\n")
# print(Zbarra)

################################################################### CURTO CIRCUITO TRIFÁSICO ###################################################################


 