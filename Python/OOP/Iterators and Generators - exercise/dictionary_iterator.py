class dictionary_iter:
    def __init__(self, elements: dict):
        self.elements = elements
        self.kvp = [kvp for kvp in self.elements.items()]
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == len(self.elements) - 1:
            raise StopIteration

        self.counter += 1
        return self.kvp[self.counter]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


