from takeInputFile import takeInput
from memoryFile import memory
import matplotlib.pyplot as plt

import os.path
from os import path 


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
    # print(myInstruction)

    if(opcode=="00010"):
        #mov with second operand as immediate value
        # now next 3 bits are for destination register
        # then 8 digits represents the immediate value
        subStr=myInstruction[5:]
        dest=subStr[0:3]
        imm=subStr[3:]
        # now udating the value in the destination register
        register[dest]="00000000"+imm

        # resetting flags register
        register["111"]="0000000000000000"

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

        # resetting flags register
        register["111"]="0000000000000000"

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
        if(valueDestination>65535):
            # set overflow flag
            register["111"]=register["111"][:-4]+"1"+register["111"][-3:]
        else:
            #updating the value in the destination register
            register[dest]=immediateToBinaryRegister(valueDestination)
            # resetting flags register
            register["111"]="0000000000000000"
        

        # update pc accordingly
        pc+=1
        return False,pc

    elif(opcode=="00001"):
        # for subtraction operation
        subStr=myInstruction[7:]
        dest=subStr[0:3]
        src1=subStr[3:6]
        src2=subStr[6:9]

        valueDestination=binaryToImmediate(register[src1])-binaryToImmediate(register[src2])
        #updating the value in the destination register
        if(valueDestination>=0):
            register[dest]=immediateToBinaryRegister(valueDestination)
            # resetting flags register
            register["111"]="0000000000000000"
        else:
            register[dest]="0000000000000000"
            # set overflow flag
            register["111"]=register["111"][:-4]+"1"+register["111"][-3:]

        pc+=1
        return False,pc
    elif(opcode=="00110"):
        # this is mul operation
        # hence next two bits must be unsed bits and hence after that we have 9 bits for three registers
        subStr=myInstruction[7:]
        dest=subStr[0:3]
        src1=subStr[3:6]
        src2=subStr[6:9]

        valueDestination=binaryToImmediate(register[src1])*binaryToImmediate(register[src2])
        if(valueDestination>65535):
            # overflow
            register["111"]=register["111"][:-4]+"1"+register["111"][-3:]
        else:
            #updating the value in the destination register
            register[dest]=immediateToBinaryRegister(valueDestination)
            # resetting flags register
            register["111"]="0000000000000000"
        
        pc+=1
        return False,pc

    elif(opcode=="00111"):
        #div operation
        #also next five bits are unused bits
        subStr=myInstruction[10:]
        dest=subStr[0:3]
        src=subStr[3:]
        #updating the value in the destination register
        destValueQ=int(binaryToImmediate(register[dest])/binaryToImmediate(register[src]))
        destValueR=binaryToImmediate(register[dest])%binaryToImmediate(register[src])

        register["000"]=immediateToBinaryRegister(destValueQ)
        register["001"]=immediateToBinaryRegister(destValueR)

        # resetting flags register
        register["111"]="0000000000000000"
        #updating the pc accordingly
        pc+=1
        return False,pc

    elif(opcode=="01000"):
        # right shift
        #mov with second operand as immediate value
        # now next 3 bits are for destination register
        # then 8 digits represents the immediate value
        subStr=myInstruction[5:]
        dest=subStr[0:3]
        imm=subStr[3:]
        # now udating the value in the destination register
        shift=binaryToImmediate(imm)
        destValue=int(binaryToImmediate(register[dest])/shift)
        register[dest]=immediateToBinaryRegister(destValue)

        # resetting flags register
        register["111"]="0000000000000000"

        # updating the pc accordingly
        pc+=1
        return False,pc

    elif(opcode=="01001"):
        # left shift
        #mov with second operand as immediate value
        # now next 3 bits are for destination register
        # then 8 digits represents the immediate value
        subStr=myInstruction[5:]
        dest=subStr[0:3]
        imm=subStr[3:]
        # now udating the value in the destination register
        shift=binaryToImmediate(imm)
        destValue=int(binaryToImmediate(register[dest])*shift)
        register[dest]=immediateToBinaryRegister(destValue)

        # resetting flags register
        register["111"]="0000000000000000"

        # updating the pc accordingly
        pc+=1
        return False,pc

    elif(opcode=="01010"):
        # this is logical xor operation
        # hence next two bits must be unsed bits and hence after that we have 9 bits for three registers
        subStr=myInstruction[7:]
        dest=subStr[0:3]
        src1=subStr[3:6]
        src2=subStr[6:9]
        result=""
        #updating the value in the destination register
        for i in range(len(register[src1])):
            comp1=1-int(register[src1][i])
            comp2=1-int(register[src2][i])
            result+=str((int(register[src1][i]) and comp2) or (int(register[src2][i]) and comp1))

        register[dest]=result

        # resetting flags register
        register["111"]="0000000000000000"

        pc+=1
        return False,pc

    elif(opcode=="01011"):
        # this is logical or operation
        # hence next two bits must be unsed bits and hence after that we have 9 bits for three registers
        subStr=myInstruction[7:]
        dest=subStr[0:3]
        src1=subStr[3:6]
        src2=subStr[6:9]
        result=""
        #updating the value in the destination register
        for i in range(len(register[src1])):
            result+=str(int(register[src1][i]) or int(register[src2][i]))

        register[dest]=result

        # resetting flags register
        register["111"]="0000000000000000"

        pc+=1
        return False,pc

    elif(opcode=="01100"):
        # this is logical and operation
        # hence next two bits must be unsed bits and hence after that we have 9 bits for three registers
        subStr=myInstruction[7:]
        dest=subStr[0:3]
        src1=subStr[3:6]
        src2=subStr[6:9]
        result=""
        #updating the value in the destination register
        for i in range(len(register[src1])):
            result+=str(int(register[src1][i]) and int(register[src2][i]))

        register[dest]=result

        # resetting flags register
        register["111"]="0000000000000000"

        pc+=1
        return False,pc

    elif(opcode=="01101"):
        #not operation
        #also next five bits are unused bits
        subStr=myInstruction[10:]
        dest=subStr[0:3]
        src=subStr[3:]
        #updating the value in the destination register
        result=""
        for i in range(len(register[src])):
            if register[src][i]=="0":
                result+="1"
            else:
                result+="0"

        register[dest]=result

        # resetting flags register
        register["111"]="0000000000000000"
        #updating the pc accordingly
        pc+=1
        return False,pc


    elif(opcode=="00101"):
        # this is the store operation
        # first 5 bits are of opcode then 3 bits are of source register and next 8 bits are the 
        # we shall first computer the address which is the line number (index number) in the memory list
        subStr=myInstruction[5:]
        src=subStr[0:3]
        # variable=subStr[3:]
        address=subStr[3:]
        #updating the value from the register at the address
        lineNumber=binaryToImmediate(address)
        memoryList[lineNumber]=register[src]
        

        # resetting flags register
        register["111"]="0000000000000000"
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
        # value=binaryToImmediate(variable)
        register[src]=immediateToBinaryRegister(value)

        # resetting flags register
        register["111"]="0000000000000000"

        #updating the pc accordingly
        pc+=1
        return False,pc

    elif(opcode=="01110"):
        # compare operation
        #also next five bits are unused bits
        # here we have to set flags
        subStr=myInstruction[10:]
        operand1=register[subStr[0:3]]
        operand2=register[subStr[3:]]
        value1=binaryToImmediate(operand1)
        value2=binaryToImmediate(operand2)
        # print(value1,"@",value2)

        if(value1==value2):
            # set equal flag E
            # print("equal")
            register["111"]=register["111"][:-1]+"1"
        elif(value1>value2):
            # set greater than flag G
            register["111"]=register["111"][:-2]+"1"+register["111"][-1]
        else:
            # set less than flag L
            register["111"]=register["111"][:-3]+"1"+register["111"][-2:]

        #updating the pc accordingly
        pc+=1
        return False,pc
    
    elif(opcode=="01111"):
        # unconditional jump
        label=myInstruction[7:] # here to jump
        # resetting flags register
        register["111"]="0000000000000000"
        # setting pc to this label
        pc=binaryToImmediate(label)
        return False,pc

    elif(opcode=="10000"):
        # conditional jump
        label=myInstruction[7:] # if have to jump then here to jump

        if(register["111"][-3]=="1"):
            # need to jump
            # setting pc to this label
            pc=binaryToImmediate(label)

        else:
            pc+=1

        # resetting flags register
        register["111"]="0000000000000000"
    
        return False,pc

    elif(opcode=="10001"):
        # conditional jump
        label=myInstruction[7:] # if have to jump then here to jump

        if(register["111"][-2]=="1"):
            # need to jump
            # setting pc to this label
            pc=binaryToImmediate(label)

        else:
            pc+=1

        # resetting flags register
        register["111"]="0000000000000000"
    
        return False,pc

    elif(opcode=="10010"):
        # conditional jump
        label=myInstruction[7:] # if have to jump then here to jump

        if(register["111"][-1]=="1"):
            # need to jump
            # setting pc to this label
            pc=binaryToImmediate(label)

        else:
            pc+=1

        # resetting flags register
        register["111"]="0000000000000000"
    
        return False,pc



    elif(opcode=="10011"):
        # this is halt operation
        # here we update pc as -1
        
        pc=-1
        return True,pc

