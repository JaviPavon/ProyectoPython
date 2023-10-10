import requests

# URL de la API
url = 'https://fixturedownload.com/feed/json/la-liga-2022'

# Realiza la solicitud GET
response = requests.get(url)

# Convierte la respuesta JSON en una lista de diccionarios de Python
data = response.json()

def ListarTodo():
# Ordena los datos por el campo 'MatchNumber' de menor a mayor
  data_sorted = sorted(data, key=lambda x: x['MatchNumber'])

# Ahora puedes trabajar con los datos ordenados
  for partido in data_sorted:
      print("Partido:", partido['MatchNumber'])
      print("Fecha:", partido['DateUtc'])
      print("Local:", partido['HomeTeam'])
      print("Visitante:", partido['AwayTeam'])
      print("Resultado:", partido['HomeTeamScore'], "-", partido['AwayTeamScore'])
      print("Ubicación:", partido['Location'])
      print("Ronda:", partido['RoundNumber'])
      print()


ListarTodo()
  #Ejemplo de datos

# [{"MatchNumber":1,
#   "RoundNumber":1,
#   "DateUtc":"2022-08-12 19:00:00Z",
#   "Location":"Estadio El Sadar",
#   "HomeTeam":"CA Osasuna",
#   "AwayTeam":"Sevilla FC",
#   "Group":null,"HomeTeamScore":2,
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