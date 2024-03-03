class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")


info = input()
emails = []

while info != 'Stop':
    sender,receiver,content = info.split(" ")
    email = Email(sender, receiver, content)
    emails.append(email)
    info = input()


indexes = [int(index) for index in input().split(", ")]

for index in indexes:
    emails[index].send()

for current_email in emails:
    current_email.get_info()

