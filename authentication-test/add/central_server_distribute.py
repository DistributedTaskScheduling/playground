#! /usr/bin/python
from time import sleep
from os import remove

server_log = open('jobs.log', 'a')

while True:
    sleep(5.0)
    try:
        database = open('database', 'r')
    except Exception:  # Exception type different between Python 2/3
        continue
    read_lines = database.readlines()
    for read_line in read_lines:
        print('Distributed job %s' % read_line)
        server_log.write('Distributed job %s' % read_line)
    database.close()
    remove('database')
