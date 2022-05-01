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

# case 1: dependencies between instructions with 0 instructions among them
# instructionElements => string list
# typeDictionary => string dictionary
# opcodeDictionary => string dictionary
def stallInsertionCase1(instructionElements, typeDictionary, opcodeDictionary):

    result = instructionElements.copy()

    # this insertion avoids index out of range error
    result.append("*")

    stall = ['SUM', 'R0', 'R0', 'R0', "********************"]

    i = 0

    # loop to iterate each instruction
    for j in result:

        if(len(j) > 1):

            if(result[i + 1] == "*" or result[i + 2] == "*"):
                break

            currentInstruction = j[0]

            currentInstructionType = typeDictionary[currentInstruction]

            currentDestiny = j[1]

            if(currentDestiny != "R0"):

                # instruction
                if(len(result[i + 1]) > 1):

                    nextInstructionElements = result[i + 1]

                # label
                else:

                    nextInstructionElements = result[i + 2]

                nextInstruction = nextInstructionElements[0]

                nextInstructionType = typeDictionary[nextInstruction]           

                # control instruction
                if(currentInstructionType == "00"):

                    result.insert(i + 1, stall)
                    result.insert(i + 2, stall)
                    result.insert(i + 3, stall)
                    result.insert(i + 4, stall)
                    
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

        i += 1

    return result[:-1]

# case 2: dependencies between instructions with 1 instruction among them
# instructionElements => string list
# typeDictionary => string dictionary
# opcodeDictionary => string dictionary
def stallInsertionCase2(instructionElements, typeDictionary, opcodeDictionary):

    result = instructionElements.copy()

    # this insertion avoids index out of range error
    result.append("*")

    stall = ['SUM', 'R0', 'R0', 'R0', "********************"]

    i = 0

    # loop to iterate each instruction
    for j in result:

        if(len(j) > 1):

            if(result[i + 2] == "*" or result[i + 3] == "*"):
                break

            currentInstruction = j[0]

            currentInstructionType = typeDictionary[currentInstruction]

            currentDestiny = j[1]

            if(currentDestiny != "R0"):

                # instruction
                if(len(result[i + 2]) > 1):

                    nextInstructionElements = result[i + 2]

                # label
                else:

                    nextInstructionElements = result[i + 3]

                nextInstruction = nextInstructionElements[0]

                nextInstructionType = typeDictionary[nextInstruction]           
                    
                # memory instruction
                if(currentInstructionType == "01" and currentInstruction == "CRG"):            
                    
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
                    
                    # data instruction
                    elif(nextInstructionType == "10"):

                        nextSource2 = nextInstructionElements[2]
                        nextSource3 = nextInstructionElements[3]

                        if(currentDestiny == nextSource2 or currentDestiny == nextSource3):

                            result.insert(i + 1, stall)
                            result.insert(i + 2, stall)

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
                        
                        # CRG instruction
                        else:

                            nextSource = nextInstructionElements[4]

                            if(currentDestiny == nextSource):

                                result.insert(i + 1, stall)
                                result.insert(i + 2, stall)

                    # data instruction
                    else:

                        nextSource2 = nextInstructionElements[2]
                        nextSource3 = nextInstructionElements[3]

                        if(currentDestiny == nextSource2 or currentDestiny == nextSource3):

                            result.insert(i + 1, stall)
                            result.insert(i + 2, stall)

        i += 1

    return result[:-1]

