import csv
from sshbase import SSH
from datetime import datetime
from os import path

############## PERSONALIZAR ##############

usuario = 'yourusersudo'
senha = 'yourpass'

################## FIM ###################

data = str(datetime.now())
hora = data[11:16]
data = data[0:11]
cmdlist = []
iplist = []
logfullpath = (f'log/{data}_log-exec.csv')

#Gravação arquivo de log
if not path.exists(f'{logfullpath}'):
    logfile = open(f'{logfullpath}', 'w')
    logfile.write('Horario;IP;Status')
else:
    logfile = open(f'{logfullpath}', 'a')

#Leitura banco de IPs:

with open('database/iphostsdb.csv', 'r', encoding='utf-8') as ipdbhosts:
    csvips = csv.reader(ipdbhosts, delimiter=';')
    for i in csvips:
        iplist.append(i[0])
    ipdbhosts.close()
    
#Leitura banco de comandos:
   
with open('database/dbcmd.csv', 'r', encoding='utf-8') as dbcmd:
    csvcmd = csv.reader(dbcmd, delimiter=';')
    for c in csvcmd:
        cmdlist.append(c[0])
    dbcmd.close()

#Execução dos comandos nos hosts em série:

for i in iplist:
    print('\n')
    print('-------------------- INÍCIO DA EXECUÇÃO --------------------')
    print('\n')
    client = SSH(i, usuario, senha)
    print(f'EXECUTANDO NO IP: {i}')
    for c in cmdlist:
        client.exec_cmd(senha, c)
    if client.conterror != 0:
        logfile.write(f'\n{hora};{i};Erro na execução dos comandos')
    else:
        logfile.write(f'\n{hora};{i};Comandos executados com sucesso')
    print('\n')
    print('-------------------- FIM DA EXECUÇÃO --------------------')
