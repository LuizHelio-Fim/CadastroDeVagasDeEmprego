import os

# Criação da matriz
matriz_vagas = []

skills_linha = ['Java', 'Python', 'SQL', 'Figma', 'Comunicação', 'Power BI']
vagas_coluna = ['Dev. Java', 'Analista de dados', 'Ux Designer', 'Dev. FrontEnd', 'Designer Gráfico']

while True:
    print("------------------------------")
    print("        MENU PRINCIPAL        ")
    print("------------------------------")
    print("1 - Cadastrar Dados na Planilha")
    print("2 - Cadastrar Uma nova Skill")
    print("3 - Cadastrar Uma nova Vaga")
    print("4 - Alterar Dados na Planilha")
    print("5 - Ver Planilha")
    print("0 - Sair")
    resposta = (input("> "))

    match resposta:
        case "1": 
        # Cadastrar dados na matriz
            for i in range(len(skills_linha)):
                skills = []
                for j in range(len(vagas_coluna)):
                    while True:
                        resposta = input(f"A vaga '{vagas_coluna[j]}' utiliza a skill '{skills_linha[i]}'? (S/N): ")
                        if resposta.upper() == "S":
                            skills.append(True)
                            break
                        elif resposta.upper() == "N":
                            skills.append(False)
                            break
                        else:
                            print("RESPOSTA INVALIDA, Digite S ou N")
                matriz_vagas.append(skills)

        case "2":
        # Cadastrar uma nova skill
            while True:
                nova_Skill = input("Qual skill deseja adicionar?\n> ")
                conferir = input(f"{nova_Skill} está correto? (S/N)\n>")
                if conferir.upper() == "S":
                    skills_linha.append(nova_Skill)

                    if input("Deseja Adicionar outra skill? (S/N)\n> ").upper() == "S":
                        continue
                    else:
                        break
                elif conferir.upper() == "N":
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA")
                    continue
            
        case "3":
        # Cadastrar uma nova vaga
            while True:
                nova_vaga = input("Qual vaga deseja adicionar?\n> ")
                conferir = input(f"{nova_vaga} está correto? (S/N)\n>")
                if conferir.upper() == "S":
                    vagas_coluna.append(nova_vaga)

                    if input("Deseja Adicionar outra vaga? (S/N)\n> ").upper() == "S":
                        continue
                    else:
                        break

        case "4":
        # Alterar dados na matriz
            for skills in range(len(skills_linha)):
                print(f"{skills+1} - {skills_linha[skills]}")
            skill_alterar = int(input("Qual skill deseja alterar?\n> "))

            for vagas in range(len(vagas_coluna)):
                print(f"{vagas+1} - {vagas_coluna[vagas]}")
            vaga_alterar = int(input("Qual vaga deseja alterar?\n> "))

            # Verificar se a skill e a vaga existem na matriz
            if 1 <= skill_alterar <= len(skills_linha) and 1 <= vaga_alterar <= len(vagas_coluna):
                skill_index = skill_alterar - 1
                vaga_index = vaga_alterar - 1
            else:
                print("Skill ou vaga inválida.")

            if skill_index == -1 or vaga_index == -1:
                print("ERRO: Skill ou vaga não encontrada na matriz")
                continue

            while True:
                resposta = (input(f"A skill '{skill_alterar}' é utilizada na vaga '{vaga_alterar}'? (S/N): "))
                if resposta.upper() == "S":
                    matriz_vagas[skill_index][vaga_index] = True
                    break
                elif resposta.upper() == "N":
                    matriz_vagas[skill_index][vaga_index] = False
                    break
                else:
                    print("RESPOSTA INVALIDA, Digite S ou N")

            if input("Deseja alterar outra skill/vaga? (S/N)\n> ").upper() == "S":
                continue
            else:
                break

        case "5":
        # Printar a matriz
            print("                    ", end=' ')
            for vaga in vagas_coluna:
                print("{:<20}".format(vaga), end=' ')
            print()

            if len(matriz_vagas) > 0:
                for i in range(len(matriz_vagas)):
                    print("{:<20}".format(skills_linha[i]), end=' ')
                    for elemento in matriz_vagas[i]:
                        print("{:<20}".format(str(elemento)), end=' ')
                    print()
            else:
                for i in range(len(skills_linha)):
                    print(f"{skills_linha[i]}")

        case "0":
            if resposta == "0":
                exit()

        case _:
            os.system('cls')
            print("ERRO: OPÇÃO SELECIONADA INVALIDA")
            continue