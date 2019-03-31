FROM python:3

LABEL maintainer="Alvaro Paco"
LABEL contact="alvaropaconeto@gmail.com"

RUN pip install pytest

WORKDIR /mnt

COPY . /mnt

CMD [ "python", "./main.py" ]
