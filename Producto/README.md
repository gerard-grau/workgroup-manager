Bienvenido a su gestor de grupos.

Para poder utilizar la aplicación debe tener instaladas las últimas verisiones de python y de MySQL.
- Python: https://www.python.org/downloads/
- MySQL: https://www.mysql.com/downloads/ (o a través de un comando en Linux)


También debe tener importadas las siguentes librerías, que se pueden instalar con los siguientes comandos:
- Tkcalendar: pip3 install tkcalendar
- MySQL connector: pip3 install mysql-connector-python


Por útlimo, tras instalar el sistema de gestión de bases de datos MySQL debe crear una base de datos con el nombre "gestor_de_grupos" (CREATE DATABASE gestor_de_grupos).
Para poder establecer la connexión con su base de datos, debe introducir el nombre de usuario y la contraseña de su base de datos MySQL en el archivo "config.txt".
Debe introducir los datos separados con un espacio después de los dos puntos, como se muestra a continuación:

    Usuario: user
    Contraseña: password


Para abrir la aplicación debe ejecutar el archivo gestor.py con la última versión de Python3.
