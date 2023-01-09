# lectura de archivos
import csv

'''with open ('data/movimientos.csv',"r") as resultado :
    leer = resultado.read()
    print(type(leer))
    
    
#otra manera
datos = [] 
result =    open ('data/movimientos.csv',"r")
lectura = result.readline()
print (lectura)

# otro ejemplo

mifichero =  open ('data/movimientos.csv',"r")
mifichero = csv.reader(mifichero,delimiter =",", quatechar = '"')

for registros in mifichero :
    print(registros)
    datos.append(registros)
    
    print("Estos son los datos",datos)'''
 # añadir registros a movimientos. txt   
'''mifichero = open('data/movimientos.csv', 'a',newline = '')
lectura = csv.writer(mifichero, delimiter =',',quotechar='"')
lectura.writerow(['5/01/20023','cervezas',-60])

mifichero.close()'''

'''from datetime import date

print (" la fecha de hoy es : ", date.today())'''


         #crear id
fichero = open ("data/movimientos.csv","r")
csvReader = csv.reader(fichero,delimiter=",",quotechar='"')
lista_id = []
for item in csvReader:
    lista_id.append(item[0])
    
  
    print (lista_id [len(lista_id)-1])# asi obtengo el ultimo de la lista
 

    
        
   