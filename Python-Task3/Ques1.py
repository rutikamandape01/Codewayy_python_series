#Program containing personal details using five different functions

#funcrtion myName
def myName():
    myName=input("Enter your full nam :")
    print("My name is :",myName)

#function myMarks
def myMarks():
    dataStructure=int(input("Enter marks:"))
    computerNetwork=int(input("Enter marks:"))
    operatingSystem=int(input("Enter marks:"))
    artificialIntelligence=int(input("Enter marks:"))
    global totalMarks
    totalMarks=dataStructure+computerNetwork+operatingSystem+artificialIntelligence
    print("Total marks is : ",totalMarks)

#function myPercentage
def myPercentage():
    global score
    score=(totalMarks)/4
    print("My percentage is : ",score,"%")

#function myGrade  
def myGrade():
    if(score>=95):
        print("Your Grade is :A")
    elif(score>=85 and score<=95):
       print("Your Grade is : B")
    elif(score>=75 and score<=85):
        print("Your Grade is : C")
    elif(score>=65 and score<=75):
        print("Your Grade is : D")
    else:
        print("You are fail ")

        
#creating studentDetails fucntion to call other fucntions
def studentDetails():
    myName()
    myMarks()
    myPercentage()
    myGrade()
studentDetails()
    
    
   
    
    


    
