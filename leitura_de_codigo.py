casais = {
    "masculino": ["Miguel", "Arthur", "Bernardo", "Heitor", "Davi", "Lorenzo", "Théo", "Pedro", "Gabriel", "Enzo",],
    "feminino": ["Alice", "Sophia", "Helena", "Sofia", "Laura", "Isabella", "Manuela", "Júlia", "Heloísa", "Luiza",],
    "qtde_de_filhos": [2, 3, 5, 1, 2, 1, 0, 5, 0, 6]
}
#dicionário

print("index \t| mensagem \t")
print(20 * "--")


for index, casal in enumerate(zip(casais["masculino"], casais["feminino"], casais["qtde_de_filhos"])):
    mensagem = f"{casal[0]} é casado com {casal[1]} e tem {casal[2]} filhos"
    print(f"{index} \t| {mensagem} \t")
print(20 * "--")