# taking the input value
memoryInputList=takeInput()
# print(memoryInputList)

pc=0 # using it as a variable
halted=False
cycle=0
stateList=[]
memoryList=memoryDump(memoryInputList)
# print(memoryList,"memlist")

#making the list of tuples with cycle and the memory access in decimal as elements of single tuple
coordinatesList=[]
while not halted:
    # print("h")
    #getting the instrcution to be executed
    inst=memory(pc,memoryInputList)
    # pc will always point to memory access(line number) of the program
    coordinatesList.append((cycle,pc))

    #note that in load and store instructions we are again accessing memories and hence has to plot this too
    if inst[0:5]=="00101" or inst[0:5]=="00100":
        memBin=inst[8:]
        coordinatesList.append((cycle,binaryToImmediate(memBin)))
    #now executing the instruction
    halted,nextpc=executeInstruction(pc,inst,memoryList)
    # if(halted==True):
    #     print(halted)
    # printing the current state of pc and other registers
    stateList.append(stateDump(pc,register))
    pc=nextpc
    cycle+=1
# print(stateList,"hello")

#output file
output=open("ouputFile.txt",'w')
for i in stateList:
    output.write(i)
    output.write("\n")
    print(i,end="\n")
# memoryList=memoryDump(memoryInputList)

for i in memoryList:
    # print("output")
    output.write(i)
    output.write("\n")
    print(i,end="\n")
output.close()

# print(coordinatesList)

# generating the scatter graph between cycles- memory access
x,y=zip(*coordinatesList)
plt.style.use('seaborn')
plt.scatter(x,y)
plt.title("Memory Access Trace Graph")
plt.xlabel("Cycle Number")
plt.ylabel("Memmory Address (Line Number)")
plt.show()

#code in order to ouput graph for each test case separately
testcase=1
name="output1.png"

while True:
    if(path.exists(name)):
        testcase=int(name[6])+1
        name="output"+str(testcase)+".png"
    else:
        plt.savefig(name)
        break
        
