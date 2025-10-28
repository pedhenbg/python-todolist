import os
tarefas =[]
try:
    with open ("tarefas.txt","r") as f:
       for linha in f:
           tarefas.append(linha.strip())
    print("----Lista carregada----")
except FileNotFoundError:
    print("Nenhum arquivo de tarefas encontrado,começando do zero.")
    pass
def limpar_tela():
    os.system('cls' if os.name== 'nt' else 'clear')
rodando = True
while rodando:
    limpar_tela()
    print("----To do list----")
    print("O que deseja fazer?(Digite o numero correspondente)")
    print("1-Ver lista de tarefas")
    print("2-Adicionar tarefa")
    print("3-Remover tarefa")
    print("4-Salvar e sair")
    print("...................................................")
    decisao = input("1,2,3,4?")

    if decisao == "1":
        if len(tarefas) == 0:
            input("Lista de tarefas vazia!(Digite qualquer tecla para continuar)")

        else:
            for indice, tarefa in enumerate(tarefas):
                print(f"{indice}: {tarefa}")
 
    elif decisao == "2":
        tarefa = input("Digite a tarefa a ser adicionada na lista")
        tarefas.append(tarefa)

    elif decisao == "3":
        if len(tarefas) == 0:
            input("Lista de tarefas vazia!(Digite qualquer tecla para continuar)")

        else:
            print("---Tarefas Atuais:---")
            for indice, tarefa in enumerate(tarefas):
                print(f"{indice}: {tarefa}")
            print("--------------------------")

            try:


                indice_excluir = int(input("Qual o indice da tarefa que deseja exclui?"))
                tarefas.pop(indice_excluir)
            except ValueError:
                print("Erro:Digite um numero!")
            except IndexError:
                print(f"Erro: O índice {indice_excluir} não existe!")


    elif decisao =="4":
        print("Salvando Tarefas...")

        with open("tarefas.txt","w") as f:
            for tarefa in tarefas:
                f.write(f"{tarefa}\n")
        input("Programa sendo finalizado(Digite qualquer tecla para finalizar)")
        break
    else:
        print("Numero invalido.")
        continue