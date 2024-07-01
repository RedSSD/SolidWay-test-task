FROM python:3.10.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /soliway
WORKDIR /solidway

COPY requirements.txt /solidway/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y cron && touch /var/log/cron.log

EXPOSE 5432

ADD . /solidway/