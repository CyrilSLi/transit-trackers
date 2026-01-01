import requests as r, time, threading

bus_ids = [
    "--- XHE40 & XHE60 ---",
    284, 285, 286, 287, 292, 293, 294, 295,
    "--- XE40 & XE60 ---",
    288, 289, 290, 291, 296, 297, 298, 299,
    "--- 500s NOT PHOTOGRAPHED ---",
    588, 590,
    # "--- 500s Retired? ---",
    # 570, 573, 574, 575, 576, 578, 580, 581, 583, 584, 585, 587, 589, 591, 593, 595, 596, 599,
    "--- Photographed 500s ---",
    571, 572, 577, 579, 582, 586, 592, 594, 597,
    "--- Pride ---",
    980
]

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