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

years = { # Update from and/or contribute to the CPTDB Wiki
    (4201, 4202, "2003"),
    (4203, 4273, "2004"),
    (4274, 4309, "2005"),
    (4310, 4439, "2005"),
    (4440, 4526, "2006")
}
years = {k: v for start, end, v in years for k in range(start, end + 1)}

statuses = []
for entity in feed.entity:
    try:
        vehicle_id = int(entity.vehicle.vehicle.id)
    except ValueError:
        continue
    if vehicle_id >= 4201 and vehicle_id <= 4526: # NFI D40i
        statuses.append((entity.vehicle.trip.route_id or "N/A", vehicle_id, entity.vehicle.position.latitude, entity.vehicle.position.longitude, years.get(vehicle_id, "N/A")))

statuses.sort()
print("Bus     Year    Route   Coordinates\n" + "\n".join(f"{str(i[1]).ljust(8)}{i[4].ljust(8)}{i[0].ljust(8)}({i[2]}, {i[3]})" for i in statuses))