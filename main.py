# Задание 1
# Создайте реализацию паттерна Builder. Протестируйте 
# работу созданного класса

class Computer:
    def __init__(self, processor, memory, storage, graphics_card):
        self.processor: str = processor
        self.memory: int = memory
        self.storage: str = storage
        self.graphics_card: str = graphics_card

    def __str__(self):
        return f"Computer: Processor - {self.processor}, Memory - {self.memory}, Storage - {self.storage}, Graphics Card - {self.graphics_card}"

class ComputerBuilder:
    def __init__(self):
        self.processor = str
        self.memory = int
        self.storage = str
        self.graphics_card = str

    def set_processor(self, processor):
        self.processor = processor
        return self

    def set_memory(self, memory):
        self.memory = memory
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self

    def set_graphics_card(self, graphics_card):
        self.graphics_card = graphics_card
        return self

    def build(self):
        return Computer(self.processor, self.memory, self.storage, self.graphics_card)


builder = ComputerBuilder()
computer = builder.set_processor("Intel i7").set_memory("16GB").set_storage("512GB SSD").set_graphics_card("Nvidia RTX 2080").build()

print(computer)


# создайте приложение для приготовления пасты. Приложение должно и{% load иметь_tags %} создавать минимум три вида пасты. Классы различной пасты должны иметь следующие 
# методы:
# ■ Тип пасты;
# ■ Соус;
# ■ Начинка;
# ■ Добавки.
# Для реализации используйте порождающие паттерны.


from abc import ABC, abstractmethod


class Pasta(ABC):
    
@abstractmethod
def get_type(self):
  raise ValueError(“Обязательно”)


@abstractmethod
 def get_sauce(self):
  raise ValueError(“Обязательно”)

@abstractmethod
 def get_fillings(self):
  raise ValueError(“Обязательно”)

@abstractmethod
 def get_toppings(self):
  raise ValueError(“Обязательно”)


class Spaghetti(Pasta):
 
 def get_type(self):
  return “Спагетти”

 def get_sauce(self):
  return “Томатный соус”

 def get_fillings(self):
  return “Говяжий фарш”

 def get_toppings(self):
  return “Сыр Пармезан”


class Penne(Pasta):
 
 def get_type(self):
  return “Пенне”

 def get_sauce(self):
  return “Песто”

 def get_fillings(self):
  return “Брокколи”

 def get_toppings(self):
  return “Оливковое масло”


class Fettuccine(Pasta):
 
 def get_type(self):
  return “Феттучини”

 def get_sauce(self):
  return “Крем-соус”

 def get_fillings(self):
  return “Курица”

 def get_toppings(self):
  return “Петрушка”


class PastaFactory:

@staticmethod
def create_pasta(pasta_type):
 if pasta_type == “спагетти”:
 return Spaghetti()
elif pasta_type == “пенне”:
 return Penne()
elif pasta_type == “феттучини”:
 return Fettuccine()
else:
 raise ValueError(“Неизвестный тип пасты”)


def main():
pasta_type = input(“Введите тип пасты (спагетти, пенне, феттучини): “).lower()
pasta = PastaFactory.create_pasta(pasta_type)

print(f”Тип пасты: {pasta.get_type()}”)
print(f”Соус: {pasta.get_sauce()}”)
print(f”Начинка: {pasta.get_fillings()}”)
print(f”Добавки: {pasta.get_toppings()}”)

if __name__ == “__main__”:
main()



# {% load Создайте реализацию паттерна Prototype. Протестируйте работу созданного класса._tags %}

import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype1(Prototype):
    def __init__(self, name: str):
        self.name:str = name
    
    def __str__(self):
        return f"ConcretePrototype1: {self.name}"

class ConcretePrototype2(Prototype):
    def __init__(self, name str, value: int):
        self.name: str = name
        self.value:int = value
    
    def __str__(self):
        return f"ConcretePrototype2: {self.name}, {self.value}"
    
    def main():
    # Создание прототипов
    prototype1 = ConcretePrototype1
    prototype2 = ConcretePrototype2

    # Клонирование
    clone1 = prototype1.clone()
    clone2 = prototype2.clone()

    # Вывод информации о клонах
    print(clone1) 
    print(clone2) 

    
    prototype1.name = "Modified Prototype 1"
    prototype2.value = 99

    print(prototype1) 
    print(clone1)     
    
    print(prototype2) 
    print(clone2)     
