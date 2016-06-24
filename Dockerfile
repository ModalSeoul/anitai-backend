FROM python:3.5

ENV CPATH=/usr/local/include/python3.5m

RUN mkdir /anitai
WORKDIR /anitai

ADD requirements.txt /anitai/requirements.txt
RUN pip install --no-cache-dir --src /usr/src -r requirements.txt

ADD . /anitai
