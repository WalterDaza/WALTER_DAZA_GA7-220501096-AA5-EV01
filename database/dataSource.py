from pydal import DAL, Field #Importamos librerias

class DataSourceMysql:
    db = "" #conector Base de datos

    #constructor
    def __init__(self, host, user, passw, database, port, tipo_bd):

        # Conector Sqlite
        if tipo_bd == "sqlite":
            self.db = DAL("sqlite://" + database + ".db")
        
        # Conector Mysql
        elif tipo_bd == "mysql":
            self.db = DAL("mysql://" + user + ":" + passw + "@" + host + "/" + database)

        # Conector Postgresql
        elif tipo_bd == "postgres":
            self.db = DAL("postgres://" + user + ":"  + passw + "@" + host + "/" + database )
    
        # Conector Sql server
        elif tipo_bd == "sqlserver":
            self.db = DAL("mssql4://" + user + ":" + passw+ "@" + host+ "/" + database )
    
        # Conector Firebird
        elif tipo_bd == "firebird":
            self.db = DAL("firebird://" + user + ":" + passw+ "@" + host+ "/" + database )

        # Conector Oracle
        elif tipo_bd == "oracle":
            self.db = DAL("oracle://" + user + ":" + passw+ "@" + host+ "/" + database )  
        
        # Conector BD2
        elif tipo_bd == "db2":
            self.db = DAL("db2://" + user + ":" + passw+ "@" + database )

        # Conector Ingress
        elif tipo_bd == "ingres":
            self.db = DAL("ingres://" + user + ":" + passw + "@" + host + "/" + database )
        

    # funcion para la ejecucion de consultas sql tipo insert, delete, update
    def query (self, sql):
        try:
            self.db.executesql(sql)
            self.db.commit()
            return True
        except:
            return False
    
    # funcion para la ejecucion de transancciones (multiples consultas sql) 
    def transaction (self, list):
        try:
            for l in list:
                self.db.executesql(l)
            self.db.commit()
            return True
        except:
            return False

    # funcion para la ejecucion de consultas sql tipo select (obtener datos)        
    def getdata(self, sql):
        q = self.db.executesql(sql)
        self.db.commit()
        return q
        

