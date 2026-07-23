from flask import Flask

app = Flask(__name__)

@app.route("/usuario/<nome>")
def user(nome):
  return f"Perfil de {nome}"

@app.route("/dobro/<numero>")
def dobro(numero):
  numero = int(numero)
  return str(numero*2)

@app.route("/soma/<a>/<b>")
def soma(a, b):
  a = int(a)
  b = int(b)
  return str(a+b)

