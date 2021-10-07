FROM python:3.8.0

WORKDIR .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

ENTRYPOINT [ "python", "app/server.py" ]