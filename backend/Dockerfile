FROM python:3.9

ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONPATH .

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1 

RUN python3.9 -m pip install --no-cache-dir --upgrade pip==23.2.1

COPY ./requirements.txt /requirements.txt

RUN python3.9 -m pip install --no-cache-dir -r /requirements.txt

ENV API_ENV DEV

COPY ./entrypoint.sh /entrypoint.sh

CMD [ "/entrypoint.sh" ]