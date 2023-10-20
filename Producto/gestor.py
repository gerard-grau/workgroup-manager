from tkinter import *
from tkinter import messagebox          # és necessari!!
from tkcalendar import Calendar, DateEntry
from tkinter.ttk import Treeview
import datetime
import db
import clases

''' global variables '''
white = 'white'
black = 'black'
grey = '#ececec'

lletra = 'MONOSPACED'
bold = 'bold'
title_font = (lletra, 20, bold)


class Root():
    def __init__(self):
        self.win = Tk()
        self.win.title('Gestor de grupos')
        self.win.config(bg = white)
        self.win.resizable(False, False)

        self.frame = PortadaFrame(self.win)
        self.frame.pack()



    def change(self, frame):
        self.frame.pack_forget()
        self.frame = frame(self.win)
        self.frame.pack()


class PortadaFrame(Frame):
    def __init__(self, win):
        Frame.__init__(self, win)
        db.crear_tablas()

        self.config(bg = white)

        Label(self, text = 'Bienvenido a Gestor de grupos', font = title_font, bg = white, fg = black, justify = 'center').grid(row=0, column = 0, padx = 60, pady = (40, 30))
        Button(self, text = 'Iniciar Sesión', font = (lletra, '20'), bg = grey, fg = black, activebackground = white, activeforeground = black,width = '15', height = '3', command = self.iniciar_sesion).grid(row = 1, pady = (0, 30))
        Button(self,  text = 'Registrarse', font = (lletra, '20'), bg = grey, fg = black, activebackground = white, activeforeground = black, width = '15', height = '3', command = self.registrarse).grid(row = 2, pady = (0, 30))
        Button(self, text = "Cerrar la aplicación", bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.cerrar).grid(row = 3, pady = (0, 30))

    def iniciar_sesion(self):
        root.change(IniciarSesionFrame)

    def registrarse(self):
        root.change(RegistrarseFrame)

    def cerrar(self):
         root.win.destroy()

class RegistrarseFrame(Frame):
    def __init__(self, win):
        Frame.__init__(self, win)

        self.config(bg = white)
        row = 0
        Label(self, text = 'Crear una cuenta nueva', font = title_font, bg = white, fg = black).grid(row = row, column = 0, columnspan = 3, padx = 50, pady = 20 )

        row = 1
        Label(self, text = 'Nombre de usuario:', font = (lletra, 12), bg = white, fg = black).grid(row = 1, column = 0, padx = 20, pady = 0)
        self.nombre = Entry(self, bg = white, fg = black, width = 30)
        self.nombre.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)

        row = 2
        Label(self, text = 'Contraseña:', font = (lletra, 12), bg = white, fg = black).grid(row = row, column = 0, padx = 20, pady = 10)
        self.contra1 = Entry(self, bg = white, fg = black, width = 30, show = '•')
        self.contra1.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)

        row = 3
        Label(self, text = 'Repita su contraseña:', font = (lletra, 12), bg = white, fg = black).grid(row = row, column = 0, padx = 20, pady = 0)
        self.contra2 = Entry(self, bg = white, fg = black, width = 30, show = '•')
        self.contra2.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)

        row = 4
        Button(self, text = 'Retroceder', font = (lletra, '10'), bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.retroceder).grid(row = row, column = 1, padx = 20, pady = 20)
        Button(self, text = 'Crear Cuenta', font = (lletra, '10'), bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.crear_cuenta).grid(row = row, column = 2, padx = 20, pady = 20)

    def retroceder(self):
        root.change(PortadaFrame)

    def crear_cuenta(self):
        if (self.nombre.get() == "" or self.contra1.get() == "" or self.contra2.get() == ""):
            messagebox.showwarning("Advertencia", "Los campos no pueden estar en blanco.")
        elif (self.contra1.get() != self.contra2.get()):
            messagebox.showwarning("Advertencia", "Las contraseñas no coinciden.")
        else:

            if (self.nombre.get() in db.get_usuarios()): #el nombre de usuario ya está en la base de datos
                messagebox.showwarning("Advertencia", "El nombre de usuario ya está en uso. Introduzca otro nombre de usuario.")
                #muestra el mensaje emergente

            else: #el nombre de usuario no está en uso
                db.crear_usuario(self.nombre.get(), self.contra1.get())
                messagebox.showinfo('Información', 'Cuenta creada con éxito.' )
                #muestra el mensaje emergente

                root.change(PortadaFrame)


