class vowels:

    def __init__(self, string):
        self.string = string
        self.start_index = - 1
        self.vowels_list = ['a', 'e', 'i', 'u', 'y', 'o']
        self.vowels = [s for s in self.string if s.lower() in self.vowels_list]

    def __iter__(self):
        return self

    def __next__(self):
        self.start_index += 1
        if self.start_index < len(self.vowels):
            return self.vowels[self.start_index]
        raise StopIteration


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


