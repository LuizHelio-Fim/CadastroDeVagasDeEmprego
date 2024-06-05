# Criação da matriz
matriz_vagas = []

vagas_linha = ['Dev. Java', 'Analista de dados', 'Ux Designer', 'Dev. FrontEnd', 'Designer Gráfico']
skills_coluna = ['Java', 'Python', 'SQL', 'Git', 'Spring', 'Figma', 'Comunicação', 'Power BI']

# Cadastrar dados na matriz
for i in range(5):
    vagas = []
    for j in range(8):
        while True:
            resposta = input(f"A vaga '{vagas_linha[i]}' utiliza a skill '{skills_coluna[j]}'? (S/N): ")
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
print(" ", end=' ')
for skill in skills_coluna:
    print("{:<20}".format(skill), start='                  ', end=' ')
print()

for i in range(len(matriz_vagas)):
    print("{:<20}".format(vagas_linha[i]), end=' ')
    for elemento in matriz_vagas[i]:
        print("{:<20}".format(str(elemento)), end=' ')
    print()