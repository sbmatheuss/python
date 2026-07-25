from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/saudacao", methods=["POST"])
def name():
    dados = request.get_json()
    nome_recebido = dados["___"]
    return jsonify({"mensagem: " f"Olá, {nome_recebido}!"})

