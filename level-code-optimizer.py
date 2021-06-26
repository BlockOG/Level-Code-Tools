import sys
import re
from encoder import decode_string, decode_dict, encode_number

levelcode = sys.argv[1]

if re.match(r"V1;\d+;\d+;[\w\d]*;([0-8]\.[0-3]\.\d+\.\d+,)*([0-8]\.[0-3]\.\d+\.\d+)?;[\w\d]*;", levelcode):
    levelcode = levelcode.split(";")
    
    levelcode[4] = re.sub(r"([5-8])\.[0-3](\.\d+\.\d+)", r"\1.0\2", levelcode[4])
    levelcode[4] = re.sub(r"(4)\.[02](\.\d+\.\d+)", r"\1.0\2", levelcode[4])
    levelcode[4] = re.sub(r"(4)\.[13](\.\d+\.\d+)", r"\1.1\2", levelcode[4])
    
    print("Your level code is optimized:")
    print("   " + ";".join(levelcode))

elif levelcode[:3] == "V3;":
    levelcode = levelcode.split(";")
    cellcode = levelcode[3]
    long = ""
    i = 0
    while i < len(cellcode):
        if cellcode[i] == ")" or cellcode[i] == "(":
            offset = ""
            distance = ""
            if cellcode[i] == ")":
                i += 1
                offset = cellcode[i]
                i += 1
                distance = cellcode[i]
            else:
                i += 1
                while not (cellcode[i] == ")" or cellcode[i] == "("):
                    offset += cellcode[i]
                    i += 1
                if cellcode[i] == ")":
                    i += 1
                    distance = cellcode[i]
                else:
                    i += 1
                    while cellcode[i] != ")":
                        distance += cellcode[i]
                        i += 1
            offset = decode_string(offset)
            distance = decode_string(distance)
            for j in range(distance):
                long += long[-(offset + 1)]
        else:
            long += cellcode[i]
        i += 1

    longmin = ""
    for char in long:
        if char == "{" or char == "}":
            longmin += char
            continue
        celltype = decode_dict[char] % 18 // 2
        if celltype == 0 or celltype == 3 or celltype == 4:
            longmin += char
            continue
        longmin += encode_number(decode_dict[char] % 18)

    print(longmin)

    # TODO re-compress the level string

else:
    print("Invalid Level Code (If It's A V2 Code It's Not Supported Yet)")