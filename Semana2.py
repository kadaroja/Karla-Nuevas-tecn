biblioteca = {
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}
def agregar_libro():
    titulo = input("Ingrese el titulo del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = int(input("Ingrese el año del libro: "))

    biblioteca[titulo]={"autor": autor, "año": año, "disponible": True}

agregar_libro()

print(biblioteca)

def prestar_libro():
    """Marca un libro como no disponible."""
    titulo = input("Introduce el título del libro que deseas prestar: ")
    if titulo in biblioteca:
        if biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = False
            print(f"El libro '{titulo}' ha sido prestado.")
        else:
            print(f"El libro '{titulo}' ya está prestado.")
    else:
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

def devolver_libro():
    """Marca un libro como disponible."""
    titulo = input("Introduce el título del libro que deseas devolver: ")
    if titulo in biblioteca:
        if not biblioteca[titulo]["disponible"]:
            biblioteca[titulo]["disponible"] = True
            print(f"El libro '{titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{titulo}' ya está disponible.")
    else:
        print(f"El libro '{titulo}' no se encuentra en la biblioteca.")

def mostrar_libros():
    """Muestra todos los libros en la biblioteca con su información."""
    if not biblioteca:
        print("La biblioteca está vacía.")
    else:
        for titulo, info in biblioteca.items():
            disponibilidad = "Disponible" if info["disponible"] else "Prestado"
            print(f"Título: {titulo}")
            print(f"  Autor: {info['autor']}")
            print(f"  Año: {info['año']}")
            print(f"  Estado: {disponibilidad}")
            print()

def libros_por_año():
    """Muestra los libros publicados en un año específico."""
    año = int(input("Introduce el año para buscar libros: "))
    encontrados = False
    for titulo, info in biblioteca.items():
        if info["año"] == año:
            if not encontrados:
                print(f"Libros publicados en {año}:")
                encontrados = True
            disponibilidad = "Disponible" if info["disponible"] else "Prestado"
            print(f"Título: {titulo}")
            print(f"  Autor: {info['autor']}")
            print(f"  Estado: {disponibilidad}")
            print()
    if not encontrados:
        print(f"No se encontraron libros publicados en {año}.")

def menu():
    """Muestra el menú y gestiona la interacción del usuario."""
    while True:
        print("Menú:")
        print("1. Agregar un nuevo libro")
        print("2. Prestar un libro")
        print("3. Devolver un libro")
        print("4. Ver todos los libros")
        print("5. Buscar libros por año")
        print("6. Salir")
        
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            prestar_libro()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            mostrar_libros()
        elif opcion == "5":
            libros_por_año()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 6.")


menu()

    