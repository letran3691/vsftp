#!/usr/local/bin/python3.6
import os,fileinput,time,subprocess

def quit():

    exit(0)


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

    print('sql ssl')
    time.sleep(3)
    os.system('mkdir /etc/ssl/private')
    #os.system('openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/vsftpd.key -out /etc/ssl/certs/vsftpd.crt')
    os.system('openssl req -new -nodes -days 365 -newkey rsa:4096 -keyout /etc/ssl/private/vsftpd.key -out /etc/ssl/certs/vsftpd.crt -subj "/C=VN/ST=HN/L=HD/O=Dis/CN=vsftp.local"')

    ip = subprocess.check_output('dig +short myip.opendns.com @resolver1.opendns.com',shell=True,universal_newlines=True)

    print('Your ip public: ',ip)

    add = ''

    while add != 'q':

        print('Enter 1 use ip public.')
        print('Enter 2 use hostname.')
        print('Enter q exit.\n')

        add = input('Enter option: ')

        if add == '1':

            with fileinput.FileInput('/etc/vsftpd/vsftpd.conf', inplace=True,backup=False) as  f:
                for line in f:
                    print(line.replace('pasv_address=','pasv_address='+ip),end='')
                f.close()

        elif add == '2':

            domain = input('Enter your domain:')

            with open('/etc/vsftpd/vsftpd.conf', 'a+') as f1:
                f1.write('pasv_addr_resolve=YES')
                f1.close()

            with fileinput.FileInput('/etc/vsftpd/vsftpd.conf', inplace=True, backup=False) as  f:
                for line in f:
                    print(line.replace('pasv_address=', 'pasv_address=' + domain), end='')
                f.close()


        elif add == 'q':

            quit()


        else:
            print('\nOption error!!! Please chose again\n'.upper())



        os.system('systemctl restart vsftpd')


        print('\nInstall done!!! Press q to exit\n'.title())


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

n = ''

while n != 'q' :
    print('\nEnter 1 to install vsftp')
    print('Enter 2 to create user ftp')
    print('Enter 3 to delete user ftp')
    print('Enter q to exit\n')

    n = input('\nPlease enter function: ')
    if n == '1':
        install()

    elif n == '2':
        create_use()
        print('\nCreate user done!!!\n')

    elif n == 3:
        del_use()
        print('\nDelete user done!!!\n')

    elif n == 'q':
        quit()

    else:
        print('\nOption error!!! Please chose again\n'.upper())
