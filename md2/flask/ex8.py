from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/usuario", methods=["POST"])
def user():
  dados = request.get_json()
  user = dados["nome"]
  idade = dados["idade"]
  if idade >= 18:
    return jsonify({"mensagem": f"{user} é maior de idade"})
  else:
    return jsonify({"mensagem": f"{user} é menor de idade"})