import re
import requests as r
page = r.get ("https://radar.mta.info/map").text
index_js_path = re.search (r'"/assets/index.*?\.js"', page).group ().strip ('"')
index_js = r.get ("https://radar.mta.info" + index_js_path).text

