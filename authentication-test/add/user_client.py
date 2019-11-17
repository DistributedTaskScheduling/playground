#! /usr/bin/python
import argparse
import paramiko

parser = argparse.ArgumentParser(description="Connect to given host via ssh with given username and password.")
parser.add_argument('--hostname')
parser.add_argument('--username')
parser.add_argument('--password')
parser.add_argument('--job')
args = parser.parse_args()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(policy=paramiko.AutoAddPolicy())
client.connect(hostname=args.hostname, username=args.username, password=args.password)
stdin, stdout, stderr = client.exec_command('./central_server_add.py --job=%s' % args.job)
for line in stdout:
    print(line)
for line in stderr:
    print(line)
client.close()
