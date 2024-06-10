import os

# Criação da matriz
matriz_vagas = []

skills_linha = ['JAVA', 'PYTHON', 'JAVASCRIPT', 'POWER BI', 'FIGMA']
vagas_coluna = ['DEV. JAVA', 'ANALISTA DE DADOS', 'DEV. FRONTEND', 'UX DESIGNER']

while True:
    print(" ")
    print("--------------------------------")
    print("         MENU PRINCIPAL         ")
    print("--------------------------------")
    print("1 - Cadastrar Dados na Planilha")
    print("2 - Cadastrar Skill")
    print("3 - Cadastrar Vaga")
    print("4 - Remover Skill")
    print("5 - Remover Vaga")
    print("6 - Alterar Dados na Planilha")
    print("7 - Ver Planilha")
    print("0 - Sair")
    print("--------------------------------")
    print("Digite 'LIMPAR' para limpar o console")
    print("--------------------------------")
    resposta = (input("> ")).upper()
    print(" ")

    match resposta:
        case "1": 
        # Cadastrar dados na matriz
            while True:
                if len(matriz_vagas) != 0:
                    print("Planilha já com dados cadastrados, Deseja recadastrar novos dados? (S/N)")
                    conferir = input("> ").upper()
                    if conferir == "S":
                        matriz_vagas = []
                        break
                    elif conferir == "N":
                        break
                    else:
                        print("ERRO: RESPOSTA INVALIDA, Digite S ou N")
                        continue
                else:
                    break
            
            if len(matriz_vagas) == 0:
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
                                print("ERRO: RESPOSTA INVALIDA, Digite S ou N")
                    matriz_vagas.append(skills)  

        case "2":
        # Cadastrar uma nova skill
            while True:
                nova_Skill = input("Qual skill deseja adicionar?\n> ").upper()
                conferir = input(f"{nova_Skill} está correto? (S/N)\n>")
                if conferir.upper() == "S":
                    skills_linha.append(nova_Skill)

                    outra = input("Deseja Adicionar outra skill? (S/N)\n> ").upper()

                    if outra == "S":
                        continue
                    elif outra == "N":
                        print("Cadastrado com Sucesso")
                        break
                    else:
                        print("ERRO: RESPOSTA INVALIDA\n")

                elif conferir.upper() == "N":
                    print("OPERAÇÃO CANCELADA.")
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA")
                    continue

        case "3":
        # Cadastrar uma nova vaga
            while True:
                nova_vaga = input("Qual vaga deseja adicionar?\n> ").upper()
                conferir = input(f"{nova_vaga} está correto? (S/N)\n>")
                if conferir.upper() == "S":
                    vagas_coluna.append(nova_vaga)

                    outra = input("Deseja Adicionar outra vaga? (S/N)\n> ").upper()
                    if outra == "S":
                        continue
                    elif outra == "N":
                        print("Cadastrado com Sucesso")
                        break
                    else:
                        print("ERRO: RESPOSTA INVALIDA\n")

                elif conferir.upper() == "N":
                    print("OPERAÇÃO CANCELADA.")
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA")
                    continue

        case "4":
        # Remover SKILLS
            if len(matriz_vagas) != 0:
                print("ERRO: A planilha está completa")
                resetar = input("Deseja resetar a planilha para remover skill? (S/N)\n> ")
                if resetar.upper() == "S":
                    matriz_vagas = []
                elif resetar.upper() == "N":
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA")
                    continue

            for skills in range(len(skills_linha)):  # Imprime todas as skills
                print(f"{skills_linha[skills]}")
            
            remove = input("\nQual skill deseja remover?\n> ").upper()
            if remove in skills_linha:  # Confere se a skill digitada existe no vetor skills_linha
                conferir = input(f"Deseja mesmo remover {remove}? (S/N)\n> ")
                if conferir.upper() == "S":
                    skills_linha.remove(remove)
                elif conferir.upper() == "N":
                    print("OPERAÇÃO CANCELADA.")
                else:
                    print("ERRO: RESPOSTA INVALIDA, Digite S ou N."),
            else:
                print("ERRO: Skill não encontrada.")

        case "5":
        # Remover VAGAS
            if len(matriz_vagas) != 0:
                print("ERRO: A planilha está completa")
                resetar = input("Deseja resetar a planilha para remover vaga? (S/N)\n> ")
                if resetar.upper() == "S":
                    matriz_vagas = []
                elif resetar.upper() == "N":
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA")
                    continue

            for vagas in range(len(vagas_coluna)):  # Imprime todas as vagas
                print(f"{vagas_coluna[vagas]}")
            
            remove = input("\nQual skill deseja remover?\n> ").upper()
            if remove in vagas_coluna:  # Confere se a vaga digitada existe no vetor vagas_coluna
                conferir = input(f"Deseja mesmo remover {remove}? (S/N)\n> ")
                if conferir.upper() == "S":
                    vagas_coluna.remove(remove)
                elif conferir.upper() == "N":
                    print("OPERAÇÃO CANCELADA.")
                else:
                    print("ERRO: RESPOSTA INVALIDA, Digite S ou N.")
            else:
                print("ERRO: Skill não encontrada.")

        case "6":
        #Verificar se existem dados na matriz
            if len(matriz_vagas) == 0:
                print("NENHUM DADO ENCONTRADO NA PLANILHA.\n")
                continue

        # Alterar dados na matriz
            for vagas in range(len(vagas_coluna)):  # Imprime todas as vagas
                print(f"{vagas_coluna[vagas]}")

            while True:
                vaga_alterar = input("\nQual vaga deseja alterar?\n> ").upper()
                conferir = input(f"{vaga_alterar} está correto? (S/N)\n> ")
                if conferir.upper() == "S":
                    if vaga_alterar in vagas_coluna:  # Confere se a vaga digitada existe no vetor vagas_coluna
                            indice_coluna = vagas_coluna.index(vaga_alterar)  # Busca o indice da coluna digitada
                            break
                    else:
                        print("ERRO: Vaga não encontrada")
                elif conferir.upper() == "N":
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA, Digite S ou N.")

            print(" ")
            
            for skills in range(len(skills_linha)):  # Imprime todas as vagas
                print(f"{skills_linha[skills]}")

            while True:
                skill_alterar = input("\nQual skill deseja alterar?\n> ").upper()
                conferir = input(f"{skill_alterar} está correto? (S/N)\n> ")
                if conferir.upper() == "S":
                    if skill_alterar in skills_linha:  # Confere se a skill digitada existe no vetor skills_linha
                            indice_linha = skills_linha.index(skill_alterar)  # Busca o indice da linha digitada
                            break
                    else:
                        print("ERRO: Vaga não encontrada")
                elif conferir.upper() == "N":
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA, Digite S ou N.")

            while True:
                alterar = input(f"A vaga '{vagas_coluna[indice_coluna]}' utiliza a skill '{skills_linha[indice_linha]}'? (S/N)\n> ")
                if alterar.upper() == "S":
                    matriz_vagas[indice_linha][indice_coluna] = True
                    break
                elif alterar.upper() == "N":
                    matriz_vagas[indice_linha][indice_coluna] = False
                    break
                else:
                    print("ERRO: RESPOSTA INVALIDA, Digite S ou N.")

        case "7":
        # Printar a matriz
            print("                    ", end=' ')
            for vaga in vagas_coluna:
                print("{:<20}".format(vaga), end=' ')
            print()

            if len(matriz_vagas) > 0:
                for i in range(len(skills_linha)):
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
                print("Obrigado por usar Cadastro de Vagas de Emprego!\nGITHUB Repository: https://github.com/LuizHelio-Fim/CadastroDeVagasDeEmprego_TrabalhoFinal \n\n")
                exit()

        case "LIMPAR":
            os.system('cls')
            continue

        case _:
            print("ERRO: OPÇÃO SELECIONADA INVALIDA.")
            continue