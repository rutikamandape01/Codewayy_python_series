#personal details

#declaring variables
firstName="Rutika"
middleName="Balkrushna"
lastName="Mandape"
collegeName="Yeshwantrao Chavan College of Engineering"
address="Nagpur,Maharashtra "
marksEconomics = 90
marksSoftwareEngineering =75
marksComputerNetwork = 87
marksOperatingSystem = 83
marksAI =85

#String concatention for full name
fullName=firstName+middleName+lastName
#string concatenation for college name and address
collegeAddress= collegeName+","+address

#printing full name
print("My name is ",fullName)
#printing college name and address
print(collegeAddress)

#printing marks in every all subject

print("Economics=",marksEconomics)
print("Software Engineering=",marksSoftwareEngineering)
print("Computer network=",marksComputerNetwork)
print("operating system=",marksOperatingSystem
print("Artificial intelligence=",marksAI)

#printing total marks
totalMarks=marksEconomics+marksSoftwareEngineering+marksComputerNetwork+marksOperatingSystem+marksAI
print("Total marks=",totalMarks)
#printing percentage
percentage=round((totalMarks/500)*100)
percentage="{}% ".format(percentage)
print("percentage=",percentage)

