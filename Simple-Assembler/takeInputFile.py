
# function to remove the empty lines from the instruction list 
def removeEmptyLines(myList):
    ansList=[]
    for i in myList:
        if i[0]==" ":
            continue
        elif(len(i)>3):
            #appending the instruction lines and also removing '\n' from them
            ansList.append(i)

    return ansList

def checkVar(myList):
    #checking if there is any variable instruction at all in the program
    for i in myList:
        if("var" in i):
            return True
    return False
def rearrangeVarInList(myList):
    #getting the index of the last instruction where the var is defined
    if(not checkVar(myList)):
        return myList
    startCode=0
    lastIn=""
    for i in myList:
        if(("var" in i)or (len(i)==1)):
            startCode+=1
            lastIn=i
        else:
            break
    ansList=[]
    if(len(lastIn)>1):
        ansList=myList[startCode:]+myList[0:startCode]
    else :
        startCode=startCode-1
        ansList=myList[startCode:]+myList[0:startCode]
    
    return ansList

# function take a text file as the input and the remove the empty lines and generates the list of each line 
def takeInput():
    inTempList=[]
    # fileRead=open(r"input.txt","r")
    # inTempList=fileRead.readlines()
    # fileRead.close()

    #taking input using console
    
    while True:
        try:
            temp=input()
            # if(temp=="-1"):
            #     break
            inTempList.append(temp)
        except EOFError as e:
            break
    # making a dictionary for each instruction with its original line number in the code
    d={}
    for i in range(len(inTempList)):
        if(len(inTempList[i])!=1):
            d[inTempList[i]]=i+1

    #print(inTempList," dekho",d)
    
    # Now adding the location number to the non-empty lines
    lst=inTempList[:]
    locationNum=0
    for i in range(len(lst)):
        if(len(lst[i])!=1):
            lst[i]=lst[i]+" "+str(locationNum)+" "+str(d[inTempList[i]])
        locationNum+=1
    lst1=removeEmptyLines(lst)
    # print("lst is : ",lst1)
    # inTempList=removeEmptyLines(inTempList)
    inTempList=rearrangeVarInList(inTempList)
    locationNum=0
    for i in range(len(inTempList)):
        if(len(inTempList[i])!=1):
            inTempList[i]=inTempList[i]+" "+str(locationNum)+" "+str(d[inTempList[i]])
        locationNum+=1
    # print("hello",inTempList)
    instructionList=removeEmptyLines(inTempList)
    # instructionList=inTempList
    # print("instructionList is : ",instructionList)
    
    # print(d,lst,"foo",instructionList,"see")
    return [lst1,instructionList]

# ans=takeInput()
# print(ans[0])
# print(ans[1])
# # ans[1]=removeEmptyLines(ans[1])
# for i in ans[0]:
#     print(i," ",len(i))
