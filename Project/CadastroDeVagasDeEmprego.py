import os

# Criação da matriz
matriz_vagas = []

skills_linha = ['JAVA', 'PYTHON', 'JAVASCRIPT', 'POWER BI', 'FIGMA']
vagas_coluna = ['DEV. JAVA', 'ANALISTA DE DADOS', 'DEV. FRONTEND', 'UX DESIGNER']

while True:
    print(" ")
    print("  CADASTRO DE VAGAS DE EMPREGO  ")
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
    print("8 - Pesquisas")
    print("0 - Sair")
    print("--------------------------------")
    print("Digite 'LIMPAR' para limpar o console")
    print("--------------------------------")
    resposta = input("> ").upper().strip()
    print(" ")

    match resposta:
        case "1": 
        # Cadastrar dados na matriz
            while True:
                if len(matriz_vagas) != 0:
                    print("Planilha já com dados cadastrados, Deseja recadastrar novos dados? (S/N)")
                    conferir = input("> ").upper().strip()
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
                            resposta = input(f"A vaga '{vagas_coluna[j]}' utiliza a skill '{skills_linha[i]}'? (S/N): ").strip()
                            if resposta.upper() == "S":
                                skills.append(True)
                                break
                            elif resposta.upper() == "N":
                                skills.append(False)
                                break
                            else:
                                print("ERRO: RESPOSTA INVALIDA, Digite S ou N")
                    matriz_vagas.append(skills)
                print(f"\nDADOS CADASTRADOS COM SUCESSO")

        case "2":
        # Cadastrar uma nova skill
            while True:
                if len(matriz_vagas) > 0:
                    print("ERRO: Lista preenchida, deseja resetar a planilha? (S/N)")
                    resetar = input("> ").upper().strip()
                    if resetar == "S":
                        matriz_vagas = []
                        break
                    elif resetar == "N":
                        break
                    else:
                        print("ERRO: RESPOSTA INVALIDA, Digite S ou N")
                        continue

                nova_Skill = input("Qual skill deseja adicionar?\n> ").upper().strip() 
                if nova_Skill in skills_linha:
                    print("ERRO: Skill já cadastrada")
                    continue

                conferir = input(f"{nova_Skill} está correto? (S/N)\n>")
                if conferir.upper() == "S":
                    skills_linha.append(nova_Skill)

                    outra = input("Deseja Adicionar outra skill? (S/N)\n> ").upper().strip()
                    if outra == "S":
                        continue
                    elif outra == "N":
                        print("\nCadastrado com Sucesso") 
                        break
                    else:
                        print("ERRO: RESPOSTA INVALIDA, Digite S ou N")

                elif conferir.upper() == "N":
                    print("OPERAÇÃO CANCELADA.")
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA")
                    continue

        case "3":
        # Cadastrar uma nova vaga
            while True:
                if len(matriz_vagas) > 0:
                    print("ERRO: Lista preenchida, deseja resetar a planilha? (S/N)")
                    resetar = input("> ").upper().strip()
                    if resetar == "S":
                        matriz_vagas = []
                        break
                    elif resetar == "N":
                        break
                    else:
                        print("ERRO: RESPOSTA INVALIDA, Digite S ou N")
                        continue

                nova_vaga = input("Qual vaga deseja adicionar?\n> ").upper().strip()
                if nova_vaga in vagas_coluna:
                    print("ERRO: Vaga já cadastrada")
                    continue
                conferir = input(f"{nova_vaga} está correto? (S/N)\n>")
                if conferir.upper() == "S":
                    vagas_coluna.append(nova_vaga)

                    outra = input("Deseja Adicionar outra vaga? (S/N)\n> ").upper().strip()
                    if outra == "S":
                        continue
                    elif outra == "N":
                        print("Cadastrado com Sucesso")
                        break
                    else:
                        print("ERRO: RESPOSTA INVALIDA, Digite S ou N")

                elif conferir.upper() == "N":
                    print("OPERAÇÃO CANCELADA.")
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA, Digite S ou N")
                    continue

        case "4":
        # Remover SKILLS
            if len(matriz_vagas) != 0:
                print("ERRO: A planilha está completa")
                resetar = input("Deseja resetar a planilha para remover skill? (S/N)\n> ").strip()
                if resetar.upper() == "S":
                    matriz_vagas = []
                elif resetar.upper() == "N":
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA, Digite S ou N")
                    continue

            for skills in range(len(skills_linha)):  # Imprime todas as skills
                print(f"{skills_linha[skills]}")
            
            remove = input("\nQual skill deseja remover?\n> ").upper().strip()
            if remove in skills_linha:  # Confere se a skill digitada existe no vetor skills_linha
                conferir = input(f"Deseja mesmo remover {remove}? (S/N)\n> ").strip()
                if conferir.upper() == "S":
                    skills_linha.remove(remove)
                    print(f"\n {remove} REMOVIDO COM SUCESSO")
                elif conferir.upper() == "N":
                    print("OPERAÇÃO CANCELADA.")
                else:
                    print("ERRO: RESPOSTA INVALIDA, Digite S ou N")
            else:
                print("ERRO: Skill não encontrada.")

        case "5":
        # Remover VAGAS
            if len(matriz_vagas) != 0:
                print("ERRO: A planilha está completa.")
                resetar = input("Deseja resetar a planilha para remover vaga? (S/N)\n> ").strip()
                if resetar.upper() == "S":
                    matriz_vagas = []
                elif resetar.upper() == "N":
                    continue
                else:
                    print("ERRO: RESPOSTA INVALIDA, Digite S ou N")
                    continue

            for vagas in range(len(vagas_coluna)):  # Imprime todas as vagas
                print(f"{vagas_coluna[vagas]}")
            
            remove = input("\nQual vaga deseja remover?\n> ").upper()
            if remove in vagas_coluna:  # Confere se a vaga digitada existe no vetor vagas_coluna
                conferir = input(f"Deseja mesmo remover {remove}? (S/N)\n> ").strip()
                if conferir.upper() == "S":
                    vagas_coluna.remove(remove)
                    print(f"\n {remove} REMOVIDO COM SUCESSO")
                elif conferir.upper() == "N":
                    print("OPERAÇÃO CANCELADA.")
                else:
                    print("ERRO: RESPOSTA INVALIDA, Digite S ou N")
            else:
                print("ERRO: Vaga não encontrada.")

        case "6":
        #Verificar se existem dados na matriz
            if len(matriz_vagas) == 0:
                print("ERRO: NENHUM DADO ENCONTRADO NA PLANILHA.\n")
                continue

        # Alterar dados na matriz
            for vagas in range(len(vagas_coluna)):  # Imprime todas as vagas
                print(f"{vagas_coluna[vagas]}")

            while True:
                vaga_alterar = input("\nQual vaga deseja alterar?\n> ").upper().strip()
                if vaga_alterar in vagas_coluna:  # Confere se a vaga digitada existe no vetor vagas_coluna
                        indice_coluna = vagas_coluna.index(vaga_alterar)  # Busca o indice da coluna digitada
                        break
                else:
                    print("ERRO: Vaga não encontrada.") 
                    continue

            print(" ")
            
            for skills in range(len(skills_linha)):  # Imprime todas as vagas
                print(f"{skills_linha[skills]}")

            while True:
                skill_alterar = input("\nQual skill deseja alterar?\n> ").upper().strip()
                if skill_alterar in skills_linha:  # Confere se a skill digitada existe no vetor skills_linha
                        indice_linha = skills_linha.index(skill_alterar)  # Busca o indice da linha digitada
                        break
                else:
                    print("ERRO: Skill não encontrada.")
                    continue

            while True:
                alterar = input(f"A vaga '{vagas_coluna[indice_coluna]}' utiliza a skill '{skills_linha[indice_linha]}'? (S/N)\n> ")
                if alterar.upper() == "S":
                    matriz_vagas[indice_linha][indice_coluna] = True
                    break
                elif alterar.upper() == "N":
                    matriz_vagas[indice_linha][indice_coluna] = False
                    break
                else:
                    print("ERRO: RESPOSTA INVALIDA, Digite S ou N")

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

        case "8":
            os.system("cls")
            while True:
                print(" ")
                print(f"  CADASTRO DE VAGAS DE EMPREGO  ")
                print("--------------------------------")
                print("            PESQUISAS           ")
                print(f"--------------------------------")
                print(f"1 - Filtrar Skills por Vagas")
                print("2 - Filtrar Vagas por Skills")
                print(f"0 - Voltar")
                print(f"--------------------------------")
                print("Digite 'LIMPAR' para limpar o console")
                print(f"--------------------------------")
                resposta_pesquisa = input("> ").upper().strip()

                match resposta_pesquisa:
                    case "1":
                        if len(matriz_vagas) == 0:
                            print("ERRO: Planilha sem dados.\n")
                            continue
                    
                        for vagas in range(len(vagas_coluna)):  # Imprime todas as vagas
                            print(f"{vagas_coluna[vagas]}")

                        vaga_filtrar = input("Qual vaga deseja filtrar?\n> ").upper().strip()
                        if vaga_filtrar not in vagas_coluna:
                            print("ERRO: Vaga não encontrada.\n")
                            continue

                        skills_utilizadas = []
                        for i in range(len(skills_linha)):
                            if matriz_vagas[i][vagas_coluna.index(vaga_filtrar)]:
                                skills_utilizadas.append(skills_linha[i])

                        if len(skills_utilizadas) == 0:
                            print(f"\nA vaga '{vaga_filtrar}' não utiliza nenhuma skill.\n")
                        else:
                            print(f"\nA vaga '{vaga_filtrar}' utiliza as seguintes skills:")
                            for skill in skills_utilizadas:
                                print(skill)
                            print(" ")
                        break

                    case "2":
                        if len(matriz_vagas) == 0:
                            print("ERRO: Planilha sem dados.\n")
                            continue

                        for skills in range(len(skills_linha)):  # Imprime todas as skills
                            print(f"{skills_linha[skills]}")

                        skill_filtrar = input("Qual skill deseja filtrar?\n> ").upper().strip()
                        if skill_filtrar not in skills_linha:
                            print("ERRO: Skill não encontrada.\n")
                            continue

                        vagas_utilizadas = []
                        for i in range(len(vagas_coluna)):
                            if matriz_vagas[skills_linha.index(skill_filtrar)][i]:
                                vagas_utilizadas.append(vagas_coluna[i])

                        if len(vagas_utilizadas) == 0:
                            print(f"\nA skill '{skill_filtrar}' não é utilizada em nenhuma vaga.\n")
                        else:
                            print(f"\nA skill '{skill_filtrar}' é utilizada nas seguintes vagas:")
                            for vaga in vagas_utilizadas:
                                print(vaga)
                            print(" ")
                        break

                    case "0":
                        os.system("cls")
                        break

                    case "LIMPAR":
                        os.system('cls')
                        continue

        case "0":
            os.system('cls')
            if resposta == "0":
                print(" Programa feito como TRABALHO FINAL da Disciplina de LP1")
                print("\nINTEGRANTES: Erick Lauretti\n             João Guilherme\n             Luiz Hélio \n")
                print("Obrigado por usar Cadastro de Vagas de Emprego!\nGITHUB Repository: https://github.com/LuizHelio-Fim/CadastroDeVagasDeEmprego_TrabalhoFinal \n\n")
                exit()

        case "LIMPAR":
            os.system('cls')
            continue

        case _:
            print("ERRO: OPÇÃO SELECIONADA INVALIDA.")
            continue