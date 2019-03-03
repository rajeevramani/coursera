def sxor(s1,s2):    
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))


if __name__ == "__main__":
    print()
    key = sxor('attack at dawn',"6c73d5240a948c86981bc294814d".decode("hex"))
    print(key)
    newtext = sxor('attack at dusk',key)
    print(newtext)
    print(newtext.encode('hex'))