import requests as r

headers = {
    "Referrer": "https://link.rideralerts.com/InfoPoint/",
    "Host": "link.rideralerts.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}
models = ( # Update from and/or contribute to the CPTDB Wiki
    (309, 312, "Gillig 29'"),
    (338, 349, "Gillig 40'"),
    (510, 524, "Ford E450"),
    (813, 822, "BYD K9S"),
    (823, 825, "BYD K8M"),
    (860, 861, "BYD K7M"),
    (862, 869, "BYD K7M-ER"),
    (1601, 1607, "Ford E450")
)

models = {k: v for start, end, v in models for k in range(start, end + 1)}
routes = r.get("https://link.rideralerts.com/InfoPoint/rest/Routes/GetVisibleRoutes", headers=headers).json()
vehicles = {}

for route in routes:
    for vehicle in route["Vehicles"]:
        vehicles[int(vehicle["VehicleId"])] = f'{route["RouteAbbreviation"]} {vehicle["Destination"]}'

print("Bus    Model         Route\n" + "\n".join(f'{str(k).ljust(7)}{models.get(k, "N/A").ljust(14)}{v}' for k, v in sorted(vehicles.items())))