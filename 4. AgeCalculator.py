#Ask the user for their birth year, calculate their age (use 2025 as current year), and tell them how old they'll be in 10 years.

birthYear = int( input( "type in your birth year\n" ) )
currentYear = 2025

currentAge = currentYear - birthYear

agein10Years = currentAge + 10

print(f'you will be {agein10Years} years old in 10 years')