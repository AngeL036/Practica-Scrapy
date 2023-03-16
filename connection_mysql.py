import mysql.connector
from mysql.connector  import Error
class DB:
    def __init__(self,host,port,user,password,db) -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
    def StartConnection(self)->None:
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                port=self.port,
                user = self.user,
                password = self.password,
                db=self.db
            )
        except Error as ex:
            print("Error durante la conexión:" ,ex)
    def EndConection(self):
        if self.connection.is_connected():
            self.connection.close()
           # print("Conexion finalizada...")
    def insert(self,list)->None:
        if self.connection.is_connected():
            
            #infoServer = self.connection.get_server_info()
            #print("Info del servidor: ",infoServer)
            cursor = self.connection.cursor()
            cursor.executemany("""INSERT INTO mochilas(ProductName,ProductPrice,ProductDescription,fecha) 
            VALUES (%s,%s,%s,%s)""",list)
            self.connection.commit()
            print("Datos insertados")
    def consulta(self,palabra_buscada1,palabra_buscada2,palabra_buscada3):
        if self.connection.is_connected():
            cursor = self.connection.cursor()

            #consulta = "SELECT * FROM mochilas WHERE ProductDescription LIKE '%{}%'".format(palabra_buscada)
            consulta = """ SELECT * FROM mochilas WHERE ProductDescription LIKE '%{}%' AND  ProductDescription LIKE '%{}%' AND ProductDescription LIKE  '%{}%' ORDER BY ProductPrice LIMIT 50
            """.format(palabra_buscada1,palabra_buscada2,palabra_buscada3)
            cursor.execute(consulta)  
            resultado = cursor.fetchall()
            return resultado
    def busca_precio(self,precio):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            consulta = f"SELECT * FROM mochilas WHERE ProductPrice < {precio} ORDER BY ProductPrice LIMIT 50"
            cursor.execute(consulta)
            a = cursor.fetchall()
            return a
    def busca_marca(self,marca):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            consulta = "SELECT ProductPrice,ProductDescription FROM mochilas WHERE ProductName = '{}' ORDER BY ProductPrice LIMIT 50".format(marca)
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
    def busca_marca_precio(self,marca,precio):
         if self.connection.is_connected():
            cursor = self.connection.cursor()
            consulta = "SELECT ProductPrice,ProductDescription FROM mochilas WHERE ProductName = '{}' AND ProductPrice < {} ORDER BY ProductPrice LIMIT 50".format(marca,precio)
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado
    def todo(self):
         if self.connection.is_connected():
            cursor = self.connection.cursor()
            consulta = "SELECT * FROM mochilas ORDER BY ProductPrice "
            cursor.execute(consulta)
            resultado = cursor.fetchall()
            return resultado