class IniciarSesionFrame(Frame):
    def __init__(self, win):
        Frame.__init__(self, win)

        self.labelGrupo = None

        self.config(bg = white)
        row = 0
        Label(self, text = 'Introduzca sus credenciales', font = title_font, bg = white, fg = black).grid(row = row, column = 0, columnspan = 3, padx = 50, pady = 20)
        row = 1
        Label(self, text = 'Nombre de usuario:', font = (lletra, 12), bg = white, fg = black).grid(row = 1, column = 0, padx = 20, pady = 0)
        self.nombre_usuario = Entry(self, bg = white, fg = black, width = 30)
        self.nombre_usuario.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)
        row = 2
        Label(self, text = 'Contraseña:', font = (lletra, 12), bg = white, fg = black).grid(row = row, column = 0, padx = 20, pady = 10)
        self.contra_usuario = Entry(self, bg = white, fg = black, width = 30, show = '•')
        self.contra_usuario.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)
        row = 3
        Button(self, text = 'Retroceder', font = (lletra, 10), bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.retroceder).grid(row = row, column = 1, padx = 20, pady = 20)
        Button(self, text = 'Acceder', font = (lletra, 10), bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.acceder).grid(row = row, column = 2, padx = 20, pady = 20)

    def retroceder(self):
        root.change(PortadaFrame)

    def acceder(self):
        if (self.nombre_usuario.get() == "" or self.contra_usuario.get() == ""):
            messagebox.showwarning("Advertencia", "Los campos no pueden estar en blanco.")
        elif self.nombre_usuario.get() not in db.get_usuarios():
            messagebox.showwarning('Advertencia', 'El nombre usuario no se encuentra en la base de datos.' )
        elif db.get_contra(self.nombre_usuario.get()) == self.contra_usuario.get():
            messagebox.showinfo('Información', 'Se ha accedido correctamente.' )
            global user
            user = clases.Usuario(self.nombre_usuario.get())
            root.change(MainFrame)

        else:
            messagebox.showwarning("Advertencia", "El nombre de usuario o la contraseña no coinciden con la base de datos.")

