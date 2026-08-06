from flask import Flask, render_template

app = Flask(__name__)

@app.route("/precos")
def precos():
  produtos = [
    {"nome": "Caderno", "preco": 12.50},
    {"nome": "Caneta", "preco": 3.0},
    {"nome": "Mochila", "preco": 89.90}
  ]
  return render_template("precos.html", produtos=produtos)

if __name__ == "__main__":
  app.run(debug=True)
