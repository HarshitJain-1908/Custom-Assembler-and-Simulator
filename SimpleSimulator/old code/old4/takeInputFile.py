# function which takes input using stdin and returns the list of the instrcutions
def takeInput():
    inTempList=[]

    # ********************************un comment if taking input from input.txt file but comment while testing ******************************
    # fileRead=open(r"input.txt","r")
    # inTempList=fileRead.readlines()
    # fileRead.close()
    # #removing newline character from each instruction
    # for i in range(len(inTempList)-1):
    #     inTempList[i]=inTempList[i][0:-1]
    #*************************************************************************************************************************
    
    #-------------- uncomment to take input for testing but comment if taking input manually -------------------------
    while True:
        try:
            temp=input()
            inTempList.append(temp)
            
        except EOFError as e:
            break
    #---------------------------------------------------------------------------------------------------------------
    return inTempList

# ans=takeInput()
# for i in ans:
#     print(i," ",len(i))
