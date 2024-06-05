import os

# Criação da matriz
matriz_vagas = []

vagas_linha = ['Dev. Java', 'Analista de dados', 'Ux Designer', 'Dev. FrontEnd', 'Designer Gráfico']
skills_coluna = ['Java', 'Python', 'SQL', 'Figma', 'Comunicação', 'Power BI']

while True:
    print("------------------------------")
    print("        MENU PRINCIPAL        ")
    print("------------------------------")
    print("1 - Cadastrar Dados na Planilha")
    print("2 - Cadastrar Uma nova vaga")
    print("3 - Cadastrar Uma nova Skill")
    print("4 - Alterar Dados na Planilha")
    print("5 - Ver Planilha")
    print("0 - Sair")
    resposta = (input("> "))

    match resposta:
        case "1": 
        # Cadastrar dados na matriz
            for i in range(len(vagas_linha)):
                vagas = []
                for j in range(len(skills_coluna)):
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

        case "2":
        # Cadastrar uma nova vaga
            while True:
                nova_Vaga = input("Qual vaga deseja adicionar?\n> ")
                conferir = input(f"{nova_Vaga} está correto? (S/N)\n>")
                if conferir.upper() == "S":
                    vagas_linha.append(nova_Vaga)

                    if input("Deseja Adicionar outra vaga? (S/N)\n> ").upper() == "S":
                        continue
                    else:
                        break
                elif conferir.upper() == "N":
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA")
                    continue
            
        case "3":
        # Cadastrar uma nova Skill
            while True:
                nova_Skill = input("Qual skill deseja adicionar?\n> ")
                conferir = input(f"{nova_Skill} está correto? (S/N)\n>")
                if conferir.upper() == "S":
                    skills_coluna.append(nova_Skill)

                    if input("Deseja Adicionar outra skill? (S/N)\n> ").upper() == "S":
                        continue
                    else:
                        break
                elif conferir.upper() == "N":
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA")
                    continue
        case "4":
        # Alterar dados na matriz
            while True:
                for vagas in range(len(vagas_linha)):
                    print(f"{vagas+1} - {vagas_linha[vagas]}")
                vaga_alterar = int(input("Qual vaga deseja alterar?\n> "))
                
                for skills in range(len(skills_coluna)):
                    print(f"{skills+1} - {skills_coluna[skills]}")
                skill_alterar = int(input("Qual skill deseja alterar?\n> "))
                
                # Verificar se a vaga e a skill existem na matriz
                if 1 <= vaga_alterar <= len(vagas_linha) and 1 <= skill_alterar <= len(skills_coluna):
                    vaga_index = vaga_alterar - 1
                    skill_index = skill_alterar - 1
                else:
                    print("Vaga ou skill inválida.")

                if vaga_index == -1 or skill_index == -1:
                    print("ERRO: Vaga ou skill não encontrada na matriz")
                    continue

                while True:
                    resposta = (input(f"A vaga '{vaga_alterar}' utiliza a skill '{skill_alterar}'? (S/N): "))
                    if resposta.upper() == "S":
                        matriz_vagas[vaga_index][skill_index] = True
                        break
                    elif resposta.upper() == "N":
                        matriz_vagas[vaga_index][skill_index] = False
                        break
                    else:
                        print("RESPOSTA INVALIDA, Digite S ou N")

                if input("Deseja alterar outra vaga/skill? (S/N)\n> ").upper() == "S":
                    continue
                else:
                    break

        case "5":
        # Printar a matriz
            print("                    ", end=' ')
            for skill in skills_coluna:
                print("{:<20}".format(skill), end=' ')
            print()

            for i in range(len(matriz_vagas)):
                print("{:<20}".format(vagas_linha[i]), end=' ')
                for elemento in matriz_vagas[i]:
                    print("{:<20}".format(str(elemento)), end=' ')
                print()

        case "0":
            if resposta == "0":
                exit()

        case _:
            os.system('cls')
            print("ERRO: OPÇÃO SELECIONADA INVALIDA")
            continue