Для парсинга новостей используйте команду python manage.py parser_news
Парсинг происходит из модуля newsapi-python.

-В при добавление картинок из админки, их не видно в шаблоне.
-Исправляется добавление в 20 строку шаблона: .url
-"\<img src="{{ item.image.url }}" alt="">\"
-Но при этом перестают отображаться картинки, которые загружены по url. Не смог решить эту проблему, потому что не работаю с шаблонами.

-Так же добавил API

-/api/news  - все новости.
-/api/<pk>"  - новость по id.

-Есть фильтр и поиск.

-api/news/?ordering=create_at - сортировка по дате создания.
-api/news/?search= - поиск.

-Так же есть CRUD у новостей.

-Добавлять пермишены не стал.
