Mi proyecto se basa en la temporada pasada de LaLiga, la cual usa un JSON en línea de todos los resultados de los partidos disputados y las fechas correspondientes en los que se jugaron.

Cómo se instala

Deberemos crear un entorno virtual para trabajar en él y tener el mínimo de problemas a la hora de ejecutar nuestro proyecto, para ello, en la terminal ejecutaremos 'pip install virtualenv', y despúes con el virtualenv instalado creamos el entorno virtual con 'virtualenv env1', (Puedes sustituir el nombre env1 por el nombre que desees). En la carpeta en la que hallamos creado en entorno virtual ejecutamos el comando 'source env1/bin/activate' para activar el entorno; en el caso de qindows sería 'env1\Scripts\activate'.
Ya dentro del entorno virtual ya podremos seguir trabajando, para utilizar mi programa es necesario la instalacion de request para la recogida de datos del JSON en línea, para su instalación crearemos un txt llamado 'requirements.txt' en la carpeta en la que estamos trabajando en la que pondremos 'requests==2.26.0', guardamos el archivo, abrimos el terminal y asegurandonos de estar en el entorno virtual instalaremos el contenido del txt con el siguiente comando, 'pip install -r requirements.txt' y ya podremos ejecutar el programa sin problemas.

Al ejecutar el programa cos saltará un Menú con distintas funciones para realizar, pasaré a explicar cada función:
