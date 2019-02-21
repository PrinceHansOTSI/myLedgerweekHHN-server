
# base image
FROM ubuntu:18.04

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install python3-pip python3

WORKDIR /data
# add dependencies file
ADD requirements.txt .
# install dependencies
RUN pip3 install -r requirements.txt

CMD [ "python3", "-u", "server.py" ]