class MainFrame(Frame):
    def __init__ (self, win):
        Frame.__init__(self,win)
        self.config (bg = white)

        self.labelGrupos = None
        col = 0
        row = 0
        Label(self, text = 'Gestor de grupos del usuario "'+user.nombre+'"', font = title_font, bg = white, fg = black).grid(row = row, column = col, columnspan = 6, padx = 50, pady = (20, 0))
        col = 0
        row = 1
        Label(self, text = 'Mis grupos:', font = (lletra, 12), bg = white, fg = black).grid(row = row, column = col, columnspan = 3, pady = (20, 0))

        row = 2

        self.grupos_tree = Treeview(self, columns = (1, 2, 3), show = 'headings', selectmode="browse") # características de la tabla

        self.grupos_tree.column(1, width = 200) # creamos la columna 1 de la tabla, dandole la anchura
        self.grupos_tree.heading(1, anchor = CENTER, text = "Nombre del Grupo") # le asignamos valor a la columna 1

        self.grupos_tree.column(2, width = 250)
        self.grupos_tree.heading(2, anchor = CENTER, text = "Administrador del Grupo")

        self.grupos_tree.column(3, anchor=CENTER, width = 125)
        self.grupos_tree.heading(3, anchor = CENTER, text = "Fecha límite")

        self.grupos_tree.bind("<<TreeviewSelect>>", self.on_grupos_tree_select) # acción que se ejecuta al seleccionar una fila

        self.grupos_tree.grid(row = row, column = col, rowspan = 2, columnspan = 3, padx = (50, 10), pady = (15, 20))
        # mostar la tabla grupos_table por pantalla

        row = 4

        Button(self, text = 'Crear grupo', width = 19, height = 2,  bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.crear_grupo).grid(row = row, column = 0, padx = (50, 0), pady= (0, 50))
        Button(self, text = 'Unirse a un grupo', width = 19, height = 2,  bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.unirse_al_grupo).grid(row = row, column = 1, padx = 0, pady= (0, 50))
        Button(self, text = 'Invitar al grupo (A)', width = 19, height = 2,  bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.invitar_frame).grid(row = row, column = 2, padx = (0, 10), pady= (0, 50))

        col = 3
        row = 1
        self.grupo = None

        if not self.grupo:
            self.labelGrupos = Label(self, text = 'Seleccione un grupo para ver los miembros del grupo', font = (lletra, 12), bg = white, fg = black)
            self.labelGrupos.grid(row = row, column = col, columnspan = 3, pady = (20, 0))
        row = 2

        self.pers_tree = Treeview(self, columns = (1, 2), show = 'headings')

        self.pers_tree.column(1, anchor=CENTER, width = 250)
        self.pers_tree.heading(1, anchor = CENTER, text = "Nombre del Miembro")
        self.pers_tree.column(2, anchor=CENTER, stretch=YES , width = 150)
        self.pers_tree.heading(2, anchor = CENTER, text = "Rol")
        self.pers_tree.bind("<Double-1>", self.disp_pers_frame)

        self.actualizar_grupos_tree()
        self.pers_tree.grid(row = row, column = col, rowspan = 2, columnspan = 3, padx = 50, pady = (15, 20))


        row = 4
        Button(self, text = 'Calendario', height = 2,  bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.calendario).grid(row = row, column = 3, padx = (50, 0), pady= (0, 50))
        Button(self, text = 'Editar grupo (A)', height = 2, bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.editar_grupo_frame).grid(row = row, column = 4, pady= (0, 50))
        Button(self, text = 'Eliminar grupo (A)', height = 2, bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.eliminar_grupo).grid(row = row, column = 5, padx = (0, 50), pady= (0, 50))


        col = 6
        row = 2
        notifs = len(db.get_notificaciones_usuario(user.nombre))
        Button(self, text = 'Notificaciones (' + str(notifs) + ")" , bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.notificaciones_frame).grid(row = row, column = col, padx = (0, 50))


        row = 3
        Button(self, text = 'Cerrar sesión', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.cerrar_sesion).grid(row = row, column = col, padx = (0, 50))

        self.today = datetime.date.today()


    def crear_grupo(self): # hecho
        self.grupoRoot = Toplevel(self)
        self.grupoRoot.resizable(False, False)
        self.grupoRoot.attributes('-topmost', 'true')
        self.grupoRoot.grab_set()

        self.gruposFrame = Frame(self.grupoRoot)
        self.gruposFrame.pack()
        self.gruposFrame.config(bg = white)

        row = 0
        Label(self.gruposFrame, text = 'Crear grupo', font = title_font, bg = white, fg = black).grid(row = row, column = 0, columnspan = 3, padx = 50, pady = 20)
        row = 1
        Label(self.gruposFrame, text = 'Nombre para el grupo:', bg = white, fg = black).grid(row = 1, column = 0, padx = 20, pady = 10)
        self.nombre_grupo = Entry(self.gruposFrame, bg = white, fg = black, width = 30)
        self.nombre_grupo.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)
        row = 2
        Label(self.gruposFrame, text = 'Contraseña para el grupo:', bg = white, fg = black).grid(row = row, column = 0, padx = 20, pady = 10)
        self.contra_grupo = Entry(self.gruposFrame, bg = white, fg = black, width = 30, show = '•')
        self.contra_grupo.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)
        row = 3
        Label(self.gruposFrame, text = 'Fecha límite del grupo:\n(campo opcional)\n(formato: dd-mm-aaaa)', bg = white, fg = black).grid(row = row, column = 0, padx = 20, pady = 10)
        self.fechaLimite_grupo = Entry(self.gruposFrame, bg = white, fg = black, width = 30)
        self.fechaLimite_grupo.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)
        row = 4
        Button(self.gruposFrame, text = 'Retroceder', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.retroceder_grupo).grid(row = row, column = 1, padx = 20, pady = 20)
        Button(self.gruposFrame, text = 'Crear grupo', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.crear_grupo_grupo).grid(row = row, column = 2, padx = 20, pady = 20)

    def unirse_al_grupo(self): # hecho
        self.grupoRoot = Toplevel()
        self.grupoRoot.resizable(False, False)
        self.grupoRoot.attributes('-topmost', 'true')
        self.grupoRoot.grab_set()
        self.gruposFrame = Frame(self.grupoRoot)
        self.gruposFrame.pack()
        self.gruposFrame.config(bg = white)

        row = 0
        Label(self.gruposFrame, text = 'Unirse a grupo', font = title_font, bg = white, fg = black).grid(row = row, column = 0, columnspan = 3, padx = 50, pady = 20)
        row = 1
        Label(self.gruposFrame, text = 'Nombre del grupo:', bg = white, fg = black).grid(row = 1, column = 0, padx = 20, pady = 0)
        self.nombre_grupo = Entry(self.gruposFrame, bg = white, fg = black, width = 30)
        self.nombre_grupo.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)
        row = 2
        Label(self.gruposFrame, text = 'Contraseña del grupo:', bg = white, fg = black).grid(row = row, column = 0, padx = 20, pady = 10)
        self.contra_grupo = Entry(self.gruposFrame, bg = white, fg = black, width = 30, show = '•')
        self.contra_grupo.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)
        row = 3
        Button(self.gruposFrame, text = 'Retroceder', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.retroceder_grupo).grid(row = row, column = 1, padx = 20, pady = 20)
        Button(self.gruposFrame, text = 'Unirse al grupo', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.unirse_al_grupo_grupo).grid(row = row, column = 2, padx = 20, pady = 20)

    def retroceder_grupo(self): # hecho
        self.grupoRoot.destroy()

    def crear_grupo_grupo(self):# hecho
        fecha = self.fechaLimite_grupo.get()
        if not self.nombre_grupo.get() or not self.contra_grupo.get():
            messagebox.showwarning("Advertencia", 'Los campos "Nombre" y "Contraseña" no pueden estar en blanco.', parent = self.gruposFrame, )
        elif self.nombre_grupo.get() in db.get_grupos():
            messagebox.showwarning("Advertencia", 'El nombre de grupo ya está en uso. Introduzca otro diferente.', parent = self.gruposFrame)

        #la fecha tiene los guiones donde tienen que estar y los demás carácteres son sólo números
        elif fecha and not(fecha[0:2].isnumeric() and fecha[3:5].isnumeric() and fecha[6:10].isnumeric() and fecha[2]== "-" and fecha[5]=="-" and len(fecha) == 10):
            messagebox.showwarning("Advertencia", 'El formato de la fecha límite no tiene el formato correcto.', parent = self.gruposFrame)

        # la fecha corresponde a un dia real, es decir, no es el 31 de febrero
        elif fecha and not db.fecha_es_valida(fecha):
            messagebox.showwarning("Advertencia", 'La fecha introducida no existe.', parent = self.gruposFrame)

        # la fecha es posterior al día de hoy
        elif fecha and datetime.date(day = int(fecha[0:2]), month = int(fecha[3:5]), year = int(fecha[6:10])) < self.today:
            messagebox.showwarning("Advertencia", 'La fecha límite no puede ser anterior al día de hoy.', parent = self.gruposFrame)

        else:
            if fecha:
                db.crear_grupo(self.nombre_grupo.get(), self.contra_grupo.get(), user.nombre, self.fechaLimite_grupo.get())
            else:
                db.crear_grupo(self.nombre_grupo.get(), self.contra_grupo.get(), user.nombre, "-")
            db.anadir_miembro(user.nombre, self.nombre_grupo.get())
            messagebox.showinfo('Crear grupo', 'Grupo creado correctamente', parent = self.gruposFrame)
            self.grupoRoot.destroy()
            # root.change(MainFrame)
            self.actualizar_grupos_tree()

    def unirse_al_grupo_grupo(self): #hecho
        if not self.nombre_grupo.get() or not self.contra_grupo.get():
            messagebox.showwarning("Advertencia", 'Los campos no pueden estar en blanco.', parent = self.gruposFrame, )
        elif not self.nombre_grupo.get() in db.get_grupos():
            messagebox.showwarning("Advertencia", 'El grupo no existe.', parent = self.gruposFrame)
        elif self.contra_grupo.get() != db.get_propiedades(self.nombre_grupo.get())[1]:
            messagebox.showwarning("Advertencia", 'El nombre del grupo y la contraseña no coinciden.', parent = self.gruposFrame)
        elif user.nombre in db.get_mis_miembros(self.nombre_grupo.get()):
            messagebox.showwarning("Advertencia", 'El usuario ya se encuentra en este grupo.', parent = self.gruposFrame)
        else:
            db.anadir_miembro(user.nombre, self.nombre_grupo.get())
            messagebox.showinfo('Unirse al grupo', 'Unido al grupo correctamente', parent = self.gruposFrame)
            self.grupoRoot.destroy()
            # root.change(MainFrame)
            self.actualizar_grupos_tree()


    def invitar_frame(self):
        if self.grupo == None:
            messagebox.showwarning("Advertencia", 'Debe seleccionar un grupo de la tabla de la izquierda para poder invitar un usuario al grupo.')
        elif user.nombre != self.grupo.admin:
            messagebox.showwarning("Advertencia", 'Sólo el administrador de un grupo puede invitar usuarios al grupo.')
        else:
            self.invitarRoot = Toplevel()
            self.invitarRoot.resizable(False, False)
            self.invitarRoot.attributes('-topmost', 'true')
            self.invitarRoot.grab_set()
            self.invitarFrame = Frame(self.invitarRoot)
            self.invitarFrame.pack()
            self.invitarFrame.config(bg = white)

            row = 0
            Label(self.invitarFrame, text = 'Invitar usuario al grupo "' + self.grupo.nombre + '"', font = title_font, bg = white, fg = black).grid(row = row, column = 0, columnspan = 3, padx = 50, pady = (30, 10))

            row = 1
            Label(self.invitarFrame, text = 'Nombre del usuario invitado:', bg = white, fg = black).grid(row = row, column = 0, padx = 10, pady = 10)
            self.usuario = Entry(self.invitarFrame, bg = white, fg = black, width = 30)
            self.usuario.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)

            row = 2
            Label(self.invitarFrame, text = 'Mensaje para el usuario:\n(opcional)', bg = white, fg = black).grid(row = row, column = 0, padx = 20, pady = 0)
            self.mensaje = Entry(self.invitarFrame, bg = white, fg = black, width = 30)
            self.mensaje.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)

            row = 3
            Button(self.invitarFrame, text = 'Retroceder', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.retroceder_invitar_frame).grid(row = row, padx = 10, column = 1, pady = (10, 30))
            Button(self.invitarFrame, text = 'Invitar al grupo', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.invitar_usuario).grid(row = row, padx = 10, column = 2, pady = (10, 30))

    def invitar_usuario(self):
        if not self.usuario.get():
            messagebox.showwarning("Advertencia", 'El nombre del usuario invitado no puede estar en blanco', parent = self.invitarFrame)
        elif self.usuario.get() not in db.get_usuarios():
            messagebox.showwarning('Advertencia', 'El nombre de usuario no se encuentra en la base de datos', parent = self.invitarFrame)
        elif self.usuario.get() in self.grupo.get_miembros():
            messagebox.showwarning('Advertencia', 'El usuario ya se está dentro del grupo seleccionado', parent = self.invitarFrame)
        else:
            db.anadir_notificacion(self.usuario.get(), self.grupo.nombre, self.mensaje.get())
            messagebox.showinfo('Información', 'Se ha enviado la notificación de invitación al usuario "' + self.usuario.get() + '"', parent = self.invitarFrame)
            self.invitarRoot.destroy()

    def retroceder_invitar_frame(self):
        self.invitarRoot.destroy()


    def actualizar_grupos_tree(self): # función que actualiza la tabla grupos_tree

        self.grupos_tree.delete(*self.grupos_tree.get_children()) # borrar todos los datos de la tabla

        grupos = db.get_mis_grupos(user.nombre) # obtenemos los grupos del usuario que ha iniciado sesión
                                                # y los guardamos en "grupos"

        for i, g in enumerate(grupos): # iteramos sobre los grupos del usuario
            grupo = clases.Grupo(g) # creamos un objeto de la clase Grupo con el valor "g", para poder usuario
                                    # las funciones asignadas a la clase Grupo

            value = (g, grupo.admin, grupo.fechaLimite)
            self.grupos_tree.insert('', END, value = value) # añadimos el regitro value a la tabla, donde
                                                            # value = (nombre del grupo, admin del grupo,
                                                            # fecha límite del grupo)

    def on_grupos_tree_select(self, *argv): #actualiza la tabla pers_tree
        if self.grupos_tree.selection():
            item = self.grupos_tree.selection()[0]
            nombre = self.grupos_tree.item(item, "values")[0]
            self.grupo = clases.Grupo(nombre)

            # if self.labelGrupos:
            self.labelGrupos.destroy()
            self.labelGrupos = Label(self, text = 'Miembros del grupo "' + self.grupo.nombre + '":', font = (lletra, 12), bg = white, fg = black)
            self.labelGrupos.grid(row = 1, column = 3, columnspan = 3, pady = (20, 0))


            self.pers_tree.delete(*self.pers_tree.get_children())

            personas = db.get_mis_miembros(self.grupo.nombre)

            for i, p in enumerate(personas):
                if p == self.grupo.admin:
                    value = (p, "Administrador (A)")
                else:
                    value = (p, "Miembro (M)")
                self.pers_tree.insert('', END, value = value)


    def disp_pers_frame(self, e):
        if self.pers_tree.selection():

            self.dispPersRoot = Toplevel(self)
            self.dispPersRoot.resizable(False, False)
            self.dispPersRoot.attributes('-topmost', 'true')
            self.dispPersRoot.wait_visibility()
            self.dispPersRoot.grab_set()

            self.dispPersFrame = Frame(self.dispPersRoot)
            self.dispPersFrame.pack()
            self.dispPersFrame.config(bg = white)

            item = self.pers_tree.selection()[0]
            usuario = self.pers_tree.item(item, "values")[0]

            Label(self.dispPersFrame, text = 'Disponibilidades del usuario "' + usuario + '" para el grupo "' + self.grupo.nombre + '"', font = (lletra, 12), bg = white, fg = black).grid(row = 0, column = 0, padx = 20, pady = (30, 0))

            self.disp_pers_tree = Treeview(self.dispPersFrame, columns = (1), show = 'headings', height = 10)
            self.disp_pers_tree.column(1, anchor=CENTER, width = 400)
            self.disp_pers_tree.heading(1, anchor = CENTER, text = 'Fechas disponibles para el usuario "' + usuario + '"')
            self.disp_pers_tree.grid(row = 1, column = 0, padx = 50, pady = (20, 0))


            fechas = db.get_disponibilidades_grupo_usuario(self.grupo.nombre, usuario)
            for i, f in enumerate(fechas):
                self.disp_pers_tree.insert('', END, value = f)

            Button(self.dispPersFrame, text = "retroceder", bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.retroceder_disp_pers_frame).grid(row = 2, column = 0, pady = (20, 20))
            # Button(self, text = 'Acceder', font = (lletra, 10), bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.acceder).grid(row = row, column = 2, padx = 20, pady = 20)

    def retroceder_disp_pers_frame(self):
        self.dispPersRoot.destroy()


    def calendario(self):
        if self.grupo == None:
            messagebox.showwarning("Advertencia", 'Debe seleccionar un grupo de la tabla de la izquierda para poder acceder al calendario del grupo.')
        else:
            self.calendarioRoot = Toplevel()
            self.calendarioRoot.geometry('1000x450')
            self.calendarioRoot.resizable(False, False)
            self.calendarioRoot.attributes('-topmost', 'true')
            self.calendarioRoot.grab_set()
            self.calendarioFrame = Frame(self.calendarioRoot)
            self.calendarioFrame.config(bg = white)
            self.calendarioFrame.pack(fill = 'both', expand = True)

            Grid.rowconfigure(self.calendarioFrame,1,weight=1)
            Grid.columnconfigure(self.calendarioFrame,0,weight=1)

            # Grid.rowconfigure(self.calendarioFrame,3,weight=1)
            # Grid.columnconfigure(self.calendarioFrame,0,weight=1)

            Label(self.calendarioFrame, text = 'Disponibilidades del grupo "' + self.grupo.nombre + '"', font = title_font, bg = white, fg = black).grid(row = 0, column = 0, columnspan = 7, pady = (20, 0))

            self.calendarioFrameCal = Frame(self.calendarioFrame) # creamos el frame donde poner el calendario
            self.calendarioFrameCal.grid(sticky = 'nsew', row = 1, column = 0, columnspan = 4, padx = 30, pady = (20, 5)) # mostramos el frame por pantalla
            self.calendarioFrameCal.config(bg = white) # configuración del frame calendarioFrameCal

            self.calendario = Calendar(self.calendarioFrameCal, font= (lletra,  15), selectmode='day', locale='es', year=self.today.year, month=self.today.month, day=self.today.day)
            # creamos el calendario en sí, con los parámetros que se muestran justo arriba
            self.calendario.pack(fill = 'both', expand = True)
            # mostramos el calendario


            # creamos los eventos que pueden ser asignados a cada día. Asignamos a cada evento un color de
            # fondo y de letra, dependiendo de si el usuario que lo está visualizando está disponible, y
            # de cuántos usuarios más del grupo estan disponibles
            self.calendario.tag_config('si+todos', background='cyan', foreground = black)
            self.calendario.tag_config('no+todos', background='cyan', foreground = white)
            self.calendario.tag_config('si+casitodos', background='lime', foreground = black)
            self.calendario.tag_config('no+casitodos', background='lime', foreground = white)
            self.calendario.tag_config('si+muchos', background='greenyellow', foreground = black)
            self.calendario.tag_config('no+muchos', background='greenyellow', foreground = white)
            self.calendario.tag_config('si+algunos', background='gold', foreground = black)
            self.calendario.tag_config('no+algunos', background='gold', foreground = white)
            self.calendario.tag_config('si+pocos', background='orange', foreground = black)
            self.calendario.tag_config('no+pocos', background='orange', foreground = white)
            self.calendario.tag_config('si+nadie', background='tomato', foreground = black)
            self.calendario.tag_config('no+nadie', background='tomato', foreground = white)

            # asigmanos a los eventos de seleccionar un día y de cambiar de mes las funciones correspondientes:
            self.calendario.bind("<<CalendarSelected>>", self.actualizar_disps)
            self.calendario.bind("<<CalendarMonthChanged>>", self.actualizar_color_disps)


            # self.calendario.bind("<<CalendarMonthChanged>>", self.actualizar_disps)
            # padx = 4
            padx = 1
            pady = 0
            ipadx = 0
            ipady = 1
            font = (lletra, 9)
            Label(self.calendarioFrame, text = 'Disponible', font = (lletra, 9, bold), bg = 'lightgrey', fg = black, borderwidth=1, relief="solid", width = 25).grid(row = 2, column = 0, padx = (20, 10), ipady = ipady)
            Label(self.calendarioFrame, text = 'No disponible', font = (lletra, 9, bold), bg = 'darkgrey', fg = white, borderwidth=1, relief="solid", width = 25).grid(row = 3, column = 0, padx = (20, 10), pady = (0, 10), ipady = ipady)

            Label(self.calendarioFrame, text = 'Nadie disponible', font = font, bg = 'tomato', fg = black, borderwidth=1, relief="solid", width = 15).grid(row = 2, column = 1, padx = padx, ipady = ipady)
            Label(self.calendarioFrame, text = '0-25% disponibles', font = font, bg = 'orange', fg = black, borderwidth=1, relief="solid", width = 16).grid(row = 2, column = 2, padx = padx, ipady = ipady)
            Label(self.calendarioFrame, text = '25-50% disponibles', font = font, bg = 'gold', fg = black, borderwidth=1, relief="solid", width = 15).grid(row = 2, column = 3, padx = (padx, 10), ipady = ipady)

            Label(self.calendarioFrame, text = '50-75% disponibles', font = font, bg = 'greenyellow', fg = black, borderwidth=1, relief="solid", width = 15).grid(row = 3, column = 1, pady = (0, 10), ipady = ipady)
            Label(self.calendarioFrame, text = '75-100% disponibles', font = font, bg = 'lime', fg = black, borderwidth=1, relief="solid", width = 16).grid(row = 3, column = 2, pady = (0, 10), ipady = ipady)
            Label(self.calendarioFrame, text = 'Todos disponibles', font = font, bg = 'cyan', fg = black, borderwidth=1, relief="solid", width = 15).grid(row = 3, column = 3, padx = (padx, 10), pady = (0, 10), ipady = ipady)

            self.disps_tree = Treeview(self.calendarioFrame, columns = (1), show = 'headings', height = 14)

            self.disps_tree.column(1, anchor=CENTER, width = 400)
            self.disps_tree.heading(1, anchor = CENTER, text = "Miembros disponibles el dia " + db.get_fecha(str(self.calendario.selection_get())))
            # self.disps_tree.bind("<<TreeviewSelect>>")

            self.disps_tree.grid(row = 1, column = 4, columnspan = 2, padx = (30, 30), pady = (15, 0))
            # self.ev_ids = []
            self.actualizar_disps()
            self.actualizar_color_disps()

            Button(self.calendarioFrame, text = 'Alternar mi disponibilidad', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.alternar_disp).grid(row = 2, column = 4, rowspan = 2, padx = (30, 0), pady = (10, 20))
            Button(self.calendarioFrame, text = 'Retroceder', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.retroceder_calendario).grid(row = 2, column = 5, rowspan = 2, padx = (0, 30), pady = (10, 20))

    def actualizar_disps(self, *argv): #hecho
        self.disps_tree.heading(1, anchor = CENTER, text = "Miembros disponibles el dia " + db.get_fecha(str(self.calendario.selection_get())))
        self.disps_tree.delete(*self.disps_tree.get_children())

        l = str(self.calendario.selection_get()).split("-")
        self.fecha = l[2]+'-'+l[1]+'-'+l[0]
        disponibles = db.get_disponibles_grupo_fecha(self.grupo.nombre, self.fecha)
        for i, p in enumerate(disponibles):
            value = (p)
            self.disps_tree.insert('', END, value = value)

    def actualizar_color_disps(self, *argv):
        self.mes = self.calendario.get_displayed_month()[0] # obtener el mes seleccionado
        self.ano = self.calendario.get_displayed_month()[1] # obtener el dia seleccionado

        self.calendario.calevent_remove("all")

        from calendar import monthrange
        days = monthrange(self.ano, self.mes)[1] # calculamos los dias que tiene el mes seleccionado

        for i in range(1, days+1): # iteramos sobre los dias del mes, des de el 1 hasta el último dia del mes
            date = datetime.date(self.ano, self.mes, i) # creamos una fecha del dia en el que iteramos
            str_i = str(i)
            str_mes = str(self.mes)
            if len(str_i) == 1:
                str_i = '0' + str(i)
            if len(str_mes) == 1:
                str_mes = '0' + str(self.mes)
            fecha = str_i + "-" + str_mes + "-" + str(self.ano) # adaptamos la fecha a nuestro formato dd-mm-aaaa

            if (user.nombre) in db.get_disponibles_grupo_fecha(self.grupo.nombre, fecha): # miramos si el usuario que está registrado
                disp_user = 1                                                             # está disponible el dia sobre el que iteramos
            else:
                disp_user = 0

            disponibles = len(db.get_disponibles_grupo_fecha(self.grupo.nombre, fecha)) # obtenemos los miembros disponibles del dia sobre
            miembros = len(self.grupo.get_miembros())                                   # el que iteramos

            # asigmanos un valor dependeindo del porcentaje de miembros disponibles en ese día
            if disponibles == 0:
                disp_grupo = 0
            elif disponibles < 0.25 * miembros:
                disp_grupo = 1
            elif disponibles < 0.5 * miembros:
                disp_grupo = 2
            elif disponibles < 0.75 * miembros:
                disp_grupo = 3
            elif disponibles < miembros:
                disp_grupo = 4
            else:
                disp_grupo = 5

            # asigmanos el valor correspondiente al evento del calendario segun la disponibilidad del usuario y de los demás miembros
            val_disp_user = ["no+", "si+"]
            text_disp_user = ["Usuario no disponible, ", "Usuario disponible, "]
            val_disp_grupo = ["nadie", "pocos", "algunos", "muchos", "casitodos", "todos"]
            text_disp_grupo = ["ningún miembro disponible", "0-25 % miembros disponibles", "25-50 % miembros disponibles", "50-75 % miembros disponibles", "75-100 % miembros disponibles", "todos los miembros disponibles"]

            #creamos el evento en el dia sobre el que iteramos, de acuerdo con los valores anteriores
            self.calendario.calevent_create(date, text_disp_user[disp_user] + text_disp_grupo[disp_grupo], val_disp_user[disp_user]+val_disp_grupo[disp_grupo])

    def alternar_disp(self):
        if (user.nombre in db.get_disponibles_grupo_fecha(self.grupo.nombre, self.fecha)):
            db.eliminar_disponibilidad(user.nombre, self.grupo.nombre, self.fecha)
        else:
            db.anadir_disponbilidad(user.nombre, self.grupo.nombre, self.fecha)
        self.actualizar_disps()
        self.actualizar_color_disps()

    def retroceder_calendario(self):
        self.calendarioRoot.destroy()


    def editar_grupo_frame(self):
        if self.grupo == None:
            messagebox.showwarning("Advertencia", 'Debe seleccionar un grupo de la tabla de la izquierda para poder acceder al panel de edición de sus propiedades.')
        elif user.nombre != self.grupo.admin:
            messagebox.showwarning("Advertencia", 'Sólo el administrador de un grupo puede editar las propiedades del grupo.')
        else:
            self.editarGrupoRoot = Toplevel()
            self.editarGrupoRoot.resizable(False, False)
            self.editarGrupoRoot.attributes('-topmost', 'true')
            self.editarGrupoRoot.grab_set()
            self.editarGrupoFrame = Frame(self.editarGrupoRoot)
            self.editarGrupoFrame.pack()
            self.editarGrupoFrame.config(bg = white)

            row = 0
            Label(self.editarGrupoFrame, text = 'Editar propiedades del grupo "' + self.grupo.nombre + '"', font = title_font, bg = white, fg = black).grid(row = row, column = 0, columnspan = 3, padx = 50, pady = 20)
            row = 1
            Label(self.editarGrupoFrame, text = 'Nueva contraseña del grupo:\n(campo opcional)', bg = white, fg = black).grid(row = 1, column = 0, padx = 20, pady = 0)
            self.newContra_grupo = Entry(self.editarGrupoFrame, bg = white, fg = black, width = 30)
            self.newContra_grupo.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)
            row = 2
            Label(self.editarGrupoFrame, text = 'Nuevo administrador del grupo:\n(campo opcional)', bg = white, fg = black).grid(row = row, column = 0, padx = 20, pady = 10)
            self.newAdmin_grupo = Entry(self.editarGrupoFrame, bg = white, fg = black, width = 30)
            self.newAdmin_grupo.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)
            row = 3
            Label(self.editarGrupoFrame, text = 'Nueva fecha límite:\n(campo opcional)\n(formato: dd-mm-aaaa)', bg = white, fg = black).grid(row = row, column = 0, padx = 20, pady = 10)
            self.newFechaLimite_grupo = Entry(self.editarGrupoFrame, bg = white, fg = black, width = 30)
            self.newFechaLimite_grupo.grid(row = row, column = 1, columnspan = 2, padx = 10, pady = 10)
            row = 4
            Button(self.editarGrupoFrame, text = 'Retroceder', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.retroceder_editar_grupo).grid(row = row, column = 1, padx = 20, pady = 20)
            Button(self.editarGrupoFrame, text = 'Aplicar cambios', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.editar_grupo).grid(row = row, column = 2, padx = 20, pady = 20)

    def editar_grupo(self):
        newContra = self.grupo.contra
        newAdmin = self.grupo.admin
        newFechaLimite = self.grupo.fechaLimite

        if self.newContra_grupo.get():
            newContra = self.newContra_grupo.get()
        if self.newAdmin_grupo.get():
            if self.newAdmin_grupo.get() in self.grupo.get_miembros():
                newAdmin = self.newAdmin_grupo.get()
            else:
                messagebox.showwarning("Advertencia", 'El nombre de usuario del administrador no se encuentra entre los miembros del grupo seleccionado.', parent = self.editarGrupoFrame)
        if self.newFechaLimite_grupo.get():
            fecha = self.newFechaLimite_grupo.get()
            if not(fecha[0:2].isnumeric() and fecha[3:5].isnumeric() and fecha[6:10].isnumeric() and fecha[2]== "-" and fecha[5]=="-" and len(fecha) == 10):
                messagebox.showwarning("Advertencia", 'El formato de la fecha límite no tiene el formato correcto.', parent = self.editarGrupoFrame)
            elif not db.fecha_es_valida(fecha):
                messagebox.showwarning("Advertencia", 'La fecha introducida no existe.', parent = self.editarGrupoFrame)
            elif datetime.date(day = int(fecha[0:2]), month = int(fecha[3:5]), year = int(fecha[6:10])) < self.today:
                messagebox.showwarning("Advertencia", 'La fecha límite no puede ser anterior al día de hoy.', parent = self.editarGrupoFrame)
            else:
                newFechaLimite = self.newFechaLimite_grupo.get()
        if (not self.newFechaLimite_grupo.get()) or self.newFechaLimite_grupo.get() == newFechaLimite:
            self.grupo.set_contrasena(newContra)
            self.grupo.set_admin(newAdmin)
            self.grupo.set_fechaLimite(newFechaLimite)

            self.editarGrupoRoot.destroy()
            if len(self.grupos_tree.selection()) > 0:
                self.grupos_tree.selection_remove(self.grupos_tree.selection()[0])
            self.on_grupos_tree_select()
            self.actualizar_grupos_tree()
            # root.change(MainFrame)

    def retroceder_editar_grupo(self):
        self.editarGrupoRoot.destroy()

    def eliminar_grupo(self):
        if self.grupo == None:
            messagebox.showwarning("Advertencia", 'Debe seleccionar un grupo de la tabla de la izquierda para poder eliminarlo.')
        elif user.nombre != self.grupo.admin:
            messagebox.showwarning("Advertencia", 'Sólo el administrador de un grupo puede eliminar el grupo.')
        else:
            if messagebox.askokcancel('¿Desea borrar el grupo?', '¿Está seguro de que quiere eliminar el grupo "' + self.grupo.nombre + '"?\nTenga en cuenta que también se borrarán todos los datos vinculados a este grupo?') == True:
                nombre = self.grupo.nombre
                self.grupo.eliminar()
                messagebox.showinfo('Información', 'Grupo "' + nombre + '" eliminado correctamente.')
                # root.change(MainFrame)
                self.actualizar_grupos_tree()


    def notificaciones_frame(self):
        self.notifsRoot = Toplevel(self)
        self.notifsRoot.resizable(False, False)
        self.notifsRoot.attributes('-topmost', 'true')
        # self.dispPersRoot.wait_visibility()
        self.notifsRoot.grab_set()

        self.notifsFrame = Frame(self.notifsRoot)
        self.notifsFrame.pack()
        self.notifsFrame.config(bg = white)

        Label(self.notifsFrame, text = 'Invitaciones de grupo', font = title_font, bg = white, fg = black).grid(row = 0, column = 0, columnspan = 2, pady = (20, 0))
        # Label(self, text = 'Gestor de grupos del usuario "'+user.nombre+'"', font = title_font, bg = white, fg = black).grid(row = row, column = col, columnspan = 6, padx = 50, pady = (20, 0))

        self.notifs_tree = Treeview(self.notifsFrame, columns = (1, 2), show = 'headings', selectmode = "browse")

        self.notifs_tree.heading(1, anchor = CENTER, text = "Grupo")
        self.notifs_tree.heading(2, anchor = CENTER, text = "Mensaje")

        self.notifs_tree.grid(row = 1, column = 0, columnspan = 2, padx = 50, pady = (15, 20))

        notifs = db.get_notificaciones_usuario(user.nombre)
        # print(notifs)
        for i, n in enumerate(notifs):
            value = (n[0], n[1])
            self.notifs_tree.insert('', END, value = value)



        Button(self.notifsFrame, text = 'Retroceder', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.retroceder_notifs).grid(row = 2, column = 0, padx = (50, 0), pady = 20)
        Button(self.notifsFrame, text = 'Aceptar la invitación al grupo', bg = grey, fg = black, activebackground = white, activeforeground = black, command = self.aceptar_invitacion).grid(row = 2, column = 1, padx = (0, 50), pady = 20)

    def aceptar_invitacion(self):
        # s = self.notifs_tree.selection()
        # print(s)
        if not self.notifs_tree.selection():
            messagebox.showwarning("Advertencia", "Debe seleccionar una notificación para poder aceptar la invitación al grupo", parent = self.notifsFrame)
        else:
            item = self.notifs_tree.selection()[0]
            grupo = self.notifs_tree.item(item, "values")[0]
            if grupo in db.get_mis_grupos(user.nombre):
                messagebox.showwarning("Advertencia", "El usuario ya se encuentra en este grupo", parent = self.notifsFrame)
            else:
                db.anadir_miembro(user.nombre, grupo)
                messagebox.showinfo('Aceptar invitación', 'Invitación aceptada correctamente', parent = self.notifsFrame)
                db.borrar_notificacion(user.nombre, grupo   )
                self.notifsRoot.destroy()
                self.actualizar_grupos_tree()


                # l = str(self.calendario.selection_get()).split("-")
                # self.fecha = l[2]+'-'+l[1]+'-'+l[0]
                # disponibles = db.get_disponibles_grupo_fecha(self.grupo.nombre, self.fecha)
                # for i, p in enumerate(disponibles):
                #     value = (p)
                #     self.disps_tree.insert('', END, value = value)


    def retroceder_notifs(self):
        self.notifsRoot.destroy()


    def cerrar_sesion(self):
        root.change(PortadaFrame)

root = Root()
root.win.mainloop()
db.crear_tablas()
