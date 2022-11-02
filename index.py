# -*- coding: utf-8 -*-
"""Importe la líbreria"""
from flask import Flask, render_template
"""Inicialización de la página"""
pagina = Flask(__name__)
"""Flask requiere de un direccionamiento por función.
Es decir cuando va a mostrar algo en la pagina se dirige
a la ruta asignada"""

"""En este caso / indica la raíz del servidor"""
"""Función particular para mostrar algo en la página"""
@pagina.route('/')
def Funcion():
    return render_template("index.html")

"""Ejecución del servidor de flask"""
if __name__ == '__main__':
    pagina.run(host="0.0.0.0", port=6000, debug=True)