string = [el.strip()for el in input().split('|')]
string = [el.split()for el in string]
print(' '.join([el for row in string[::-1] for el in row]))