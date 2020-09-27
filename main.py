from encrypt import encrypt, decrypt, json

def escrever_json(lista):
    with open('dados/encrypted.json', 'w') as f:
        json.dump(lista, f)

def carregar_json():
    with open('dados/encrypted.json', 'r') as f:
        return json.load(f)



def lista():
    banco = carregar_json()
    i=1

    if len(banco) != 0:
        print("\nEndereços/sites cadastrados:\n")

    for nomes in banco:
        print()
        print(str(i) + ": " + nomes)
        print()
        i+=1

    if len(banco) == 0:
        print("\nNenhum cadastro encontrado.\n")
    else:
        x = input("\nDeseja lembrar um dos endereços?(S/N)\n")
        if x == 'S' or x == 's':
            lembrar()


def registrar():

    i=0
    while i < 1:
        print("\nPara sair igite \"sair\" sem as aspas em qualquer uma das repostas seguintes.\n")

        endereco = input('\nInsira o site/destino da senha (Ex: email, facebook): ')
        print('')
        if endereco == "sair":
            print("Operação cancelada.\n")
            return
        user = input('Usuário associado à senha: ')
        print('')
        if user == "sair":
            print("Operação cancelada.\n")
            return
        senha = input('Insira a senha a ser guardada: ')
        print('')
        if senha == "sair":
            print("Operação cancelada.\n")
            return
        confirmar_senha = input('Confirme a senha a inserida: ')
        print('')
        if senha != confirmar_senha:
            print('A senha inserida não confere...\nInsira os dados novamente.\n')
        else:
            break


    banco = carregar_json()
    banco[endereco] = [user] + [encrypt(senha)]
    escrever_json(banco)
    senha_escondida = ''
    i=0

    while i < len(senha):
        senha_escondida = senha_escondida + '*'
        i+=1

    print('\nConta registrada com sucesso!\n')
    print(endereco + '\n' + user + '\n' + senha_escondida)






def lembrar():
    endereco = input("\nInsira o endereço/site do qual você deseja lembrar as informações (Ex: email, facebook) ou \"sair\" sem as aspas para sair")
    if endereco == 'sair':
        return

    banco = carregar_json()

    try:
        dados = banco[endereco]

    except:
        print("\nEssa entrada não existe")

    i=0
    senha_escondida = ''
    while i < len(decrypt(dados[1])):
        senha_escondida = senha_escondida + '*'
        i+=1

    print("\n" + endereco + "\n" + dados[0] + "\n" + senha_escondida + "\n")
    x = input("\nDeseja receber essas informações?(S/N) ")
    if x == 's' or x == 'S':
        print("\n" + endereco + "\n" + dados[0] + "\n" + decrypt(dados[1]) + "\n")

if __name__ == "__main__":

    print("\nBem vindo ao Holocron\n")

    while True:

        resposta = input("\nPara guardar um cadastro digite 1, para lembrar um digite 2, para mostrar a lista de endereços 3, para sair digite 0.\n")

        if resposta == '1':
            registrar()
            x = input("\nDeseja realizar outra operação? (S/N) ")
            if x == "n" or x == "N":
                break
        elif resposta == '2':
            lembrar()
            x = input("\nDeseja realizar outra operação? (S/N) ")
            if x == "n" or x == "N":
                break
        elif resposta == '3':
            lista()
            x = input("\nDeseja realizar outra operação? (S/N) ")
            if x == "n" or x == "N":
                break
        elif resposta == '0':
            break
        else:
            print("\nErro, símbolo inserido não reconhecido")
            x = input("\nDeseja realizar outra operação? (S/N) ")
            if x == "n" or x == "N":
                break
        
