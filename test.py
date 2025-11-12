import json
import requests as r
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Version": "3.0",
    "Host": "backend-unified.mylirr.org",
    "Origin": "https://radar.mta.info",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}
resp = r.get ("https://backend-unified.mylirr.org/locations?geometry=TRACK_TURF&railroad=BOTH", headers = headers)
for train in resp.json ():
    cars = []
    for car in train ["consist"] ["cars"]:
        if car ["type"].upper () in ["M1", "M3", "M3A"]:
            if not cars:
                print (f"{railroad} {branch} Branch to {headsign}"