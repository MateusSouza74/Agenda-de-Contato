def salvar_info(lista):
    with open("contatos.txt", "wt") as arquivo:  
        for info in lista:
            arquivo.write("{}#{}#{}#\n".format(info['nome'], info['cpf'], info['tel']))

        arquivo.close()

def carregar_info():
  lista = []  

  try:
    arquivo = open("contatos.txt", "r") 

    for linha in arquivo.readlines():
      coluna = linha.strip().split("#")
      info = {
        "cpf": coluna[1],
        "nome": coluna[0],
        "tel": coluna[2]
      }
      lista.append(info)

    arquivo.close()

  except FileNotFoundError: 
    pass

  return lista

        
def existe_info(lista, cpf):

    if lista is None or len(lista) == 0:
        return False

    for info in lista:
        if info['cpf'] == cpf:
            return True

    return False


def adicionar(lista):

    while True:

        cpf = input("Digite o CPF do contato: ")

        if not existe_info(lista, cpf):
            break
        else:
            print("CPF já cadastrado.")
            print("Insira outro CPF!")

    info = {
        "cpf": cpf,
        "nome": input("Digite o nome do contato: "),
        "tel": input("Digite o número de telefone: ")
    }
    lista.append(info)

    print("O contato {} foi cadastrado com sucesso!\n".format(info['nome']))


def alterar(lista):
    print(" == Alterar Contato ==")
    if len(lista) > 0:

        cpf = input("Digite o CPF do contato que deseja alterar: ")
        if existe_info(lista, cpf):

            for info in lista:
                if info['cpf'] == cpf:
                    print("\tNome: {}".format(info['nome']))
                    print("\tCPF: {}".format(info['cpf']))
                    print("\tTelefone: {}".format(info['tel'])) 

                    info['nome'] = input("Digite o novo nome do Contato.")
                    info['tel'] = input("Digite o novo telefone do Contato.")
                    print("Os dados do contato com o CPF {} foram alterados com sucesso.\n".format(info['cpf']))
                    break

        else:
            print ("Não há nenhum contato na lista com o cpf {}.\n".format(cpf))
def excluir(lista):
    print(" == Excluir Contato ==")
    if len(lista) > 0:

        cpf = input("Digite o CPF do contato que deseja exluir: ")
        if existe_info(lista, cpf):

            for i, info in enumerate(lista):
                if info['cpf'] == cpf:
                    print("\tNome: {}".format(info['nome']))
                    print("\tCPF: {}".format(info['cpf']))
                    print("\tTelefone: {}".format(info['tel'])) 
                    del lista[i]

                    print("O contado de CPF {} foi excluído com sucesso.\n".format(info['cpf']))
                    break
        else:
            print ("Não há nenhum contato na lista com o cpf {}.\n".format(cpf))
def buscar(lista):
    print(" == Busca de Contatos ==")
    if len(lista) > 0:

        cpf = input("Digite o CPF do contato que deseja encontrar: ")
        if existe_info(lista, cpf):

            for info in lista:
                if info['cpf'] == cpf:
                    print("\tNome: {}".format(info['nome']))
                    print("\tCPF: {}".format(info['cpf']))
                    print("\tTelefone: {}".format(info['tel'])) 
                    break
        else:
            print ("Não há nenhum contato na lista com o cpf {}.\n".format(cpf))


def listar(lista):
    print(" == Lista de Contatos ==")
    if len(lista) > 0:
        for i, info in enumerate(lista):
            print("Contato{}:".format(i+1))
            print("\tNome: {}".format(info['nome']))
            print("\tCPF: {}".format(info['cpf']))
            print("\tTelefone: {}".format(info['tel'])) 

            print("Quantidade de contatos: {}\n".format(len(lista)))
            break
        else:
            print ("Não há nenhum contato na lista.")
            

def principal():

  lista = carregar_info()

  while True:
    print("1 - Adicionar Contato")
    print("2 - Alterar Contato")
    print("3 - Excluir Contato")
    print("4 - Buscar Contato")
    print("5 - Listar Contato")
    print("6 - Encerrar Programa")
    opcao = int(input("> "))

    if opcao == 1:
        adicionar(lista)
        salvar_info(lista)
    elif opcao == 2:
        alterar(lista)
        salvar_info(lista)
    elif opcao == 3:
        excluir(lista)
        salvar_info(lista)
    elif opcao == 4:
        buscar(lista)  
    elif opcao == 5:
        listar(lista)
    elif opcao == 6:
        print("Programa Encerrado.")
        break
    else:
        print("Selecione uma opção válida.")  

principal()  
