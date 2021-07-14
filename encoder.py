key = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!$%&+-.=?^{}"

encode_tuple = tuple(list(key))

decode_dict = {}
for i in range(74):
    decode_dict[key[i]] = i

def decode_string(char_string):
    global decode_dict
    result = 0
    for char in char_string:
        result *= 74
        result = result + decode_dict[char]
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
    try:
        import PySimpleGUI as sg
    except ModuleNotFoundError:
        try:
            from termcolor import colored
            import colorama
            colorama.init()
        except ModuleNotFoundError:
            def colored(text, _): return text
        
        print(colored("1)", "white"), colored("Decoder", "blue"))
        print(colored("2)", "white"), colored("Encoder", "cyan"))
        print(colored("3)", "white"), colored("Exit", "red"))
        inp = input(colored("Choose: ", "yellow"))
        if inp == "1":
            print(colored("Decoder", "blue"), colored("chosen\n", "yellow"))
            
            string = input("Write/paste string here: ")
            string_dec = decode_string(string)
            print("String decoded")
            print(f"The original string is {string}")
            print(f"The decoded number is {string_dec}\n")
            
        elif inp == "2":
            print(colored("Encoder", "cyan"), colored("chosen\n", "yellow"))
            
            number = input("Write/paste number here: ")
            number_enc = encode_number(int(number))
            print("Number encoded")
            print(f"The original number is {number}")
            print(f"The encoded string is {number_enc}\n")
            
        elif inp == "3": pass
        else:
            print("You have chosen something that's not in the options!")
    else:
        layout = [[sg.Input(key="-DECODER IN-"), sg.Button("Decode", key="-DECODE-")],
                  [sg.Input(key="-ENCODER IN-"), sg.Button("Encode", key="-ENCODE-")],
                  [sg.Exit()]]
        
        window = sg.Window("Encoder/Decoder", layout)
        
        while True:
            event, values = window.read()
            
            if event == sg.WIN_CLOSED or event == "Exit":
                break
            
            if event == "-DECODE-":
                window["-ENCODER IN-"].update(decode_string(values["-DECODER IN-"]))
            
            if event == "-ENCODE-":
                window["-DECODER IN-"].update(encode_number(int(values["-ENCODER IN-"])))
        
        window.close()
