#Program containing personal details using five different functions

#funcrtion myName

def myName(name):
    return(name)

#function myMarks

def myMarks(marksList):
    totalMarks=sum(marksList)
    return (totalMarks)

#function myPercentage

def myPercentage(noOfSubjects,totalMarks):
    
    perc=(totalMarks)/(noOfSubjects)
    return(perc)

#function myGrade  

def myGrade(score):
    if(score>=95):
        return('A')
    elif(score>=85 and score<=95):
       return('B')
    elif(score>=75 and score<=85):
       return('C')
    elif(score>=65 and score<=75):
       return('D')
    else:
        return ("You are fail")

        
#creating studentDetails fucntion to call other fucntions

def studentDetails(name, noOfSubjects,marksList):
    print("My name is",my name(name))
    totalMarks=myMarks(marksList)

    print("My marks is",totalMarks)
    score=myPercentage(noOfSubjects, totalMarks)
    print("My percentage is",score)

    grade=myGrade(score)
    print("My grade is",grade)

name=input("Enter your name")

marksList=[]
noOfSubjects=int(input("Enter the number of subjects"))

for i in range (noOfSubjects):
    marks=int(input("Enter marks"))
    marksList.append(marks)

studentDetails(name, noOfSubjects, marksList)
    
    
   
    
    


    
