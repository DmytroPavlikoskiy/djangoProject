FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /lotokingsman

WORKDIR /lotokingsman

RUN apt-get update

RUN apt-get install default-libmysqlclient-dev

RUN pip install mysqlclient

COPY ./requirements.txt /lotokingsman

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ./wait-for-it.sh db:3306 -- python3 LotoKingsMan/manage.py runserver