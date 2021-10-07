import psycopg2, os, json
from kafka import KafkaConsumer

TOPIC_NAME = "locations"
SERVER_URL = "kafka-service:9092"




DB_NAME = os.environ["DB_NAME"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[SERVER_URL])

def save_to_db(location):
    db_conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    db_cursor = db_conn.cursor()
    person_id = int(location["person_id"])
    latitude, longitude = float(location["latitude"]), float(location["longitude"])
   
    sql = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))".format(person_id, latitude, longitude)
    db_cursor.execute(sql)
    db_conn.commit()
    db_cursor.close()
    db_conn.close()



for location in consumer:
    message = location.value.decode('utf-8')
    location_data = json.loads(message)
    save_to_db(location_data)