from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/produto", methods=["POST"])
def product():
  dados = request.get_json()
  nome_recebido = dados["nome"]
  preco_recebido = dados["preco"]
  return jsonify({"mensagem": f"O {nome_recebido} custa R$ {preco_recebido}"})

