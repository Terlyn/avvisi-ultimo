from flask import Flask, jsonify, redirect, request, url_for, render_template, flash, session
from scripts import baseDatos
import os
import json
app = Flask(__name__)


@app.route("/")
@app.route("/base")
def base():
    categorias = baseDatos.obtener_categorias()
    #if categorias is not None:
        #jsonify(categorias)  # Devuelve las categorías en formato JSON
    return render_template("base.html")  # Esto buscará "base.html" en "templates/"


def ruta_productos_por_categoria():
    # Obtener la categoría desde los parámetros de consulta de la URL
    categoria = request.args.get("categoria")
    productos = baseDatos.obtener_productos_por_categoria(categoria)
    if productos is not None:
        return jsonify(productos)  # Devuelve los productos en formato JSON
    else:
        return jsonify({"mensaje": "Error al obtener los productos"}), 500

def ruta_clientes():
    clientes = obtener_clientes()
    if clientes is not None:
        return jsonify(clientes)  # Devuelve los clientes en formato JSON
    else:
        return jsonify({"mensaje": "Error al obtener los clientes"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Cambia el puerto si el 5000 está en uso
