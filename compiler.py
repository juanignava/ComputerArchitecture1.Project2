# Global variables
instructionType = "00"
opcode = "0"
reg1 = "000"
reg2 = "000"
reg3 = "000"
direction = "0"
immediate = "000"


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

    "SUM": "0000",
    "RES": "0001",
    "MUL": "0010",
    "DIV": "0011",
    "RSD": "0100",
    "SUMI": "1000",
    "RESI": "1001",
    "MULI": "1010",
    "DIVI": "1011",
    "RSDI": "1100"
}

registerDictionary = {
    "R0": "000",
    "R1": "001",
    "R2": "010",
    "R3": "011",
    "R4": "100",
    "R5": "101",
    "RR": "110",
    "RS": "111"
}













# open code.txt file for reading
codeFile = open('code.txt', 'r')
codeLines = codeFile.readlines()


for line in codeLines:

    memoryFlag = 0

    print(line + "\n")

    elements = []

    temp = ""
    
    for char in line:

        print("char = ", char)

        if(char == " " or char == "," or char == "(" or char == ")"):

            if(char == "("):
                memoryFlag = 1

            if(temp != ""):

                elements.append(temp)

            temp = ""            

        else:

            temp += char

        print("temp = ", temp)
        print("elements = ", elements)
        print("\n")

    temp = temp[:-1]
    elements.append(temp)    
    
    if(memoryFlag == 1):
        elements.pop()

    print("elements = ", elements)
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    break
    




    






codeFile.close()









