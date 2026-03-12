import requests as r

headers = {
    "Accept": "application/json, text/javascript, */*",
    "Origin": "https://myride.minotnd.gov",
    "Referer": "https://myride.minotnd.gov/RouteMap",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
models = { # Update from and/or contribute to the CPTDB Wiki
    1002: "AmTran RE",
    1003: "AmTran RE",
    1004: "AmTran RE",
    1005: "EZ Rider II MAX 32'",
    1006: "EZ Rider II MAX 32'",
    1007: "EZ Rider II BRT 32'",
    1008: "EZ Rider II BRT 32'",
    1009: "International RE",
    1010: "EZ Rider II BRT 32'",
    1011: "EZ Rider II BRT 32'",
    1013: "IC Corp. RE300"
}

base_data = r.post ("https://myride.minotnd.gov/RouteMap/GetBaseData/", headers = headers).json ()
routes = {i ["key"]: f'{i ["shortName"]} {i ["name"]}' for i in base_data ["routes"]}

vehicles = r.post (
    "https://myride.minotnd.gov/RouteMap/GetVehicles/",
    headers = dict (headers, **{"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}),
    data = {"routeKeys": routes.keys ()}
).json ()

status, count = {}, 0
for i in vehicles:
    for j in i ["vehiclesByDirections"]:
        for k in j ["vehicles"]:
            status [int (k ["name"])] = routes [i ["routeKey"]]
            count += 1
print(f"Count: {count}\nBus    Model                  Route\n" + "\n".join(f'{str(k).ljust(7)}{models.get(k, "N/A").ljust(23)}{v}' for k, v in sorted(status.items())))