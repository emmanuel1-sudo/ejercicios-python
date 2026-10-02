from flask import Flask, render_template, request, session
import mysql.connector

from clases.par_impar import ParImpar
from clases.tabla_multiplicar import TablaMultiplicar
from clases.adivina_numero import AdivinaNumero


app = Flask(__name__)

app.secret_key = "clave_ejercicios_python"


def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ejercicios_python"
    )



@app.route("/")
def inicio():
    return render_template("index.html")




@app.route("/par-impar", methods=["GET", "POST"])
def par_impar():

    resultado = None
    error = None

    if request.method == "POST":

        dato = request.form.get("numero", "").strip()

        try:
            numero = int(dato)

            ejercicio = ParImpar(numero)

            resultado = ejercicio.comprobar()

        except ValueError:

            error = "Por favor, ingresa un número entero válido."

    return render_template(
        "par_impar.html",
        resultado=resultado,
        error=error
    )




@app.route("/tabla", methods=["GET", "POST"])
def tabla():

    resultados = None
    numero_tabla = None
    error = None

    if request.method == "POST":

        dato = request.form.get("numero", "").strip()

        try:

            numero = int(dato)

            ejercicio = TablaMultiplicar(numero)

            resultados = ejercicio.generar()

            numero_tabla = numero

            conexion = conectar_bd()
            cursor = conexion.cursor()

            for fila in resultados:

                sql = """
                INSERT INTO tablas_multiplicar
                (numero, multiplicador, resultado)
                VALUES (%s, %s, %s)
                """

                cursor.execute(
                    sql,
                    (
                        numero,
                        fila["multiplicador"],
                        fila["resultado"]
                    )
                )

            conexion.commit()

            cursor.close()
            conexion.close()

        except ValueError:

            error = "Por favor, ingresa un número entero válido."

    return render_template(
        "tabla.html",
        tabla=resultados,
        numero_tabla=numero_tabla,
        error=error
    )




@app.route("/adivinar", methods=["GET", "POST"])
def adivinar():

    mensaje = None
    error = None

    if "secreto" not in session:

        juego = AdivinaNumero()

        session["secreto"] = juego.secreto

    if request.method == "POST":

        dato = request.form.get("intento", "").strip()

        try:

            intento = int(dato)

            juego = AdivinaNumero()

            juego.secreto = session["secreto"]

            mensaje = juego.comprobar(intento)

            if intento == juego.secreto:

                session.pop("secreto", None)

        except ValueError:

            error = "Por favor, ingresa un número entero válido."

    return render_template(
        "adivinar.html",
        mensaje=mensaje,
        error=error
    )




@app.route("/reiniciar")
def reiniciar():

    session.pop("secreto", None)

    return render_template(
        "adivinar.html",
        mensaje="Se ha iniciado un nuevo juego.",
        error=None
    )




if __name__ == "__main__":
    app.run(debug=True)