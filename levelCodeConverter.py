import numpy as np
from loadCode import loadFromInput
from encoder import encode_number
from compressV3 import compressV3

main = True

def convertV1toV3(V1):
    global main
    if __name__ != "__main__": main = False
    
    if main:
        V1 = loadFromInput(V1)
    
    V1[3] = V1[3].split(",")
    for i in range(len(V1[3])):
        V1[3][i] = V1[3][i].split(".")
    
    V1[4] = V1[4].split(",")
    for i in range(len(V1[4])):
        V1[4][i] = V1[4][i].split(".")
    
    grid_array = np.array([72] * (int(V1[1]) * int(V1[2])), dtype=int)
    grid_string = ""
    
    try:
        if len(V1[3][0][0]) != 0 :
            for i in V1[3]:
                grid_array[int(i[0]) + int(i[1]) * int(V1[2])] += 1
    except IndexError:
        print(colored("Somehow, some placeable background is outside your grid", "red"))
    
    try:
        if len(V1[4][0][0]) != 0 :
            for i in V1[4]:
                grid_array[int(i[2]) + int(i[3]) * int(V1[2])] += 2 * int(i[0]) + 18 * int(i[1]) - 72
    except IndexError:
        print(colored("Somehow, a block is outside your grid", "red"))
    
    for i in grid_array:
        grid_string += encode_number(i)
    
    V3 = []
    
    V3.append("V3")
    V3.append(encode_number(int(V1[1])))
    V3.append(encode_number(int(V1[2])))
    if main:
        V3.append(compressV3(grid_string, int(V1[1]), int(V1[2])))
    else:
        V3.append(grid_string)
    V3.append(V1[5])
    V3.append(V1[6])
    
    
    if main:
        return ";".join(V3) + ";"
    else:
        return V3

if __name__ == '__main__':
    try:
        from termcolor import colored
        import colorama
        colorama.init()
    except ModuleNotFoundError:
        def colored(text, _): return text
    
    print(colored("Paste level code here: ", "green"), end="")
    convert = convertV1toV3(input())
    
    print()
    print(colored("Your level code is converted:", "blue"))
    print("\t" + convert)
    print()