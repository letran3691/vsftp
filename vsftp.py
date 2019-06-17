#!/usr/local/bin/python3.6
import os,fileinput,time

def install():

    os.system('yum -y install epel-release ')
    os.system('yum install bind-utils db4-utils db4 lftp vsftpd -y')


    with open('/etc/pam.d/vsftpd_virtual','w') as file:
        file.write('#%PAM-1.0\n')
        file.write('auth    required        pam_userdb.so   db=/etc/vsftpd/virtual_users\n')
        file.write('account required        pam_userdb.so   db=/etc/vsftpd/virtual_users\n')
        file.write('session required        pam_loginuid.so\n')
        file.close()

    os.system('mv /etc/vsftpd/vsftpd.conf  /etc/vsftpd/vsftpd.conf.bak')

    os.system('cp /root/vsftp/vsftpd.conf /etc/vsftpd/')
    os.system('systemctl restart vsftpd')


    print('Install done!!!')
    time.sleep(4)
    exit(0)

def create_use():

    name = input('Enter username fpt: ')
    pas = input('Enter password: ')

    print("Remember this info, it's account ftp")

    with open('/etc/vsftpd/virtual_users.txt', 'a+') as user:
        user.write(name + '\n')
        user.write(pas + '\n')
        user.close()

    os.system('db_load -T -t hash -f /etc/vsftpd/virtual_users.txt /etc/vsftpd/virtual_users.db')


    os.system('mkdir -p /ftp/virtual/'+name)

    os.system('chown -R '+name+':ftp /ftp/virtual/'+name+'/')

def quit():

    exit(0)

print('\nEnter 1 to install vsftp')
print('Enter 2 to create user ftp')
print('Enter 3 to exit\n')

while True :
    n = int(input('Please enter function: '))
    if n == 1:
        #print('11111111111111111')
        install()

    elif n == 2:
        #print('2222222222222222222')
        create_use()
        print('Create user done')

    elif n == 3:
        quit()

    else:
        print('Option error!!! Please chose again\n')



