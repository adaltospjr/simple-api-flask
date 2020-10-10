from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/cep/')
def cep():
    args = dict(request.args)
    if cep not in args:
        return ... 
    ...


'''

@app.route("/caminho/<cep>/")
def teste(cep):
    with open(file="cep.txt", mode="r", encoding="utf-8") as file:
        ceps = file.read().split("\n")
        for i in ceps:
            if cep == i:
                return "Cep Existe"
            else:
                return "Cep não existe"

'''

#==============================================


# como retornar html ao invés de uma string ou array.

@app.route("/index/")
def index():
    return render_template("index.html")


@app.route("/for/<nome>/")
def index_for(nome):
    title = f"olá eu sou o {nome}"
    users = [{"username": nome, "url":"https://www.google.com/"}]
    return render_template("for.html", title=title, users=users)


@app.route("/if/<nome>")
def index_if(nome):
    title = "olá eu sou o {nome}"
    users = [{"username": nome, "url": "https://pm1.narvii.com/6432/2f966a1c09a59b2a0ca297a1a45e7e530d06aa14_hq.jpg"}]
    return render_template("if.html", title=title, users=users)

#============================================================

users_list = []

@app.route("/add/user/")
def add_user():
    args = dict(request.args)
    if "username" not in args or "url" not in args:
        return ({"message": "invalid user"}, 400)
    
    users_list.append(args)
    return ({"message": "add user successful"}, 201)

@app.route("/get/users/")
def get_user():
    return render_template("users.html", users=users_list)  

@app.route("/file/", methods=["GET", "POST"])
def files():
    if request.method == "GET":
        return render_template("form.html")
    files = request.files.getlist("file")
    for file in files:
        path = f"app/file/{file.filename}"
        file.save(path)
    return ({"message": "Olá, esse method é um post"}, 201)



# criar banco de dados em memória

banco_de_dados = []

@app.route("/pessoa/", methods=["GET"])
@app.route("/pessoa/<int:id>", methods=["GET"])
def get_pessoa(id: int = None):
    ''' Consultar um id e retornar um dict caso exista, caso não ele retorna vazio'''
    if not id:
        return ({"pessoas": banco_de_dados})

    for pessoa in banco_de_dados:
        if id in pessoa:
            return (pessoa, 200)
    return ({"message": "id não encontrado"}, 400)

@app.route("/pessoa/", methods=["POST"])
def add_pessoa():
    ''' criar um registro caso o body não seja vazio'''
    dados= request.json
    condition = ("nome" in dados, "idade" in dados, "altura" in dados, "cor_de_pele" in dados)
    if not all(condition):
        return ({"message": "dados invalido"}, 400)
    
    aux = 0
    for i in banco_de_dados:
        pivot = list(i.keys())[0]
        if aux < pivot:
            aux = pivot
    
    id = aux + 1
    banco_de_dados.append({aux+1: dados})
    return ({"message": f"Usuário {dados['nome']} inserido com sucesso."}, 200)
        
@app.route("/pessoa/<int:id>/", methods=["DELETE"])
def delete_pessoa(id: int):
    aux = None
    for index, value in enumerate(banco_de_dados):
        if id in value:
            aux = index

    if aux is not None:
        result = banco_de_dados.pop(aux)
        return ({"message": "usuário removido com sucesso", "user": result}, 200)
    return ({"message":"usuário não encontrado"}, 404)

@app.route("/pessoa/<int:id>/", methods=["PUT"])
def update_pessoa(id: int):
    json = request.json
    dados = ("nome" in dados, "idade" in dados, "altura" in dados, "cor_de_pele" in dados)
    if not all(condition):
        return ({"message": "dados invalido"}, 400)
    
    for index, value in enumerate(banco_de_dados):
        if id in value:
            banco_de_dados[index].update({id: dados})
            return ({"message": "dados atualizados"}, 200)
    
    return ({"message": "dados invalido"}, 400)     