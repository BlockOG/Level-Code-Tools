key = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&+-.=?^{}"

encode_tuple = tuple(list(key))

decode_dict = {}
for i in range(74):
    decode_dict[key[i]] = i


def decode_string(char_string):
    result = 0
    for char in char_string:
        result *= 74
        result += decode_dict[char]
    return result

def encode_number(num):
    if num == 0: return "0"
    
    result = ""
    counter = 0
    
    while num >= (74 ** counter):
        result += key[num // (74 ** counter) % 74]
        counter += 1
    
    return result[::-1]