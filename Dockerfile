FROM python:3.9-slim-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y pkg-config default-libmysqlclient-dev build-essential

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]