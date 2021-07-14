import re
from encoder import decode_string

def loadFromInput(inp):
    
    if re.search(r"V1;\d+;\d+;(\d\.\d,)*(\d\.\d)?;([0-8]\.[0-3]\.\d+\.\d+,)*([0-8]\.[0-3]\.\d+\.\d+)?;[\w\d]*;", inp):
        inp = inp.split(";")
        
        return inp
        
    elif re.search(r"V3;([\da-zA-Z!$%&+-.=?^{}\(\)]+;){2}[\da-zA-Z!$%&+-.=?^{}\(\)]*;[\w\s-]*;", inp):
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
        
        return inp
        
    else:
        return None