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