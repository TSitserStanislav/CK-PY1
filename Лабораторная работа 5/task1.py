from pprint import pprint

list_dict = [{"bin": bin(a), "dec": (a), "hex": hex(a), "oct": oct(a)} for a in range(16)]
pprint(list_dict)