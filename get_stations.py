import json, re
import requests as r

page = r.get ("https://radar.mta.info/map").text
index_js_path = re.findall (r'"/assets/index.*?\.js"', page)
if len (index_js_path) != 1:
    raise SystemExit (f"Found {len (index_js_path)} index.js paths, expected 1")

index_js = r.get ("https://radar.mta.info" + index_js_path [0].strip ('"')).text
stations_str = re.findall (r'\[{.+?"name":"Hollis".+?}\]', index_js)
if len (stations_str) != 1:
    raise SystemExit (f"Found {len (stations_str)} stations lists, expected 1")

stations = {i ["code"]: i ["name"] for i in json.loads (stations_str [0])}
print (json.dumps (stations, sort_keys = True, separators = (",", ":")))
print (len (stations), "stations found")