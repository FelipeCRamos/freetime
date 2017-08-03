# CODED BY FelipeCRamos
# FOR FREETIME

''' funcs stay here '''
def main(): # main func
    answer = input("\nPlease select one operation: ")
    if (answer == 'sum'): # if user selects 'sum'
        sum(convert(getPolynom()), convert(getPolynom())) # working
    elif(answer == 'sub'): # if user selects 'sub'
        sub(convert(getPolynom()), convert(getPolynom())) # working
    elif(answer == 'multi'): # if user selects 'multi'
        print("This operation it's not ready yet.")
        main()
        #multi(convert(getPolynom()), convert(getPolynom())) # not working yet
    elif(answer == 'div'): # if user selects 'div'
        print("This operation it's not ready yet.")
        main()
        #div(convert(getPolynom()), convert(getPolynom())) # not working yet
    else:
        print("Please select a valid operation keyword!")
        main()

def sum(p1, p2):
    length = int(len(p1))-1
    counter = 0
    result = []
    while (counter <= length):
        try:
            result.append(p1[counter] + p2[counter])
            counter += 1
        except ValueError:
            print("Invalid operation, please put only numbers on the entry field.")
            main()
    print("The result was: %sx² %sx %s" %(representPolynom(result)))
    main()

def sub(p1, p2):
    length = int(len(p1))-1
    counter = 0
    result = []
    while (counter <= length):
        try:
            result.append(p1[counter] - p2[counter])
            counter += 1
        except ValueError:
            print("Invalid operation, please put only numbers on the entry field.")
            main()
    print("The result was: %sx² %sx %s" %(representPolynom(result)))
    main()

def multi(p1, p2):
    length = int(len(p1))-1
    length2 = int(len(p2))-1
    counter = 0
    result = []
    if (length == length2):
        c = 0
        while c <= (int(len(p1))-1):
            c2 = 0
            result_line = []
            while c2 <= 2:
                result_line.append(p1[c]*p2[c2])
                c2 += 1
            result.append(result_line)
            c += 1
        print(result)

#def div(p1, p2):
    # in development

def convert(p):
    length = int(len(p))-1
    counter = 0
    converted = []
    while (counter <= length):
        try:
            converted.append(int(p[counter]))
            counter += 1
        except ValueError:
            print("Invalid operation, please put only numbers on the entry field.")
            main()
    return converted

def getPolynom():
    p = input("Please, type the polynom here: (using only numbers, i.a.: '1 3 -5' to represent '1x² + 3x - 5') ").split(' ')
    return p

def representPolynom(p):
    length = int(len(p))-1
    counter = 0
    r = [] # representation of the polynom
    while (counter <= length):
        try:
            if (counter == 0):
                if (p[counter] == 1):
                    r.append(' ')
                elif (p[counter] == -1):
                    r.append('-')
                elif (p[counter] > 1):
                    r.append(str(p[counter]))
                elif (p[counter] < -1):
                    r.append('-' + str(p[counter])[1:])
                elif(p[counter] == 0):
                    r.append('0')
            elif (counter == 2):
                if (p[counter] == 1):
                    r.append('+ 1')
                elif (p[counter] == -1):
                    r.append('- 1')
                elif (p[counter] == 0):
                    r.append(' ')
                elif (p[counter] > 1):
                    r.append('+ ' + str(p[counter]))
                elif (p[counter] < 1):
                    r.append('- ' + str(p[counter])[1:])
            else:
                if (p[counter] > 0):
                    if (p[counter] == 1):
                        r.append('+ ')
                    else:
                        r.append('+ ' + str(p[counter]))
                elif (p[counter] < 0):
                    if (p[counter] == -1):
                        r.append('- ')
                    else:
                        r.append('- ' + str(p[counter])[1:])
                elif (p[counter] == 0):
                    r.append('+ 0')
                else: # what the f* is this number?
                    print("i have not preddicted this number, congrats! :)")
            counter += 1
        except ValueError:
            print("Could you please use only integers, please? ")
            main()
    return r[0], r[1], r[2]



''' end funcs '''

print("\n\n     Be welcome to the Polynom Calculator\n\n     Developed by Felipe Ramos    v1.1\n\n")
print("-------------------- Guide --------------------")
print("Use one of the following keywords to use the calculator;")
print("'sum', 'sub', 'multi', 'div';")
print("-----------------------------------------------")
main()
