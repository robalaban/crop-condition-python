FROM alpine:3.7

ADD ./app /home/app/
WORKDIR /home/app/

RUN apk add --no-cache postgresql-dev gcc python3 python3-dev musl-dev && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && \
    pip3 install -r requirements.txt

EXPOSE 6000

ENTRYPOINT ["python3", "app.py"]
