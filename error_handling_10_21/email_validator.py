class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


mail = input()
valid_domains = {"com", "bg", "net", "org"}
while not mail == "End":
    if '@' not in mail:
        raise MustContainAtSymbolError("Email must contain @")
    name, domain = mail.split('@')
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")
    if domain.split('.')[-1] not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    print("Email is valid")
    mail = input()
