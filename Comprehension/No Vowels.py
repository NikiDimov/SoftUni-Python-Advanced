result = [char for char in input() if not (char.lower() == "a" or char.lower() == "o" or char.lower() == "u"
                                           or char.lower() == "e" or char.lower() == "i")]
print(''.join(result))
