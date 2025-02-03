print("Welcome to the Tips Calculator")
bill = float ( input( "What was the total bill? $ " ) )
tip = float ( input( "How much tip would you like to give? 10, 12, or 15 ?" )) 
tip_perc = tip / 100
tip_amount = tip_perc * bill
new_bill = bill + tip_amount
bill_split = float( input ( "how many people to split the bill?" ) )
pay_per_person = round( new_bill / bill_split, 2 )

print( f"Each person should pay : $ {pay_per_person}" )
