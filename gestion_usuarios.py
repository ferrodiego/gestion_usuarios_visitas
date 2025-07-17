import json
from pathlib import Path

archivo_usuarios = Path('usuarios.json')

if not archivo_usuarios.exists():
    with open(archivo_usuarios, 'w', encoding='utf-8') as f:
        json.dump({}, f, indent=4, ensure_ascii=False)


def registrar_usuario(nombre, clave):
    """Registra un nuevo usuario si no existe
    """
    try:
        with open(archivo_usuarios, 'r', encoding='utf-8') as f:
            usuarios = json.load(f)
    except json.JSONDecodeError:
        print('Error al abrir el archivo, se inicia vacio')
        usuarios = {}
    
    if not nombre:
        print('El nombre de usuario no puede estar vacio')
        return
    if nombre in usuarios:
        print(f"El nombre {nombre}, ya se encuentra registrado")
        return
    
    if not clave:
        print('Su clave no puede estar vacio')
        return
    
    usuarios[nombre] = clave
    with open(archivo_usuarios, 'w', encoding='utf-8') as f:
        json.dump(usuarios, f, indent=4)
    
    print(f" Usuario {nombre} registrado con exito")
    


def inicio_sesion(nombre, clave):
    """Inicia sesion, verifica registro y clave de usuario
    """
    try:
        with open(archivo_usuarios, 'r', encoding='utf-8') as f:
            usuarios = json.load(f)
    except json.JSONDecodeError:
        print('Error al intentar leer el archivo')
        return

    if nombre not in usuarios:
        print('El usuario no está registrado.')
        return False
    elif usuarios[nombre] != clave:
        print('Clave incorrecta.')
        return False
    else:
        print('Inicio de sesión exitoso.')
        return True


def cambiar_contrasenia(nombre, nueva_clave):
    """Verifica que el usuario exista, y si es asi, cambia su clave
    """    
    try:
        with open(archivo_usuarios, encoding='utf-8') as f:
            usuarios = json.load(f)
    except json.JSONDecodeError:
        print('Error al abrir el archivo')
        return
    
    if nombre not in usuarios:
        print(f"El usuario {nombre} no está registrado.")
        return
    
    nueva_clave = input("Ingresa la nueva clave: ")
    if not nueva_clave:
        print("La nueva clave no puede estar vacía.")
        return
    
    usuarios[nombre] = nueva_clave

    with open(archivo_usuarios, 'w', encoding='utf-8') as f:
            json.dump(usuarios, f, indent=4, ensure_ascii=False)
    
    print(f"Contraseña cambiada con éxito para el usuario {nombre}.")
        
