import re
from encoder import encode_number

def compressV3(code):
    code = code[::-1]
    
    lastRepeatingPattern = re.match(r"(.+?)\1{2,}", code)
    
    while lastRepeatingPattern is not None:
        lastRepeatingPattern = re.match(r"(.+?)\1{2,}", code)
        
        code = list(code)
        
        counter = 0
        for i in range(lastRepeatingPattern.span()[0]-1, lastRepeatingPattern.span()[1] - len(lastRepeatingPattern[1])-1):
            code.pop(i - counter)
            counter += 1
        
        if len(lastRepeatingPattern[1]) - 1 > 73:
            if len(lastRepeatingPattern[0]) - len(lastRepeatingPattern[1]) > 73:
                code.insert(lastRepeatingPattern.span()[0], "(")
                code.insert(lastRepeatingPattern.span()[0], encode_number(len(lastRepeatingPattern[1]) - 1))
                code.insert(lastRepeatingPattern.span()[0], "(")
                code.insert(lastRepeatingPattern.span()[0], encode_number(len(lastRepeatingPattern[0]) - len(lastRepeatingPattern[1])))
                code.insert(lastRepeatingPattern.span()[0], ")")
            else:
                code.insert(lastRepeatingPattern.span()[0], "(")
                code.insert(lastRepeatingPattern.span()[0], encode_number(len(lastRepeatingPattern[1]) - 1))
                code.insert(lastRepeatingPattern.span()[0], ")")
                code.insert(lastRepeatingPattern.span()[0], encode_number(len(lastRepeatingPattern[0]) - len(lastRepeatingPattern[1])))
        else:
            code.insert(lastRepeatingPattern.span()[0], ")")
            code.insert(lastRepeatingPattern.span()[0], encode_number(len(lastRepeatingPattern[1]) - 1))
            code.insert(lastRepeatingPattern.span()[0], encode_number(len(lastRepeatingPattern[0]) - len(lastRepeatingPattern[1])))
        
        code = "".join(code)
        
        lastRepeatingPattern = re.match(r"(.+?)\1{2,}", code)
    return code[::-1]