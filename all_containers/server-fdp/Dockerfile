#FROM python:3.7
FROM python:3.7-slim-buster

WORKDIR /usr/src/app
COPY ./server-fdp .
RUN ls
RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements_fdp.txt

CMD ["python3", "fdp.py"]
