import requests as r

bus_ids = [
    "--- D40LFR ---",
    51, 52, 53, 54,
    "--- D35LFR ---",
    55, 56, 57, 58, 59, 60, 61,
    "--- Nova LFS ---",
    67, 68, 69, 70,
    "--- XD40 ---",
    71, 72
]
headers = {
    "Accept": "application/json, text/javascript, */*",
    "Origin": "https://myride.brandontransit.ca",
    "Referer": "https://myride.brandontransit.ca/RouteMap",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

base_data = r.post ("https://myride.brandontransit.ca/RouteMap/GetBaseData/", headers = headers).json ()
routes = {i ["key"]: f'{i ["shortName"]} {i ["name"]}' for i in base_data ["routes"]}

vehicles = r.post (
    "https://myride.brandontransit.ca/RouteMap/GetVehicles/",
    headers = dict (headers, **{"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}),
    data = {"routeKeys": routes.keys ()}
).json ()

status, count = {}, 0
for i in vehicles:
    for j in i ["vehiclesByDirections"]:
        for k in j ["vehicles"]:
            status [int (k ["name"])] = routes [i ["routeKey"]]
            count += 1
print (f"Count: {count}\nBus\t\tRoute\n" + "\n".join (f'{i}\t\t{status.get (i, "N/A")}' if type (i) is not str else i for i in bus_ids))