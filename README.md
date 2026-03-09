# transit-trackers

Small Python scripts to track interesting transit vehicles by fleet number

## Installation

Use on any Python environment with the standard library and `requests`.

**Note**: `oc-d40i-d60lf.py` and `grt-electric.py` require the `gtfs-realtime-bindings` library and the former also requires an OC Transpo GTFS-realtime API key.

These scripts are designed to run on mobile devices with a Python interpreter app ([example on iOS](https://apps.apple.com/app/id1397406775)) to track vehicles on the go.

## List of Scripts/Cities

- `winnipeg/winnipeg.py`: Winnipeg Transit buses (Winnipeg, MB)
  - Edit the `bus_ids` list with the fleet numbers to track, add section dividers with strings (see existing format in the file)
- `nyc/nyc-m3.py`: Long Island Rail Road & Metro-North M3 rail cars (New York, NY)
- `brandon/brandon.py`: Brandon Transit buses (Brandon, MB)
- `north-dakota/cities-area-transit.py`: Cities Area Transit busses (Grand Forks, ND)
- `north-dakota/matbus.py`: MATBUS buses (Fargo, ND)
- `north-dakota/minot.py`: Minot City Transit buses (Minot, ND)
- `ontario/grt-electric.py`: Grand River Transit electric buses (Kitchener-Waterloo, ON)
- `ontario/oc-d40i-d60lf.py`: OC Transpo D40i and D60LF buses (Ottawa, ON)
- `washington/wenatchee.py`: Link Transit buses (Wenatchee, WA)

## Demo

Run `demo.py` to quickly see the output of all scripts in one place.