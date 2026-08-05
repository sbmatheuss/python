
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/perfil")
def perfil():
    nome = "Matheus"
    idade = "23"
    return render_template("perfil.html", nome=nome, idade=idade)

if __name__ == "__main__":
    app.run(debug=True)

