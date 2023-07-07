from tkinter import*
from Ventana import*

def main():
    root = Tk()
    root.wm_title("Tabla de Datos")
    app = Ventana (root)
    app.mainloop() 

if __name__ == "__main__":
    main() 