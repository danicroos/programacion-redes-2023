'''
Autor: Zuñiga Olvera Jorge Daniel
lab: 2.3.1.16
fecha: 20-Nov-2023
'''
def display_siete_segmentos(numero):
    patrones = [
        ["###", "# #", "# #", "# #", "###"],
        ["  #", "  #", "  #", "  #", "  #"],
        ["###", "  #", "###", "#  ", "###"],
        ["###", "  #", "###", "  #", "###"],
        ["# #", "# #", "###", "  #", "  #"],
        ["###", "#  ", "###", "  #", "###"],
        ["###", "#  ", "###", "# #", "###"],
        ["###", "  #", "  #", "  #", "  #"],
        ["###", "# #", "###", "# #", "###"],
        ["###", "# #", "###", "  #", "###"]
    ]

    for i in range(5):
        fila = " ".join(patrones[int(digito)][i] for digito in str(numero))
        print(fila)

numero_ingresado = int(input("Ingresa un numero: "))
display_siete_segmentos(numero_ingresado)
