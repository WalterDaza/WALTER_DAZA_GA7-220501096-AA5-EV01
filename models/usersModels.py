from database.dataSource import DataSourceMysql #importación de conexión de base de datos
from database.settings import configuracion #asignación de valores db

connetion = DataSourceMysql(
    configuracion["host"],
    configuracion["user"],
    configuracion["password"],
    configuracion["db"],
    configuracion["port"],
    configuracion["tipo_bd"]
)

#Registrar usuarios*******************************************************
def registroUsuariosModel(datos):
    sql = """
    INSERT INTO users
        (id, usuario, contrasena)
    VALUES
        (NULL, '{0}', '{1}')
    """.format(datos[0], datos[1])

    return connetion.query(sql)

#Login Usuaarios**********************************************************
def loginUsuarioModel(datos):
    sql = """
    SELECT * FROM `users` 
    WHERE 
        `usuario` = '{0}' and 
        `contrasena` = '{1}';
    """.format(datos[0], datos[1]) #consulta la información en db y devuelve la consulta

    result = connetion.getdata(sql)

    if result: #si existe el usuario traera un [] con la información del usuario encontrado
        return result
    else: 
        return None #si trae información que retorne None