key = ["bin", "dec", "hex", "oct"]
list_dict = [{"bin": bin(a), "dec": (a), "hex": hex(a), "oct": oct(a)} for a in range(16)]

from pprint import pprint
pprint(list_dict)