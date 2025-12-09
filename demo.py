from runpy import run_path
import os
scripts = [
    "winnipeg.py: Winnipeg Transit busses",
    "nyc-m3.py: Long Island Rail Road & Metro-North M3 rail cars",
    "brandon.py: Brandon Transit busses"
]
while True:
    try:
        num = input ("\nNumber\tScript\n" + "\n".join (f"{j}\t{i}" for j, i in enumerate (scripts, 1)) + "\nEnter the number of the script to run: ").strip ()
        if num in (str (i) for i in range (1, len (scripts) + 1)):
            print ()
            run_path (os.path.join (os.path.dirname (__file__), scripts [int (num) - 1].split (":") [0]))
        else:
            print ("Invalid selection, please try again.")
    except (KeyboardInterrupt, EOFError):
        print () # demo only
    except Exception as e:
        print (f"\nAn error occurred. {e.__class__.__name__}: {e}\n")