Holocron é um software simples em desenvolvimento por mim com a finalidade de ser um banco de senhas criptografadas. Ele tem a função de criptografar e guardar as senhas num arquivo de formato json e também disponibilizar a verificação de todas as senhas registradas (ainda criptografadas) e por fim permite a seleção da senha desejada e retorna a mesma na forma original.

Esse projeto é um estudo para refinar minhas habilidades de programação e também servir como utilidade para mim e qualquer pessoa que se interessar.

O arquivo crypto.py, que guarda as informações de criptografia, não está disponível por motivos óbvios. Porém este código tem a finalidade de ser simples e precisar apenas de uma forma de criptografia para funcionar. Assim, qualquer pessoa que pretender utilizá-lo precisará apenas escrever uma forma de criptografia (e de descriptografia), ou pegar uma existente, e salvá-la como crypto.py que será reconhecida e utilizada para gerar seu banco de senhas.

Modo de usar:
Crie um arquivo chamado "encrypt.py", ele deve possuir, pelo menos, duas funções:
A função encrypt(senha) que recebe uma string com a senha e retorna uma string com a senha criptografada.
E a função decrypt(senha) que recebe uma string com a senha criptografada e retorna uma string com a senha original.
Coloque o arquivo "encrypt.py" no diretório do Holocron.
Execute o arquivo "main.py"
