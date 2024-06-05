# Criação da matriz
matriz_vagas = []

vagas_coluna = ['Dev. Java', 'Analista de dados', 'Ux Designer', 'Dev. FrontEnd', 'Designer Gráfico']
skills_linha = ['Java', 'Python', 'SQL', 'Git', 'Spring', 'Figma', 'Comunicação', 'Power BI']

# Cadastrar dados na matriz
for i in range(5):
    vagas = []
    for j in range(8):
        while True:
            resposta = input(f"A vaga '{vagas_coluna[i]}' utiliza a skill '{skills_linha[j]}'? (S/N): ")
            if resposta.upper() == "S":
                vagas.append(True)
                break
            elif resposta.upper() == "N":
                vagas.append(False)
                break
            else:
                print("RESPOSTA INVALIDA, Digite S ou N")
    matriz_vagas.append(vagas)

# Mostrar a matriz (teste)
for vagas in matriz_vagas:
    for elemento in vagas:
        print(elemento, end=' ')
    print()