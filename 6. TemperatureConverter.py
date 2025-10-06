#Make a temperature converter that asks for a Celsius temperature and converts it to both Fahrenheit and Kelvin. Display the results nicely formatted.

_temperature_in_celcius = float( input( 'enter a temperature number in celcius\n' ) )

_temperature_in_kelvin = str ( _temperature_in_celcius + 273.15 ) + 'K'

_temperature_in_farenheit = str( ( 1.8 * _temperature_in_celcius ) + 32 ) + 'F'

print(f' The equivalent of this temperature {_temperature_in_celcius} is {_temperature_in_kelvin} in Kelvin and {_temperature_in_farenheit} in farenheit' )