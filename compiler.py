# binary => string
def twoComplement(binary):

    aux = ""

    for i in binary:

        if(i == "0"):

            aux += "1"
        
        else:

            aux += "0"

    aux = int(aux, 2)

    aux += 1

    aux = bin(aux).replace("0b", "")

    return aux

# number => int
# instructionType => string
# opcode => string
# pointerLine => int
def signExtension(number, instructionType, opcode, pointerLine):

    # control instruction
    if(instructionType == "00"):

        immediate = number - pointerLine

    # memory or data instruction
    else:

        immediate = number

    binary = bin(abs(immediate)).replace("0b", "")

    binaryLength = len(binary)

    # control instruction
    if(instructionType == "00"):

        conditional = opcode[0]

        # conditional instruction
        if(conditional == "1"):

            extension = "0" * (20 - binaryLength)

            binary = extension + binary

            # PC - direction
            if(immediate < 0):

                binary =  twoComplement(binary)

            return binary
            
        # unconditional instruction
        else:

            extension = "0" * (28 - binaryLength)

            binary = extension + binary

            # PC - direction
            if(immediate < 0):

                binary =  twoComplement(binary)

            return binary            

    # memory instruction
    elif(instructionType == "01"):

        extension = "0" * (18 - binaryLength)

        binary = extension + binary

        # PC - direction
        if(immediate < 0):

            binary =  twoComplement(binary)

        return binary 

    # data instruction
    else:

        flagImmediate = opcode[0]

        # immediate
        if(flagImmediate == "1"):

            extension = "0" * (17 - binaryLength)

            binary = extension + binary

            # PC - direction
            if(immediate < 0):

                binary =  twoComplement(binary)

            return binary


# instructionElements => string list
def riskControlUnit(instructionElements, typeDictionary, opcodeDictionary):

    """
    ['SUM', 'R1', 'R2', 'R3']
    ['RES', 'R4', 'R1', 'R2']

    ['SUM', 'R1', 'R2', 'R3']
    ['RES', 'R4', 'R2', 'R1']

    -------------------------
    ['MUL', 'R1', 'R2', 'R3']
    ['DIV', 'R1', 'R2', 'R3']



    ['CRG', 'R1', '2', '4', 'R2']
    ['GDR', 'R2', '1', '4', 'R1']
    




    ['SCI', 'R1', 'R2', 'elif']
    ['SCD', 'R1', 'R2', 'ciclo']














    ['SCI', 'R1', 'R2', 'elif']
    ['SCD', 'R1', 'R2', 'ciclo']
    ['SI', 'for_loop']
    ['SIF', 'check']

    ['GDR', 'R1', '1', '4', 'R3']
    ['CRG', 'R1', '2', '4', 'R3']

    ['SUM', 'R1', 'R2', 'R3']
    ['RES', 'R1', 'R2', 'R3']
    ['MUL', 'R1', 'R2', 'R3']
    ['DIV', 'R1', 'R2', 'R3']
    ['RSD', 'R1', 'R2', 'R3']

    ['SUMI', 'R1', 'R2', '1']
    ['RESI', 'R1', 'R2', '-2']
    ['MULI', 'R1', 'R2', '3']
    ['DIVI', 'R1', 'R2', '-4']
    ['RSDI', 'R1', 'R2', '5']













# case 2: dependencies between instructions with 1 instruction among them

# case 3: dependencies between instructions with 2 instructions among them







    """

    result = instructionElements.copy()

    instructionElementsLength = len(instructionElements)

    stall = ['SUM', 'R0', 'R0', 'R0']

    # loop to iterate each instruction
    for i in range(instructionElementsLength):

        currentInstructionElements = instructionElements[i]

        currentInstruction = currentInstructionElements[0]

        currentInstructionType = typeDictionary[currentInstruction]

        currentDestiny = currentInstructionElements[1]            

        # case 1: dependencies between instructions with 0 instructions among them

        nextInstructionElements = instructionElements[i + 1]
        
        nextInstruction = nextInstructionElements[0]

        nextInstructionType = typeDictionary[nextInstruction]

        # control instruction
        if(currentInstructionType == "00"):
            
            # control instruction
            if(nextInstructionType == "00"):
                pass
                




            # memory instruction
            elif(nextInstructionType == "01"):
                pass




            # data instruction
            else:
                pass









        # memory instruction
        elif(currentInstructionType == "01" and currentInstruction == "CRG"):            

            # control instruction
            if(nextInstructionType == "00"):

                nextOpcode = opcodeDictionary[nextInstruction]

                nextBranch = nextOpcode[0]

                # conditional instruction
                if(nextBranch == "1"):

                    nextSource1 = nextInstructionElements[1]
                    nextSource2 = nextInstructionElements[2]

                    if(currentDestiny == nextSource1 or currentDestiny == nextSource2):

                        result.insert(i + 1, stall)
                        result.insert(i + 2, stall)
                        result.insert(i + 3, stall)

            # data instruction
            elif(nextInstructionType == "10"):

                nextSource2 = nextInstructionElements[2]
                nextSource3 = nextInstructionElements[3]

                if(currentDestiny == nextSource2 or currentDestiny == nextSource3):

                    result.insert(i + 1, stall)
                    result.insert(i + 2, stall)
                    result.insert(i + 3, stall)





        # data instruction
        else:
            
            # control instruction
            if(nextInstructionType == "00"):

                nextOpcode = opcodeDictionary[nextInstruction]

                nextBranch = nextOpcode[0]

                # conditional instruction
                if(nextBranch == "1"):

                    nextSource1 = nextInstructionElements[1]
                    nextSource2 = nextInstructionElements[2]

                    if(currentDestiny == nextSource1 or currentDestiny == nextSource2):

                        result.insert(i + 1, stall)
                        result.insert(i + 2, stall)
                        result.insert(i + 3, stall)
                
            # memory instruction
            elif(nextInstructionType == "01"):

                nextOpcode = opcodeDictionary[nextInstruction]

                nextIns = nextOpcode[0]
                
                # GRD instruction
                if(nextIns == "0"):

                    nextSource = nextInstructionElements[1]

                    if(currentDestiny == nextSource):

                        result.insert(i + 1, stall)
                        result.insert(i + 2, stall)
                        result.insert(i + 3, stall)
                
                # CRG instruction
                else:

                    nextSource = nextInstructionElements[4]

                    if(currentDestiny == nextSource):

                        result.insert(i + 1, stall)
                        result.insert(i + 2, stall)
                        result.insert(i + 3, stall)

            # data instruction
            else:

                nextSource2 = nextInstructionElements[2]
                nextSource3 = nextInstructionElements[3]

                if(currentDestiny == nextSource2 or currentDestiny == nextSource3):

                    result.insert(i + 1, stall)
                    result.insert(i + 2, stall)
                    result.insert(i + 3, stall)



            

            
            
        break    















































    return result














