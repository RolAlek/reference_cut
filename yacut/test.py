from random import sample, shuffle
import string


symbols = list(string.ascii_letters + string.digits)
shuffle(symbols)
short_id = ''.join(sample(symbols, 6))
print(short_id)