import mysql.connector

f = open("config.txt", "r")
user = f.readline().split(" ")[1][:-1]
contra = f.readline().split(" ")[1][:-1]


connection = mysql.connector.connect(host='localhost',
                                     database='gestor_de_grupos',
                                     user=user,
                                     password=contra)

cursor = connection.cursor()


''' tables '''
def create_table_Usuarios():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Usuarios (
        Nombre varchar(255) NOT NULL,
        Contra varchar(255) NOT NULL,
        PRIMARY KEY(Nombre))
    ''')
    connection.commit()
def create_table_Grupos():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Grupos (
        Nombre varchar(255) NOT NULL,
        Contra varchar(255),
        Admin varchar(255),
        FechaLimite varchar(10),
        PRIMARY KEY (Nombre),
        FOREIGN KEY (Admin) REFERENCES Usuarios(Nombre))
    ''')
    connection.commit()
def create_table_Miembros():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Miembros (
        IDMiembro int AUTO_INCREMENT,
        Grupo varchar(255) NOT NULL,
        Usuario varchar(255) NOT NULL,
        PRIMARY KEY(IDMiembro),
        FOREIGN KEY(Grupo) REFERENCES Grupos(Nombre),
        FOREIGN KEY(Usuario) REFERENCES Usuarios(Nombre))
    ''')
    connection.commit()
def create_table_Disps():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Disps (
        IDDisp int AUTO_INCREMENT,
        Usuario varchar(255) NOT NULL,
        Grupo varchar(255),
        Fecha varchar(10) NOT NULL,
        PRIMARY KEY(IDDisp),
        FOREIGN KEY(Usuario) REFERENCES Usuarios(Nombre),
        FOREIGN KEY(Grupo) REFERENCES Grupos(Nombre))
    ''')
    connection.commit()
