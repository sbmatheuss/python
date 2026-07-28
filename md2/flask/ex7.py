from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/soma", methods=["POST"])
def somar():
  dados = request.get_json()
  a_recebida = dados["a"]
  b_recebida = dados["b"]
  return jsonify({"resultado": a_recebida + b_recebida})
  