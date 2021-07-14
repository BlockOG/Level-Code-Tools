import numpy as np
from encoder import decode_string, encode_number, key
import re

def compressV3(code: str, width: int, height: int) -> str:
    export = ""
    amount = width * height
    grid_array = np.array([72] * amount, dtype=int)
    
    for cell in range(len(code)):
        grid_array[cell] = decode_string(code[cell])
    
    num3 = 0
    i = 0
    while i < len(grid_array):
        num4 = 0
        for j in range(1, i+1):
            num6 = 0
            while i + num6 < len(grid_array) and grid_array[i+num6] == grid_array[i+num6-j]:
                num6 += 1
                if num6 > num4:
                    num4 = num6
                    num3 = j - 1
        if num4 > 3:
            if len(encode_number(num4)) == 1:
                if len(encode_number(num3)) == 1:
                    export += ")" + encode_number(num3) + encode_number(num4)
                    i += num4 - 1
                elif num4 > 3 + len(encode_number(num3)):
                    export += "(" + encode_number(num3) + ")" + encode_number(num4)
                    i += num4 -1
                else:
                    export += str(key[grid_array[i]])
            else:
                export += "(" + encode_number(num3) + "(" + encode_number(num4) + ")"
                i += num4 - 1
        else:
            export += str(key[grid_array[i]])
        i += 1
    
    regex1 = r"\{{1,4}$"
    regex2 = r"\{\)0[\da-zA-Z!\$%&\+-\.=\?\^\{\}]$"
    regex3 = r"\{\(0\([\da-zA-Z!\$%&\+-\.=\?\^\{\}]+\)$"
    subst = ""
    
    if re.search(regex1, export):
        export = re.sub(regex1, subst, export, 0)
    elif re.search(regex2, export):
        export = re.sub(regex2, subst, export, 0)
    elif re.search(regex3, export):
        export = re.sub(regex3, subst, export, 0)
    
    
    return export

if __name__ == "__main__":
    try:
        from termcolor import colored
        import colorama
        colorama.init()
    except ModuleNotFoundError:
        def colored(text, _): return text
    
    try:
        print(colored("Paste level code here: ", "green"), end="")
        compress = input()
        list_compress = compress.split(";")
        compress = compressV3(list_compress[3], decode_string(list_compress[1]), decode_string(list_compress[2]))
    except Exception:
        print(colored("ERROR", "red"))
    else:
        print()
        print(colored("Your level code is compressed:", "blue"))
        print("\t" + compress)
        print()