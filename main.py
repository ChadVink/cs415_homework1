from add_mult import *
#import conversions

debug = True
test_option = "1"
input_string = "5,43,31,34"

def main():
    if(debug):
        print("Testing option " + test_option)
        user_option = test_option
    else:
        user_option = str(input( "Would you like to test Problem3a(1) or Problem3b(2) or quit(3)?   "))

    if user_option == "3":
        # User option to quit the program
        print("Quiting.")
        exit()

    ui = getInput() # User Input

    if user_option == "1": #Problem3a
        print("Problem3a: " + str(pow(ui[0], ui[1])-pow(ui[2], ui[3])))
        solution = Problem3a(ui[0], ui[1], ui[2], ui[3])
        print(solution)

    elif user_option == "2": #Problem3b
        print("Problem3b:")
        (quotient, remainder) = Problem3b(ui[0], ui[1], ui[2], ui[3])
        print(quotient, remainder)

    else:
        print("Invalid input. Please enter option number 1, 2, or 3.")
        print("Exiting program.")
        exit()

    print("Program complete.")
    return

def Problem3a(a, b, c, d):
    # Outputs A^B-C^D
    ab = power(dec2bin(a),dec2bin(b))
    cd = power(dec2bin(c),dec2bin(d))
    solution, isNegitive = subtract(ab, cd)
    if isNegitive: # if c^d > a^b
        return bin2dec(solution) * -1
    else:
        return bin2dec(solution) # likely faster
    # return Subtract(Power(a,b),Power(c,d)) # More readable

def Problem3b(a, b, c, d):
    #  quotient and the remainder when A^B is divided by C^D
    return a, b

def power(a, x):
    # a, x are binary lists
    # Power of a^x
    r = [1]
    b = a # multiplier
    while len(x) > 1:
        if not even(x):
            r = mult(r, b)
        x = div2(x)
        b = mult(b,b)
    r = mult(r,b)
    return r

def Power(a, x):
    # a, x are ints
    # Power of a^x
    return bin2dec(power(dec2bin(a), dec2bin(x)))

def subtract(a, b):
    # subtracts two binary arrays
    # with LSB stored in index 0
    # return the binary array and a negitive flag
    numBits = len(b)
    c = add(a, twosCompliment(b))
    if len(c) > numBits: # c is positive
        c = addOne(c)
        isNegitive = False
        c.pop() # Remove the overflow bit
    else: # c is negitve
        c = twosCompliment(c)
        isNegitive = True
    return c, isNegitive

def Subtract(a, b):
    # subtract two ints
    if(debug):
        print(str(a) + "-" + str(b))
    return bin2dec(subtract(dec2bin(a),dec2bin(b)))

def twosCompliment(a):
    # Return negation of bit arrays
    for i in range(len(a)):
        if(a[i] == 0):
            a[i] = 1
        else:
            a[i] = 0
    return a

def addOne(a):
    # add one to binary array
    i = 0
    for i in range(len(a)):
        if a[i] == 0:
            a[i] = 1
            return a
        else:
            a[i] = 0
    return a.append(1)

def getInput():
    #Return the user input as an int list.
    if(debug):
        # If debug is turned on it will skip asking user for an input list and use a default list instead
        user_input = input_string
        print("user_input is: " + user_input)
    else:
        user_input = raw_input("Please enter four integers seperated by commas: ")
    int_list = map(int, user_input.split(',')) # Divids the user_input string into an int list

    if len(int_list) == 4: # Must have exactly four ints
        # Check if the four ints have been entered correctly
        for i in int_list:
            if not 0 < i < 1000:
                print("Invalid input. Please enter integers between 0 and 1000.")
                exit()
    else:
        print("Invalid input. Please enter four integers")
        exit()

    return int_list


if debug:
    main()
else:
    while True:
        main()
