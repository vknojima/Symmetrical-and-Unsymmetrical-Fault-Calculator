import ast

################################################################### INSERINDO TODOS OS ELEMENTOS DO SISTEMA ###################################################################

barras_Sistema = [] # Armazanando as barras do sistema
ele_Sistema = [] # Armazenando os elementos do sistema
num_barras = int(input("Quantas barras o Sistema de Potencia tem: "))

class Barras():
    def __init__(self, nome: str, Vb: float):
        self.nome = "B" + nome
        self.Vb = Vb

for _ in range(num_barras):
    print("Barra:")
    nome_barra = input("Numeracao da barra (e.g. 1, 2, etc) ")
    tensao_base_barra = float(input("Tensao base na barra em kV: "))
    barra = Barras(nome_barra, tensao_base_barra)
    barras_Sistema.append(barra)

class Maquina():    
    def __init__(self, nome: str, Vn: float, Sn: int, x_pos: float, barras_conectadas: list): # Construtor (Criando o objeto e atribuindo dados a ele)
        self.nome = "M" + nome
        self.Vn = Vn
        self.Sn = Sn
        self.x_pos = x_pos # reatância subtransitória em PU e na base do sistema
        self.barras_conectadas = [0] * num_barras
        for i in range(len(barras_conectadas)):
            if barras_conectadas[i] > num_barras:
                print("Número da barra é maior que a quantidade totais de barras.")
                break 
            loc_SelfBarras_Conectadas = barras_conectadas[i]-1
            self.barras_conectadas[loc_SelfBarras_Conectadas] = self.barras_conectadas[loc_SelfBarras_Conectadas] + 1

class LinhaTransmissao():
    def __init__(self, nome: str, Sn: int, x_pos: float, barras_conectadas: list):
        self.nome = "LT" + nome
        self.Sn = Sn
        self.x_pos = x_pos # reatância subtransitória em PU e na base do sistema
        self.barras_conectadas = [0] * num_barras
        for i in range(len(barras_conectadas)):
            if barras_conectadas[i] > num_barras:
                print("Número da barra é maior que a quantidade totais de barras.")
                break 
            loc_SelfBarras_Conectadas = barras_conectadas[i]-1
            self.barras_conectadas[loc_SelfBarras_Conectadas] = self.barras_conectadas[loc_SelfBarras_Conectadas] + 1

class Transformador():
    def __init__(self, nome: str, Sn: int, x_pos: float, barras_conectadas: list):
        self.nome = "TRAFO" + nome
        self.Sn = Sn
        self.x_pos = x_pos # reatância subtransitória em PU e na base do sistema
        self.barras_conectadas = [0] * num_barras
        for i in range(len(barras_conectadas)):
            if barras_conectadas[i] > num_barras:
                print("Número da barra é maior que a quantidade totais de barras.")
                break 
            loc_SelfBarras_Conectadas = barras_conectadas[i]-1
            self.barras_conectadas[loc_SelfBarras_Conectadas] = self.barras_conectadas[loc_SelfBarras_Conectadas] + 1

print("Inseriu todas as máquinas do sistema? Digitar: Sair.")
while True:
    nome_maquina = input("Número da Máquina no Sistema (e.g. 1, 2, etc): ")
    if nome_maquina == "Sair":
        break
    else:
        tensao_nominal_maquina = float(input("Tensao nominal da maquina: "))
        potencia_nominal_maquina = int(input("Potencia nominal da maquina: "))
        reatancia_positiva_maquina = float(input("Reatancia positiva subtransitoria da maquina: "))
        barra_conectada_maquina = list(map(int, ast.literal_eval(input("Barra conectada com a máquina (inserir como uma lista, ex: [1, 2, 3]): "))))
        maquina = Maquina(nome_maquina, tensao_nominal_maquina, potencia_nominal_maquina, reatancia_positiva_maquina, barra_conectada_maquina)
        ele_Sistema.append(maquina)

print("Inseriu todas as linhas de transmissoes do sistema? Digitar: Sair.")
while True:
    nome_linha = input("Nome da LT no sistema (e.g. 1, 2, etc): ")
    if nome_linha == "Sair":
        break
    else:
        potencia_nominal_linha = int(input("Potencia nominal da linha: "))
        reatancia_positiva_linha = float(input("Reatancia positiva subtransitoria da linha: "))
        barra_conectada_linha = list(map(int, ast.literal_eval(input("Barras conectadas com a linha (inserir como uma lista, ex: [1, 2]): "))))
        linha = LinhaTransmissao(nome_linha, potencia_nominal_linha, reatancia_positiva_linha, barra_conectada_linha)
        ele_Sistema.append(linha)

print("Inseriu todos os transformadores do sistema? Digitar: Sair.")
while True:
    nome_trafo = input("Número do transformador no sistema (e.g. 1, 2, etc): ")
    if nome_trafo == "Sair":
        break
    else:
        razao_trafo = float(input("Razao de tensao do transformador do primario para o secundario: "))
        potencia_nominal_trafo = int(input("Potencia nominal do transformador: "))
        reatancia_positiva_trafo = float(input("Reatancia positiva subtransitoria do transformador: "))
        barra_conectada_trafo = list(map(int, ast.literal_eval(input("Barras conectadas com o transformador (inserir como uma lista, ex: [1, 2]): "))))
        trafo = Transformador(nome_trafo, potencia_nominal_trafo, reatancia_positiva_trafo, barra_conectada_trafo)
        ele_Sistema.append(trafo)

################################################################### FUNÇÕES AUXILIARES PARA REALIZAR TESTES ###################################################################

def print_elements():
    for i in range(len(ele_Sistema)):
        if ele_Sistema[i].nome[0] == "M":
            print(ele_Sistema[i].nome, ele_Sistema[i].Vn, ele_Sistema[i].Sn, ele_Sistema[i].x_pos, ele_Sistema[i].barras_conectadas)
        elif ele_Sistema[i].nome[0] == "L":
            print(ele_Sistema[i].nome, ele_Sistema[i].Sn, ele_Sistema[i].x_pos, ele_Sistema[i].barras_conectadas)
        else:
            print(ele_Sistema[i].nome, ele_Sistema[i].Sn, ele_Sistema[i].x_pos, ele_Sistema[i].barras_conectadas)

################################################################### CALCULANDO YBARRA E ZBARRA ###################################################################