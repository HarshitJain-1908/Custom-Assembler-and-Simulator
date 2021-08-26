from takeInputFile import takeInput
from memoryFile import memory


# initializing the program counter

# dictionary which manages the values in the registers
register={}
# directly mapping the binary value of the register names with the values stored in them
register['000']="0000000000000000"
register['001']="0000000000000000"
register['010']="0000000000000000"
register['011']="0000000000000000"
register['100']="0000000000000000"
register['101']="0000000000000000"
register['110']="0000000000000000"
register['111']="0000000000000000" #flags register

# function to get the integer type decimal immediate value from the binary string
def binaryToImmediate(myBin):
    value=0
    for index in reversed(range(len(myBin))):
        value=(int(myBin[index]) * pow(2,len(myBin)-(index+1)))+value
    return value

def immediateToBinary(num):
    #getting the binary value
    subNum=bin(int(num)).replace("0b","")
    numZero2add=8-len(subNum)
    for i in range(numZero2add):
        subNum="0"+subNum
    return subNum

def immediateToBinaryRegister(num):
    #getting the binary value
    subNum=bin(int(num)).replace("0b","")
    numZero2add=16-len(subNum)
    for i in range(numZero2add):
        subNum="0"+subNum
    return subNum

#function to output the state of the registers
def stateDump(pc,register):
    ans=""
    # print(immediateToBinaryRegister(pc),end=" ")
    ans=ans+immediateToBinary(pc)+" "
    for i in register:
        # print(register[i],end=" ")
        ans=ans+register[i]+" "
    # print("")
    return ans

#function to output the state of the memory
def memoryDump(memoryInputList):
    ans=[]
    ans=ans+memoryInputList
    num=len(memoryInputList)
    #first printing the memory input list
    # for i in memoryInputList:
    #     print(i)
    #now printing the rest of the memory which is empty
    for i in range(256-len(memoryInputList)):
        # print("0000000000000000")
        ans.append("0000000000000000")
    return ans


# making the executionInstrcution function which executes the code and changes the register files accordingly
def executeInstruction(pc,myInstruction,memoryList):
    # global pc
    #parsing the 5 bits opcode first
    opcode=myInstruction[0:5]

    if(opcode=="00010"):
        #mov with second operand as immediate value
        # now next 3 bits are for destination register
        # then 8 digits represents the immediate value
        subStr=myInstruction[5:]
        dest=subStr[0:3]
        imm=subStr[3:]
        # now udating the value in the destination register
        register[dest]="00000000"+imm

        # updating the pc accordingly
        pc+=1
        return False,pc

    elif(opcode=="00011"):
        #mov with second operand as a register
        #also next five bits are unused bits
        subStr=myInstruction[10:]
        dest=subStr[0:3]
        src=subStr[3:]
        #updating the value in the destination register
        register[dest]=register[src]

        #updating the pc accordingly
        pc+=1
        return False,pc

    elif(opcode=="00000"):
        # this is add operation
        # hence next two bits must be unsed bits and hence after that we have 9 bits for three registers
        subStr=myInstruction[7:]
        dest=subStr[0:3]
        src1=subStr[3:6]
        src2=subStr[6:9]

        valueDestination=binaryToImmediate(register[src1])+binaryToImmediate(register[src2])
        #updating the value in the destination register
        register[dest]=immediateToBinaryRegister(valueDestination)
        
        
        pc+=1
        return False,pc
    elif(opcode=="00001"):
        # for subtraction operation
        subStr=myInstruction[7:]
        dest=subStr[0:3]
        src1=subStr[3:6]
        src2=subStr[6:9]

        valueDestination=binaryToImmediate(register[src1])+binaryToImmediate(register[src2])
        #updating the value in the destination register
        if(valueDestination>=0):
            register[dest]=immediateToBinaryRegister(valueDestination)
        else:
            register[dest]="0000000000000000"

        pc+=1
        return False,pc
    elif(opcode=="00110"):
        # this is multiply operation
        # hence next two bits must be unsed bits and hence after that we have 9 bits for three registers
        subStr=myInstruction[7:]
        dest=subStr[0:3]
        src1=subStr[3:6]
        src2=subStr[6:9]

        valueDestination=binaryToImmediate(register[src1])*binaryToImmediate(register[src2])
        #updating the value in the destination register
        register[dest]=immediateToBinaryRegister(valueDestination)
        
        pc+=1
        return False,pc

    elif(opcode=="00111"):
        #div operator
        #also next five bits are unused bits
        subStr=myInstruction[10:]
        dest=subStr[0:3]
        src=subStr[3:]
        
        #updating the value in the destination register
        destValueQ=register[dest]/register[src]
        destValueR=register[dest]%register[src]

        register[dest]=immediateToBinaryRegister(destValueQ)
        register[src]=immediateToBinaryRegister(destValueR)
        #updating the pc accordingly
        pc+=1
        return False,pc
    elif(opcode=="00101"):
        # this is the store operation
        # first 5 bits are of opcode then 3 bits are of source register and next 8 bits are the address
        # we shall first computer the address which is the line number (index number) in the memory list
        subStr=myInstruction[5:]
        src=subStr[0:3]
        address=subStr[3:]

        #updating the value from the register at the address
        lineNumber=binaryToImmediate(address)
        memoryList[lineNumber]=register[src]
        
        #updating the pc accordingly
        pc+=1
        return False,pc
    elif(opcode=="00100"):
        #this is load operation
        subStr=myInstruction[5:]
        src=subStr[0:3]
        address=subStr[3:]
        #updating the value from the address in the register
        lineNumber=binaryToImmediate(address)
        value=binaryToImmediate(memoryList[lineNumber])
        register[src]=immediateToBinaryRegister(value)

        #updating the pc accordingly
        pc+=1
        return False,pc
    elif(opcode=="10011"):
        # this is halt operation
        # here we update pc as -1
        
        pc=-1
        return True,pc

# taking the input value
memoryInputList=takeInput()

pc=0 # using it as a variable
halted=False
cycle=0
stateList=[]
memoryList=memoryDump(memoryInputList)
while not halted:
    #getting the instrcution to be executed
    inst=memory(pc,memoryInputList)
    #now executing the instruction
    halted,nextpc=executeInstruction(pc,inst,memoryList)
    # printing the current state of pc and other registers
    stateList.append(stateDump(pc,register))
    pc=nextpc
    cycle+=1

#output file
output=open("ouputFile.txt",'w')
for i in stateList:
    output.write(i)
    output.write("\n")
    print(i,end="\n")



for i in memoryList:
    output.write(i)
    output.write("\n")
    print(i,end="\n")
output.close()