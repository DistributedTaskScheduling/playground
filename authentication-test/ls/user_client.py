#! /usr/bin/python3
import argparse
import paramiko

parser = argparse.ArgumentParser(description="Connect to given host via ssh with given username and password.")
parser.add_argument('--hostname')
parser.add_argument('--username')
parser.add_argument('--password')
args = parser.parse_args()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(policy=paramiko.AutoAddPolicy())
client.connect(hostname=args.hostname, username=args.username, password=args.password)
stdin, stdout, stderr = client.exec_command('ls')
for line in stdout:
    print(line.strip('\n'))
client.close()
