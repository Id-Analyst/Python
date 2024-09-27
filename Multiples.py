# print multiples of any number up to a max number

i = 0 # this is the start point
j = int( input( "enter the multiples you want: " ) ) # the multiples you want
iRange = range( int( input( "enter the max number: " ) ) ) # makes a list of all numbers up to a max

while i <= max(iRange):
    if i % j == 0 and i != 0:
        print(i)
    i += 1