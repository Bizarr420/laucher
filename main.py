import os
import sys
import ctypes
import subprocess

def es_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception as e:
        print(f"Error al verificar los permisos de administrador: {e}")
        return False

def run_batch_script():
    script_path = r"C:\xampp\htdocs\laucher\crear_directorios.bat"
    result = subprocess.run(script_path, shell=True, text=True, capture_output=True)
    if result.stdout:
        print("Salida:", result.stdout)
    if result.stderr:
        print("Errores:", result.stderr)

def main():
    if not es_admin():
        if sys.platform == 'win32':
            print("El script no tiene permisos de administrador. Intentando elevar permisos...")
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        else:
            print("No se pueden elevar los permisos. Ejecute el script como administrador.")
        return
    run_batch_script()
    input("Presiona Enter para cerrar...")

if __name__ == '__main__':
    main()
