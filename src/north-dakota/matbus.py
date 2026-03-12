import requests as r, threading, time

headers = {
    "Referrer": "https://ridematbus.com/map",
    "Host": "ridematbus.com",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
}
models = ( # Update from and/or contribute to the CPTDB Wiki

    # North Dakota fleet
    (1173, 1176, "D35LFR"),
    (1184, 1188, "D35LFR"),
    (1195, 1199, "D35LFR"),
    (1200, 1201, "DE35LFR"),
    (1220, 1223, "XDE40"),
    (4151, 4152, "XDE40"),
    (4171, 4172, "XD35"),
    (4181, 4187, "XD35"),

    # Minnesota fleet
    (2151, 2151, "XD35"),
    (2161, 2164, "XD35"),
    (2171, 2172, "XD35"),
    (2181, 2182, "XD35"),
    (2201, 2202, "XD35")

)

models = {k: v for start, end, v in models for k in range(start, end + 1)}
routes = r.get("https://ridematbus.com/Region/0/Routes", headers=headers).json()

vehicles = {}
def get_line(route):
    global vehicles
    for v in r.get(f'https://ridematbus.com/Route/{route["ID"]}/Vehicles', headers=headers).json():
        vehicles[int(v["Name"])] = route["DisplayName"]
    print("*", end="", flush=True)

threads = [threading.Thread(target=get_line, args=(route,)) for route in routes]
for t in threads:
    t.start()
while any(t.is_alive() for t in threads):
    time.sleep(0.1)

print("\nBus    Model       Route\n" + "\n".join(f'{str(k).ljust(7)}{models.get(k, "N/A").ljust(12)}{v}' for k, v in sorted(vehicles.items())))