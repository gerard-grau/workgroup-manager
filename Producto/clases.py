import db

class Grupo:
    def __init__ (self, grupo): # el constructor de la clase
        props = db.get_propiedades(grupo) # obtenemos la lista de propiedades que hacen
                                          # referencia al grupo de la base de datos

        self.nombre = props[0] # asigmanos a los atributos de la clase grupo los
        self.contra = props[1] # valores obtenidos anteriormente
        self.admin = props[2]
        self.fechaLimite = props[3]

    # setters:
    def set_contrasena(self, contra):
        self.contra = contra
        self.actualizar_props()
    def set_admin(self, admin):
        self.admin = admin
        self.actualizar_props()
    def set_fechaLimite(self, fechaLimite): # fechaLimite = "dd-mm-aaaa"
        self.fechaLimite = fechaLimite
        self.actualizar_props()

    # otros
    def get_miembros(self): # obtenemos los miembros del grupo, a través de la base de datos
        return db.get_mis_miembros(self.nombre)

    def get_disps(self): # obtenemos las disponibilidades referentes al grupo
        return db.get_disponibilidades_grupo(self.nombre)

    def get_props(self): # obtenemos las propiedades del grupo, guardadas el la base de datos
        return db.get_propiedades(self.nombre)

    def eliminar(self): # elimina el grupo y todo lo referente a él (disponibilidades y miembros)
        db.eliminar_disponibilidad_grupo(self.nombre)
        db.eliminar_miembros_grupo(self.nombre)
        db.eliminar_grupo(self.nombre)
        del self

    def actualizar_props(self): # actualiza las propiedades del grupo, cogiendo las de la base de datos
        db.editar_grupo(self.nombre, self.contra, self.admin, self.fechaLimite)


class Usuario:
    def __init__ (self, usuario):
        self.nombre = usuario
        self.contra = db.get_contra(usuario)
        self.grupos = db.get_mis_grupos(usuario)

    # otros
    def anadir_grupo(self, grupo):
        db.anadir_miembro(self.nombre, grupo)
    def get_grupos(self):
        return db.get_mis_grupos(self.nombre)
    def anadir_disponbilidad(self, grupo, fecha):
        db.anadir_disponbilidad(self.nombre, grupo, fecha)
    def eliminar(self):
        db.eliminar_disponibilidad_usuario(self.nombre)
        db.eliminar_miembros_usuario(self.nombre)
        db.eliminar_usuario(self.nombre)
        del self
