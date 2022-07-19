from paramiko import SSHClient, AutoAddPolicy

class SSH:
    conterror = 0
    def __init__(self, ip, usuario, pwd):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        self.ssh.connect(hostname=ip, username=usuario,password=pwd)
             
    def exec_cmd(self, pwd, cmd):
        stdin,stdout,stderr = self.ssh.exec_command('sudo ' + cmd, get_pty=True)
        stdin.write(pwd + '\n')
        stdin.flush()
        if stderr.channel.recv_exit_status() != 0:
            print('-> Erro na execução do comando!!!')
            print(f'-----> {cmd}')
            self.conterror += 1
            
        else:
            print('-> Comando executado com sucesso!!!')
            print(f'-----> {cmd}')