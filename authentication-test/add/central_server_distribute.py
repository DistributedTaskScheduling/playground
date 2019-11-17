#! /usr/bin/python
from time import sleep
from os import remove


while True:
    sleep(5.0)
    try:
        database = open('database', 'r')
    except Exception:  # Exception type different between Python 2/3
        print('No new jobs found')
        continue
    read_lines = database.readlines()
    server_log = open('jobs.log', 'a')
    for read_line in read_lines:
        print('Distributed job %s' % read_line)
        server_log.write('Distributed job %s' % read_line)
    server_log.close()
    database.close()
    remove('database')
