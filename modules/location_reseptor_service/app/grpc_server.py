import time, json
from concurrent import futures
import grpc
import location_pb2
import location_pb2_grpc
from kafka import KafkaProducer

TOPIC_NAME = "locations"
KAFKA_SERVER = "kafka-service:9092"

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):

        request_value = {
            'person_id': request.person_id,
            'longitude': request.longitude,
            'latitude': request.latitude
        }
        
        kafka_request = json.dumps(request_value).encode('utf-8')
        producer.send(TOPIC_NAME, kafka_request)
        producer.flush()

        
        return location_pb2.LocationMessage(**request_value)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)

server.add_insecure_port("[::]:5005")
server.start()

server.wait_for_termination()