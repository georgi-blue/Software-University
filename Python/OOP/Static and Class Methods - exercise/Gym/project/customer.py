from project.new_id_mixin import NewIdMixin

class Customer(NewIdMixin):
    id = 1
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()
        self.increment_id()

    def __repr__(self):
        return (f"Customer <{self.id}> {self.name}; "
                f"Address: {self.address}; Email: {self.email}")


