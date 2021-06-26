import re
from encoder import decode_string
from compressV3 import compressV3
from levelCodeConverter import convertV1toV3

def loadFromInput(inp):
    
    if re.match(r"V1;\d+;\d+;(\d\.\d,)*(\d\.\d)?;([0-8]\.[0-3]\.\d+\.\d+,)*([0-8]\.[0-3]\.\d+\.\d+)?;[\w\d]*;", inp):
        inp = inp.split(";")
        
        return inp
        
    elif re.match(r"V3;([\da-zA-Z!$%&+-.=?^{}\(\)]+;){2}[\da-zA-Z!$%&+-.=?^{}\(\)]*;[\w\s-]*;", inp):
        inp = inp.split(";")
        
        level_cells = ""
        data_index = 0  # iterate through data optimally without re-slicing it every step
        data = inp[3]
        
        while data_index < len(data):
            if data[data_index] == "(" or data[data_index] == ")":
                if data[data_index] == ")":
                    offset = data[data_index + 1]
                    distance = data[data_index + 2]
                    data_index += 3
                
                else:
                    offset = ""
                    data_index += 1
                    while data[data_index] != "(" and data[data_index] != ")":
                        offset += data[data_index]
                        data_index += 1
                    if data[data_index] == ")":
                        distance = data[data_index + 1]
                        data_index += 2
                    else:
                        distance = ""
                        data_index += 1
                        while data[data_index] != ")":
                            distance += data[data_index]
                            data_index += 1
                        data_index += 1
                
                
                for d in range(decode_string(distance)):
                    level_cells += level_cells[-decode_string(offset) - 1]
            
            else:
                level_cells += data[data_index]
                data_index += 1
        
        
        inp[3] = level_cells
        
        lastRepeatingPattern = compressV3(inp[3])
        
        print("lastRepeatingPattern", lastRepeatingPattern)
        
        
        
    else:
        return None

def optimize(cellarray):
    
    # g  rcw rccw m  s  p  w  e  t
    # 01 23  45   67 89 ab cd ef gh
    # ij kl  mn   op qr st uv wx yz
    # AB CD  EF   GH IJ KL MN OP QR
    # ST UV  WX   YZ !$ %& +- .= ?^
    # + empty
    # { }
    
    
    cellarray = re.sub(r"[wO.]", r"e", cellarray)
    cellarray = re.sub(r"[xP=]", r"f", cellarray)

    cellarray = re.sub(r"[yQ?]", r"g", cellarray)
    cellarray = re.sub(r"[yQ?]", r"g", cellarray)

    cellarray = re.sub(r"[wO.]", r"e", cellarray)
    cellarray = re.sub(r"[xP=]", r"f", cellarray)

    cellarray = re.sub(r"[yQ?]", r"g", cellarray)
    cellarray = re.sub(r"[zR^]", r"h", cellarray)
    
    # cellarray = re.sub(r"([125-8])\.[0-3](\.\d+\.\d+)", r"\1.0\2", cellarray)
    # cellarray = re.sub(r"(4)\.[02](\.\d+\.\d+)", r"\1.0\2", cellarray)
    # cellarray = re.sub(r"(4)\.[13](\.\d+\.\d+)", r"\1.1\2", cellarray)
    
    return cellarray
    

levelcode = input("Paste level code here: ")
inputData = loadFromInput(levelcode)

if not inputData:
    print("ERROR")
    
else:
    inputData = convertV1toV3(inputData)
    
    
    print("Your level code is optimized:")
    print("   " + ";".join(inputData))
    