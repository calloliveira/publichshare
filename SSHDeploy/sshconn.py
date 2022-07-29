import csv
from structure import SSH

cmdlist = []
iplist = []

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

def conecta_sudo(usuario, senha):
    for i in iplist:
        print()
        print('-------------------- INÍCIO DA EXECUÇÃO --------------------')
        print()

        try:
            client = SSH(i, usuario, senha)
            print(f'EXECUTANDO NO IP: {i}')
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
            client = SSH(i, usuario, senha)
            print(f'EXECUTANDO NO IP: {i}')
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
