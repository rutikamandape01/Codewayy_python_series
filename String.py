#personal details

#Declaring variables for full name
#declaring variables
fname="Rutika"
mname="Balkrushna"
lname="Mandape"
College_name="Yeshwantrao Chavan College of Engineering"
Address="Nagpur,Maharashtra "
Marks_Economics = 90
Marks_software_Engineering =75
Marks_computer_network = 87
Marks_operating_system = 83
Marks_AI =85

#String concatention for full name
Full_name=fname+mname+lname
#string concatenation for college name and address
college_Address= College_name+","+Address

#printing full name
print("My name is ",Full_name)
 #printing college name and address
print(college_Address)

#printing marks in every all subject

print("Economics=",Marks_Economics)
print("Software Engineering=",Marks_software_Engineering)
print("Computer network=",Marks_computer_network)
print("operating system=",Marks_operating_system)
print("Artificial intelligence=",Marks_AI)

#printing total marks
total_marks=Marks_Economics+Marks_software_Engineering+Marks_computer_network+Marks_operating_system+Marks_AI
print("Total marks=",total_marks)
#printing percentage
percentage=round((total_marks/500)*100)
percentage="{}% ".format(percentage)
print("percentage=",percentage)

