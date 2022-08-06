FROM python:3.7


WORKDIR /code

COPY . /code

RUN apt-get update
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE  8000

ENTRYPOINT [ "./entrypoint.sh" ]
