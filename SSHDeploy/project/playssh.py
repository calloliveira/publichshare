from pwinput import pwinput
import csv
from structure import SSH
from os import listdir
scriptpath = listdir("scripts/") 

############################## INFORMAÇÕES ##########################################

print()
print('Programa  :   SSHDeploy')
print('Autor     :   Carlos R. de Oliveira')
print('GitHub    :   calloliveira')
print('LinkedIn  :   carlos-oliveira-it')
print('\n')
print(' ####################### FERRAMENTA DE DEPLOY SSH ##############################')
print(' #                                                                             #')
print(' #   1 - Certifique-se de ter copiado o script de instalação que deseja fazer  #')
print(' #   o deploy para terminal SSH remoto;  (scripts/)                            #')
print(' #                                                                             #')
print(' #   2 - Certifique-se de ter preenchido a base de IPs a serem alcançados pela #')
print(' #   ferramenta. (database/ipdbhosts.csv)                                      #')
print(' #                                                                             #')
print(' ###############################################################################')
print()

#######################################################################################

################################# CONEXÃO SSH #########################################

senha = cont ='null'
senha2 = 'llun'
iplist = []
print('Scripts para deployment')
print()
for i, file in enumerate(scriptpath):
    print(f'[ {i} ] - {file}')
print()
scriptopt = int(input('Digite a opção: '))
print()
scriptfile = scriptpath[scriptopt]
cmdlist = [f'chmod +x /tmp/{scriptfile}',
        f'/bin/bash /tmp/{scriptfile}',
        f'rm -rf /tmp/{scriptfile}']

#Leitura banco de IPs:
with open('database/iphostsdb.csv', 'r', encoding='utf-8') as ipdbhosts:
    csvips = csv.reader(ipdbhosts, delimiter=';')
    for i in csvips:
        iplist.append(i[0])
    ipdbhosts.close()

def conecta_sudo(usuario, senha):
    for i in iplist:
        print()
        print('-------------------- INÍCIO DA EXECUÇÃO --------------------')
        print()
        try:
            client = SSH(i, usuario, senha, scriptfile)
            for c in cmdlist:
                client.exec_cmd_sudo(senha, c)
            if client.conterror != 0:
                client.salva_log(i, 'Erro na execução dos comandos')
            else:
                client.salva_log(i, 'Comandos executados com sucesso')
        except:
            client.salva_log(i, 'Erro na conexão SSH')

        print()
        print('-------------------- FIM DA EXECUÇÃO --------------------')

def conecta_root(usuario, senha):
    for i in iplist:
        print()
        print('-------------------- INÍCIO DA EXECUÇÃO --------------------')
        print()
        try:
            client = SSH(i, usuario, senha, scriptfile)
            for c in cmdlist:
                client.exec_cmd_root(senha, c)
            if client.conterror != 0:
                client.salva_log(i, 'Erro na execução dos comandos')
            else:
                client.salva_log(i, 'Comandos executados com sucesso')
        except:
            client.salva_log(i, 'Erro na conexão SSH')

        print()
        print('-------------------- FIM DA EXECUÇÃO --------------------')

#######################################################################################

############################ INTERAÇÃO USUÁRIO ########################################

print('=' * 80)
print(f'{"TIPO DE USUARIO":-^80}')
print('=' * 80)
print('1 - Root')
print('2 - Sudo')
print('=' * 80)
print()

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

while senha != senha2:
    senha = pwinput(prompt=f'Digite a senha para {usuario}: ')
    senha2 = pwinput(prompt=f'Confirme a senha para {usuario}: ')
    if not senha == senha2:
        print()
        print('As senhas não conferem, digite novamente!!!')
        print()

while not cont in 'SNsn':
    print()
    cont = str(input(f'Deseja prosseguir com a execução através do usuário {usuario} [S/N]? '))      
    if not cont in 'SsNn':
        print()
        print('Opção inválida, digite a correta!!!')

if cont in 'Ss':
    if usuario == 'root':
        conecta_root(usuario, senha)
    else:
        conecta_sudo(usuario, senha)
else:
    print()
    print('Deploy SSH finalizado!!!')
    print('Obrigado!!!')
    print('By Call Oliveira')
    print()
print()
input('Pressione qualquer tecla para sair... ')

############################################################################
