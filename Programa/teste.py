import Programa as pg

pg.barras_Sistema.append(pg.Barras("1", 138))
pg.barras_Sistema.append(pg.Barras("2", 138))
pg.barras_Sistema.append(pg.Barras("3", 138))
pg.barras_Sistema.append(pg.Barras("4", 138))

#nome: str, Vn: float, Sn: int, x_pos: complex, x_zero: complex, conex_ger: str, x_aterramento: complex, barras_conectadas: list

pg.ele_Sistema.append(pg.Maquina("1", 13.8, 100, 0.35j, 0j, "Y", 0j, [1]))
pg.ele_Sistema.append(pg.Maquina("2", 13.8, 100, 0.3j, 0j, "Y", 0j, [3]))
pg.ele_Sistema.append(pg.Maquina("3", 13.8, 100, 0.4j, 0j, "Y", 0j, [2]))

#nome: str, Sn: int, x_pos: complex, x_zero: complex, barras_conectadas: list

pg.ele_Sistema.append(pg.LinhaTransmissao("14", 100, 0.2j, 0j, [1, 4]))
pg.ele_Sistema.append(pg.LinhaTransmissao("13", 100, 0.25j, 0j, [1, 3]))
pg.ele_Sistema.append(pg.LinhaTransmissao("34", 100, 0.125j, 0j, [3, 4]))
pg.ele_Sistema.append(pg.LinhaTransmissao("23", 100, 0.4j, 0j, [2, 3]))
pg.ele_Sistema.append(pg.LinhaTransmissao("24", 100, 0.2j, 0j, [2, 4]))

#nome: str, Sn: int, x_pos: complex, x_zero: complex, x_aterramento: complex, barras_conectadas: list, conex_trafo: str

pg.ele_Sistema.append(pg.Transformador("1", 100, 0.1j, 0.2j, 0.15j, [1, 2], "Y_aterrado-D"))
pg.ele_Sistema.append(pg.Transformador("2", 100, 0.2j, 0.25j, 0.1j, [3, 4], "Y-D"))
pg.ele_Sistema.append(pg.Transformador("3", 100, 0.15j, 0.3j, 0.2j, [5, 26], "Y_aterrado-Y_aterrado"))

pg.print_elements()

# Ybarra = pg.Ybarra_pos_neg()
# Zbarra = pg.Zbarra(Ybarra)

# print(Ybarra)
# print("\n")
# print(Zbarra)

