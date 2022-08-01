from paramiko import SSHClient, AutoAddPolicy
from datetime import datetime
from os import path

class SSH:
    conterror = 0
    def __init__(self, ip, usuario, pwd, scriptfile):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh.connect(hostname=ip, username=usuario,password=pwd)
        print(f'\033[32m-> Conexão SSH efetuada com sucesso... IP: {ip}\033[m')
        ftp_client = self.ssh.open_sftp()
        ftp_client.put(localpath=f'scripts/{scriptfile}', remotepath=f'/tmp/{scriptfile}')
        print(f'\033[32m-> Script ({scriptfile}) copiado com sucesso!!!\033[m')

    def exec_cmd_sudo(self, pwd, cmd):
        stdin, stdout, stderr = self.ssh.exec_command('sudo ' + cmd, get_pty=True)
        stdin.write(pwd + '\n')
        stdin.flush()
        print(f'Executando Comando... ({cmd})')
        if stderr.channel.recv_exit_status() != 0:
            print('\033[31m'+'-> Erro na execução do comando!!!\033[m')
            self.conterror += 1
        else:
            print('\033[32m'+'-> Comando executado com sucesso!!!\033[m')

    def exec_cmd_root(self, pwd, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        print(f'Executando Comando... ({cmd})')
        if stderr.channel.recv_exit_status() != 0:
            print('\033[31m-> Erro na execução do comando!!!\033[m')
            self.conterror += 1
        else:
            print('\033[32m-> Comando executado com sucesso!!!\033[m')
        

    def salva_log(self, ip, msglog):
        data = str(datetime.now())
        hora = data[11:16]
        data = data[0:11]
        logfullpath = (f'log/{data}_log-exec.csv')
        if not path.exists(f'{logfullpath}'):
            logfile = open(f'{logfullpath}', 'w')
            logfile.write('Horario;IP;Status')
        else:
            logfile = open(f'{logfullpath}', 'a')

        logfile.write(f'\n{hora};{ip};{msglog}')
        logfile.close()
