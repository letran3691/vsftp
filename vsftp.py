#!/usr/local/bin/python3.6
import os,fileinput,time,subprocess

def install():

    os.system('yum -y install epel-release ')
    os.system('yum install bind-utils db4-utils db4 lftp vsftpd -y')


    with open('/etc/pam.d/vsftpd_virtual','w') as file:
        file.write('#%PAM-1.0\n')
        file.write('auth    required        pam_userdb.so   db=/etc/vsftpd/virtual_users\n')
        file.write('account required        pam_userdb.so   db=/etc/vsftpd/virtual_users\n')
        file.write('session required        pam_loginuid.so\n')
        file.close()

    os.system('cp -f /root/vsftp/vsftpd.conf /etc/vsftpd/')

    ip = subprocess.check_output('dig +short myip.opendns.com @resolver1.opendns.com',shell=True,universal_newlines=True)

    print('Your ip public: ',ip)

    with fileinput.FileInput('/etc/vsftpd/vsftpd.conf', inplace=True,backup=False) as  f:
        for line in f:
            print(line.replace('pasv_address=','pasv_address='+ip),end='')
        f.close()

    os.system('systemctl restart vsftpd')


    print('Install done!!!')
    time.sleep(4)
    exit(0)

def create_use():

    name = input('Enter username ftp: ')
    pas = input('Enter password: ')

    print("\nRemember this info, it's account ftp")

    with open('/etc/vsftpd/virtual_users.txt', 'a+') as user:
        user.write(name + '\n')
        user.write(pas + '\n')
        user.close()

    os.system('db_load -T -t hash -f /etc/vsftpd/virtual_users.txt /etc/vsftpd/virtual_users.db')


    os.system('mkdir -p /ftp/virtual/'+name)

    os.system('chown -R ftp: /ftp/virtual/')

def del_use():
    name = input('Enter username fpt: ')

    os.system("rm -rf /ftp/virtual/"+name)

def quit():

    exit(0)

while True :
    print('\nEnter 1 to install vsftp')
    print('Enter 2 to create user ftp')
    print('Enter 3 to delete user ftp')
    print('Enter 4 to exit\n')

    n = int(input('\nPlease enter function: '))
    if n == 1:
        install()

    elif n == 2:
        create_use()
        print('\nCreate user done!!!')

    elif n == 3:
        del_use()
        print('\nDelete user done!!!')

    elif n == 4:
        quit()

    else:
        print('\nOption error!!! Please chose again\n')



