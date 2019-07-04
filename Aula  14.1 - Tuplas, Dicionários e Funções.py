alunos = []

controle = True

while controle:
    q = int(input("Escolha uma das opções: \n1 - Cadastrar novo aluno \n2 - Excluir aluno \n3 - Alterar \n4 - Listar \n0 - Sair \n"))
    
    #Cadastrar o aluno
    if q == 1:
        print("\n******** CADASTRAR ALUNO ********")
        nome = str(input("Digite o nome do aluno: ")).upper()
        idade = int(input("Digite a idade: "))
        dic_aluno = {'nome':nome, 'idade':idade}
        alunos.append(dic_aluno)

    #Excluir o aluno
    elif q == 2:
        print("Excluir aluno")

    #Alterar o aluno
    elif q == 3:
        print(alunos)
    
    #Listar todos os alunos
    elif q == 4:
        print("Listar alunos")
    
    #Sair
    elif q == 0:
        controle = False
        print("Saindo")
    else:
        print("Escolha uma opção válida.")
    
print(alunos)