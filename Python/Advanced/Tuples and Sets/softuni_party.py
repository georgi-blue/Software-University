tickets = set()

for _ in range(int(input())):
    current_ticket = input()

    tickets.add(current_ticket)


ticket = input()

while ticket != "END":
    if ticket in tickets:
        tickets.remove(ticket)
    ticket = input()

print(len(tickets))
for t in sorted(tickets):
    print(t)