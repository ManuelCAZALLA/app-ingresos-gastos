# Aplicacion web de Ingresos y Gastos

Programa hecho en python con el framework Flask,App Ingresos Gastos

## En su entorno de python ejecutar el comando
````
pip install - r requierements.txt
````
- La libreria utilizada es Flask https://flask.palletsprojects.com/en/2.2.x/

# Ejecución del programa
- inicializar el servidor de flask :
- en mac : export FLASK_APP=hello.py
- en windows : set FLASK_APP=hello.py
### Otra alternativa seria :
- FLASK_APP = main.py
- FLASK_DEBUG = true

# Comandos Utiles Para Nuestra App
- Comando ejecutar para el servidor:
- flask --app hello run
- Comando para actualizar el servidor con cambios de codigo en tiempo real :
- flask --app main --debug run
- Comando especial para lanzar el servidor en un puerto diferente :
flask --app hello run -p 5001
- Comando para lanzar en modo debug y con puerto cambiado:
flask --app hello --debug run -p 5001


