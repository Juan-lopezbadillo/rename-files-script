#!/usr/bin/env python3
import os
print(f"Directorio de trabajo actual: {os.getcwd()}")

# Directorio donde se encuentran los archivos (ruta relativa)
folder_path = 'Files/'

# Obtener la lista de archivos en la carpeta
try:
    files = os.listdir(folder_path)
except FileNotFoundError:
    print(f"Error: the folder '{folder_path}' not found")
    exit()

new = input("Update with?: ")
# Iterar sobre los archivos y renombrarlos
for filename in files:
    # Define the new name
    new_name = f"{new}_{filename}"
    
    # Ruta completa de los archivos actuales y nuevos
    src = os.path.join(folder_path, filename)
    dst = os.path.join(folder_path, new_name)
    
    # Renombrar los archivos
    try:
        os.rename(src, dst)
    except FileNotFoundError:
        print(f"Error: File '{src} not found'")
    except OSError as e:
        print(f"Error renaming {src} to {dst}: {e}")
print("Renaming files completed!")
