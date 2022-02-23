import csv

nombre_Archivo = "calles_de_medellin_con_acoso.csv"
with open(nombre_Archivo,newline='\n') as ar:
    data = csv.reader(ar,delimiter=';')
    calles =list(data)
print(calles)