import ast
import numpy as np

################################################################### INSERINDO TODOS OS ELEMENTOS DO SISTEMA ###################################################################

barras_Sistema = [] # Armazanando as barras do sistema
ele_Sistema = [] # Armazenando os elementos do sistema

num_barras = 7 # Inserir essa variável de acordo com o número de barras do sistema (Esse teste é feito desse jeito porque é mais rápido)

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
        self.barras_conectadas_1 = barras_conectadas
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
    def __init__(self, nome: str, Sn: int, x_pos: complex, x_zero: complex, x_aterramento: complex, barras_conectadas: list, conex_trafo: str):
        self.nome = "T" + nome
        self.Sn = Sn
        self.x_pos = x_pos # reatância subtransitória em PU e na base do sistema
        self.x_neg = x_pos
        self.x_zero = x_zero
        self.x_aterramento = x_aterramento
        self.barras_conectadas = [0] * num_barras
        self.conex_trafo = conex_trafo # O primário corresponde a barra na primeira posição da lista "barras_conectadas" e o secundário a barra da segunda posição.
        self.list_conex_trafo = conex_trafo.split("-")
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

def print_elements(): # Atualizar, pois adicionei atributos novos para as classes do sistema
    for i in range(len(ele_Sistema)):
        if ele_Sistema[i].nome[0] == "M":
            print(ele_Sistema[i].nome, ele_Sistema[i].Vn, ele_Sistema[i].Sn, ele_Sistema[i].x_pos, ele_Sistema[i].x_zero, ele_Sistema[i].conex_ger, ele_Sistema[i].x_aterramento, ele_Sistema[i].barras_conectadas, "\n")
        elif ele_Sistema[i].nome[0] == "L":
            print(ele_Sistema[i].nome, ele_Sistema[i].Sn, ele_Sistema[i].x_pos, ele_Sistema[i].x_zero, ele_Sistema[i].barras_conectadas, "\n")
        else:
            print(ele_Sistema[i].nome, ele_Sistema[i].Sn, ele_Sistema[i].x_pos, ele_Sistema[i].x_zero, ele_Sistema[i].x_aterramento, ele_Sistema[i].barras_conectadas,  ele_Sistema[i].list_conex_trafo, "\n")

def admitancia(impedancia):
    return 1/impedancia

def round_3(valor):
    return np.round(valor, 3)

def transformadaFontescue(X_zero, X_pos, X_neg):
    X_a = X_zero + X_pos + X_neg
    X_b = X_zero + X_pos*(-0.5-0.866j) + X_neg*(-0.5+0.866j)
    X_c = X_zero + X_pos*(-0.5+0.866j) + X_neg*(-0.5-0.866j)
    return [[float(round_3(np.abs(X_a))), float(round_3(np.angle(X_a, deg=True)))], [float(round_3(np.abs(X_b))), float(round_3(np.angle(X_b, deg=True)))], [float(round_3(np.abs(X_c))), float(round_3(np.angle(X_c, deg=True)))]]

def correnteBase(barraFalta):
    return ((100*10**6)/(np.sqrt(3)*barraFalta.Vb*10**3))/(10**3) # Em kA

################################################################### CALCULANDO YBARRA E ZBARRA DE SEQ. POS., NEG. E ZERO ###################################################################

def Ybarra_pos_neg():
    Ybarra = np.zeros((num_barras, num_barras), dtype=complex) 
    for i in range(len(ele_Sistema)):
        if ele_Sistema[i].nome[0] == "M": 
            for j in range(len(ele_Sistema[i].barras_conectadas)):
                if ele_Sistema[i].barras_conectadas[j] == 1:
                    Ybarra[j,j] += round_3(admitancia(ele_Sistema[i].x_pos))
                    break
        else:
            pos_EntreBarras = []
            for j in range(len(ele_Sistema[i].barras_conectadas)):
                if ele_Sistema[i].barras_conectadas[j] == 1:
                    pos_EntreBarras.append(j)
                    Ybarra[j,j] += round_3(admitancia(ele_Sistema[i].x_pos))
            Ybarra[pos_EntreBarras[0],pos_EntreBarras[1]] += round_3(-admitancia(ele_Sistema[i].x_pos))
            Ybarra[pos_EntreBarras[1],pos_EntreBarras[0]] += round_3(-admitancia(ele_Sistema[i].x_pos))
    return Ybarra

