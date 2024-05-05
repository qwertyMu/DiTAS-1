print("Hello World")
print("Hello again")


#Variables 

#Int
lengthOfCupboard = 3

#Float
widthOfCupboard = 0.45

#String
nameOfCupboard = "3"

#Boolean
tired = True

#Operations
areaOfCupboard = lengthOfCupboard * widthOfCupboard




#Lists

listOfCars = ["Volvo", "Nissan", "BMW"]

#Loop

for car in listOfCars:
    print(car)



#Functions

def addTwoNumbersTogether(ageOfTom, ageOfTim):
    return ageOfTom + ageOfTim

#....



ageOfTom = 34
ageOfTim = 40

print(addTwoNumbersTogether(ageOfTom, ageOfTim))


#CONDITIONAL LOGIC


# If statement
age = 20
if age >= 18:
    print("You are an adult")

# If-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not too hot outside.")

# If-elif-else statement
score = 85
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
else:
    print("You need to improve.")

# Nested if statements
x = 10
y = 5
if x > 5:
    if y > 2:
        print("Both conditions are true.")





