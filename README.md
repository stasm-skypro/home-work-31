# Домашняя работа к модулю 8
# Тема 30.2 Сериализаторы

## 1. Сериализатор модели 'Курс'

В сериализатор для модели 'Курс' добавлено новое поле - 'Количество уроков'. 

## 2.  Добавлена новая модель 'Платежи (Payment)' в приложение 'users'.

Поля:

    * пользователь (user) - пользователь, который совершает оплату (внешний ключ на модель 'пользователь'),
    * дата оплаты,
    * оплаченный курс - внешний ключ на модель 'курс',
    * оплаченный урок - внешний ключ на модель 'урок',
    * сумма оплаты,
    * способ оплаты: наличные или перевод на счет.


## 3. Изменён сериализатор модели 'Курс (Course)'
Создан дополнительный сериализатор, который для детального просмотра курса дополнительно выводит вложенный список уроков.
Таким образом при просмотре всех курсов в админке будет отображаться количество уроков в курсе. При просмотре детальной информации об одном уроке - количество уроков в курсе и их подробный список.

Например, команда ```http://localhost:8000/course/``` выводи список курсов и количество уроков в каждом курсе.

```json
[
    {
        "name": "Django с нуля",
        "description": "Создание веб-приложений на Django.",
        "lessons_count": 1
    },
    {
        "name": "Python для начинающих",
        "description": "Основы языка Python.",
        "lessons_count": 2
    },
    ...
]
```

команда ```http://localhost:8000/course/1/``` выводит детальную информацию об одном курсе, количество уроков в нем и подробную информацию о каждом уроке.

```json
{
    "name": "Python для начинающих",
    "description": "Основы языка Python.",
    "lessons_count": 2,
    "lessons": [
        {
            "id": 1,
            "name": "Введение в Python",
            "description": "История и применение Python.",
            "image": "http://localhost:8000/media/lessons/python_intro.jpg",
            "video": "http://localhost:8000/media/lessons/python_intro.mp4",
            "course": 1
        },
        {
            "id": 2,
            "name": "Переменные и типы данных",
            "description": "Разбор переменных и основных типов данных.",
            "image": "http://localhost:8000/media/lessons/python_vars.jpg",
            "video": "http://localhost:8000/media/lessons/python_vars.mp4",
            "course": 1
        }
    ]
}
```


## 4. Настроена фильтрация для эндпоинта вывода списка платежей с возможностями

* по дате оплаты,
команда: ```http://localhost:8000/users/payment/?ordering=date``` выводит список оплат в порядке возрастания даты оплаты.

```json
 [
        "id": 5,
        "date": "2025-03-11T19:10:00+05:00",
        "amount": "3999.99",
        "payment_method": "transfer",
        "user": 5,
        "course": 3,
        "lesson": null
    },
    {
        "id": 4,
        "date": "2025-03-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 1
    },
    {
        "id": 3,
        "date": "2025-03-13T14:00:00+05:00",
        "amount": "6999.99",
        "payment_method": "transfer",
        "user": 3,
        "course": 2,
        "lesson": null
    },
    {
        "id": 2,
        "date": "2025-03-14T20:20:00+05:00",
        "amount": "999.99",
        "payment_method": "cash",
        "user": 2,
        "course": null,
        "lesson": 3
    },
    {
        "id": 1,
        "date": "2025-03-15T15:30:00+05:00",
        "amount": "4999.99",
        "payment_method": "transfer",
        "user": 1,
        "course": 1,
        "lesson": null
    },
    {
        "id": 7,
        "date": "2025-04-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 2
    },
    {
        "id": 9,
        "date": "2025-04-14T20:20:00+05:00",
        "amount": "999.99",
        "payment_method": "cash",
        "user": 2,
        "course": null,
        "lesson": 5
    },
    {
        "id": 6,
        "date": "2025-04-15T15:30:00+05:00",
        "amount": "4999.99",
        "payment_method": "transfer",
        "user": 1,
        "course": 1,
        "lesson": null
    },
    {
        "id": 8,
        "date": "2025-05-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 3
    },
    {
        "id": 10,
        "date": "2025-05-13T14:00:00+05:00",
        "amount": "6999.99",
        "payment_method": "transfer",
        "user": 3,
        "course": 2,
        "lesson": null
    }
]
```

