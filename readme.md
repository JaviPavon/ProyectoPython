Mi proyecto se basa en la temporada pasada de LaLiga, la cual usa un JSON en línea de todos los resultados de los partidos disputados y las fechas correspondientes en los que se jugaron.

Cómo se instala

Deberemos crear un entorno virtual para trabajar en él y tener el mínimo de problemas a la hora de ejecutar nuestro proyecto, para ello, en la terminal ejecutaremos 'pip install virtualenvwrapper', y despúes con el virtualenvwrapper instalado creamos el entorno virtual con 'mkvirtualenvwrapper env1', (Puedes sustituir el nombre env1 por el nombre que desees). En la carpeta en la que hallamos creado en entorno virtual ejecutamos el comando 'source env1/bin/activate' para activar el entorno; en el caso de Windows sería 'env1\Scripts\activate'.
Ya dentro del entorno virtual ya podremos seguir trabajando, para utilizar mi programa es necesario la instalacion de request para la recogida de datos del JSON en línea, para su instalación crearemos un txt llamado 'requirements.txt' en la carpeta en la que estamos trabajando en la que pondremos 'requests==2.26.0', guardamos el archivo, abrimos el terminal y asegurandonos de estar en el entorno virtual instalaremos el contenido del txt con el siguiente comando, 'pip install -r requirements.txt' y ya podremos ejecutar el programa sin problemas.

Al ejecutar el programa cos saltará un Menú con distintas funciones para realizar, pasaré a explicar cada función:

1-Listaría todo el JSON en sí con un buen formato para que sea leíble

2-El programa le pide al usuario un equipo y el usuario según el quipo que introduzque, se le muestra sus partidos disputados

3-Esta función te lista todos los equipos que están

4-Muestra una clasificación de todos los equipos según los partidos disputados

5-Esta función esta echa para salir del menú

Para ejecutarlo deberemos estar en la misma carpeta donde este el archivo .py y después en la terminal introducimos "python3 archivo.py" en este caso archivo es GestionarDatos.py