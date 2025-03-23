# Домашняя работа к модулю 8
# Тема 31 Права доступа в DRF

## 1. CRUD для пользователей с использованием JWT-авторизации.

### Создание пользователя (Create)

Для создания пользователя создан отдельный сериализатор, который делает валидацию необходимых полей.
Переопределены методы create, list, retrieve, update, destroy, в которых определены разрешения и логирование. При этом неавторизованные пользователя имеют доступ только к созданию пользователя.

Команда: ```POST``` ```http://127.0.0.1:8000/users/user/```

```json
{
        "username": "nikolaypanarin",
        "email": "nikolay.panarin@example.com",
        "password": "1234",
        "first_name": "Николай",
        "last_name": "Панарин"
}
```
### Просмотр списка пользователей (Read)
Команда: ```POST``` ```http://127.0.0.1:8000/users/user/```

```json
[
  {
        "id": 1,
        "username": "stasm226",
        "email": "stasm226@gmail.com",
        "first_name": "Stanislav",
        "last_name": "Mayatskiy",
        "phone": null,
        "city": null,
        "payments": [
            6
        ]
    },
    {
        "id": 2,
        "username": "andrewdevyatov",
        "email": "andrew.devyatov@example.com",
        "first_name": "Андрей",
        "last_name": "Девятов",
        "phone": "+1234567890",
        "city": "Moscow",
        "payments": [
            2,
            9
        ]
    },
    ...,
    {
        "id": 6,
        "username": "keithkellog",
        "email": "keith.kellog@example.com",
        "first_name": "Кит",
        "last_name": "Келлог",
        "phone": "+1234567890",
        "city": "Дейтон",
        "payments": []
    },
    {
        "id": 9,
        "username": "nikolaypanarin",
        "email": "nikolay.panarin@example.com",
        "first_name": "Николай",
        "last_name": "Панарин",
        "phone": null,
        "city": null,
        "payments": []
    }
]
```

### Просмотр информации об одном пользователе
Команда: ```GET``` ```http://127.0.0.1:8000/users/user/10/```
```json
{
    "id": 10,
    "username": "irinatsy",
    "email": "irina.tsy@example.com",
    "first_name": "Ирина",
    "last_name": "Цыцорина",
    "phone": null,
    "city": null,
    "is_staff": false,
    "is_active": true,
    "date_joined": "2025-03-23T14:16:16.619238+05:00",
    "payments": []
}
```

### Редактирование пользователя (Update)
Команда: ```PATCH``` ```http://127.0.0.1:8000/users/user/10/```
```json
{
    "phone": "+1234567890",
    "city": "Aqtobe"
}
```

```json
{
    "id": 10,
    "username": "irinatsy",
    "email": "irina.tsy@example.com",
    "first_name": "Ирина",
    "last_name": "Цыцорина",
    "phone": "+1234567890",
    "city": "Aqtobe",
    "payments": []
}
```


## 2 Создание группы 'Модераторы'
Группа наделяется правами просматривать и редактировать курсы и кроки.
Для создания группы есть кастомная команда:
```./manage.py create_moderator_group```

Заполнить группу можно через shell командами:
```
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

# Так как используется кастомная модель пользователя, то сначла нужно получить класс User
User = get_user_model()

# Получаем группу "Модераторы"
moderators_group, created = Group.objects.get_or_create(name="Модераторы")

# Получаем пользователей
user1 = User.objects.get(id=11)
user2 = User.objects.get(id=8)

# Добавляем пользователей в группу
moderators_group.user_set.add(user1, user2)
```

Таким образом пользователи Владимир Путин и Дональд Трамп назначены модераторами.
