###Author: Tyler Freeman
###Date 09/06/2021
###Professor BobleDyk
###Assignment: logical expression calculator based on 2 binary inputs



###@getInputA() - prompt the user for the first piece of input and return as a variable @value1
def getInputA():
    #prompt and set your variable
    value1 = input("Please enter a binary value for input 1:\n");
    #check for valid inputs else try again
    if(value1 != "0" and value1 != "1"):
        print("You have entered an invalid value of type " + str(type(value1)));
        getInputA();  
    #type change variable
    value1 = int(value1);
    #return the variable
    return value1

###@getInputB() - prompt the user to enter the second piece of input and return @value2
def getInputB():
    #prompt and capture variable
    value2 = input("Please enter a binary value for input 2:\n");
    #check for valid inputs
    if(value2 != "0" and value2 != "1"):
        print("You have entered an invalid value of type" + str(type(value2)));
        getInputB();
    #type change variable
    value2 = int(value2);
    #return variable
    return value2

###@getOperator() - prompt the user to enter a logical expression and capture in a variable and return @operator
def getOperator():
    #prompt and capture variable
    operator = input("Enter the operator you'd like to perform by entering \"OR\", \"XOR\", or \"AND\"\n");
    #check for valid input else go again
    if operator != "AND" and operator != "OR" and operator != "XOR":
        print("You have entered an invalid operator please try again")
        getOperator();
    #return input
    return operator;

###@goAgain() - After the user is done, ask them if they'd like to calculate another expression or quit return @go
def goAgain():
    #capture and prompt user for input to control the program
    go = input("If you would like to calculate another expression press \'y\'.\nIf you would like to quit press \'q\':\n")
    #check for valid input else try again
    if go != 'y' and go != 'q':
        print("You entered an incorrect key, please try again");
        goAgain();
    #decide what to do based on input
    else:
        if go == 'y':
          main();
        if go == 'q':
            print("Thanks for using the expression calculator");

###@main() function starts the program and calls appropriate helper functions
def main():

    print("We are going to enter two binary inputs (0 or 1) and compute \nthe logical OR, XOR, or AND expressions of the two inputs.");
    value1 = getInputA();
    #print(str(value1) + " " + str(type(value1))); type checking
    value2 = getInputB();
    #print(str(value2) + " " + str(type(value2))); type checking
    operator = getOperator();

    #convert inputs to booleans to perform boolean logic
    if value1 == 0:
        value1 = False;
    if value1 == 1:
        value1 = True;
    if value2 == 0:
        value2 = False;
    if value2 == 1:
        value2 = True;

    #If the operator is AND then calculate the result and convert data types to input format
    if operator == "AND":
        result = value1 and value2;
        if result == False:
            result = 0;
        if result == True:
            result = 1;
        print("The result of " + str(int(value1)) + " AND " + str(int(value2)) + " is: " + str(result));

    #If the operator is XOR then calculate the result and convert data types back to input format
    if operator == "XOR":
        result = value1 ^ value2;
        if result == False:
            result = 0;
        if result == True:
            result = 1;
        print("The result of " + str(int(value1)) + " XOR " + str(int(value2)) + " is: " + str(result));

    #If the operator is OR then calculate the result and convert data types to input format
    if operator == "OR":
        result = value1 or value2;
        if result == False:
            result = 0;
        if result == True:
            result = 1;
        print("The result of " + str(int(value1)) + " OR " + str(int(value2)) + " is: " + str(result));

    goAgain();

       

if __name__ == "__main__":
    main();