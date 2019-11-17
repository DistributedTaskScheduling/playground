#! /usr/bin/python3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--job')
args = parser.parse_args()

database = open('database', mode='a')
database.write(args.job + '\n')
database.close()
