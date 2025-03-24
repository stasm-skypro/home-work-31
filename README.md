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
```commandline
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

### Авторизация пользователя-модератора

### Шаг 1 - Получение токена

```POST``` ```http://127.0.0.1:8000/users/token/```

В теле запроса передать данные пользователя:
```json
{
  "email": "donal.dtrump@example.com",
  "password": "hardpassword"
}
```

### Шаг 2 - Добавление токена в заголовки

### Шаг 3 - Проверка прав модератора

#### 1. Модератор имеет право просматривать всем курсы и уроки!

```GET``` ```http://127.0.0.1:8000/course/```

Получаем:
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
    {
        "name": "SQL для начинающих",
        "description": "Основы работы с базами данных.",
        "lessons_count": 1
    },
    {
        "name": "Основы веб-разработки",
        "description": "Введение в HTML, CSS и JavaScript.",
        "lessons_count": 0
    },
    {
        "name": "Алгоритмы и структуры данных",
        "description": "Разбор алгоритмов и структур данных.",
        "lessons_count": 1
    }
]
```

#### 2. Модератор имеет право просматривать конкретный курс и его уроки!

```GET``` ```http://127.0.0.1:8000/course/1/```

Получаем:
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
            "image": "http://127.0.0.1:8000/media/lessons/python_intro.jpg",
            "video": "http://127.0.0.1:8000/media/lessons/python_intro.mp4",
            "course": 1
        },
        {
            "id": 2,
            "name": "Переменные и типы данных",
            "description": "Разбор переменных и основных типов данных.",
            "image": "http://127.0.0.1:8000/media/lessons/python_vars.jpg",
            "video": "http://127.0.0.1:8000/media/lessons/python_vars.mp4",
            "course": 1
        }
    ]
}
```

#### 3. Модератор имеет право редактировать курсы и уроки!

```PATCH``` ```http://127.0.0.1:8000/course/12/```

Тело запроса:
```json
{ 
  "name": "Новый курс 5-1",
  "description": "Новое описание курса 5"
}
```

Ответ:
```json
{
    "id": 12,
    "name": "Новый курс 5-1",
    "description": "Новое описание курса 5",
    "lessons_count": 0
}
```

#### 4. Модератор не имеет права добавлять новый курс или урок!

```POST``` ```http://127.0.0.1:8000/course/```

Тело запроса:
```json
{
  "name": "Новый курс 6",
  "description": "Описание нового курса 6 с примерами"
}
```
Ответ:
```json
{
    "detail": "You do not have permission to perform this action."
}
```

#### 5. Модератор не имеет права удалять курсы и уроки!
```DELETE``` ```http://127.0.0.1:8000/course/6/```

Ответ:
```json
{
    "detail": "You do not have permission to perform this action."
}
```
