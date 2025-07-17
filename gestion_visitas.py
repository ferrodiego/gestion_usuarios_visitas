import csv
from pathlib import Path
from datetime import datetime

archivo_csv = Path('historial.csv')
        
        
def registrar_visita(nombre):
    """ Registra el historial de visitas en un archivo csv"""
    
    fecha_hora = datetime.now().strftime('%d/%m/%y %H:%M:%S')
    campos = ['usuario', 'fecha_hora']
    
    archivo_nuevo = not archivo_csv.exists()
    
    if not archivo_csv.exists():
        with open(archivo_csv, 'a', newline='', encoding='utf-8') as f:            
            writer = csv.DictWriter(f, fieldnames=campos)
            
            if archivo_nuevo:
                writer.writeheader()
            
            writer.writerow({
                'usuario': nombre,
                'fecha_hora': fecha_hora
            })



def filtrar_visitas_por_usuario(nombre):
    """Filtra visitas por usuario, detallando total de visitas
    y horario
    """
    
    if not archivo_csv.exists():
        print('No existe historial de visitas')
        return
    
    visitas_usuario = []
    with open(archivo_csv, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila.get('usuario') == nombre:
                visitas_usuario.append(fila)
    
    if visitas_usuario:
        print(f"\n Visitas de {nombre} (Total: {len(visitas_usuario)}) ")
        for i, visita in enumerate(visitas_usuario, start=1):
            print(f"{i}. Fecha: {visita.get('fecha_hora')}")
    else:
        print(f"No hay visitas registradas para el usuario {nombre}.")
    


def borrar_historial():
    """Borra el archivo de historial de visitas
    """    
    if archivo_csv.exists():
        archivo_csv.unlink()
        print('✅ Historial borrado correctamente')
    else:
        print('No hay historial para borrar')