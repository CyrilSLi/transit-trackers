import requests as r, time, threading

bus_ids = [
    "--- XE40 & XE60 ---",
    288, 289, 290, 296,
    "--- NOT PHOTOGRAPHED ---",
    586, 579, 590, 597,
    "--- Retired? ---",
    570, 573, 574, 575, 576, 578, 580, 581, 583, 584, 585, 587, 589, 591, 593, 595, 596, 599,
    "--- Photographed 500s ---",
    571, 572, 577, 582, 588, 592, 594,
    "--- Pride ---",
    980
]

# bus_ids = list (range (570, 600))

status = {}
def check_bus (bus_id):
    global status
    try:
        resp = r.get (f"https://winnipegtransit.com/api/v2/trips/schedule?bus_id={bus_id}&live=true").json ()
        if resp.get ("status") == "not_found":
            status [bus_id] = "Not in service"
        else:
            status [bus_id] = resp ["route"] ["id"]
    except Exception as e:
        status [bus_id] = "Error: " + str (e)
    print ("*", end = "", flush = True)

threads = []
for i in bus_ids:
    if type (i) is str:
        continue
    t = threading.Thread (target = check_bus, args = (i, ))
    threads.append (t)
    t.start ()
while threads:
    threads = [t for t in threads if t.is_alive ()]
    time.sleep (0.1)
print ("\nBus\t\tRoute\n" + "\n".join (f"{i}\t\t{status [i]}" if type (i) is not str else i for i in bus_ids))