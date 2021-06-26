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
        
        return 
        
    else:
        return None

def optimize(levelTypeIndicator, cellarray):
    if levelTypeIndicator = "V1":
        # Optimizing V1 code
        cellarray = re.sub(r"([125-8])\.[0-3](\.\d+\.\d+)", r"\1.0\2", cellarray)
        cellarray = re.sub(r"(4)\.[02](\.\d+\.\d+)", r"\1.0\2", cellarray)
        cellarray = re.sub(r"(4)\.[13](\.\d+\.\d+)", r"\1.1\2", cellarray)
        
        # Returning the cell array
        return cellarray
        
    elif levelTypeIndicator = "V3":
        # Optimizing V3 code
        
        # g  rcw rccw m  s  p  w  e  t
        # 01 23  45   67 89 ab cd ef gh
        # ij kl  mn   op qr st uv wx yz
        # AB CD  EF   GH IJ KL MN OP QR
        # ST UV  WX   YZ !$ %& +- .= ?^
        # + empty
        # } {
        
        # rotator cw
        cellarray = re.sub(r"[kCU]", r"2", cellarray)
        cellarray = re.sub(r"[lDV]", r"3", cellarray)
        
        # rotator ccw
        cellarray = re.sub(r"[mEW]", r"4", cellarray)
        cellarray = re.sub(r"[nFX]", r"5", cellarray)
        
        # slide
        cellarray = re.sub(r"I", r"8", cellarray)
        cellarray = re.sub(r"J", r"9", cellarray)
        cellarray = re.sub(r"!", r"q", cellarray)
        cellarray = re.sub(r"$", r"r", cellarray)
        
        # push
        cellarray = re.sub(r"[sK%]", r"a", cellarray)
        cellarray = re.sub(r"[tL&]", r"b", cellarray)
        
        # wall
        cellarray = re.sub(r"[uM+]", r"c", cellarray)
        cellarray = re.sub(r"[vM-]", r"d", cellarray)
        
        # enemy
        cellarray = re.sub(r"[wO.]", r"e", cellarray)
        cellarray = re.sub(r"[xP=]", r"f", cellarray)
        
        # trash
        cellarray = re.sub(r"[yQ?]", r"g", cellarray)
        cellarray = re.sub(r"[zR^]", r"h", cellarray)
        
        # Returning the cell array
        return cellarray
    

# Accepting an input of the level code
levelcode = input("Paste level code here: ")

# Loading the inputed code
inputData = loadFromInput(levelcode)

if not inputData:
    # ERROR
    print("ERROR")
    
else:
    # Convert to V3 code if V1
    if inputData[0] = "V1":
        inputData = convertV1toV3(inputData)
    
    # Optimize V3 code
    inputData[3] = optimize(inputData[0], inputData[3])
    
    # Compress V3 code
    inputData[3] = compressV3(inputData[3])
    
    # Printing the output
    print("Your level code is optimized:")
    print("   " + ";".join(inputData))
    