from flask import Flask 

app = Flask(__name__)


@app.route("/")
def home():
  return "Seja Bem-Vindo ao meu site"

@app.route("/sobre")
def sobre():
  return "Essa página é SOBRE MIM"

@app.route("/contato")
def pagina_contato():
  return "PÁGINA PARA OS MEUS CONTATOS"

@app.route("/soma")
def somar():
  return str(2+2)

if __name__ == "__main__":
  app.run(debug=True)
  

  