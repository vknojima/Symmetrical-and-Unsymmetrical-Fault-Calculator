import Programa as pg
import numpy as np

# Lembrar de alterar a variável "num_barras"

pg.barras_Sistema.append(pg.Barras("1", 13.8))
pg.barras_Sistema.append(pg.Barras("2", 230))
pg.barras_Sistema.append(pg.Barras("3", 230))
pg.barras_Sistema.append(pg.Barras("4", 230))
pg.barras_Sistema.append(pg.Barras("5", 6.9))
pg.barras_Sistema.append(pg.Barras("6", 230))
pg.barras_Sistema.append(pg.Barras("7", 230))

#nome: str, Vn: float, Sn: int, x_pos: complex, x_zero: complex, conex_ger: str, x_aterramento: complex, barras_conectadas: list

pg.ele_Sistema.append(pg.Maquina("1", 13.8, 100, 0.25j, 0.08j, "Y_aterrado", 0.0j, [1]))
pg.ele_Sistema.append(pg.Maquina("5", 13.8, 100, 0.3j, 0.1j, "Y_aterrado", 0j, [5]))

#nome: str, Sn: int, x_pos: complex, x_zero: complex, barras_conectadas: list

pg.ele_Sistema.append(pg.LinhaTransmissao("23", 100, 0.0473j, 0.0473j, [2,3]))
pg.ele_Sistema.append(pg.LinhaTransmissao("34", 100, 0.0519, 0.0519j, [3,4]))
pg.ele_Sistema.append(pg.LinhaTransmissao("26", 100, 0.0378j, 0.0378j, [2,6]))
pg.ele_Sistema.append(pg.LinhaTransmissao("36", 100, 0.05j, 0.05j, [3,6]))
pg.ele_Sistema.append(pg.LinhaTransmissao("37", 100, 0.05j, 0.05j, [3,7]))
pg.ele_Sistema.append(pg.LinhaTransmissao("47", 100, 0.05j, 0.05j, [4,7]))

#nome: str, Sn: int, x_pos: complex, x_zero: complex, x_aterramento: complex, barras_conectadas: list, conex_trafo: str

pg.ele_Sistema.append(pg.Transformador("1", 100, 0.1j, 0.1j, 0j, [1,2], "D-Y_aterrado"))
pg.ele_Sistema.append(pg.Transformador("2", 100, 0.15j, 0.15j, 0j, [4,5], "D-Y_aterrado"))

Ybarra_pos_neg = pg.Ybarra_pos_neg()
Ybarra_zero = pg.Ybarra_zero()
Zbarra_pos_neg = pg.Zbarra(Ybarra_pos_neg)
Zbarra_zero = pg.Zbarra(Ybarra_zero)

barraCurto = pg.barras_Sistema[5]
#print(Ybarra_zero)
#print("\n")
#print(Zbarra_zero)

If, Ifpos = pg.correnteFaltaBifasica(barraCurto, Zbarra_pos_neg,0)
print(If)
d1, d2 = pg.correnteContribuicaoBifasica(Ifpos, barraCurto, Zbarra_pos_neg)
print(d1)
print("\n")
print(d2)