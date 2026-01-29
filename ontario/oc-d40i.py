from dotenv import load_dotenv
from google.transit import gtfs_realtime_pb2
import os, requests
os
load_dotenv()
API_KEY = os.getenv("OC_TRANSPO_API_KEY")

feed = gtfs_realtime_pb2.FeedMessage()
feed.ParseFromString(requests.get(
    "https://nextrip-public-api.azure-api.net/octranspo/gtfs-rt-vp/beta/v1/VehiclePositions",
    headers={"Ocp-Apim-Subscription-Key": API_KEY}
).content)

statuses = []
for entity in feed.entity:
    try:
        vehicle_id = int(entity.vehicle.vehicle.id)
    except ValueError:
        continue
    if vehicle_id >= 4203 and vehicle_id <= 4526: # NFI D40i
        statuses.append((entity.vehicle.trip.route_id or "N/A", vehicle_id, entity.vehicle.position.latitude, entity.vehicle.position.longitude))

statuses.sort()
print("Bus     Route   Coordinates\n" + "\n".join(f"{str(i[1]).ljust(8)}{i[0].ljust(8)}({i[2]}, {i[3]})" for i in statuses))