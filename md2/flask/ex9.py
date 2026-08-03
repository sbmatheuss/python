<<<<<<< HEAD
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/cadastro", methods=["POST"])
def cadastro():
  dados = request.get_json()
  usuario = dados["nome"]
  idade = dados["idade"]
  return jsonify({"mensagem":   f"{usuario} tem {idade} anos"})

=======
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/perfil")
def perfil():
    nome = "Matheus"
    idade = "23"
    return render_template("perfil.html", nome=nome, idade=idade)

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 5c4569dc00787a3e69f75a6fe9773cfef8451236
