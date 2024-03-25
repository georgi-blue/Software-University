from abc import ABC, abstractmethod
from math import log2


class Computer(ABC):
    ONE_BLOCK_OF_RAM_PRICE: int = 100

    def __init__(self, manufacturer: str, model: str):
        self.model = model
        self.processor = None
        self.manufacturer = manufacturer
        self.ram = None
        self.price = 0

    @staticmethod
    def power_of_two(ram: int):
        result = log2(ram)
        return result.is_integer()

    @property
    @abstractmethod
    def max_ram(self):
        ...
    @property
    @abstractmethod
    def allowed_processors(self):
        ...

    @property
    @abstractmethod
    def type(self):
        ...

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")

        self.__model = value

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")

        self.__manufacturer = value

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.allowed_processors:
            raise ValueError(f"{processor} is not compatible with {self.type} {self.manufacturer} {self.model}!")

        if ram > self.max_ram or not self.power_of_two(ram):
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")

        self.set_parts(processor, ram)

        return f"Created {self.__repr__()} for {self.price}$."

    def set_parts(self, processor: str, ram: int):
        self.processor = processor
        self.ram = ram
        self.price += self.allowed_processors[processor]
        self.price += int(log2(ram)) * self.ONE_BLOCK_OF_RAM_PRICE

    def __repr__(self):
        return f"{self.manufacturer} {self.model} with {self.processor} and {self.ram}GB RAM"