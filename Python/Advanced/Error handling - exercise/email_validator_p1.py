class NameTooShort(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

command = input()
ALLOWED_DOMAINS = (".bg",".com",".org",".net")

while command != "End":
    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")

    elif len(command[0]) <= 4:
        raise NameTooShort("Name must be more than 4 characters")

    elif command.split(".")[-1] not in ALLOWED_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    command = input()