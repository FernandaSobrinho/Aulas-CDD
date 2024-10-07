resposta = -1
registros = {}

while resposta != 0:
    print("==========================")
    print("1 - Registrar novo usuário")
    print("2 - Logar")
    print("0 - Sair")
    print("==========================")
    resposta = int(input("Escolha uma das opções acima: "))

    if resposta == 1:
        registronome = input("Crie um nome de usuário: ")
        registrosenha = input("Crie uma senha: ")
        registros[registronome] = registrosenha
        print("==========================")
        print("Usuário registrado com sucesso!")

    elif resposta == 2:
        nome = input("Informe o nome de usuário: ")
        senha = input("Informe a senha: ")

        if nome in registros and registros[nome] == senha:
                print("==========================")
                print(f"Usuário {nome} logado com sucesso!")
        else:
                print("==========================")
                print("Usuário ou senha incorretas! Tente novamente!")

    elif resposta == 0:
        print("==========================")
        print("Saindo do menu.")

    else:
        print("==========================")
        print("Resposta invalida! Tente novamente.")