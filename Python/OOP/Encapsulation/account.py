class Account:
    def __init__(self, a_id: int, balance: float, pin: int):
        self.__id = a_id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin: int) -> str:
        if self.__pin != pin:
            return "Wrong pin"

        return self.__id

    def change_pin(self, old_pin: int, new_pin: int) -> str:
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"

        return "Wrong pin"

account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))

