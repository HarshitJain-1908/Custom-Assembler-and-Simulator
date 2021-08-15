# functiion to return the location of the variable and the location of the label instruction

def symbolLocation(myInstructionList):
    # now we make the sublist of labels and variables
    # Basically, making a dictionary with labels and variables with the assumption 
    # that they have been defined only once in the program
    symbol={}
    
    #iterating over the instruction list
    for i in myInstructionList:
        # checking for statements with labels
        if(":" in i):
            #first get the label name and then it's location
            #Before that getting the keywords in the instruction list
            termList=i.split()
            #removing :
            termList[0]=termList[0][0:len(termList[0])-1]
            #putting the key with value in our dictionary
            symbol[termList[0]]=termList[len(termList)-1]
        elif("var" in i):
            termList=i.split()
            symbol[termList[1]]=termList[2]
    return symbol