# case 3: dependencies between instructions with 2 instructions among them
# instructionElements => string list
# typeDictionary => string dictionary
# opcodeDictionary => string dictionary
def stallInsertionCase3(instructionElements, typeDictionary, opcodeDictionary):

    result = instructionElements.copy()

    # this insertion avoids index out of range error
    result.append("*")

    stall = ['SUM', 'R0', 'R0', 'R0', "********************"]

    i = 0

    # loop to iterate each instruction
    for j in result:

        if(len(j) > 1):

            if(result[i + 3] == "*" or result[i + 4] == "*"):
                break

            currentInstruction = j[0]

            currentInstructionType = typeDictionary[currentInstruction]

            currentDestiny = j[1]

            if(currentDestiny != "R0"):

                # instruction
                if(len(result[i + 3]) > 1):

                    nextInstructionElements = result[i + 3]

                # label
                else:

                    nextInstructionElements = result[i + 4]

                nextInstruction = nextInstructionElements[0]

                nextInstructionType = typeDictionary[nextInstruction]           
                    
                # memory instruction
                if(currentInstructionType == "01" and currentInstruction == "CRG"):            
                    
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
                    
                    # data instruction
                    elif(nextInstructionType == "10"):

                        nextSource2 = nextInstructionElements[2]
                        nextSource3 = nextInstructionElements[3]

                        if(currentDestiny == nextSource2 or currentDestiny == nextSource3):

                            result.insert(i + 1, stall)

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

                    # memory instruction
                    elif(nextInstructionType == "01"):

                        nextOpcode = opcodeDictionary[nextInstruction]

                        nextIns = nextOpcode[0]
                        
                        # GRD instruction
                        if(nextIns == "0"):

                            nextSource = nextInstructionElements[1]

                            if(currentDestiny == nextSource):

                                result.insert(i + 1, stall)
                        
                        # CRG instruction
                        else:

                            nextSource = nextInstructionElements[4]

                            if(currentDestiny == nextSource):

                                result.insert(i + 1, stall)

                    # data instruction
                    else:

                        nextSource2 = nextInstructionElements[2]
                        nextSource3 = nextInstructionElements[3]

                        if(currentDestiny == nextSource2 or currentDestiny == nextSource3):

                            result.insert(i + 1, stall)

        i += 1

    return result[:-1]

# instructionElements => string list
# typeDictionary => string dictionary
# opcodeDictionary => string dictionary
def riskControlUnit(instructionElements, typeDictionary, opcodeDictionary):

    case1 = stallInsertionCase1(instructionElements, typeDictionary, opcodeDictionary)

    case2 = stallInsertionCase2(case1, typeDictionary, opcodeDictionary)

    case3 = stallInsertionCase3(case2, typeDictionary, opcodeDictionary)

    return case3

def getInstructionElements():

    # open code.txt file for reading
    codeFile = open('code.txt', 'r')
    codeLines = codeFile.readlines()

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

        # current line contains a label
        if(aux == ":"):
            
            instructionElements.append([line[:-2]])

        # current line contains an instruction
        else:

            #pointerLine += 1

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

            instructionElements.append(elements)
            
    return instructionElements

# instructionElements => string list list
def getLabelDictionary(instructionElements):
    
    labelDictionary = {}

    # variable to know the number of the current line
    pointerLine = 0

    for instruction in instructionElements:

        pointerLine += 1

        instructionLength = len(instruction)

        # label
        if(instructionLength == 1):

            labelDictionary[instruction[0]] = pointerLine

            instructionElements.remove(instruction)

    return labelDictionary, instructionElements

# instructionElements => string list list
def binaryInstructions(instructionElements, typeDictionary, opcodeDictionary, registerDictionary, labelDictionary):

    # open binaryCode.txt file for writing
    binaryCodeFile = open('binaryCode.txt', 'w')

    # variable to know the number of the current line
    pointerLine = 0

    for elements in instructionElements:

        pointerLine += 1

        print("elements = ", elements)        
            
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
        
        print(" ")

        binaryCodeFile.write(instruction + "\n")

    return instructionElements

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

instructionElements = getInstructionElements()

instructionElements = riskControlUnit(instructionElements, typeDictionary, opcodeDictionary)

labelDictionary, instructionElements = getLabelDictionary(instructionElements)

binaryInstructions(instructionElements, typeDictionary, opcodeDictionary, registerDictionary, labelDictionary)
