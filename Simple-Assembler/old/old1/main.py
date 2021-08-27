from takeInputFile import *
from symbolTableFile import *


#defining each register in a dcitionary with 3-bit key representing the register and the 16-bit value representing the value stored in the register
register={}
register["R0"]=["000","0000000000000000"]
register["R1"]=["001","0000000000000000"]
register["R2"]=["010","0000000000000000"] 
register["R3"]=["011","0000000000000000"] 
register["R4"]=["100","0000000000000000"] 
register["R5"]=["101","0000000000000000"] 
register["R6"]=["110","0000000000000000"] 
reg=["FLAGS","111","0000000000000000"]
def immediateToBinary(num):
    #getting the binary value
    subNum=bin(int(num)).replace("0b","")
    numZero2add=8-len(subNum)
    for i in range(numZero2add):
        subNum="0"+subNum
    return subNum

def binCode(line,myInstruction,symbol,d):
    ansOpcode=""
    termList=myInstruction.split()
    operation=termList[0]
    # type="A"
    # now using if-else to process each operation term
    if(operation=="mov"):
        if (termList[1] not in register):
                s="error in line "+line
                print(s)
                return -1

        elif(termList[2]==reg[0]):
            #third operand is  a flag register
                opcode="00011"
                unusedBits="00000"
                destinationRegister=register[termList[1]][0]
                sourceRegister=reg[1]
                instruction=opcode+unusedBits+destinationRegister+sourceRegister
                return instruction

        #now checking if the third operand is general register or an immediate value
        elif (termList[2] not in register):
            if(termList[2][0]=='$'):
                if (int(termList[2][1:])<=255) and (int(termList[2][1:])>=0):
                    #then third operand is a an immediate value
                    #first converting the immediate value to proper binary value of 8 bit
                    immediateValue=immediateToBinary(termList[2][1:])
                    opcode="00010"
                    destinationRegister=register[termList[1]][0]
                    unusedBits=""
                    instruction=opcode+unusedBits+destinationRegister+immediateValue
                    return instruction
                else:
                    s="error in line "+line
                    print(s)
                    return -1
            else:
                s="error in line "+line
                print(s)
                return -1
        else:
            #third operand is also a register
                opcode="00011"
                unusedBits="00000"
                destinationRegister=register[termList[1]][0]
                sourceRegister=register[termList[2]][0]
                instruction=opcode+unusedBits+destinationRegister+sourceRegister
                return instruction
    elif(operation=="div"):
        if (termList[1] not in register) or (termList[2] not in register):
            s="error in line "+line
            print(s)
            return -1
        else:
            opcode="00111"
            unusedBits="00000"
            Register1=register[termList[1]][0]
            Register2=register[termList[2]][0]
            instruction=opcode+unusedBits+Register1+Register2
            return instruction

    elif(operation=="not"):
        if (termList[1] not in register) or (termList[2] not in register):
            s="error in line "+line
            print(s)
            return -1
        else:
            opcode="01101"
            unusedBits="00000"
            Register1=register[termList[1]][0]
            Register2=register[termList[2]][0]
            instruction=opcode+unusedBits+Register1+Register2
            return instruction

    elif(operation=="cmp"):
        if (termList[1] not in register) or (termList[2] not in register):
            s="error in line "+line
            print(s)
            return -1
        else:
            opcode="01110"
            unusedBits="00000"
            Register1=register[termList[1]][0]
            Register2=register[termList[2]][0]
            instruction=opcode+unusedBits+Register1+Register2
            return instruction

    elif(operation=="rs"):
        if (termList[1] not in register):
            s="error in line "+line
            print(s)
            return -1
        elif(termList[2][0]=='$'):
            #first converting the immediate value to proper binary value of 8 bit
            immediateValue=immediateToBinary(termList[2][1:])
            opcode="01000"
            destinationRegister=register[termList[1]][0]
            unusedBits=""
            instruction=opcode+unusedBits+destinationRegister+immediateValue
            return instruction
        else:
            s="error in line "+line
            print(s)
            return -1

    elif(operation=="ls"):
        if (termList[1] not in register):
            s="error in line "+line
            print(s)
            return -1
        elif(termList[2][0]=='$'):
            #first converting the immediate value to proper binary value of 8 bit
            immediateValue=immediateToBinary(termList[2][1:])
            opcode="01000"
            destinationRegister=register[termList[1]][0]
            unusedBits=""
            instruction=opcode+unusedBits+destinationRegister+immediateValue
            return instruction
        else:
            s="error in line "+line
            print(s)
            return -1

    elif(operation=="add"):
        if (termList[1] not in register) or (termList[2] not in register) or (termList[3] not in register):
            s="error in line "+line
            print(s)
            return -1
        else:
            opcode="00000"
            unusedBits="00"
            destinationRegister=register[termList[1]][0]
            sourceRegister1=register[termList[2]][0]
            sourceRegister2=register[termList[3]][0]
            instruction=opcode+unusedBits+destinationRegister+sourceRegister1+sourceRegister2
            return instruction

    elif(operation=="sub"):
        if (termList[1] not in register) or (termList[2] not in register) or (termList[3] not in register):
            s="error in line "+line
            print(s)
            return -1
        else:
            opcode="00001"
            unusedBits="00"
            destinationRegister=register[termList[1]][0]
            sourceRegister1=register[termList[2]][0]
            sourceRegister2=register[termList[3]][0]
            instruction=opcode+unusedBits+destinationRegister+sourceRegister1+sourceRegister2
            return instruction
    elif(operation=="mul"):
        if (termList[1] not in register) or (termList[2] not in register) or (termList[3] not in register):
            s="error in line "+line
            print(s)
            return -1
        else:
            opcode="00110"
            unusedBits="00"
            destinationRegister=register[termList[1]][0]
            sourceRegister1=register[termList[2]][0]
            sourceRegister2=register[termList[3]][0]
            instruction=opcode+unusedBits+destinationRegister+sourceRegister1+sourceRegister2
            return instruction

    elif(operation=="xor"):
        if (termList[1] not in register) or (termList[2] not in register) or (termList[3] not in register):
            s="error in line "+line
            print(s)
            return -1
        else:
            opcode="01010"
            unusedBits="00"
            destinationRegister=register[termList[1]][0]
            sourceRegister1=register[termList[2]][0]
            sourceRegister2=register[termList[3]][0]
            instruction=opcode+unusedBits+destinationRegister+sourceRegister1+sourceRegister2
            return instruction

    elif(operation=="or"):
        if (termList[1] not in register) or (termList[2] not in register) or (termList[3] not in register):
            s="error in line "+line
            print(s)
            return -1
        else:
            opcode="01011"
            unusedBits="00"
            destinationRegister=register[termList[1]][0]
            sourceRegister1=register[termList[2]][0]
            sourceRegister2=register[termList[3]][0]
            instruction=opcode+unusedBits+destinationRegister+sourceRegister1+sourceRegister2
            return instruction

    elif(operation=="and"):
        if (termList[1] not in register) or (termList[2] not in register) or (termList[3] not in register):
            s="error in line "+line
            print(s)
            return -1
        else:
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
        if((termList[2] not in d) or (termList[1] not in register)):
            s="error in line "+line
            print(s)
            return -1

        else:
            immediateValue=immediateToBinary(d[termList[2]])
            unusedBits=""
            instruction=opcode+unusedBits+destinationRegister+immediateValue
            return instruction

    elif(operation=="st"):
        opcode="00101"
        destinationRegister=register[termList[1]][0]
        if((termList[2] not in d) or (termList[1] not in register)):
            s="error in line "+line
            print(s)
            return -1
        else:
            immediateValue=immediateToBinary(d[termList[2]])
            unusedBits=""
            instruction=opcode+unusedBits+destinationRegister+immediateValue
            return instruction

    elif(operation=="jmp"):
        #unconditional jump
        if(termList[1] not in symbol):
            s="error in line "+line
            print(s)
            return -1
        else:
            opcode="01111"
            unusedBits="000"
            immediateValue=immediateToBinary(symbol[termList[1]])
            instruction=opcode+unusedBits+immediateValue
            return instruction

    elif(operation=="jlt"):
    
        if(termList[1] not in symbol):
            s="error in line "+line
            print(s)
            return -1
        else:
            opcode="10000"
            unusedBits="000"
            immediateValue=immediateToBinary(symbol[termList[1]])
            instruction=opcode+unusedBits+immediateValue
            return instruction
    
    elif(operation=="jgt"):
        if(termList[1] not in symbol):
            s="error in line "+line
            print(s)
            return -1
        else:
            opcode="10001"
            unusedBits="000"
            immediateValue=immediateToBinary(symbol[termList[1]])
            instruction=opcode+unusedBits+immediateValue
            return instruction

    elif(operation=="je"):
        
        if(termList[1] not in symbol):
            s="error in line "+line
            print(s)
            return -1
        else:
            opcode="10010"
            unusedBits="000"
            immediateValue=immediateToBinary(symbol[termList[1]])
            instruction=opcode+unusedBits+immediateValue
            return instruction

    elif(operation=="hlt"):
        return "1001100000000000"
    
    elif(":" in operation):
        # here you handle label
        #just pass the instruction aside from the label
        if(len(termList)==3):
            pass
        else:
            myInstruction=' '.join(termList[1:])
            return binCode(line,myInstruction,symbol,d)

    elif(operation=="var"):
        pass
    else:
        s="error in line "+line
        print(s)
        return -1

