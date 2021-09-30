from config import *
from modelo import Pessoa

@app.route("/")
def inicio():
    return 'Sistema de cadastro de pessoas. '+\
        '<a href="/listar_pessoas">Operação listar</a>'

@app.route("/listar_pessoas")
def listar_pessoas():
    # obter as pessoas do cadastro
    pessoas = db.session.query(Pessoa).all()
    # aplicar o método json que a classe Pessoa possui a cada elemento da lista
    pessoas_em_json = [ x.json() for x in pessoas ]
    # converter a lista do python para json
    resposta = jsonify(pessoas_em_json)
    # PERMITIR resposta para pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

# iniciar o servidor web
app.run(debug=True, host='0.0.0.0')    

# curl localhost:5000/listar_pessoas
# 
