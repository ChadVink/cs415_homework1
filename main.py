from add_mult import *
#import conversions

debug = False
showSolution = False
test_option = "2"
input_string = "5,9,9,4"

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
        if showSolution:
            a = pow(ui[0], ui[1])
            b = pow(ui[2], ui[3])
            sol = a-b
            print("Problem3a solution: " + str(a) + " - " + str(b) + " = " + str(sol) )
        solution = Problem3a(ui[0], ui[1], ui[2], ui[3])
        print(solution)

    elif user_option == "2": #Problem3b
        if showSolution:
            a = pow(ui[0], ui[1])
            b = pow(ui[2], ui[3])
            quo = a/b
            rem = a%b
            print("Problem3b solution: " + str(a) + " / " + str(b) + " = " + str(quo) + "r" + str(rem) )
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

    if debug:
        m = ab[:]
        n = cd[:]
        print("Test: " + str(bin2dec(m)) + "-" + str(bin2dec(n)))

    solution, isNegitive = subtract(ab, cd)
    if isNegitive: # if c^d > a^b
        return bin2dec(solution) * -1
    else:
        return bin2dec(solution)

def Problem3b(a, b, c, d):
    #  quotient and the remainder when A^B is divided by C^D
    ab = power(dec2bin(a),dec2bin(b))
    cd = power(dec2bin(c),dec2bin(d))

    print(bin2dec(ab), bin2dec(cd))

    q, r = divide(ab,cd)
    return bin2dec(q), bin2dec(r)

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
    numBits = max(len(b), len(a)) # Length of largest number to check for overflow bit
    if len(a) > len(b): # Make b the same length of a so 2's compliment works properly
        for i in range(len(a)-len(b)):
            b.append(0)

    c = add(a, twosCompliment(b))
    if len(c) > numBits: # c has overflow bit so it is positive
        c = addOne(c)
        isNegitive = False
        c.pop() # Remove the overflow bit
    else: # c doesn't have overflow bit so it is negitve
        c = twosCompliment(c)
        isNegitive = True
    return c, isNegitive

def Subtract(a, b):
    # subtract two ints
    if(debug):
        print(str(a) + "-" + str(b))
    return bin2dec(subtract(dec2bin(a),dec2bin(b)))

def divide(n, d):
    # n(umerator)/d(enominator) in a binary array
    #returns the quotient and remainder
    if zero(d):
        print("Cannot divide by 0.")
        exit()
    if zero(n):
        return [], []
    q, r = divide(div2(n), d)
    q = shift(q,1)
    r = shift(r,1)
    if not even(n):
        r = addOne(r)
    if isGreater(r, d):
        r, flag = subtract(r,d)
        q = addOne(q)
    return q, r



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

def isGreater (A, B): # is A greater than B
    A1 = A[:]
    B1 = B[:]
    n = len(A1)
    m = len(B1)
    if n < m:
        for j in range(len(B1)-len(A1)):
            A1.append(0)
    else:
        for j in range(len(A1)-len(B1)):
            B1.append(0)
    N = max(m, n)
    # print("A1:", A1, "B1:", B1)
    for i in range (N-1, 0, -1): # compare bit by bit
        if A1[i] != B1[i]: # bits are not equal
            if A1[i] == 1: # most significant bit is higher than B
                # print("a > b")
                return True
            else:    # B is greater than A
                # print("b > a")
                return False
    return True

    # if len(A) > len(B):
    #     return True
    # if len(A) < len(B):
    #     return False
    # else:   # we know they are the same length
    #     for i in range (len(A)-1, 0): # compare bit by bit
    #         if A[i] != B[i]: # bits are not equal
    #             if A[i] == 1: # most significant bit is higher than B
    #                 return True
    #             else:    # B is greater than A
    #                 return False
    # return True    # they are equal


if debug:
    main()
else:
    while True:
        main()
