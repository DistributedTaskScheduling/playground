FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 && apt-get clean

COPY factorial.py /data/application.py

CMD python3 /data/application.py
