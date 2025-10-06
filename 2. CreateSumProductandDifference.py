# Ask the user for two numbers using input(), then print their total, difference, and product.

num1 = int( input( "type in your first number\n" ) )
num2 = int( input( "type in your second number\n" ) )

product = num1 * num2
difference = num1 - num2
total = num1 + num2

print(f'Here is the result of the numbers: total = {total}, difference = {difference}, and product = {product}')