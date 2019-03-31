FROM python:3

LABEL maintainer="Alvaro Paco"
LABEL contact="alvaropaconeto@gmail.com"

RUN pip install pytest pytest-cov mock

WORKDIR /mnt

COPY . /mnt

CMD [ "pytest" ,"--cov" ,"./tests" ]
