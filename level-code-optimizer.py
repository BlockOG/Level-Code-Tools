import sys
import re

levelcode = sys.argv[1]

if re.match(r"V1;\d+;\d+;[\w\d]*;([0-8]\.[0-3]\.\d+\.\d+,)*([0-8]\.[0-3]\.\d+\.\d+)?;[\w\d]*;", levelcode):
    levelcode = levelcode.split(";")
    
    levelcode[4] = re.sub(r"([5-8])\.[0-3](\.\d+\.\d+)", r"\1.0\2", levelcode[4])
    levelcode[4] = re.sub(r"(4)\.[02](\.\d+\.\d+)", r"\1.0\2", levelcode[4])
    levelcode[4] = re.sub(r"(4)\.[13](\.\d+\.\d+)", r"\1.1\2", levelcode[4])
    
    print("Your level code is optimized:")
    print("   " + ";".join(levelcode))
else:
    print("Invalid Level Code (If It's A V3 Code It's Not Supported Yet)")