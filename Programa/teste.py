import Programa as pg

pg.barras_Sistema.append(pg.Barras("1", 13.8))
pg.barras_Sistema.append(pg.Barras("2", 13.8))
pg.barras_Sistema.append(pg.Barras("3", 13.8))
pg.barras_Sistema.append(pg.Barras("4", 138))
pg.barras_Sistema.append(pg.Barras("5", 138))
pg.barras_Sistema.append(pg.Barras("6", 138))
pg.barras_Sistema.append(pg.Barras("7", 138))

#nome: str, Vn: float, Sn: int, x_pos: complex, x_zero: complex, conex_ger: str, x_aterramento: complex, barras_conectadas: list

pg.ele_Sistema.append(pg.Maquina("1", 13.8, 100, 0.25j, 0j, "Y_aterrado", 0.0889j, [1]))
pg.ele_Sistema.append(pg.Maquina("2", 13.8, 100, 0.3j, 0j, "Y_aterrado", 0j, [2]))
pg.ele_Sistema.append(pg.Maquina("3", 13.8, 100, 0.2j, 0j, "Y_aterrado", 0j, [3]))

#nome: str, Sn: int, x_pos: complex, x_zero: complex, barras_conectadas: list

pg.ele_Sistema.append(pg.LinhaTransmissao("54", 100, 0.2j, 0.0392j, [5,4]))
pg.ele_Sistema.append(pg.LinhaTransmissao("53", 100, 0.25j, 0.0392j, [5,7]))
pg.ele_Sistema.append(pg.LinhaTransmissao("74", 100, 0.125j, 0.0392j, [7,4]))
pg.ele_Sistema.append(pg.LinhaTransmissao("64", 100, 0.2j, 0.0392j, [6,4]))
pg.ele_Sistema.append(pg.LinhaTransmissao("63", 100, 0.4j, 0.0392j, [6,7]))


#nome: str, Sn: int, x_pos: complex, x_zero: complex, x_aterramento: complex, barras_conectadas: list, conex_trafo: str

pg.ele_Sistema.append(pg.Transformador("1", 100, 0.1j, 0.0457j, 0j, [1,5], "Y_aterrado-D"))
pg.ele_Sistema.append(pg.Transformador("2", 100, 0.1j, 0.0457j, 0j, [2,6], "Y_aterrado-D"))
pg.ele_Sistema.append(pg.Transformador("3", 100, 0.1j, 0.0457j, 0j, [3,7], "Y_aterrado-D"))

Ybarra_pos_neg = pg.Ybarra_pos_neg()
#Ybarra_zero = pg.Ybarra_zero()
Zbarra_pos_neg = pg.Zbarra(Ybarra_pos_neg)#
#Zbarra_zero = pg.Zbarra(Ybarra_zero)

print(Ybarra_pos_neg)
print("\n")
print(Zbarra_pos_neg)
print("\n")
# print(Ybarra_zero)
# print("\n")
# print(Zbarra_zero)

If = pg.correnteFaltaTrifasica(pg.barras_Sistema[6], Zbarra_pos_neg)
print(If*pg.correnteBase(pg.barras_Sistema[6]))
d1, d2 = pg.correnteContribuicao(If, pg.barras_Sistema[6], Zbarra_pos_neg)
print(d1)
print("\n")
print(d2)