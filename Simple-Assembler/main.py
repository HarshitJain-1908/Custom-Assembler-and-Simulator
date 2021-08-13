from takeInputFile import *
from symbolTableFile import *
# from binaryInstructionTable import *



#defining each register in a dcitionary with 3-bit key representing the register and the 16-bit value representing the value stored in the register
register={}
register["R0"]=["000","0000000000000000"]
register["R1"]=["001","0000000000000000"]
register["R2"]=["010","0000000000000000"] 
register["R3"]=["011","0000000000000000"] 
register["R4"]=["100","0000000000000000"] 
register["R5"]=["101","0000000000000000"] 
register["R6"]=["110","0000000000000000"] 
register["R7"]=["111","0000000000000000"]
def immediateToBinary(num):
    #getting the binary value
    subNum=bin(int(num)).replace("0b","")
    numZero2add=8-len(subNum)
    for i in range(numZero2add):
        subNum="0"+subNum
    return subNum

def binCode(myInstruction,symbol):
    ansOpcode=""
    termList=myInstruction.split()
    operation=termList[0]
    # type="A"
    # now using if-else to process each operation term 
    if(operation=="mov"):
        #now first checking if the third operand is register or an immediate value
        if termList[2] not in register:
            #then third operand is a an immediate value
            #first converting the immediate value to proper binary value of 8 bit
            immediateValue=immediateToBinary(termList[2][1:])
            opcode="00010"
            destinationRegister=register[termList[1]][0]
            unusedBits=""
            instruction=opcode+unusedBits+destinationRegister+immediateValue
            return instruction
        else:
            #third operand is also a register
            opcode="00011"
            unusedBits="00000"
            destinationRegister=register[termList[1]][0]
            sourceRegister=register[termList[2]][0]
            instruction=opcode+unusedBits+destinationRegister+sourceRegister
            return instruction
    elif(operation=="div"):
        opcode="00111"
        unusedBits="00000"
        Register1=register[termList[1]][0]
        Register2=register[termList[2]][0]
        instruction=opcode+unusedBits+Register1+Register2
        return instruction
    
    elif(operation=="not"):
        opcode="01101"
        unusedBits="00000"
        Register1=register[termList[1]][0]
        Register2=register[termList[2]][0]
        instruction=opcode+unusedBits+Register1+Register2
        return instruction

    elif(operation=="cmp"):
        opcode="01110"
        unusedBits="00000"
        Register1=register[termList[1]][0]
        Register2=register[termList[2]][0]
        instruction=opcode+unusedBits+Register1+Register2
        return instruction

    elif(operation=="rs"):
        #first converting the immediate value to proper binary value of 8 bit
        immediateValue=immediateToBinary(termList[2][1:])
        opcode="01000"
        destinationRegister=register[termList[1]][0]
        unusedBits=""
        instruction=opcode+unusedBits+destinationRegister+immediateValue
        return instruction
    elif(operation=="ls"):
        #first converting the immediate value to proper binary value of 8 bit
        immediateValue=immediateToBinary(termList[2][1:])
        opcode="01000"
        destinationRegister=register[termList[1]][0]
        unusedBits=""
        instruction=opcode+unusedBits+destinationRegister+immediateValue
        return instruction
    
    elif(operation=="add"):
        opcode="00000"
        unusedBits="00"
        destinationRegister=register[termList[1]][0]
        sourceRegister1=register[termList[2]][0]
        sourceRegister2=register[termList[3]][0]
        instruction=opcode+unusedBits+destinationRegister+sourceRegister1+sourceRegister2
        return instruction

    elif(operation=="sub"):
        opcode="00001"
        unusedBits="00"
        destinationRegister=register[termList[1]][0]
        sourceRegister1=register[termList[2]][0]
        sourceRegister2=register[termList[3]][0]
        instruction=opcode+unusedBits+destinationRegister+sourceRegister1+sourceRegister2
        return instruction
    elif(operation=="mul"):
        opcode="00110"
        unusedBits="00"
        destinationRegister=register[termList[1]][0]
        sourceRegister1=register[termList[2]][0]
        sourceRegister2=register[termList[3]][0]
        instruction=opcode+unusedBits+destinationRegister+sourceRegister1+sourceRegister2
        return instruction

    elif(operation=="xor"):
        opcode="01010"
        unusedBits="00"
        destinationRegister=register[termList[1]][0]
        sourceRegister1=register[termList[2]][0]
        sourceRegister2=register[termList[3]][0]
        instruction=opcode+unusedBits+destinationRegister+sourceRegister1+sourceRegister2
        return instruction

    elif(operation=="or"):
        opcode="01011"
        unusedBits="00"
        destinationRegister=register[termList[1]][0]
        sourceRegister1=register[termList[2]][0]
        sourceRegister2=register[termList[3]][0]
        instruction=opcode+unusedBits+destinationRegister+sourceRegister1+sourceRegister2
        return instruction

    elif(operation=="and"):
        opcode="01100"
        unusedBits="00"
        destinationRegister=register[termList[1]][0]
        sourceRegister1=register[termList[2]][0]
        sourceRegister2=register[termList[3]][0]
        instruction=opcode+unusedBits+destinationRegister+sourceRegister1+sourceRegister2
        return instruction

    elif(operation=="ld"):
        opcode="00100"
        destinationRegister=register[termList[1]][0]
        if(termList[2] not in symbol):
            print("error")
            return
        else:
            immediateValue=immediateToBinary(symbol[termList[2]])
        unusedBits=""
        instruction=opcode+unusedBits+destinationRegister+immediateValue
        return instruction

    elif(operation=="st"):
        opcode="00101"
        destinationRegister=register[termList[1]][0]
        if(termList[2] not in symbol):
            print("error")
            return
        else:
            immediateValue=immediateToBinary(symbol[termList[2]])
        unusedBits=""
        instruction=opcode+unusedBits+destinationRegister+immediateValue
        return instruction

    elif(operation=="hlt"):
        #globals instructionList
        #if(len(instructionList==9)):
        # if(i!=(length-1)):
        #     print("error")
        #     return
        return "1001100000000000"
    
    elif(":" in operation):
        # here you handle label
        #just pass the instruction aside from the label
        myInstruction=' '.join(termList[1:])
        return binCode(myInstruction,symbol)



instructionList=takeInput()
length=len(instructionList)
symbolList=symbolLocation(instructionList)
# print("The sumbol list is : ")
# print(symbolList)
# function to remove the empty lines from the instruction list 
def removeEmptyLines(myList):
    ansList=[]
    for i in myList:
        if(len(i)>1):
            #appending the instruction lines and also removing '\n' from them
            ansList.append(i.strip())
    return ansList

# writing the machine code in the output text file
outputFile=open("output.txt","w")
#iterating over each instruction and converting them to binary and then writing it to output.txt file
instructionListBinary=[]
# for i in range(len(instructionList)):
#     components=instructionList[i].split()
#     variable=[]
#     if(components[0]=="var"): #var xyz
#         variable.append(components[1])
#     else:
#         k=i
#         break

#for variables declared on the top of program
# d={} #dictionary with key as variable name and value as its assigned number
# for i in range(len(variable)):
#     d[variable[i]]=length-1+i

for i in range(len(instructionList)):
    binIns=binCode(instructionList[i],symbolList)
    print(instructionList[i],"-------",binIns)
    instructionListBinary.append(binIns)




print("intsruction list is : ")
print(instructionList)
    

for i in instructionListBinary:
    if i != None:
        outputFile.write(i)
        outputFile.write('\n')
outputFile.close()
# print(decimalToBinary("7"))


