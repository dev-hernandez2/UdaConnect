FROM python:3.8

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

ENTRYPOINT [ "python", "app/grpc_server.py" ]