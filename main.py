from encrypt import encrypt, decrypt, json

def escrever_json(lista):
    with open('dados/encrypted.json', 'w') as f:
        json.dump(lista, f)

def carregar_json():
    with open('dados/encrypted.json', 'r') as f:
        return json.load(f)

def registrar():

    i=0
    while i < 1:
        print("para sair igite \"sair\" sem as aspas em qualquer uma das repostas seguintes.\n")

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

    print('Conta registrada com sucesso!\n')
    print(endereco + '\n' + user + '\n' + senha_escondida)






def lembrar():
    endereco = input("Insira o endereço/site do qual você deseja lembrar as informações (Ex: email, facebook) ou \"sair\" sem as aspas para sair. \n")
    if endereco == 'sair':
        return

    banco = carregar_json()

    try:
        dados = banco[endereco]

    except:
        print("essa entrada não existe")

    print("\n" + endereco + "\n" + dados[0] + "\n" + dados[1] + "\n")
    x = input("Deseja receber essas informações?(S/N) ")
    if x == 's' or x == 'S':
        print("\n" + endereco + "\n" + dados[0] + "\n" + decrypt(dados[1]) + "\n")

if __name__ == "__main__":

#    cripto = encrypt(input("Digite a senha:\n"))
#    print(cripto)
#    resposta = input("descriptografar? (S/N)\n")
#    if resposta == 's':
#        print(decrypt(cripto))

    print("Bem vindo ao Holocron")

    while True:

        resposta = input("para guardar um cadastro digite 1, para lembrar um digite 2, para sair digite 0.\n")

        if resposta == '1':
            registrar()
            x = input("desja realizar outra operação? (S/N) ")
            if x == "n" or x == "N":
                break
        elif resposta == '2':
            lembrar()
            x = input("desja realizar outra operação? (S/N) ")
            if x == "n" or x == "N":
                break
        elif resposta == '0':
            break
        else:
            print("Erro, símbolo inserido não reconhecido")
            x = input("desja realizar outra operação? (S/N) ")
            if x == "n" or x == "N":
                break
        
