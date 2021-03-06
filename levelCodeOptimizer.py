import re
from encoder import decode_string
from compressV3 import compressV3
from levelCodeConverter import convertV1toV3
from loadCode import loadFromInput

def optimize(cellarray):
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
    cellarray = re.sub(r"\$", r"r", cellarray)
    
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

try:
    from termcolor import colored
    import colorama
    colorama.init()
except ModuleNotFoundError:
    def colored(text, _): return text

# Accepting an input of the level code
print(colored("Paste level code here: ", "green"), end="")
levelcode = input()

# Loading the inputed code
inputData = loadFromInput(levelcode)

if not inputData:
    # ERROR
    print()
    print(colored("ERROR", "red"))
    print()
    
elif inputData == "V2":
    print()
    print(colored("Come on, it was said V2 doesn't work", "yellow"))
    print()
    
else:
    # Convert to V3 code if V1
    if inputData[0] == "V1":
        inputData = convertV1toV3(inputData)
    
    # Optimize V3 code
    inputData[3] = optimize(inputData[3])
    
    # Compress V3 code
    inputData[3] = compressV3(inputData[3], decode_string(inputData[1]), decode_string(inputData[2]))
    
    # Printing the output
    print()
    print(colored("Your level code is optimized:", "blue"))
    print("\t" + ";".join(inputData))
    print()
    
