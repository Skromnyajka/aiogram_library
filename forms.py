from typing import Union

from fields import Field


class Form:
    def __init__(self, *args) -> None:
        self.fields = args

        # Валидация полей
        if self.fields:
            for field in self.fields:
                if not isinstance(field, Field):
                    raise ValueError("Найдены объекты не типа Field")
        else:
            raise ValueError("Объекты не найдены")
        
        self.data = {}

    # Функция старта формы
    def start_form(self, u_id: int) -> str:
        self.u_id = u_id
        """
        in_form должен сохраняться в конечную машину состояний aiogram. но при этом в словаре data
        также должен создаваться раздел хранения данных определённого пользователя.
        """
        self.data[u_id] = {
            'in_form': True,
            'state': self.fields[0].state
            }

        return self.fields[0].text

    # Функия работы формы и формирования data
    def form_handler(self, msg, state) -> Union[dict, str]:

        for f in self.fields:
            if f.state == state:
                current_field = f

        validate_field = current_field.validate(msg)

        if type(validate_field) == True:
            self.data[self.u_id].update({current_field.text: msg})
            self.data[self.u_id].update({'state': current_field.state})
            return self.data
        # else:
        #     return validate_field
        
'''
1. Я сделал так, чтобы validate всегда возвращал тип bool, но теперь он не сможет пользователю вывести ошибку
о том, что его ответ не прошел валидацию
2. В form_handler не понимаю как оно должно поочередно отправлять вопрос пользователю и сохранять состояние
Если я использую return, то всё будет сбиваться. Уже начинать использовать aiogram (отправлять через
него сообщения пользователю)?
3. Если in_form нужно сохранять в машину aiogram, то мне уже подключать сам aiogram к проекту?
'''