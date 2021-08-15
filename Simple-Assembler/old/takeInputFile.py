
# function to remove the empty lines from the instruction list 
def removeEmptyLines(myList):
    ansList=[]
    for i in myList:
        if(len(i)>1):
            #appending the instruction lines and also removing '\n' from them
            ansList.append(i.strip())
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
    # fileRead=open(r"input.txt","r")
    # inTempList=fileRead.readlines()
    # fileRead.close()

    #taking input using console
    inTempList=[]
    # temp=""
    # while temp != "hlt":
    #     temp=str((input()))
    #     inTempList.append(temp)
    while True:
        try:
            temp=str((input()))
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
        if(len(lst[i])!=0):
            lst[i]=lst[i]+" "+str(locationNum)+" "+str(d[inTempList[i]])
        locationNum+=1
    lst=removeEmptyLines(lst)
    inTempList=rearrangeVarInList(inTempList)
    locationNum=0
    for i in range(len(inTempList)):
        if(len(inTempList[i])!=0):
            inTempList[i]=inTempList[i]+" "+str(locationNum)+" "+str(d[inTempList[i]])
        locationNum+=1
    instructionList=removeEmptyLines(inTempList)

    
    #sprint(lst,"foo",instructionList,"see")
    return lst,instructionList

# ans=takeInput()
# print(ans[0])
# print(ans[1])