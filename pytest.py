print("hey guys")
print("try again")

def calculateSalary(hours, costPerHr):
    return hours * costPerHr

def calculateSalaryUs(salary):
    return salary * 0.8

mySalary = calculateSalary(30, 50)
mySalaryUs = calculateSalaryUs(mySalary)

print(mySalary)
print(mySalaryUs)
print("finished")