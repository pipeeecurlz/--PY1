from pprint import pprint

pprint([{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(16)])

