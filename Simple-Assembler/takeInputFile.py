
# function to remove the empty lines from the instruction list 
def removeEmptyLines(myList):
    ansList=[]
    for i in myList:
        if(len(i)>1):
            #appending the instruction lines and also removing '\n' from them
            ansList.append(i.strip())
    return ansList
# function take a text file as the input and the remove the empty lines and generates the list of each line 
def takeInput():
    fileRead=open(r"input.txt","r")
    inTempList=fileRead.readlines()
    fileRead.close()

    instructionList=removeEmptyLines(inTempList)
    # for i in instructionList:
    #     print(len(i)," ")
    # print(instructionList)
    return instructionList