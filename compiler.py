# dictionary definitions
typeDictionary = {
    "SCI": "00",
    "SCM": "00",
    "SI": "00",
    "SIF": "00",

    "GDR": "01",
    "CRG": "01",

    "SUM": "10",
    "RES": "10",
    "MUL": "10",
    "DIV": "10",
    "RSD": "10",
    "SUMI": "10",
    "RESI": "10",
    "MULI": "10",
    "DIVI": "10",
    "RSDI": "10"
}

opcodeDictionary = {
    "SCI": "10",
    "SCM": "11",
    "SI": "00",
    "SIF": "01",

    "GDR": "0",
    "CRG": "1",

    "SUM": "00000",
    "RES": "00001",
    "MUL": "00010",
    "DIV": "00011",
    "RSD": "00100",    
    "SUMI": "11000",
    "RESI": "11001",
    "MULI": "11010",
    "DIVI": "11011",
    "RSDI": "11100"
}

registerDictionary = {
    "R0": "0000",
    "R1": "0001",
    "R2": "0010",
    "R3": "0011",
    "R4": "0100",
    "R5": "0101",
    "R6": "0110",
    "R7": "0111",
    "R8": "1000",
    "R9": "1001",
    "R10": "1010",
    "R11": "1011",
    "R12": "1100",
    "R13": "1101",
    "RR": "1110",
    "RS": "1111"
}

# open code.txt file for reading
codeFile = open('code.txt', 'r')
codeLines = codeFile.readlines()

# variable to know tue number of the current line
pointerLine = -1

# loop to iterate the code file line by line
for line in codeLines:

    pointerLine += 1
    
    # variable to know if the current instruction is a memory one (type 01)
    memoryFlag = 0   

    elements = []
    temp = ""
    
    # loop to iterate the current line char by char
    for char in line:

        if(char == " " or char == "," or char == "(" or char == ")"):

            # check if the current instruction is a memory one to change the flag
            if(char == "("):
                memoryFlag = 1

            if(temp != ""):
                elements.append(temp)

            temp = ""            

        else:

            temp += char

    # slice \n from the last element
    temp = temp[:-1]

    elements.append(temp)    
    
    # remove last element if the current instruction is a memory one
    if(memoryFlag == 1):
        elements.pop()

    print("elements = ", elements)   

    instructionType = typeDictionary[elements[0]]
    opcode = opcodeDictionary[elements[0]]

    register1 = ""
    register2 = ""
    register3 = ""
    direction = ""
    immediate = ""
    filling = "0000000000000"

    # control instruction
    if(instructionType == "00"):

        branch = opcode[0]

        # conditional instruction
        if(branch == "1"):

            register1 = registerDictionary[elements[1]]
            register2 = registerDictionary[elements[2]]
            direction = elements[3]

            instruction = instructionType + " " + opcode + " " + register1 + " " + register2 + " " + register3 + direction

        # unconditional instruction
        else:

            direction = elements[1]

            instruction = instructionType + " " + opcode + " " + direction

    # memory instruction
    elif(instructionType == "01"):

        register1 = registerDictionary[elements[1]]
        immediate = elements[2]
        register2 = registerDictionary[elements[3]]       

        instruction = instructionType + " " + opcode + " " + register1 + " " + register2 + " " + immediate

    # data instruction
    else:

        i = opcode[0]

        # immediate
        if(i == "1"):

            register1 = registerDictionary[elements[1]]
            register2 = registerDictionary[elements[2]]
            immediate = elements[3]

            instruction = instructionType + " " + opcode + " " + register1 + " " + register2 + " " + immediate

        # no immediate
        else:

            register1 = registerDictionary[elements[1]]
            register2 = registerDictionary[elements[2]]
            register3 = registerDictionary[elements[3]]

            instruction = instructionType + " " + opcode + " " + filling + " " + register1 + " " + register2 + " " + register3



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    print(instruction + "\n")
    
    
    
    
    
    
    
  
    
    



    






codeFile.close()









