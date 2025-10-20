from flask import Flask, render_template
import webbrowser
import threading
import time

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def open_browser():
    time.sleep(1)  # Espera 1 segundo para que el servidor inicie
    webbrowser.open('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # Inicia el navegador en un hilo separado
    threading.Thread(target=open_browser).start()
    app.run(debug=False)  # Cambia a debug=False para producción