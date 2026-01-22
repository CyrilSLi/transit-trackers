import requests as r, threading, time

headers = {
    "Referrer": "https://catprowler.org/map",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}
models = { # Update from and/or contribute to the CPTDB Wiki
    103: "DE35LFR",
    104: "DE35LFR",
    105: "D35LFR",
    106: "D35LFR",
    162: "Chevy G4500",
    183: "XD35",
    184: "XD35",
    185: "XD35",
    191: "Ram 3500",
    192: "Ram 3500",
    193: "Enviro200",
    194: "Enviro200",
    201: "XD35",
    202: "XD35",
    203: "XD35"
}

routes = r.get("https://catprowler.org/Region/0/Routes", headers=headers).json()
if any(len(i["Patterns"]) != 1 for i in routes):
    raise SystemExit("Unexpected number of patterns in route data")

vehicles = {}
def get_line(route):
    global vehicles
    for v in r.get(f'https://catprowler.org/Route/{route["ID"]}/Vehicles', headers=headers).json():
        vehicles[int(v["Name"])] = route["DisplayName"]
    print("*", end="", flush=True)

threads = [threading.Thread(target=get_line, args=(route,)) for route in routes]
for t in threads:
    t.start()
while any(t.is_alive() for t in threads):
    time.sleep(0.1)

print("\nBus    Model       Route\n" + "\n".join(f'{str(k).ljust(7)}{models.get(k, "N/A").ljust(12)}{v}' for k, v in sorted(vehicles.items())))