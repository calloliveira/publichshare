import sshconn
from pwinput import pwinput

print('Programa: SSHDeploy')
print('Autor: Carlos R. de Oliveira')
print('github: calloliveira')
print('LinkedIn: carlos-oliveira-it')
print('\n')
print(' ####################### FERRAMENTA DE DEPLOY SSH ##############################')
print(' #                                                                             #')
print(' #   1 - Certifique-se de ter populado a base de comandos a serem digitados    #')
print(' #   no terminal SSH remoto;  (database/dbcmd.csv)                             #')
print(' #                                                                             #')
print(' #   2 - Certifique-se de ter populado a base de IPs a serem alcançados pela   #')
print(' #   ferramenta. (database/ipdbhosts.csv)                                      #')
print(' #                                                                             #')
print(' ###############################################################################')
print('\n')
senha = cont ='null'
senha2 = 'llun'

print('=' * 80)
print(f'{"TIPO DE USUARIO":-^80}')
print('=' * 80)
print('1 - Root')
print('2 - Sudo')
print('=' * 80)
print('\n')

while True:
    usertype = int(input('Tipo de execução: '))
    if usertype == 1:
        usuario = 'root'
        break
    elif usertype == 2:
        usuario = str(input('Digite o usuário: '))
        break
    else:
        print('OPÇÃO INVÁLIDA')

#senha = str(input(f'Digite a senha de <{usuario}>: '))

while senha != senha2:
    senha = pwinput(prompt=f'Digite a senha para {usuario}: ')
    senha2 = pwinput(prompt=f'Confirme a senha para {usuario}: ')
    if not senha == senha2:
        print('\n')
        print('As senhas não conferem, digite novamente!!!')
        print('\n')

while not cont in 'SNsn':
    print('\n')
    cont = str(input(f'Deseja prosseguir com a execução através do usuário {usuario} [S/N]? '))      
    if not cont in 'SsNn':
        print('\n')
        print('Opção inválida, digite a correta!!!')

if cont in 'Ss':
    if usuario == 'root':
        sshconn.conecta_root(usuario, senha)
    else:
        sshconn.conecta_sudo(usuario, senha)
else:
    print('\n')
    print('Deploy SSH finalizado!!!')
    print('Obrigado!!!')
    print('By Call Oliveira')
    print('\n')
input('Pressione para fechar a janela!!!')