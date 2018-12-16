ARG inbound_api_key
FROM python:3

ARG inbound_api_key
ENV API_KEY=$inbound_api_key
RUN echo $API_KEY

ENV PYTHONUNBUFFERED 1

RUN mkdir /news_api
WORKDIR /news_api
ADD requirements.txt /news_api/
RUN pip install -r requirements.txt

ADD . /news_api