# writing the machine code in the output text file
instn=takeInput()
if(instn!=-1):
    lst=instn[0]
    instructionList=instn[1]
    #print(instructionList,'---',lst)
    count=0
    for i in range(len(instructionList)):
        l=instructionList[i].split()
        if(l[0][-1]==":"):
            if(l[1]=="hlt"):
                count+=1
                j=i
        if(l[0]=="hlt"):
            if(count==0):
                j=i
            count+=1
        if(count>1):
            break
    if (count==0): #halt error handling
        print("hlt missing error")
    elif count>1:
        line=instructionList[j][-1]
        print("error in line",line)

    else:
        variable={}#stores variable name and their actual location.
        for i in range(len(instructionList)):
            components=instructionList[i].split()
            line=instructionList[i][-1]
            e=0
            if(components[0]=="var"):
                if(len(components)!=4):
                    print("error in line",line)
                    e=1
                    break
            #print(components,components[1])
                else:
                    variable[components[1]]=int(components[2])
            else:
                continue
        if(e==0):
            symbolList=symbolLocation(lst,instructionList)
            if(symbolList==-1):
                pass
            else:
        
        #iterating over each instruction and converting them to binary and then writing it to output.txt file
                instructionListBinary=[]

                error=0
        #print(symbolList)
                for i in range(len(instructionList)):
                    line=instructionList[i][-1]
                    binIns=binCode(line,instructionList[i],symbolList,variable)
                    if(binIns==-1):
                        error=1
                #print(instructionList[i],"-------",binIns)
                        break
            #print(instructionList[i],"-------",binIns)
                    instructionListBinary.append(binIns)
                if(error==0):

                    for i in instructionListBinary:
                
                        if i != None:
                            print(i)
