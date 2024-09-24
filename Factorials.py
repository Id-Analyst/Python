num = int( input('Type a number ') )
def product (num ):
    if num < 0:
        return None
    return num + product( num - 1)

product(4)



