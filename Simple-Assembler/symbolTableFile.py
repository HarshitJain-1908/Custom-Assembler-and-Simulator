# function to return the location of the variable and the location of the label instruction

def symbolLocation(lst,mylist):
    # now we make the sublist of labels and variables
    # Basically, making a dictionary with labels and variables with the assumption 
    # that they have been defined only once in the program
    symbol={}

    count_var=0
    flag=0
    for i in range(len(lst)):
        l=lst[i].split()
        if(l[0]=="var"):
            count_var+=1
            if(flag==1):
                flag=2
                break
        else:
            flag=1
    if(flag==2):
        line=lst[i][-1]
        print("error in line",line)
        return -1
    
    #iterating over the instruction list
    for i in range(len(mylist)):
        # checking for statements with labels
        if( ":" in mylist[i]):
            lst=mylist[i].split()
            if(lst[0][-1]==":"):
                #first get the label name and then it's location
                #Before that getting the keywords in the instruction list
                termList=mylist[i].split()
                #removing :
                termList[0]=termList[0][0:len(termList[0])-1]
                #putting the key with value in our dictionary
                symbol[termList[0]]=int(termList[-2])
            else:
                line=lst[i][-1]
                print("error in line",line)
                return -1

    return symbol


