from encrypt import *

def escrever_json(lista):
    with open('dados/encrypted.json', 'w') as f:
        json.dump(lista, f)

def carregar_json(arquivo):
    with open(arquivo, 'r') as f:
        return json.load(f)


base = carregar_json('dados/base.json')

def registrar(endereco, user, senha):

    vetor = [user, encrypt(senha)]

    dic = {endereco: vetor}

    escrever_json(dic)

    senha_escondida = ''
    i=0

    while i < len(senha):
        senha_escondida = senha_escondida + '*'
        i+=1

    print('Conta registrada com sucesso!\n')
    print(endereco + '\n' + user + '\n' + senha_escondida)


if __name__ == "__main__":

#    cripto = encrypt(input("Digite a senha:\n"))
#    print(cripto)
#    resposta = input("descriptografar? (S/N)\n")
#    if resposta == 's':
#        print(decrypt(cripto))
    i=0

    while i < 1:

        endereco = input('\nInsira o site/destino da senha: ')
        print('')
        user = input('Usuário associado à senha: ')
        print('')
        senha = input('Insira a senha a ser guardada: ')
        print('')
        confirmar_senha = input('Confirme a senha a inserida: ')
        print('')
        if senha != confirmar_senha:
            print('A senha inserida não confere...\n')
        else:
            registrar(endereco, user, senha)
            break
