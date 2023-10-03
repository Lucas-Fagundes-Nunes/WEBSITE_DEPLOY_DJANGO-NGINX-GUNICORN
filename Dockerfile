FROM python:3.8-alpine

RUN pip install --upgrade pip

RUN mkdir /logs && chmod +w /logs

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./django_project /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]

