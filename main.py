from gestion_usuarios import registrar_usuario, inicio_sesion, cambiar_contrasenia
from gestion_visitas import filtrar_visitas_por_usuario, registrar_visita, borrar_historial

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Filtrar visitas por usuario")
        print("4. Cambiar contraseña")
        print("5. Borrar historial de visitas")
        print("6. Salir")

        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            nombre = input("\nNombre de usuario: ")
            clave = input("Clave: ")
            registrar_usuario(nombre, clave)
        
        elif opcion == '2':
            nombre = input("\nNombre de usuario: ")
            clave = input("Clave: ")
            if inicio_sesion(nombre, clave):
                registrar_visita(nombre)
        
        elif opcion == '3':
            nombre = input("\nNombre de usuario para filtrar visitas: ")
            filtrar_visitas_por_usuario(nombre)
        
        elif opcion == '4':
            nombre = input("\nNombre de usuario: ")
            cambiar_contrasenia(nombre)

        elif opcion == '5':
            borrar_historial()

        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()