def Ybarra_zero():
    Ybarra = np.zeros((num_barras, num_barras), dtype=complex)
    for i in range(len(ele_Sistema)):
        if ele_Sistema[i].nome[0] == "M": # Acessando um elemento do tipo Máquina Síncrona
            if ele_Sistema[i].conex_ger == "Y_aterrado": # Nesse caso, vamos adicionar as impedâncias que estão conecatadas na respectiva barra
                for j in range(len(ele_Sistema[i].barras_conectadas)):
                    if ele_Sistema[i].barras_conectadas[j] == 1:
                        x_serie = ele_Sistema[i].x_zero + (ele_Sistema[i].x_aterramento)*3
                        Ybarra[j,j] += round_3(admitancia(x_serie))
                        break # Estou sempre considerando que o gerador está conecatado a somente uma barra
            # Se a conexão de aterramento for "D" ou "Y", não vamos adicioanar ou modificar nada
        elif ele_Sistema[i].nome[0] == "L": # Acessando um elemento do tipo Linha de Transmissão
            pos_EntreBarras = []
            for j in range(len(ele_Sistema[i].barras_conectadas)):
                if ele_Sistema[i].barras_conectadas[j] == 1:
                    pos_EntreBarras.append(j)
                    Ybarra[j,j] += round_3(admitancia(ele_Sistema[i].x_zero))
            Ybarra[pos_EntreBarras[0],pos_EntreBarras[1]] += round_3(-admitancia(ele_Sistema[i].x_zero))
            Ybarra[pos_EntreBarras[1],pos_EntreBarras[0]] += round_3(-admitancia(ele_Sistema[i].x_zero))
        else: # Acessando um elemento do tipo Transformador
            if ele_Sistema[i].list_conex_trafo == ["Y_aterrado","D"] or ["D","Y_aterrado"]:
                pos_EntreBarras = []
                posicao = 0
                x_serie = ele_Sistema[i].x_zero + (ele_Sistema[i].x_aterramento)*3
                if ele_Sistema[i].list_conex_trafo[1] == "Y_aterrado":
                    posicao = 1
                for j in range(len(ele_Sistema[i].barras_conectadas)):
                    if ele_Sistema[i].barras_conectadas[j] == 1:
                        pos_EntreBarras.append(j)
                Ybarra[pos_EntreBarras[posicao],pos_EntreBarras[posicao]] += round_3(admitancia(x_serie))
            elif ele_Sistema[i].list_conex_trafo == ["Y_aterrado","Y_aterrado"]:
                x_serie = 2*(3*(ele_Sistema[i].x_aterramento)) + ele_Sistema[i].x_zero
                pos_EntreBarras = []
                for j in range(len(ele_Sistema[i].barras_conectadas)):
                    if ele_Sistema[i].barras_conectadas[j] == 1:
                        pos_EntreBarras.append(ele_Sistema[i].barras_conectadas[j])
                Ybarra[pos_EntreBarras[0],pos_EntreBarras[1]] += round_3(-admitancia(x_serie))
                Ybarra[pos_EntreBarras[1],pos_EntreBarras[0]] += round_3(-admitancia(x_serie))
    return Ybarra            

def Zbarra(Ybarra):
   return np.round(np.linalg.inv(Ybarra), 3)

################################################################### CURTO CIRCUITO SIMÉTRICO ###################################################################

def correnteFaltaTrifasica(barraFalta, Zbarra_pos):
    #Considerando um curto na fase "a"
    Vpf = 1 + 0j
    numero = int(barraFalta.nome[1])-1
    If = Vpf/(Zbarra_pos[numero,numero])
    return If

def correnteContribuicao(If, barraFalta, Zbarra_pos):
    numero = int(barraFalta.nome[1])-1
    tensoesBarras = {} # Tensoes das barras sem correção
    correntesDeContribuicao = {} # Correntes de contribuicao
    Vpf = 1 + 0j
    for i in range(len(ele_Sistema)):
        if ele_Sistema[i].nome[0] == "M": #Maquina
            barra = int(ele_Sistema[i].nome[1])-1
            V_pos = Vpf - If*(Zbarra_pos[numero,barra])
            Vabc = transformadaFontescue(0, V_pos, 0)
            tensoesBarras[ele_Sistema[i].nome] = Vabc
            Icontribuicao_pos = (Vpf-V_pos)/(ele_Sistema[i].x_pos)
            Iabc_contribuicao = transformadaFontescue(0, Icontribuicao_pos*correnteBase(barras_Sistema[2]), 0)
            correntesDeContribuicao[ele_Sistema[i].nome] = Iabc_contribuicao
    
    return tensoesBarras, correntesDeContribuicao

# def correcaoContricuicao(): # Analisar o grupo de tensões e os transformadores. Onde o curto está sendo realizado?

################################################################### CURTO CIRCUITO ASSIMÉTRICO ###################################################################

