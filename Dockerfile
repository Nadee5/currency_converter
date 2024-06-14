FROM python:3

WORKDIR /currency_converter

COPY ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
