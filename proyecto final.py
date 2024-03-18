import sqlite3
from datetime import datetime

conn = sqlite3.connect('biblioteca.db')
cursor = conn.cursor()

def crear_tablas():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            direccion TEXT,
            telefono TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Libros (
            id INTEGER PRIMARY KEY,
            titulo TEXT NOT NULL,
            autor TEXT,
            precio REAL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Facturas (
            id INTEGER PRIMARY KEY,
            id_cliente INTEGER,
            id_libro INTEGER,
            monto REAL,
            FOREIGN KEY (id_cliente) REFERENCES Clientes(id),
            FOREIGN KEY (id_libro) REFERENCES Libros(id)
        )
    ''')

crear_tablas()

def agregar_cliente(nombre, direccion, telefono):
    cursor.execute('''
        INSERT INTO Clientes (nombre, direccion, telefono)
        VALUES (?, ?, ?)
    ''', (nombre, direccion, telefono))
    conn.commit()
    print("Cliente agregado exitosamente.")

def ver_clientes():
    cursor.execute('SELECT * FROM Clientes')
    clientes = cursor.fetchall()
    for cliente in clientes:
        print(cliente)

def eliminar_cliente(id_cliente):
    cursor.execute('''
        DELETE FROM Clientes
        WHERE id = ?
    ''', (id_cliente,))
    conn.commit()
    print("Cliente eliminado exitosamente.")

def editar_cliente(id_cliente, nombre, direccion, telefono):
    cursor.execute('''
        UPDATE Clientes
        SET nombre = ?,
            direccion = ?,
            telefono = ?
        WHERE id = ?
    ''', (nombre, direccion, telefono, id_cliente))
    conn.commit()
    print("Cliente actualizado exitosamente.")

def ver_libros():
    cursor.execute('SELECT * FROM Libros')
    libros = cursor.fetchall()
    for libro in libros:
        print(libro)

def agregar_libro(titulo, autor, precio):
    cursor.execute('''
        INSERT INTO Libros (titulo, autor, precio)
        VALUES (?, ?, ?)
    ''', (titulo, autor, precio))
    conn.commit()
    print("Libro agregado exitosamente.")

def eliminar_libro(id_libro):
    cursor.execute('''
        DELETE FROM Libros
        WHERE id = ?
    ''', (id_libro,))
    conn.commit()
    print("Libro eliminado exitosamente.")

def editar_libro(id_libro, titulo, autor, precio):
    cursor.execute('''
        UPDATE Libros
        SET titulo = ?,
            autor = ?,
            precio = ?
        WHERE id = ?
    ''', (titulo, autor, precio, id_libro))
    conn.commit()
    print("Libro actualizado exitosamente.")

def generar_factura(id_cliente, id_libro):
    cursor.execute('SELECT precio FROM Libros WHERE id = ?', (id_libro,))
    precio = cursor.fetchone()[0]
    cursor.execute('''
        INSERT INTO Facturas (id_cliente, id_libro, monto)
        VALUES (?, ?, ?)
    ''', (id_cliente, id_libro, precio))
    conn.commit()
    print("Factura generada exitosamente.")
    print(f"Cliente ID: {id_cliente}, Libro ID: {id_libro}, Monto: {precio}")

while True:
    print("\nMenú Principal:")
    print("1. Cliente")
    print("2. Libro")
    print("3. Factura")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("\nMenú Cliente:")
        print("1. Agregar un cliente")
        print("2. Ver todos los clientes")
        print("3. Eliminar un cliente")
        print("4. Editar información de un cliente")
        print("5. Volver al menú principal")

        opcion_cliente = input("Seleccione una opción: ")

        if opcion_cliente == '1':
            nombre = input("Nombre del cliente: ")
            direccion = input("Dirección del cliente: ")
            telefono = input("Teléfono del cliente: ")
            agregar_cliente(nombre, direccion, telefono)

        elif opcion_cliente == '2':
            ver_clientes()

        elif opcion_cliente == '3':
            id_cliente = int(input("Ingrese el ID del cliente a eliminar: "))
            eliminar_cliente(id_cliente)

        elif opcion_cliente == '4':
            id_cliente = int(input("Ingrese el ID del cliente a editar: "))
            nombre = input("Nuevo nombre del cliente: ")
            direccion = input("Nueva dirección del cliente: ")
            telefono = input("Nuevo teléfono del cliente: ")
            editar_cliente(id_cliente, nombre, direccion, telefono)

        elif opcion_cliente == '5':
            continue

    elif opcion == '2':
        print("\nMenú Libro:")
        print("1. Ver libros")
        print("2. Agregar un libro")
        print("3. Eliminar un libro")
        print("4. Editar información de un libro")
        print("5. Volver al menú principal")

        opcion_libro = input("Seleccione una opción: ")

        if opcion_libro == '1':
            ver_libros()

        elif opcion_libro == '2':
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            precio = float(input("Precio del libro: "))
            agregar_libro(titulo, autor, precio)

        elif opcion_libro == '3':
            id_libro = int(input("Ingrese el ID del libro a eliminar: "))
            eliminar_libro(id_libro)

        elif opcion_libro == '4':
            id_libro = int(input("Ingrese el ID del libro a editar: "))
            titulo = input("Nuevo título del libro: ")
            autor = input("Nuevo autor del libro: ")
            precio = float(input("Nuevo precio del libro: "))
            editar_libro(id_libro, titulo, autor, precio)

        elif opcion_libro == '5':
            continue

    elif opcion == '3':
        print("\nMenú Factura:")
        id_cliente = int(input("Ingrese el ID del cliente: "))
        id_libro = int(input("Ingrese el ID del libro: "))
        generar_factura(id_cliente, id_libro)

    elif opcion == '4':
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")