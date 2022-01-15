FROM python:3

RUN sed -i "s/deb.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list && \
      sed -i "s/security.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list
RUN apt-get update && apt-get install -y libzbar-dev # for my personal need 

COPY requirements.txt requirements.txt 

RUN pip3 install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/ 

WORKDIR /app

COPY plugins/daily/souti0.txt /app/souti0.txt 