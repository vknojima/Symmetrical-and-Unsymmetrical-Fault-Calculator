class Barras():
    def __init__(self, nome, Vb):
        self.nome = nome
        self.Vb = Vb

barras_Sistema = [] # Armazanando as barras do sistema

num_barras = int(input("Quantas barras o Sistema de Potencia tem: "))
for _ in range(num_barras):
    print("Barra:")
    nome_barra = input("Nome da barra (e.g. B1, B2, BX): ")
    tensao_base_barra = input("Tensao base na barra em kV: ")
    barra = Barras(nome_barra, tensao_base_barra)
    barras_Sistema.append(barra)

print(barras_Sistema[0].nome, num_barras)

ele_Sistema = []

class Maquina():    
    def __init__(self, nome, Vn, Sn, x_pos, barras_conectadas): # Construtor (Criando o objeto e atribuindo dados a ele)
        self.nome = nome
        self.Vn = Vn
        self.Sn = Sn
        self.x_pos = x_pos # reatância subtransitória em PU e na base do sistema
        self.barras_conectadas = barras_conectadas

class LinhaTransmissao():
    def __init__(self, nome, Sn, x_pos, barras_conectadas):
        self.nome = nome
        self.Sn = Sn
        self.x_pos = x_pos # reatância subtransitória em PU e na base do sistema
        self.barras_conectadas = barras_conectadas

class Transformador():
    def __init__(self, nome, razao, Sn, x_pos, barras_conectadas):
        self.nome = nome
        self.razao = razao # razão de transformação de tensão do primário para o secundário
        self.Sn = Sn
        self.x_pos = x_pos # reatância subtransitória em PU e na base do sistema
        self.barras_conectadas = barras_conectadas      
