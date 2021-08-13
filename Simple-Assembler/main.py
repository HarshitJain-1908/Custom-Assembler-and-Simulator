from takeInputFile import *
# from binaryInstructionTable import *

#defining each register in a dcitionary with 3-bit key representing the register and the 16-bit value representing the value stored in the register
register={}
register["r0"]=["000","0000000000000000"]
register["r1"]=["001","0000000000000000"]
register["r2"]=["010","0000000000000000"] 
register["r3"]=["011","0000000000000000"] 
register["r4"]=["100","0000000000000000"] 
register["r5"]=["101","0000000000000000"] 
register["r6"]=["110","0000000000000000"] 
register["r7"]=["111","0000000000000000"]
def immediateToBinary(num):
    #getting the binary value
    subNum=bin(int(num)).replace("0b","")
    numZero2add=8-len(subNum)
    for i in range(numZero2add):
        subNum="0"+subNum
    return subNum

def binCode(myInstruction):
    # ansOpcode=""
    termList=myInstruction.split()
    operation=termList[0]
    # type="A"
    # now using if-else to process each operation term 
    if(operation=="mov"):
        #now first checking if the third operand is register or an immediate value
        if termList[2] not in register:
            #then third operand is a an immediate value
            #first converting the immediate value to proper binary value of 8 bit
            immediateValue=immediateToBinary(termList[2])
            opcode="00010"
            sourceRegister=register[termList[1]][0]
            unusedBits=""
            instruction=opcode+unusedBits+sourceRegister+immediateValue
            return instruction
    elif(operation=="add"):
        opcode="00000"
        unusedBits="00"
        destinationRegister=register[termList[1]][0]
        sourceRegister1=register[termList[2]][0]
        sourceRegister2=register[termList[3]][0]
        instruction=opcode+unusedBits+destinationRegister+sourceRegister1+sourceRegister2
        return instruction
    elif(operation=="hlt"):
        return "10011"


instructionList=takeInput()

# writing the machine code in the output text file
outputFile=open("output.txt","w")
#iterating over each instruction and converting them to binary and then writing it to output.txt file
instructionListBinary=[]
for i in instructionList:
    binIns=binCode(i)
    instructionListBinary.append(binIns)

for i in instructionListBinary:
    if i != None:
        outputFile.write(i)
        outputFile.write('\n')
outputFile.close()
# print(decimalToBinary("7"))