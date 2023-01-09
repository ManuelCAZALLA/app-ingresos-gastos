from app_registro import app
from flask import render_template,request,redirect
import csv
from datetime import date
from config import *
import os # esto es un modulo para renombrar y eliminar arhivos
from models import selec_all

@app.route("/") 

def index ():
   
   fichero = open (Movimientos_File,"r") # aqui abro archivo
   csvReader = csv.reader(fichero,delimiter = ",", quotechar= '"')# accede ala archivo y lo formatea
   datos = []# creo un array datos vacio para guardar los registros
   
   for item in csvReader : # recorro el csvReader y guardo cada registro en datos
      datos.append(item)
   fichero.close()  
   
   return render_template("index.html", pageTitle = "Listas",lista = datos) # variable que tengo en base la defino aqui 
   
       


@app.route("/new", methods = ["GET","POST"]) # ruta para new 

def create():
   if request.method == "GET": #Puede ser GET o POST 
      return render_template("new.html",pageTitle = "Alta",typeAction = "Alta",typeButon = 'Guardar',dataForm = "")

   else :
     
      error = validateForm(request.form) # aqui llamo a la funcion que controla los errores y validamos los datos
   
   if  error :
      # si hay error
      return render_template("new.html",pageTitle = "Alta",typeAction = "Alta",typeButon = 'Guardar', msgerror = error,dataForm = request.form)
   
   else:
      # no hay error lo registra
        mifichero = open(Movimientos_File, 'a',newline = '')# accede ala archivo y configura para un nuevo registro
        lectura = csv.writer(mifichero, delimiter =',',quotechar='"') # llama a write para escribir y cargo el formateo para csv
         
         #crear id
        fichero = open(Last_Id_File,"r")
        registro = fichero.read()
        if registro == "" : # si esta vacio
           new_id=1 # el new id es el primero
        else :
             new_id = int (registro)+1 # si no al ultimo le sumo 1
        fichero.close()
        
        ficheroGuardar = open (Last_Id_File,'w') # abro last_id
        ficheroGuardar.write(str(new_id)) # escribo el nuevo id
        ficheroGuardar.close()
        
        lectura.writerow([new_id,request.form['fecha'],request.form['concepto'],request.form ['cantidad']]) # registra los datos y lo añade con writerrow

  
        mifichero.close()
   return redirect("/")



@app.route("/update/<int:id>") # ruta para editar

def edit(id):
   return f"este es el id = {id} a modificar"
   #return render_template("update.html",pageTitle = "Editar",typeAction = "modificacion",typeButon = 'Editar')



@app.route ("/delete/<int:id>",methods = ["GET","POST"]) #ruta para borrar

def remove (id):
   if request.method =="GET":
      
      miFichero = open(Movimientos_File,"r")
      lectura = csv.reader(miFichero,delimiter=",",quotechar='"')
      registro_buscado = []
      for registro in lectura:
         if registro[0] == str(id):
            # aqui encuentra el dato
            registro_buscado = registro
      miFichero.close()
# si no encuentra registro 
      if len(registro_buscado) >0:
          return render_template("delete.html",pageTitle = "Eliminar",registros = registro_buscado)
      else:
         redirect ("/") 
         
   else: # aqui seria post
     fichero_old = open(Movimientos_File,"r")# aqui accede al csv de registros
     fichero = open(Movimientos_File_New,"w")# aqui accede a un archivo auxiliar
     
     csvRaeader = csv.reader(fichero_old,delimiter=",",quotechar='"')
     csvWriter = csv.writer(fichero,delimiter=",",quotechar='"')
     
     for registro in csvRaeader:
        if registro[0] != str (id) : # mientras el id sea distinto al proporcionado para borrar que escriba en fichero
           csvWriter.writerow(registro)
             
     fichero_old.close()
     fichero.close()
     
     os.remove(Movimientos_File) # funcion remove que recibe la ruta de un archivo
     os.rename(Movimientos_File_New,Movimientos_File) # funcion para renombrar archivos le paso los 2 que quiero renombrar
     
     return redirect("/")
           
      





def validateForm(requestForm):
   hoy = date.today().isoformat()
   errores = []
   
   if request.form['fecha'] > hoy :
       errores.append("Fecha Incorrecta: La fecha introducida es futura")
   if request.form['concepto'] == "" :
       errores.append("Concepto vacio : Introduce un concepto") 
   if request.form['cantidad'] == "" or float(requestForm["cantidad"]== 0.0):
       errores.append("Cantidad vacio o cero : Introduce cantidad positiva o negativa")
       
   return errores           
   
    
    
   
   
   
    
    