команда ```http://localhost:8000/users/payment/?ordering=-date``` выводит список оплат в порядке убывания даты оплаты.

```json
[
        "id": 10,
        "date": "2025-05-13T14:00:00+05:00",
        "amount": "6999.99",
        "payment_method": "transfer",
        "user": 3,
        "course": 2,
        "lesson": null
    },
    {
        "id": 8,
        "date": "2025-05-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 3
    },
    {
        "id": 6,
        "date": "2025-04-15T15:30:00+05:00",
        "amount": "4999.99",
        "payment_method": "transfer",
        "user": 1,
        "course": 1,
        "lesson": null
    },
    {
        "id": 9,
        "date": "2025-04-14T20:20:00+05:00",
        "amount": "999.99",
        "payment_method": "cash",
        "user": 2,
        "course": null,
        "lesson": 5
    },
    {
        "id": 7,
        "date": "2025-04-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 2
    },
    {
        "id": 1,
        "date": "2025-03-15T15:30:00+05:00",
        "amount": "4999.99",
        "payment_method": "transfer",
        "user": 1,
        "course": 1,
        "lesson": null
    },
    {
        "id": 2,
        "date": "2025-03-14T20:20:00+05:00",
        "amount": "999.99",
        "payment_method": "cash",
        "user": 2,
        "course": null,
        "lesson": 3
    },
    {
        "id": 3,
        "date": "2025-03-13T14:00:00+05:00",
        "amount": "6999.99",
        "payment_method": "transfer",
        "user": 3,
        "course": 2,
        "lesson": null
    },
    {
        "id": 4,
        "date": "2025-03-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 1
    },
    {
        "id": 5,
        "date": "2025-03-11T19:10:00+05:00",
        "amount": "3999.99",
        "payment_method": "transfer",
        "user": 5,
        "course": 3,
        "lesson": null
    }
]
```

команда ```http://localhost:8000/users/payment/?course=1``` выводит список оплат за 1-й курс.

```json
[
    {
        "id": 1,
        "date": "2025-03-15T15:30:00+05:00",
        "amount": "4999.99",
        "payment_method": "transfer",
        "user": 1,
        "course": 1,
        "lesson": null
    },
    {
        "id": 6,
        "date": "2025-04-15T15:30:00+05:00",
        "amount": "4999.99",
        "payment_method": "transfer",
        "user": 1,
        "course": 1,
        "lesson": null
    }
]
```

команда ```http://localhost:8000/users/payment/?lesson=1``` выводит список оплат за 1-й урок.

```json
[
    {
        "id": 4,
        "date": "2025-03-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 1
    }
]
```

команда ```http://localhost:8000/users/payment/?payment_method=cash``` выводит список всех наличных оплат.
```json
[
  {
        "id": 2,
        "date": "2025-03-14T20:20:00+05:00",
        "amount": "999.99",
        "payment_method": "cash",
        "user": 2,
        "course": null,
        "lesson": 3
    },
    {
        "id": 4,
        "date": "2025-03-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 1
    },
    {
        "id": 7,
        "date": "2025-04-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 2
    },
    {
        "id": 8,
        "date": "2025-05-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 3
    },
    {
        "id": 9,
        "date": "2025-04-14T20:20:00+05:00",
        "amount": "999.99",
        "payment_method": "cash",
        "user": 2,
        "course": null,
        "lesson": 5
    }
]
```


команда ```http://localhost:8000/users/payment/?user=4``` выводит список оплат за 4-го пользователя.

```json
[
    {
        "id": 4,
        "date": "2025-03-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 1
    },
    {
        "id": 7,
        "date": "2025-04-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 2
    },
    {
        "id": 8,
        "date": "2025-05-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 3
    }
]
```

