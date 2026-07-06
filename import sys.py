import sys

if sys.byteorder == "little":
    print("System uses Little Endian format.")
else:
    print("System uses Big Endian format.")