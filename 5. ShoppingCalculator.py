#Create a simple shopping calculator. Ask the user for 3 item prices and a discount percentage. Calculate the total, apply the discount, and show both the original total and discounted price.

_item1_price = float( input( "type in the price of item 1\n" ) )
_item2_price = float( input( "type in the price of item 2\n" ) )
_item3_price = float( input( "type in the price of item 3\n" ) )

_discount = float( input( "type in the discount percentage of item 1\n" ) )

_total_amount = ( _item1_price + _item2_price + _item3_price ) 
_total_amount_discounted = ( _item1_price + _item2_price + _item3_price ) * ( (100 - _discount ) / 100 )

print(f'The orignal order amount is {_total_amount} while the discounted amount is {_total_amount_discounted}')