from abc import ABC, abstractmethod
from typing import Callable


class Field(ABC):
    def __init__(self, text: str, state, validator: Callable[[str], bool], type_error: str = 'Ошибка типа данных', validating_error: str = 'Ошибка валидации'):
        self.text = text
        self.state = state
        self.validator = validator
        
        self.type_error = type_error
        self.validating_error = validating_error
        
    @abstractmethod
    @property
    # Функция проверки типа поля
    def field_type(self) -> bool:
        pass

    # Функция-алидатор
    def validate(self, answer: str) -> bool:
        self.answer = answer

        if self.field_type(): # Проверка типа данных
            if self.validator(self.answer): # Проверка на правильность работы функции-валидатора
                return True
            else:
                return self.validating_error
        else:
            return self.type_error

    def question(self) -> str:
        pass

# Класс строкового поля
class CharField(Field):
    def __init__(self, min_length: int=None, max_length: int=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_length = min_length # Минимальная длинна строки
        self.max_length = max_length # Максимальная длинна строки

    # Функция проверки типа поля
    def field_type(self) -> bool:
        return self.answer.isdigit() # Проверка типа данных

# Класс числового поля
class IntegerField(Field):
    # Функция проверки типа поля
    def field_type(self) -> bool:
        return isinstance(self.answer, str) # Проверка типа данных