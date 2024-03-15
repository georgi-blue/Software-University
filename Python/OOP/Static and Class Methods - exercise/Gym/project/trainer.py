from project.new_id_mixin import NewIdMixin


class Trainer(NewIdMixin):
    id = 1
    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()
        self.increment_id()

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
