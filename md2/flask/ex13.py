from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/usuario/<id>", methods=["POST"])
def user(id):
  dados = request.get_json()
  nome_user = dados["nome"]
  idade_user = dados["idade"]
  return jsonify({"id": id, "nome": nome_user, "idade": idade_user})

if __name__ == "__main__":
  app.run(debug=True)
