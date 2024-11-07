age=20
if(age>=18):
    print("can vote & apply for voting liscense")

# elif and else program
light="red"
if(light == "red"):
    print("STOP")
elif(light=="Green"):
    print("GO")
elif(light=="Yellow"):
    print("WAIT")  
    #in every elif and else program print is written after four spaces which is called indentation 
else:
    print("light is brocken") # else is always used in last and used for one time


    #program for grade of students
marks=int(input("Enter student marks: "))
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
    
print("grade of the student ->",grade)


#Nested else if statement
Age=20
if(Age>=18):
    if(Age>=80):
        print("Cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")