команда ```http://localhost:8000/users/payment/?search=pelageya@example.com``` выводит платежи пользователя с id=4.

```json
[
   {
        "id": 8,
        "date": "2025-05-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 3
    },
    {
        "id": 7,
        "date": "2025-04-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 2
    },
    {
        "id": 4,
        "date": "2025-03-12T23:45:00+05:00",
        "amount": "1499.99",
        "payment_method": "cash",
        "user": 4,
        "course": null,
        "lesson": 1
    }
]
```

команда ```http://localhost:8000/users/payment/?search=Python для начинающих``` выводит платежи за курс с названием 'Python для начинающих'.

```json
[
    {
        "id": 1,
        "date": "2025-03-15T15:30:00+05:00",
        "amount": "4999.99",
        "payment_method": "transfer",
        "user": 1,
        "course": 1,
        "lesson": null
    },
    {
        "id": 6,
        "date": "2025-04-15T15:30:00+05:00",
        "amount": "4999.99",
        "payment_method": "transfer",
        "user": 1,
        "course": 1,
        "lesson": null
    }
]
``` 

## 5. Настроен вывод истории платежей для профиля пользователя

Команда ```http://localhost:8000/users/user/``` выводит список пользователей и вложенную историю их платежей в виде списка id платежей.

```json
[
   {
        "id": 1,
        "username": "stasm226",
        "email": "stasm226@gmail.com",
        "first_name": "Stanislav",
        "last_name": "Mayatskiy",
        "is_staff": true,
        "is_active": true,
        "date_joined": "2025-03-13T14:08:45.555726+05:00",
        "payments": [
            1,
            6
        ]
    },
    {
        "id": 2,
        "username": "andrewdevyatov",
        "email": "andrew.devyatov@example.com",
        "first_name": "Андрей",
        "last_name": "Девятов",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2025-03-18T22:54:54.396177+05:00",
        "payments": [
            2,
            9
        ]
    },
    {
        "id": 3,
        "username": "sergeyshnuroff",
        "email": "sergey.shnurov@example.com",
        "first_name": "Сергей",
        "last_name": "Шнуров",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2025-03-18T22:54:54.402002+05:00",
        "payments": [
            3,
            10
        ]
    },
    {
        "id": 4,
        "username": "pelageya",
        "email": "pelageya@example.com",
        "first_name": "Пелагея",
        "last_name": "Телегина",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2025-03-18T22:54:54.402842+05:00",
        "payments": [
            4,
            7,
            8
        ]
    },
    {
        "id": 5,
        "username": "nikolaystarikov",
        "email": "nikolay.starikov@example.com",
        "first_name": "Николай",
        "last_name": "Стариков",
        "is_staff": false,
        "is_active": true,
        "date_joined": "2025-03-18T22:54:54.403444+05:00",
        "payments": [
            5
        ]
    }
]
```

команда ```http://localhost:8000/users/user/4/``` выводит детальную историю платежей пользователя с id=4.

```json
[
    {
    "id": 4,
    "username": "pelageya",
    "email": "pelageya@example.com",
    "first_name": "Пелагея",
    "last_name": "Телегина",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2025-03-18T22:54:54.402842+05:00",
    "payments": [
        {
            "id": 4,
            "date": "2025-03-12T23:45:00+05:00",
            "amount": "1499.99",
            "payment_method": "cash",
            "user": 4,
            "course": null,
            "lesson": 1
        },
        {
            "id": 7,
            "date": "2025-04-12T23:45:00+05:00",
            "amount": "1499.99",
            "payment_method": "cash",
            "user": 4,
            "course": null,
            "lesson": 2
        },
        {
            "id": 8,
            "date": "2025-05-12T23:45:00+05:00",
            "amount": "1499.99",
            "payment_method": "cash",
            "user": 4,
            "course": null,
            "lesson": 3
        }
    ]
]
```

## 6. Все модели подключены к админке.
