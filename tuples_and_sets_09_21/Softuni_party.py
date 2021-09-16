N = int(input())
party = set()
for _ in range(N):
    code = input()
    party.add(code)
guest = input()
while not guest == 'END':
    if guest in party:
        party.remove(guest)
    guest = input()
print(len(party))
for student in sorted(party):
    print(student)