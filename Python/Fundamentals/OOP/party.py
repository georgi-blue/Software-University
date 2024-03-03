class Party:
    def __init__(self):
        self.people = []

party = Party()
command = input()
total_people = 0

while command != 'End':
    name = command
    party.people.append(name)
    total_people += 1
    command = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {total_people}")