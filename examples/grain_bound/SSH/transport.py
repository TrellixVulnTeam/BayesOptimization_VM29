#!/usr/bin/env python
# -*-coding:utf-8-*-
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('../tmp/anmeng', '')

# ����SSH����
ssh = paramiko.SSHClient()
# �������Ӳ���know_hosts�ļ��е�����
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ���ӷ�����
ssh.connect(hostname='192.168.1.2', port=22, username='anmeng', pkey=private_key)

# �ļ�����
sftp = ssh.open_sftp()
# ��remove_path ���ص����� local_path
# sftp.get(remotepath='/work1/anmeng_work/zkl/PPE/bb.py', localpath=r'E:\Study\pe-pp\PPE\2.txt')
sftp.put(localpath=r'E:\Study\pe-pp\PPE\2.txt', remotepath='/work1/anmeng_work/zkl/PPE/1.txt')

# ִ������
stdin, stdout, stderr = ssh.exec_command('ls')
# ��ȡ������
result = stdout.read()
print(result.decode('utf-8'))
# �ر�����
ssh.close()
