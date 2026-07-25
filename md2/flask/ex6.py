from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/saudacao", methods=["POST"])
def name():
    saudacao = request.get_json()
    nome_recebido = saudacao["nome"]
    return jsonify({"mensagem": f"Olá, {nome_recebido}!"})

