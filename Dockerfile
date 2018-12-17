ARG inbound_api_key
FROM python:3
MAINTAINER david.nvalderrama@gmail.com

ARG inbound_api_key
ENV API_KEY=$inbound_api_key
RUN echo $API_KEY

ENV PYTHONUNBUFFERED 1

RUN mkdir /news_api
WORKDIR /news_api
ADD requirements.txt /news_api/

ADD ./start-exec.sh /news_api/
#RUN chmod -R 777 ./start-exec.sh
RUN ls -l /news_api

#ENTRYPOINT ["./start-exec.sh"]

ADD . /news_api
RUN pip install -r requirements.txt
#sudo docker-compose build --build-arg inbound_api_key=af92652e76b745a6bde8dd2fc5739bfd
