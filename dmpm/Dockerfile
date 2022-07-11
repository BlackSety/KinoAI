FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1  # Не создаем .pyc файлы

RUN apt-get update \
   && apt-get install netcat -y
RUN apt-get upgrade -y && apt-get install gcc python3-dev musl-dev -y
RUN pip install --upgrade pip

RUN mkdir dmpm
WORKDIR /dmpm
RUN mkdir static
RUN mkdir media

COPY requirements.txt /dmpm/
RUN pip install -r requirements.txt
ADD . /dmpm/
EXPOSE 8000
CMD python3 manage.py runserver 0.0.0.0:8000
