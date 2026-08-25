from flask import Flask


app = Flask(__name__)

@app.route("/sobre")
def sobre():
  return "Este é meu site pessoal"

if __name__ == "__main__":
    app.run(debug=True)