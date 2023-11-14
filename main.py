import os
from flask import Flask

def main():
    # Accede a la configuración específica que necesitas, por ejemplo, para el modo de depuración
    print("hola mundo cgallego")

    
if __name__ == "__main__":
    app = Flask(__name__)
    @app.route('/')
    def index():
        main()  # Llama a la función main cuando se accede a la ruta raíz ('/')
        return 'Procesamiento completado'  # Respuesta a enviar al navegador

    app.run(host='0.0.0.0', port=8080)