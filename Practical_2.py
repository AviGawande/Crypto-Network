def ANDOperation(s:str):
    return[(ord(i) & 127) for i in s]
def OROperation(s:str):
    return[(ord(i) | 127) for i in s]
def XOROperation(s:str):
    return[(ord(i) ^ 127) for i in s]
if __name__ == "__main__":
    input_string = "Hello World"
    print("AND: ", ANDOperation(input_string),"Characters: ","".join(chr(i) for i in ANDOperation(input_string)))
    print("OR: ", OROperation(input_string),"Characters: ","".join(chr(i) for i in OROperation(input_string)))
    print("/XOR: ", XOROperation(input_string),"Characters: ","".join(chr(i) for i in XOROperation(input_string)))