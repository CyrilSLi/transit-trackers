import os
scripts = [
    "winnipeg/winnipeg.py: Winnipeg Transit buses (Winnipeg, MB)",
    "nyc/nyc-m3.py: Long Island Rail Road & Metro-North M3 rail cars (New York, NY)",
    "brandon/brandon.py: Brandon Transit buses (Brandon, MB)",
    "north-dakota/cities-area-transit.py: Cities Area Transit busses (Grand Forks, ND)",
    "north-dakota/matbus.py: MATBUS buses (Fargo, ND)",
    "north-dakota/minot.py: Minot City Transit buses (Minot, ND)",
    "ontario/grt-electric.py: Grand River Transit electric buses (Kitchener-Waterloo, ON)",
    "ontario/oc-d40i-d60lf.py: OC Transpo D40i and D60LF buses (Ottawa, ON)",
    "washington/wenatchee.py: Link Transit buses (Wenatchee, WA)"
]
while True:
    try:
        num = input ("\nNumber\tScript\n" + "\n".join (f"{j}\t{i}" for j, i in enumerate (scripts, 1)) + "\nEnter the number of the script to run: ").strip ()
        if num in (str (i) for i in range (1, len (scripts) + 1)):
            print ()
            exec (open (os.path.join (os.path.dirname (__file__), scripts [int (num) - 1].split (":") [0])).read ())
        else:
            print ("Invalid selection, please try again.")
    except (KeyboardInterrupt, EOFError):
        print () # demo only
    except Exception as e:
        print (f"\nAn error occurred. {e.__class__.__name__}: {e}\n")