# type dictionary definition
typeDictionary = {
    "SCI": "00",
    "SCD": "00",
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

# opcode dictionary definition
opcodeDictionary = {
    "SCI": "10",
    "SCD": "11",
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

# register dictionary definition
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

# label dictionary definition
labelDictionary = {}

# open code.txt file for reading
codeFile = open('code.txt', 'r')
codeLines = codeFile.readlines()

# variable to know the number of the current line
pointerLine = 0

# loop to iterate the code file line by line
for line in codeLines:

    pointerLine += 1

    # slicing the current line to get the last element
    aux = line[-2]

    # current line contains a label
    if(aux == ":"):

        pointerLine -= 1

        labelDictionary[line[:-2]] = pointerLine + 1
        
codeFile.close()

# open code.txt file for reading
codeFile = open('code.txt', 'r')
codeLines = codeFile.readlines()

# open binaryCode.txt file for writing
binaryCodeFile = open('binaryCode.txt', 'w')

# variable to know the number of the current line
pointerLine = 0

# variable to store all the instruction elements
instructionElements = []

# loop to iterate the code file line by line
for line in codeLines:
    
    # variable to know if the current instruction is a memory one (type 01)
    memoryFlag = 0   

    elements = []
    temp = ""

    # slicing the current line to get the last element
    aux = line[-2]

    # current line contains an instruction
    if(aux != ":"):

        pointerLine += 1

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

        instructionElements.append(elements)

        instructionType = typeDictionary[elements[0]]
        opcode = opcodeDictionary[elements[0]]

        filling = "0000000000000"

        # control instruction
        if(instructionType == "00"):

            conditional = opcode[0]

            # conditional instruction
            if(conditional == "1"):

                register1 = registerDictionary[elements[1]]
                register2 = registerDictionary[elements[2]]

                direction = elements[3]
                direction = labelDictionary[direction]
                direction = signExtension(direction, instructionType, opcode, pointerLine)

                instruction = instructionType + opcode + register1 + register2 + direction

                print(instructionType + " " + opcode + " " + register1 + " " + register2 + " " + direction)

            # unconditional instruction
            else:
                direction = elements[1]
                direction = labelDictionary[direction]
                direction = signExtension(direction, instructionType, opcode, pointerLine)

                instruction = instructionType + opcode + direction

                print(instructionType + " " + opcode + " " + direction)

        # memory instruction
        elif(instructionType == "01"):

            register1 = registerDictionary[elements[1]]

            section = bin(int(elements[2])).replace("0b", "")

            sectionLength = len(section)

            # sign extension for section value
            for i in range(3 - sectionLength):
                section = "0" + section

            immediate = int(elements[3])
            immediate = signExtension(immediate, instructionType, opcode, pointerLine)

            register2 = registerDictionary[elements[4]]       

            instruction = instructionType + opcode + section + register1 + register2 + immediate

            print(instructionType + " " + opcode + " " + section + " " + register1 + " " + register2 + " " + immediate)

        # data instruction
        else:

            flagImmediate = opcode[0]

            # immediate
            if(flagImmediate == "1"):

                register1 = registerDictionary[elements[1]]
                register2 = registerDictionary[elements[2]]
                
                immediate = int(elements[3])
                immediate = signExtension(immediate, instructionType, opcode, pointerLine)

                instruction = instructionType + opcode + register1 + register2 + immediate

                print(instructionType + " " + opcode + " " + register1 + " " + register2 + " " + immediate)

            # no immediate
            else:

                register1 = registerDictionary[elements[1]]
                register2 = registerDictionary[elements[2]]
                register3 = registerDictionary[elements[3]]

                instruction = instructionType + opcode + filling + register1 + register2 + register3

                print(instructionType + " " + opcode + " " + filling + " " + register1 + " " + register2 + " " + register3)

        #print(instruction + "\n")
        print(" ")

        binaryCodeFile.write(instruction + "\n")




"""
for i in instructionElements:
    print(i)
print(" ")
"""



instructionElements = riskControlUnit(instructionElements, typeDictionary, opcodeDictionary)

for i in instructionElements:
    print(i)
print(" ")










"""
lista = [1,2,3,4,5]

lista1 = lista.copy()

lista1.insert(2, "J")

print(" ")
print(lista)
print(lista1)
"""

# closing binaryCodeFile and codeFile files
binaryCodeFile.close()
codeFile.close()




























