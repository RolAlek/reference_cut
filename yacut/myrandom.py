from random import sample, shuffle
import string


symbols = list(string.ascii_letters + string.digits)
shuffle(symbols)
result = ''.join(sample(symbols, 6))
print(result)