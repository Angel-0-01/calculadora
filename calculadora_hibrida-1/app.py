import tkinter as tk
import webview
import os

def start_webview():
    # Ruta absoluta al archivo HTML
    html_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates', 'index.html'))
    
    # Verificar si el archivo existe antes de cargar
    if not os.path.exists(html_path):
        print(f"Error: Archivo no encontrado en {html_path}")
        return
    
    # Crear ventana Tkinter (opcional, pero pywebview maneja la ventana principal)
    root = tk.Tk()
    root.title("Calculadora Híbrida")
    root.geometry("350x500")
    
    # Crear la vista web
    webview.create_window('Calculadora', f'file://{html_path}', width=320, height=450)  # Agrega 'file://' para rutas locales
    webview.start()
    
    root.destroy()

if __name__ == '__main__':
    start_webview()