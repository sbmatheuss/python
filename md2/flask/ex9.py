from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/cadastro", methods=["POST"])
def cadastro():
  dados = request.get_json()
  usuario = dados["nome"]
  idade = dados["idade"]
  return jsonify({"mensagem":   f"{usuario} tem {idade} anos"})

