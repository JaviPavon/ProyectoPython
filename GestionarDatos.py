import requests

#URL de la API
#Realiza la solicitud GET
response = requests.get('https://fixturedownload.com/feed/json/la-liga-2022')

#Convierte la respuesta JSON en una lista de diccionarios de Python
data = response.json()


#Primera función ListarTodo
def ListarTodo():
#Ordena los datos por el campo 'MatchNumber' de menor a mayor
  datos = sorted(data, key=lambda x: x['MatchNumber'])

  #datos = sorted(data, key=lambda x: x['MatchNumber'], reverse=True)    (Ordenarlo de mayor a menor)

#Ahora puedes trabajar con los datos ordenados
  for partido in datos:
      print("Partido:", partido['MatchNumber'])
      print("Fecha:", partido['DateUtc'])
      print("Local:", partido['HomeTeam'])
      print("Visitante:", partido['AwayTeam'])
      print("Resultado:", partido['HomeTeamScore'], "-", partido['AwayTeamScore'])
      print("Ubicación:", partido['Location'])
      print("Ronda:", partido['RoundNumber'])
      print()

#Segunda función PartidosEquipo
def BuscarEquipo(data, equipo):
  partidos_equipo = []
  for partido in data:
      if partido["HomeTeam"] == equipo or partido["AwayTeam"] == equipo:
          partidos_equipo.append(partido)
  return partidos_equipo

def PartidosEquipo():
  equipo_buscado = input("Introduce el nombre del equipo: ")
  partidos_equipo = BuscarEquipo(data, equipo_buscado)

  if partidos_equipo:
      print("Partidos en los que juega ",equipo_buscado, ":")
      for partido in partidos_equipo:
          print("Jornada: ", partido['RoundNumber'])
          print("Fecha: ", partido['DateUtc'])
          print(partido['HomeTeam']," ", partido['HomeTeamScore'], "-", partido['AwayTeamScore']," ",partido['AwayTeam'] )
          print()
  else:
      print(equipo_buscado," no está bien escrito o no ha jugado ningún partido en la lista proporcionada.")


#Tercera función ListarEquipos
def ListarEquipos():
  equipos = set()  #Creamos un conjunto para almacenar los equipos

  for partido in data:
      equipos.add(partido["HomeTeam"])  #Agregamos el equipo local al conjunto

  equipos_lista = sorted(list(equipos))  #Convertimos el conjunto en una lista

  print("Lista de equipos:")
  for equipo in equipos_lista:
      print(equipo)


def CalcularPuntos(data):
    #Inicializar un diccionario para realizar un seguimiento de los puntos de cada equipo
    puntos_equipo = {}

    #Procesar los datos de los partidos
    for partido in data:
        equipo_local = partido["HomeTeam"]
        equipo_visitante = partido["AwayTeam"]
        marcador_local = partido["HomeTeamScore"]
        marcador_visitante = partido["AwayTeamScore"]

        #Determinar el resultado del partido y otorgar puntos a los equipos
        if marcador_local > marcador_visitante:
            if equipo_local in puntos_equipo:
                puntos_equipo[equipo_local] = puntos_equipo.get(equipo_local, 0) + 3
            else:
                puntos_equipo[equipo_local] = 3

        elif marcador_local < marcador_visitante:
            if equipo_visitante in puntos_equipo:
                puntos_equipo[equipo_visitante] = puntos_equipo.get(equipo_visitante, 0) + 3
            else:
                puntos_equipo[equipo_visitante] = 3

        else:
            #Empate
            if equipo_local in puntos_equipo:
                puntos_equipo[equipo_local] = puntos_equipo.get(equipo_local, 0) + 1
            else:
                puntos_equipo[equipo_local] = 1

            if equipo_visitante in puntos_equipo:
                puntos_equipo[equipo_visitante] = puntos_equipo.get(equipo_visitante, 0) + 1
            else:
                puntos_equipo[equipo_visitante] = 1

    return puntos_equipo
#Cuarta función Tabla de Clasificación

def Clasificacion():
    puntos_equipo = CalcularPuntos(data)
    clasificacion = sorted(puntos_equipo.items(), key=lambda x: x[1], reverse=True)

    print("Clasificación de equipos:")
    for posicion, (equipo, puntos) in enumerate(clasificacion, start=1):
        print("{posicion}. {equipo}: {puntos} puntos")

#Quinta función DiferenciaGoles

def MostrarDiferenciaDeGoles():
    #Inicializar un diccionario para realizar un seguimiento de la diferencia de goles de cada equipo
    diferencia_goles_equipo = {}

    #Procesar los datos de los partidos
    for partido in data:
        equipo_local = partido["HomeTeam"]
        equipo_visitante = partido["AwayTeam"]
        goles_local = partido["HomeTeamScore"]
        goles_visitante = partido["AwayTeamScore"]

        #Calcular la diferencia de goles para el equipo local
        if equipo_local in diferencia_goles_equipo:
            diferencia_goles_equipo[equipo_local] += goles_local - goles_visitante
        else:
            diferencia_goles_equipo[equipo_local] = goles_local - goles_visitante

        #Calcular la diferencia de goles para el equipo visitante
        if equipo_visitante in diferencia_goles_equipo:
            diferencia_goles_equipo[equipo_visitante] += goles_visitante - goles_local
        else:
            diferencia_goles_equipo[equipo_visitante] = goles_visitante - goles_local

    print("Diferencia de goles de cada equipo:")
    for equipo, diferencia in diferencia_goles_equipo.items():
        print("{equipo}: {diferencia} goles")

#Función para mostrar el menú y obtener la selección del usuario
def Menu():
    while True:
        print("Menú:")
        print("1. Listar todo")
        print("2. Ver partidos de cualquier equipo")
        print("3. Listar equipos de la liga")
        print("4. Mostrar Clasificación de Equipos")
        print("5. Mostrar Diferencia de Goles de Equipos")
        print("6. Salir")
        
        opcion = input("Por favor, seleccione una opción: ")

        if opcion == "1":
            ListarTodo()
        elif opcion == "2":
            PartidosEquipo()
        elif opcion == "3":
            ListarEquipos()
        elif opcion == "4":
            Clasificacion()
        elif opcion == "5":
            MostrarDiferenciaDeGoles()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elija 1, 2, 3, 4, 5 o 6")

#Llama a la función del menú para comenzar la interacción con el usuario
Menu()

  #Ejemplo de datos

# [{"MatchNumber":1,
#   "RoundNumber":1,
#   "DateUtc":"2022-08-12 19:00:00Z",
#   "Location":"Estadio El Sadar",
#   "HomeTeam":"CA Osasuna",
#   "AwayTeam":"Sevilla FC",
#   "Group":null,
#   "HomeTeamScore":2,
#   "AwayTeamScore":1},
  
#   {"MatchNumber":2,
#   "RoundNumber":1,
#   "DateUtc":"2022-08-13 15:00:00Z",
#   "Location":"Estadio ABANCA Balaídos",
#   "HomeTeam":"RC Celta",
#   "AwayTeam":"RCD Espanyol de Barcelona",
#   "Group":null,
#   "HomeTeamScore":2,
#   "AwayTeamScore":2},
