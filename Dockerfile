##################Dockerfile##################
FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y openjdk-8-jdk 
RUN apt-get install -y bzip2 
RUN apt-get install -y wget
RUN apt-get install -y gcc 
RUN apt-get install -y git 
RUN apt-get install -y python3 
RUN apt-get install -y python3-pip 

RUN pip3 install Werkzeug==0.16.1
RUN pip3 install flask==1.1.2
RUN pip3 install flask_restplus==0.13.0

RUN pip3 install numpy==1.18.4
RUN pip3 install scipy==1.4.1

WORKDIR /root

RUN git clone https://github.com/gaoyuanliang/flusk_utility.git
RUN mv flusk_utility/* ./

RUN pip3 install tensorflow==2.2.0
RUN pip3 install keras==2.4.3
RUN pip3 install keras_bert==0.86.0

WORKDIR /root

RUN git clone https://github.com/gaoyuanliang/bert_text_embedding.git
RUN mv bert_text_embedding/* ./

WORKDIR /root
RUN wget https://storage.googleapis.com/bert_models/2019_05_30/wwm_uncased_L-24_H-1024_A-16.zip

RUN apt-get install -y unzip 

RUN unzip wwm_uncased_L-24_H-1024_A-16.zip
RUN rm wwm_uncased_L-24_H-1024_A-16.zip

RUN rm server_path.py
RUN wget https://raw.githubusercontent.com/gaoyuanliang/bert_text_embedding/master/server_path.py

#COPY *.py /root/

CMD python3 app_path.py
##################Dockerfile##################
