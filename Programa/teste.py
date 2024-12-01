import Programa as pg

pg.barras_Sistema.append(pg.Barras("1", 138))
pg.barras_Sistema.append(pg.Barras("2", 138))
pg.barras_Sistema.append(pg.Barras("3", 138))
pg.barras_Sistema.append(pg.Barras("4", 138))

pg.ele_Sistema.append(pg.Maquina("1", 13.8, 100, 0.35j, 0j, "Y", 0j, [1]))
pg.ele_Sistema.append(pg.Maquina("2", 13.8, 100, 0.3j, 0j, "Y", 0j, [3]))
pg.ele_Sistema.append(pg.Maquina("3", 13.8, 100, 0.4j, 0j, "Y", 0j, [2]))

pg.ele_Sistema.append(pg.LinhaTransmissao("14", 100, 0.2j, 0j, [1, 4]))
pg.ele_Sistema.append(pg.LinhaTransmissao("13", 100, 0.25j, 0j, [1, 3]))
pg.ele_Sistema.append(pg.LinhaTransmissao("34", 100, 0.125j, 0j, [3, 4]))
pg.ele_Sistema.append(pg.LinhaTransmissao("23", 100, 0.4j, 0j, [2, 3]))
pg.ele_Sistema.append(pg.LinhaTransmissao("24", 100, 0.2j, 0j, [2, 4]))

Ybarra = pg.Ybarra_pos_neg()
Zbarra = pg.Zbarra_pos_neg(Ybarra)

print(Ybarra)
print("\n")
print(Zbarra)

