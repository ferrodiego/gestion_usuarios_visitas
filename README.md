# Sistema de Gestión de Usuarios y Visitas

Proyecto en Python que permite:
- Registrar nuevos usuarios.
- Iniciar sesión (y registrar cada acceso como visita).
- Ver historial de visitas de cada usuario.
- Cambiar la contraseña de un usuario.
- Borrar todo el historial de visitas.

## Estructura de archivos

- `main.py` → Menú principal para ejecutar el programa.
- `gestion_usuarios.py` → Funciones para registrar usuarios, inicio de sesión y cambio de contraseña.
- `gestion_visitas.py` → Funciones para registrar visitas, filtrar visitas y borrar historial.
- `usuarios.json` → Archivo que guarda usuarios y sus contraseñas.
- `historial.csv` → Archivo que guarda el historial de visitas.

## Cómo ejecutar

```bash
python main.py