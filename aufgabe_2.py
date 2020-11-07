def printOutput(Name, Value):
    print("         {0}{1}".format(Name, Value) )

def inputString():
    while True:
        w = input("\n Please enter a String with >= 9 letters / symbols and < 100 letters / symbols\n \n")
        l = len(w)
        if  l >= 10 and l < 100:
            return w, l
        else:
            if l < 10:
                print("\n length of the String is < 10.\n")
                print("Enter a String with {} more letters / symbols".format(10-l) )
            elif l >= 100:
                print("\n length of the String is >= 100.\n")
                print("Enter a String with {} less letters / symbols".format(l-100) )

#####################################
# Main Programm Aufgabe 2
#
# task: read string and manipulate it
#####################################
# like allocation
# task 2.1
w = ""
l = 0

# task 2.2
A      = 0
B      = 0
AB     = 0
BA     = 0


# task 2.3
sum_AB = 0
sub_AB = 0
pro_AB = 0
div_BA = 0

# task 2.1
w, l = inputString()

# task 2.2
AB = l
A = l//10
B = l%10
# multiply B*10 to get the change to a decadic number
BA = 10*B + A
# usage of string to also get the zeros 
# length = 30 -> BA = 3 as Integer, BA2 = 03 as Strings
BA2 = str(B) + str(A)

# task 2.3
sum_AB = A + B
sub_AB = B - A
pro_AB = A * B
div_BA = B / A
# print section
#####################################
print("\nEingabe: ")
printOutput("String w: ", w)
print("Ausgabe:")
printOutput("Type: " , type(w))
printOutput("Length: " , l)
printOutput("AB = ", AB)
printOutput("BA = ", BA)
printOutput("BA = ", BA2)
printOutput("A + B = ", sum_AB)
printOutput("B - A = ", sub_AB)
printOutput("A * B = ", pro_AB)
printOutput("B / A = ", div_BA)