from scraping import Scraping
from connection_mysql import DB
import pandas as pd 
from datetime import datetime
import matplotlib.pyplot as plt

names = []
prices = []
descriptions = []
times = []
palabras = []
db = DB('localhost',3306,'root','Mariadb','mochilas')

scrap = Scraping()
pd.set_option('display.max_rows', None)  # mostrar todas las filas
#pd.set_option('display.max_columns', None) #mostrar todas las columnas 
def MostrarPD(list):
    if len(list)>0:
        for resul in list:
                names.append(resul[1])
                prices.append(resul[2])
                descriptions.append(resul[3])
                fecha_hora_dt = resul[4].strftime('%d-%m-%Y %H:%M:%S')
                times.append(fecha_hora_dt)
                datos = {'nombre':names ,'precio':prices,'descripcion':descriptions,'hora y fecha':times}
                df = pd.DataFrame(datos)
        #fecha_hora_actual = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        #nombre_archivo = f'{fecha_hora_actual}.xlsx'
        #df.to_excel(nombre_archivo,index=False)
        #dff = pd.read_excel(nombre_archivo)
        plt.ion()
        #serie = dff.nombre.value_counts()
        #x = serie.plot.barh()
        df.plot.scatter(y="nombre",x="precio")
        print()
        print(df)
        print()
    else:
        print("-------------------------------------")
        print("\n No se encontraron resultados... \n")
        print("-------------------------------------")
  

def mostrar(list):
    if len(list)>0:
        for resul in list:
            prices.append(resul[0])
            descriptions.append(resul[1])
            datos = {'precio':prices,'descripcion':descriptions}
            df = pd.DataFrame(datos)
        fecha_hora_actual = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        nombre_archivo = f'{fecha_hora_actual}.xlsx'
        df.to_excel(nombre_archivo,index=False)
        #dff = pd.read_excel(nombre_archivo)
        plt.ion()
        serie = df.precio.value_counts()
        x = serie.plot.pie()
        #df.plot.pie()
        print()
        print(df)
        print()
    else:
        print("-------------------------------------")
        print("\n No se encontraron resultados... \n")
        print("-------------------------------------")

if __name__ == '__main__':
    salir = True
    while salir:
        
        print("1) Realizar scraping")
        print("2) Busqueda Palabra clave")
        print("3) busqueda por precio")
        print("4) busqueda por marca")
        print("5) busqueda por precio y marca")
        print("6) crear excel de todos los registros")
        print("0) salir...")
        names.clear()
        prices.clear()
        descriptions.clear()
        times.clear()
        opcion = int(input("\nelige una opcion: "))
        if opcion == 1:
            scrap.principal()
        if opcion == 2:
            db.StartConnection()
            palabra_clave1 = input("\nPrimera palabra a buscar: ")
            palabra_clave2 = input("\nSegunda palabra a buscar: ")
            palabra_clave3 = input("\nTercera palabra a buscar: ")
            resultado = db.consulta(palabra_clave1,palabra_clave2,palabra_clave3)
            MostrarPD(resultado)
            db.EndConection()
        if opcion == 3:
            db.StartConnection()
            precio =  int(input("\nprecio maximo buscada: "))
            resultado = db.busca_precio(precio)
            MostrarPD(resultado)
            db.EndConection()
        if opcion == 4:
            db.StartConnection()
            marca = input("\nnombre de la marca a buscar: ")
            resultado = db.busca_marca(marca)
            mostrar(resultado)
            db.EndConection()
        if opcion == 5:
            db.StartConnection()
            marca = input("\nnombre de la marca a buscar: ")
            precio = int(input("\nprecio maximo buscada: "))
            resultado = db.busca_marca_precio(marca,precio)
            mostrar(resultado)


            db.EndConection
        if opcion == 6:
            db.StartConnection()
            resultado = db.todo()
            print(" -------------------------")
            print("Creando excel...")
            print(" -------------------------\n")
            if len(resultado) > 0:
                for resul in resultado:
                    names.append(resul[1])
                    prices.append(resul[2])
                    descriptions.append(resul[3])
                    fecha_hora_dt = resul[4].strftime('%d-%m-%Y %H:%M:%S')
                    times.append(fecha_hora_dt)
                
                datos = {'nombre':names ,'precio':prices,'descripcion':descriptions,'hora y fecha':times}
                df = pd.DataFrame(datos)
                fecha_hora_actual = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                nombre_archivo = f'{fecha_hora_actual}.xlsx'
                df.to_excel(nombre_archivo,index=False)
                dff = pd.read_excel(nombre_archivo)
                
                print(" -------------------------")
                print("excel creado y guardado con exito.")
                print(" -------------------------\n")

                
            else:
                print(" -------------------------")
                print("|No hay datos para guardar|")
                print(" -------------------------\n")
            db.EndConection()
        if opcion == 0:
            print("----------------")
            print("    Adios...    ")
            print("----------------")
            salir = False
        if opcion < 0 or opcion > 6  :
            print("\nOpcion no valida\n")