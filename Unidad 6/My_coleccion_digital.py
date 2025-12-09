import os
import pickle

TXT_FILE = "canciones.txt"
BIN_FILE = "estadisticas.bin"

def crear_archivos():
    try:
        if not os.path.exists(TXT_FILE):
            with open(TXT_FILE, "w", encoding="utf-8") as f:
                f.write("")

        if not os.path.exists(BIN_FILE):
            with open(BIN_FILE, "wb") as f:
                pickle.dump({}, f)

    except Exception as e:
        print("Error al crear archivos:", e,"...")

def agregar_cancion():
    try:
        nombre = input("Nombre de la canción: ").strip()
        if nombre == "":
            raise ValueError("El nombre no puede estar vacío.")

        artista = input("Artista: ").strip()
        anio = input("Año: ").strip()
        categoria = input("Género/Categoría: ").strip()

        try:
            calificacion = float(input("Calificación (0-10): "))
        except:
            raise ValueError("La calificación debe ser numérica.")

        with open(TXT_FILE, "a", encoding="utf-8") as file:
            file.write(f"{nombre}|{artista}|{anio}|{categoria}|{calificacion}\n")

        try:
            popularidad = int(input("Popularidad (1-100): "))
        except:
            raise ValueError("La popularidad debe ser un número entero.")

        if not (1 <= popularidad <= 100):
            raise ValueError("Popularidad debe estar entre 1 y 100.")

        with open(BIN_FILE, "rb") as f:
            datos = pickle.load(f)

        datos[nombre.lower()] = popularidad

        with open(BIN_FILE, "wb") as f:
            pickle.dump(datos, f)

        print("Canción agregada exitosamente     :)\n")

    except ValueError as ve:
        print("Error:", ve)

    except Exception as e:
        print("Ocurrió un error al agregar la canción:", e)

    finally:
        print("----------Operación finalizada----------\n")

def mostrar_canciones():
    try:
        if not os.path.exists(TXT_FILE):
            raise FileNotFoundError("El archivo de canciones no existe.")

        with open(TXT_FILE, "r", encoding="utf-8") as file:
            contenido = file.readlines()

        if len(contenido) == 0:
            print("No hay canciones registradas.\n")
            return

        print("\n========== COLECCIÓN DE CANCIONES ==========")
        for linea in contenido:
            nombre, artista, anio, categoria, calificacion = linea.strip().split("|")
            print(f"🎵 {nombre} — {artista} ({anio}) [{categoria}] ⭐{calificacion}")

        print("==============================================\n")

    except FileNotFoundError as e:
        print("Error:", e)


def buscar_cancion():
    try:
        busqueda = input("Nombre a buscar: ").strip().lower()
        if busqueda == "":
            raise ValueError("La entrada no puede estar vacía.")

        encontrado = False

        with open(TXT_FILE, "r", encoding="utf-8") as file:
            for linea in file:
                nombre, artista, anio, categoria, calificacion = linea.strip().split("|")

                if nombre.lower() == busqueda:
                    print("\n✔ Canción encontrada:")
                    print(f" {nombre} — {artista} ({anio}) [{categoria}] ⭐{calificacion}\n")
                    encontrado = True
                    break

        if not encontrado:
            print(" No se encontró la canción.\n")

    except Exception as e:
        print(" Error al buscar:", e)


def mostrar_datos_binarios():
    try:
        if not os.path.exists(BIN_FILE):
            raise FileNotFoundError("El archivo binario no existe.")

        with open(BIN_FILE, "rb") as f:
            datos = pickle.load(f)

        if len(datos) == 0:
            print("No hay datos binarios registrados.\n")
            return

        print("\n=============== DATOS BINARIOS ==============")
        for nombre, valor in datos.items():
            print(f"{nombre.title()}: Popularidad {valor}/100")
        print("==============================================\n")

    except Exception as e:
        print(" Error al leer archivo binario:", e)

def menu():
    crear_archivos()

    while True:
        print("=========== MI COLECCIÓN DIGITAL ===========")
        print("1. Agregar canción")
        print("2. Mostrar colección completa")
        print("3. Buscar canción por nombre")
        print("4. Mostrar datos binarios")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_cancion()
        elif opcion == "2":
            mostrar_canciones()
        elif opcion == "3":
            buscar_cancion()
        elif opcion == "4":
            mostrar_datos_binarios()
        elif opcion == "5":
            print(" Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.\n")

if __name__ == "__main__":
    menu()