name = input( "what is your name? " ) # gets the user's name
def welcome(name):
    print( "welcome, " + name )

welcome(name)

def inputnum():
    num = int( input ("enter a number: ") ) # gets an input from the user
    return num
    
number = inputnum() 

while number == 10:
    print("Congratulations, you got it " + name)
    break
else:
    inputnum()
