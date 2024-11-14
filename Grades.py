gradelist = []
studentgrades = 1


while True:
    grade = float(input("Enter your grade :"))
    if grade.lower() == "done":
        print("exiting...")
        break

    if 40 <= grade <= 100:
        gradelist.append(grade)
        studentgrades += 1
        
    else:
        print("Incorrect Data")
    
        
average = sum(gradelist) / len(gradelist)

failedgrades = 0
passinggrades = 0
for grade in gradelist:
    if grade >= 75:
        passinggrades += 1
    else:
        failedgrades += 1
        
passingpercentage = (passinggrades / len(gradelist)) * 100

print("List of grades given: ", gradelist)
print("Your average grade is: ", average)
print("Your passing percentage is: ", passingpercentage, "%")
print("Passed grades: ", passinggrades)
print("Failed grades: ", failedgrades)