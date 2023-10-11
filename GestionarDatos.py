import requests

# URL de la API
# Realiza la solicitud GET
response = requests.get('https://fixturedownload.com/feed/json/la-liga-2022')

# Convierte la respuesta JSON en una lista de diccionarios de Python
data = response.json()

def ListarTodo():
# Ordena los datos por el campo 'MatchNumber' de menor a mayor
  datos = sorted(data, key=lambda x: x['MatchNumber'])

  #datos = sorted(data, key=lambda x: x['MatchNumber'], reverse=True)    (Ordenarlo de mayor a menor)

# Ahora puedes trabajar con los datos ordenados
  for partido in datos:
      print("Partido:", partido['MatchNumber'])
      print("Fecha:", partido['DateUtc'])
      print("Local:", partido['HomeTeam'])
      print("Visitante:", partido['AwayTeam'])
      print("Resultado:", partido['HomeTeamScore'], "-", partido['AwayTeamScore'])
      print("Ubicación:", partido['Location'])
      print("Ronda:", partido['RoundNumber'])
      print()


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



def ListarEquipos():
  equipos = set()  # Creamos un conjunto para almacenar los equipos

  for partido in data:
      equipos.add(partido["HomeTeam"])  # Agregamos el equipo local al conjunto

  equipos_lista = sorted(list(equipos))  # Convertimos el conjunto en una lista

  print("Lista de equipos:")
  for equipo in equipos_lista:
      print(equipo)





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
