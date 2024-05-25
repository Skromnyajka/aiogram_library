
from abc import ABC, abstractmethod
from typing import Union

#Родительский класс полей
class Field(ABC):
    def __init__(self, text:str, state, validator:function=None, type_error:str='Ошибка типа данных', validating_error:str='Ошибка валидации'):
        self.text = text
        self.state = state
        self.validator = validator
        
        self.type_error = type_error
        self.validating_error = validating_error
        
    @abstractmethod
    @property
    #Функция проверки типа поля
    def field_type(self, answer:str) -> bool:
        self.answer = answer
        self.answer_type:Union[bool, None] = None
        if self.validate(answer=self.answer): #Проверка валидации
            if self.answer_type: #Проверка типа данных
                return True
            else:
                return self.type_error
        else:
            return self.validating_error

    #Функция-алидатор
    def validate(self, answer:str) -> bool:
        self.answer = answer
        try: #Проверка на правильность типа(функция) валидатора
            if self.validator(self.answer) in [True, False]: #Проверка на правильность работы функции-валидатора
                return self.validator(self.answer)
            else:
                raise ValueError('Ошибка значения валидатора')
        except:
            raise ValueError('Ошибка валидатора')

    def question(self) -> str:
        pass

#Класс строкового поля
class CharField(Field):
    def __init__(self, min_length:int=None, max_length:int=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_length = min_length #Минимальная длинна строки
        self.max_length = max_length #Максимальная длинна строки

    #Функция проверки типа поля
    def field_type(self, answer:str) -> bool:
        super().field_type(answer)
        self.answer_type:bool = self.answer.isdigit() #Проверка типа данных

#Класс числового поля
class IntegerField(Field):
    #Функция проверки типа поля
    def field_type(self, answer:str) -> bool:
        super().field_type(answer)
        self.answer_type:bool = isinstance(self.answer, str) #Проверка типа данных
