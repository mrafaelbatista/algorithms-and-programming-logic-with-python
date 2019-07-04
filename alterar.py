""" Não vou mostrar como se faz dentro das funções.
Com isso, pretendo ajudar a compreender comor realizar a funções,
mas não como responder a questão. """

pessoas = [{'nome': 'Messias', 'idade': 33}, {'nome':'João', 'idade': 55}]

#Primeiro precisamos pesquisar quem queremos alterar;

nome_para_pesquisar = str(input("Quem você deseja alterar? "))

for pessoa in pessoas:
    
    if pessoa['nome'] == nome_para_pesquisar:
        x = True
        while x:
            opcao = int(input("1 - Alterar nome \n2 - Alterar Idade \n0 - Sair \n"))
            
            if opcao == 1:
                nome_para_alterar = str(input("Digite o novo nome: "))
                pessoa['nome'] = nome_para_alterar
                print("Nome alterado para -> " + pessoa['nome'])
            elif opcao == 2:
                idade_para_alterar = int(input("Digite a nova idade: "))
                pessoa['idade'] = idade_para_alterar
                print("Idade alterado para -> " + str(pessoa['idade']))
            elif opcao == 0:
                x = False
            else:
                print("ESCOLHA UMA OPÇÃO VÁLIDA!")

print(pessoas)