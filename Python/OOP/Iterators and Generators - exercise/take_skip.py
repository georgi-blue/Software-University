class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.num_count = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num_count == self.count - 1:
            raise StopIteration

        self.num_count += 1
        return self.num_count * self.step

numbers = take_skip(2, 6)
for number in numbers:
    print(number)
