from typing import List


class EmailValidator:
    def __init__(self, min_lenght: int, mails: List, domains: List):
        self.min_lenght = min_lenght
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name: str) -> bool:
        return len(name) >= self.min_lenght

    def __is_mail_valid(self, mail: str) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain: str) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        username, data = email.split('@')
        mail, domain = data.split('.')

        is_valid = (self.__is_name_valid(username) and
                    self.__is_mail_valid(mail) and
                    self.__is_domain_valid(domain))

        if is_valid:
            return True

        return False

mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))


