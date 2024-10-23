import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error al ejecutar comando", str(e))
        return False

def install_fabric():
    fabric_version = "fabric:1.21.1"
    if run_command(["portablemc", "start", fabric_version]):
        messagebox.showinfo("Instalación completada", "Fabric ha sido instalado correctamente.")
    else:
        messagebox.showerror("Error de instalación", "No se pudo instalar Fabric.")

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Minecraft Launcher")
        master.geometry('1000x600')

        # Load the background image
        self.background_image = Image.open("C:\\xampp\\htdocs\\laucher\\source\\fondo.png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(master, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label = tk.Label(master, text="Ingresa tu nickname para jugar:", bg="#123456")  # Ajusta este color según tu imagen
        self.label.pack(pady=10)

        self.nickname_entry = ttk.Entry(master, width=20)
        self.nickname_entry.pack(pady=10)
        self.nickname_entry.focus()

        self.next_button = tk.Button(master, text="Establecer Nickname",
                                     command=self.setup_user)
        self.next_button.pack(pady=10)

        # Botones ocultos inicialmente
        self.install_button = tk.Button(master, text="Instalar Fabric 1.21.1",
                                        command=install_fabric, state=tk.DISABLED)
        self.launch_button = tk.Button(master, text="Iniciar Minecraft",
                                       command=self.launch_minecraft, state=tk.DISABLED)

    def setup_user(self):
        nickname = self.nickname_entry.get()
        if nickname:
            self.nickname = nickname
            self.label.config(text=f"Bienvenido {nickname}, ¡listo para jugar!", bg="#123456")  # Ajusta este color también
            self.install_button.pack(pady=10)
            self.launch_button.pack(pady=10)
            self.nickname_entry.pack_forget()
            self.next_button.pack_forget()
            self.install_button.config(state=tk.NORMAL)
            self.launch_button.config(state=tk.NORMAL)
        else:
            messagebox.showwarning("Nickname requerido", "Por favor, ingresa un nickname antes de continuar.")

    def launch_minecraft(self):
        fabric_version = "fabric:1.21.1"
        command = ["portablemc", "start", fabric_version, "--username", self.nickname]
        if run_command(command):
            messagebox.showinfo("Minecraft iniciado", f"Minecraft iniciado con el usuario {self.nickname}.")
        else:
            messagebox.showerror("Error al iniciar", "No se pudo iniciar Minecraft con el usuario especificado.")

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
