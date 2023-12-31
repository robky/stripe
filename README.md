## stripe
Stripe API backend

### Описание
Реализован Django + stripe API бэкенд со следующим функционалом:
- Реализованы модель заказов (Order), в которой объединяются товары (Item)
- Метод /buy/{order_id}/ с помощью которого можно получить Stripe Session Id для оплаты выбранного заказа.
- Метод /order/{order_id}/ с помощью которого можно посмотреть информацию об товарах в выбранном заказе,
  а по нажатию кнопки Buy перейти на форму оплаты Stripe.
- Просмотр и редактирование объектов моделей в Django Admin панели по адресу /admin/

### Как запустить проект:
Клонировать проект
```
git clone https://github.com/robky/stripe.git
```

Переименовать файл .env.example и изменить содержимое на актуальные данные.
```
mv .env.example .env
```

Запустить контейнер c проектом
```
docker-compose up -d
```

Выполнить миграции:
```
docker-compose exec backend python manage.py migrate
```
Добавить статические файлы:
```
docker-compose exec backend python manage.py collectstatic --no-input
```
Создать суперпользователя:
```
docker-compose exec backend python manage.py createsuperuser
```
