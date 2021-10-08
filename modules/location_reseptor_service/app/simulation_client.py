import json
import grpc

import location_pb2
import location_pb2_grpc


print("sending...")

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub((channel))

location_1 = location_pb2.LocationMessage(
    person_id=20,
    latitude=-84.2009245,
    longitude=-39.7580027
)


location_2 = location_pb2.LocationMessage(
    person_id=21,
    latitude=-84.171785,
    longitude=39.3121409
)

stub.Create(location_1)
stub.Create(location_2)


print("responding...")
# response = {"person_lications:" [location_1, location_2]}

print(location_2)