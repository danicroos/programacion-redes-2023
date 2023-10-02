'''
    Nombre:     Daniel Zuñiga
    Fecha:      18-sep-2023
    Descripcion:
    Laboratorio:
'''
hora_inicio = int(input("Hora de inicio (horas): "))
minuto_inicio = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))

minuto_final = (minuto_inicio + duracion) % 60
hora_final = (hora_inicio + (minuto_inicio + duracion) // 60) % 24

print(f"El evento termina a las {hora_final}:{minuto_final:02d}")
