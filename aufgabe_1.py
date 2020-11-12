# Gruppe 2
# Moitov,   Carina
# Flaum,    Arthur
# Ewald,    Florian

def printOutput(Name, Value):
    print("         {0}{1}".format(Name, Value) )

def inputFloat(VarName):
    while True:
        numb = input("\n Please enter a float (separator '.' ) for Variable {}\n".format(VarName))
        try:
            numb = float(numb)
            return numb
        except ValueError:
            print("That was no valid number! \n")

#####################################
# Main Programm Aufgabe 1
#
# task: arithmetic mean of x, y and z
#####################################
# like allocation
# task 1.1
x        = 0
y        = 0
z        = 0
mean_xyz = 0

# task 1.2
mean_xy = 0
length  = 0
width   = 0
area    = 0

# task 1.2
testfloat = 0
maximum   = 0

# task 1.1
# read variables
x = inputFloat("x")
y = inputFloat("y")
z = inputFloat("z")
# calculate mean
mean_xyz = ( x + y + z )/3

# task 1.2
# calculate length and width of rectangle
length  = abs( (x + y ) / 2 )
width   = z**2
area    = length * width

# task 1.3
# testfloat = float(x < y)
# if testfloat == 1.0:
#     maximum = y
# elif testfloat == 0.0:
#     # is also used if x == y
#     maximum = x
maximum = float(x>y)*x + float(x<y)*y + float(x==y)*x

# print section
#####################################
print("\nEingabe:")
printOutput("x = ", x)
printOutput("y = ", y)
printOutput("z = ", z)
print("Ausgabe:")
printOutput("Arithmetisches Mittel:  ", mean_xyz)
printOutput("Flaeche:                ", area)
printOutput("Maximum (x oder y):                ", maximum)
