from flask import Flask,render_template, jsonify

app = Flask(__name__)

@app.route("/saudacao")
def maiorI():
  nome = "Bruno"
  idade = 25
  return render_template("saudacao.html", nome=nome, idade=idade)

if __name__ == "__main__":
    app.run(debug=True)