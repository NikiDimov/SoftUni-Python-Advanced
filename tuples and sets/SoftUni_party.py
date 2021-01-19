n = int(input())
party = set()
for _ in range(n):
    guest = input()
    party.add(guest)
command = input()
while not command == "END":
    if command in party:
        party.remove(command)
    command = input()
print(len(party))
for guest in sorted(party):
    print(guest)
    