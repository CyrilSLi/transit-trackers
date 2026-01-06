import csv, json, math, os, re, sys
from winnipeg import compress_time

if not os.path.isdir (sys.argv [1]):
    raise SystemExit ("Usage: python get_runs.py <gtfs_directory>")

start_end_times = {}
with open (os.path.join (sys.argv [1], "stop_times.txt")) as f:
    for row in csv.DictReader (f):
        trip = start_end_times.setdefault (row ["trip_id"], [None, math.inf, None, -1])
        stop_sequence = int (row ["stop_sequence"])
        if stop_sequence < trip [1]:
            trip [0], trip [1] = row ["arrival_time"], stop_sequence
        if stop_sequence > trip [3]:
            trip [2], trip [3] = row ["arrival_time"], stop_sequence

trip_runs = {}
end_times = {}
with open (os.path.join (sys.argv [1], "trips.txt")) as f:
    for row in csv.DictReader (f):
        if row ["trip_id"] not in start_end_times:
            continue
        start_time, end_time = start_end_times [row ["trip_id"]] [0], start_end_times [row ["trip_id"]] [2]
        trip_runs [f'{row ["service_id"]}{row ["route_id"]}{compress_time (start_time, end_time)}'] = row ["block_id"]
        run_end_time = end_times.setdefault (row ["block_id"], "0")
        if run_end_time < end_time:
            end_times [row ["block_id"]] = end_time

for trip in trip_runs:
    trip_runs [trip] = trip_runs [trip] + " " + compress_time (end_times [trip_runs [trip]])

with open (os.path.join (os.path.dirname (__file__), "winnipeg.py")) as f:
    file = f.read ()
file = re.sub (r"(trip_runs ?= ?){[\S\s]+?}", "\\g<1>" + json.dumps (trip_runs, separators = (",\n", ":"), sort_keys = True), file)
with open (os.path.join (os.path.dirname (__file__), "winnipeg.py"), "w") as f:
    f.write (file)