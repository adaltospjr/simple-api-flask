casais = {
    "masculino": ["Miguel", "Arthur", "Bernardo", "Heitor", "Davi", "Lorenzo", "Théo", "Pedro", "Gabriel", "Enzo", ],
    "feminino": ["Alice", "Sophia", "Helena", "Sofia", "Laura", "Isabella", "Manuela", "Júlia", "Heloísa", "Luiza", ],
    "qtde_de_filhos": [2, 3, 5, 1, 2, 1, 0, 5, 0, 6]
}
# está sendo declarado o dicionário e atribuindo os valores para a variável casais.

print("index \t| mensagem \t")
# é um print para formatação
print(20 * "--")
# é um print para formatação


for index, casal in enumerate(zip(casais["masculino"], casais["feminino"], casais["qtde_de_filhos"])):
    # index numera as informação e casal apresenta as informações dentro do conjunto masculino, femino e filhos.
    # a função zip retorna as informações do dicionário organizadas em uma lista.
    # por fim a váriavel casais está sendo informada juntamente com as informações de acordo com o informação masculino, feminino e filhos.
    # em outras palavras é uma combinação onde a variável index recebe as informações da função enumerate.
    # e a variável casal recebe o conjunto de informações organizadas da função zip com referencia das informações contidas em masculino e etc...
    mensagem = f"{casal[0]} é casado com {casal[1]} e tem {casal[2]} filhos"
    # a várivel mensagem foi criada para receber esse print formatado
    print(f"{index} \t| {mensagem} \t")
    # com pouco código é feito a função do print a cima e a formatação.
print(20 * "--")
# é um print para formatação
