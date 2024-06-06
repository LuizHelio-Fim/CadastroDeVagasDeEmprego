import os

# Criação da matriz
matriz_vagas = []

skills_linha = ['Java', 'Python', 'SQL', 'Figma', 'Comunicação', 'Power BI']
vagas_coluna = ['Dev. Java', 'Analista de dados', 'Ux Designer', 'Dev. FrontEnd', 'Designer Gráfico']

while True:
    print(" ")
    print("------------------------------")
    print("        MENU PRINCIPAL        ")
    print("------------------------------")
    print("1 - Cadastrar Dados na Planilha")
    print("2 - Cadastrar Uma nova Skill")
    print("3 - Cadastrar Uma nova Vaga")
    print("4 - Remover Skill")
    print("5 - Remover Vaga")
    print("6 - Alterar Dados na Planilha")
    print("7 - Ver Planilha")
    print("0 - Sair")
    print(" \nDigite 'LIMPAR' para limpar o console")
    resposta = (input("> ")).upper()
    print(" ")

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
            print()
        
        case "5":
            print()

        case "6":
        #Verificar se existem dados na matriz
            if len(matriz_vagas) == 0:
                print("NENHUM DADO ENCONTRADO NA PLANILHA")
                continue
        # Alterar dados na matriz
            for skills in range(len(skills_linha)):
                print(f"{skills+1} - {skills_linha[skills]}")
            skill_alterar = int(input("Qual skill deseja alterar?\n> "))

            for vagas in range(len(vagas_coluna)):
                print(f"{vagas+1} - {vagas_coluna[vagas]}")
            vaga_alterar = int(input("Qual vaga deseja alterar?\n> "))

            # Verificar se a skill e a vaga existem na matriz
            skill_index = -1
            vaga_index = -1

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
                elif resposta.upper() == "N":
                    matriz_vagas[skill_index][vaga_index] = False
                else:
                    print("RESPOSTA INVALIDA, Digite S ou N")
                
                outra = input("Deseja alterar outra skill/vaga? (S/N)\n> ").upper()
                if outra == "S":
                    continue
                else:
                    break

        case "7":
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
            os.system('cls')
            if resposta == "0":
                print("Programa feito como TRABALHO FINAL da Disciplina de LP1")
                print("\nINTEGRANTES: Erick Lauretti\n             João Guilherme\n             Luiz Hélio\n")
                print("Obrigado por usar!\nGITHUB Repository: https://github.com/LuizHelio-Fim/CadastroDeVagasDeEmprego_TrabalhoFinal")
                exit()
        
        case "LIMPAR":
            os.system('cls')
            continue

        case _:
            print("ERRO: OPÇÃO SELECIONADA INVALIDA")
            continue