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

if __name__ == "__main__":
    print("1) Decoder")
    print("2) Encoder")
    inp = input("Choose: ")
    if inp == "1":
        print("Decoder chosen")
        string = input("Write/paste string here: ")
        string_dec = decode_string(string)
        print("String decoded")
        print(f"The original string is {string}")
        print(f"The decoded number is {string_dec}")
    elif inp == "2":
        print("Encoder chosen")
        number = input("Write/paste number here: ")
        number_enc = encode_number(int(number))
        print("Number encoded")
        print(f"The original number is {number}")
        print(f"The encoded string is {number_enc}")
    else:
        print("You have chosen something that's not in the options!")