def create_table_Notifs():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Notifs (
        IDNoti int AUTO_INCREMENT,
        Usuario varchar(255) NOT NULL,
        Grupo varchar(255) NOT NULL,
        Mensaje varchar(255),
        PRIMARY KEY(IDNoti),
        FOREIGN KEY(Usuario) REFERENCES Usuarios(Nombre),
        FOREIGN KEY(Grupo) REFERENCES Grupos(Nombre))
    ''')

def crear_tablas():
    create_table_Usuarios()
    create_table_Grupos()
    create_table_Miembros()
    create_table_Disps()
    create_table_Notifs()

''' Grupo '''
def crear_grupo(grupo, contra, admin, fechaLimite): # tiene que ser único
    sql = "INSERT INTO Grupos (Nombre, Contra, Admin, FechaLimite) VALUES (%s, %s, %s, %s)"
    val = (grupo, contra, admin, fechaLimite)
    cursor.execute(sql, val)
    connection.commit()
def eliminar_grupo(grupo):
    sql = 'DELETE FROM Grupos WHERE Nombre = "' + grupo + '"'
    cursor.execute(sql)
    connection.commit()
def get_mis_miembros(grupo): # retorna ['usuario1', 'usuario2' ... ]
    sql  = 'SELECT * FROM Miembros WHERE Grupo = "' + grupo + '"ORDER BY Usuario ASC'
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.commit()
    miembros = []
    for i, v in enumerate(result):
        miembros.append(v[2])
    return(miembros)
def get_propiedades(grupo): # retorna ['Grupo1', 'contra', 'admin', 'fechaLimite']
    sql = 'SELECT * FROM Grupos WHERE Nombre = "' +  grupo + '"'
    cursor.execute(sql)
    result = cursor.fetchall()[0]
    return(result)
def editar_grupo(grupo, contra, admin, fechaLimite): #no se puede editar el nombre
    sql = 'UPDATE Grupos SET Contra = "' + contra + '", Admin = "' + admin + '", FechaLimite = "' + fechaLimite + '"  WHERE Nombre = "' + grupo + '"'
    cursor.execute(sql)
    connection.commit()

''' Usuario '''
def crear_usuario(usuario, contra):
    sql = "INSERT INTO Usuarios (Nombre, Contra) VALUES (%s, %s)"
    val = (usuario, contra)
    cursor.execute(sql, val)
    connection.commit()
def eliminar_usuario(usuario):
    sql = 'DELETE FROM Usuarios WHERE Nombre = "' + usuario + '"'
    cursor.execute(sql)
    connection.commit()
def get_contra(usuario):
    sql  = 'SELECT * FROM Usuarios WHERE Nombre = "' + usuario + '"'
    cursor.execute(sql)
    result = cursor.fetchall()[0][1]
    return (result)
def editar_contra(usuario, contra):
    sql = 'UPDATE Usuarios SET Contra = "' + contra + '"WHERE Nombre = "' + usuario + '"'
    cursor.execute(sql)
    connection.commit()

def get_mis_grupos(usuario): # retorna ['Grupo1', 'Grupo2' ... ]
    sql  = 'SELECT * FROM Miembros WHERE Usuario = "' + usuario + '" ORDER BY Grupo ASC'
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.commit()
    grupos =  []
    for i, v in enumerate(result):
        grupos.append(v[1])
    return(grupos)
def anadir_miembro(usuario, grupo):
    sql = "INSERT INTO Miembros (Grupo, Usuario) VALUES (%s, %s)"
    val = (grupo, usuario)
    cursor.execute(sql, val)
    connection.commit()
def eliminar_miembros_usuario(usuario):
    sql = 'DELETE FROM Miembros WHERE Usuario = "' + usuario + '"'
    cursor.execute(sql)
    connection.commit()
def eliminar_miembros_grupo(grupo):
    sql = 'DELETE FROM Miembros WHERE Grupo = "' + grupo + '"'
    cursor.execute(sql)
    connection.commit()

''' Disponiblilidades '''
def anadir_disponbilidad(usuario, grupo, fecha):
    sql = "INSERT INTO Disps (Usuario, Grupo, Fecha) VALUES (%s, %s, %s)"
    val = (usuario, grupo, fecha)
    cursor.execute(sql, val)
    connection.commit()
def eliminar_disponibilidad(usuario, grupo, fecha):
    sql = 'DELETE FROM Disps WHERE Usuario = "' + usuario + '" AND Grupo = "' + grupo + '" AND Fecha = "' + fecha + '"'
    cursor.execute(sql)
    connection.commit()
def eliminar_disponibilidad_usuario(usuario):
    sql = 'DELETE FROM Disps WHERE Usuario = "' + usuario + '"'
    cursor.execute(sql)
    connection.commit()
def eliminar_disponibilidad_grupo(grupo):
    sql = 'DELETE FROM Disps WHERE Grupo = "' + grupo + '"'
    cursor.execute(sql)
    connection.commit()
def get_disponibilidades_usuario(usuario): # retorna [("Grupo1", IDfecha1), ("Grupo2", IDfecha2) ... ]
    sql  = 'SELECT * FROM Disps WHERE Usuario = "' + usuario + '"'
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.commit()
    disps =  []
    for i, v in enumerate(result):
        disp = (v[2], v[3])
        disps.append(disp)
    return(disps)
def get_disponibilidades_grupo(grupo): # retorna [("Grupo1", IDfecha1), ("Grupo2", IDfecha2) ... ]
    sql  = 'SELECT * FROM Disps WHERE Grupo = "' + grupo + '"'
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.commit()
    disps =  []
    for i, v in enumerate(result):
        disp = (v[1], v[3])
        disps.append(disp)
    return(disps)

def get_disponibilidades_grupo_usuario(grupo, usuario):

    # definimos la comanda para obtener las disponibilidaes que tienen el usuario y el grupo que queremos
    sql  = 'SELECT * FROM Disps WHERE Grupo = "' + grupo + '" AND Usuario = "' + usuario + '" ORDER BY Fecha'

    cursor.execute(sql) # ejecutamos la comanda SQL
    result = cursor.fetchall() # obtenemos el resultado
    connection.commit() # cerramos la conexión

    disps =  [] # definimos la lista de disponibilidades que queramos devolver al usuario
    for i, v in enumerate(result): #iteramos sobre el resultado
        disps.append(v[3]) # añadimos solamente el campo de la fecha a la lista de disponibilidades

    return(disps) # devolvemos la lista de disponibilidades

def get_disponibles_grupo_fecha(grupo, fecha): # retorna ["Usuario1", Usuario2 ... ]
    sql  = 'SELECT * FROM Disps WHERE Grupo = "' + grupo + '" AND Fecha = "' + fecha + '" ORDER BY Usuario ASC'
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.commit()
    disps =  []
    for i, v in enumerate(result):
        disp = (v[1])
        disps.append(disp)
    return(disps)


''' Notificaciones'''
def anadir_notificacion(usuario, grupo, mensaje):
    sql = "INSERT INTO Notifs (Usuario, Grupo, Mensaje) VALUES (%s, %s, %s)"
    val = (usuario, grupo, mensaje)
    cursor.execute(sql, val)
    connection.commit()
def borrar_notificacion_idnoti(IDnoti): # le tienes que passar el IDNoti
    sql = 'DELETE FROM Notifs WHERE IDNoti = "' + str(IDnoti) + '"'
    cursor.execute(sql)
    connection.commit()
def borrar_notificacion(usuario, grupo):
    sql = 'DELETE FROM Notifs WHERE Usuario = "' + usuario + '" AND Grupo = "' + grupo + '"'
    cursor.execute(sql)
    connection.commit()
def get_notificaciones_usuario(usuario): # retorna [(Grupo, "mensaje"), ...]
    sql  = 'SELECT * FROM Notifs WHERE Usuario = "' + usuario + '"'
    cursor.execute(sql)
    result = cursor.fetchall()
    connection.commit()
    disps =  []
    for i, v in enumerate(result):
        disp = (v[2], v[3])
        disps.append(disp)
    return(disps)

''' Globales '''
def get_usuarios(): # retorna todos los usuarios
    sql = 'SELECT * FROM Usuarios'
    cursor.execute(sql)
    result = cursor.fetchall()
    usuarios = []
    for i, v in enumerate(result):
        usuarios.append(v[0])
    return(usuarios)
def get_grupos(): # retorna todos los usuarios
    sql = 'SELECT * FROM Grupos'
    cursor.execute(sql)
    result = cursor.fetchall()
    grupos = []
    for i, v in enumerate(result):
        grupos.append(v[0])
    return(grupos)

''' otras funciones '''

def fecha_es_valida(fecha): # devuelve True o False, si la fecha existe o no

    f = fecha.split("-") # crea una lista de la fecha separada por guiones

    for i in range(3):
        f[i] = int(f[i]) # asigna a la lista f los valores separados de la fecha

    dias = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # días que tiene cada mes

    if f[2]%4==0 and (f[2]%100 != 0 or f[2]%400==0): # caso en el que es un año bisiesto
        dias[2] = 29 # febrero tiene 29 días

    return (1 <= f[1] <= 12 and 1 <= f[0] <= dias[f[1]])
    # devuelve True solo si todas las condiciones se cumplen


def get_fecha(dia):
    l = dia.split("-")
    fecha = l[2] + '-' + l[1] + '-' + l[0]
    return fecha
