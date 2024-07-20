# CRM - django

## Авторизация, login, logout, forms

## frontend + db = bootstrap + postgres

### postgres

$ sudo apt install postgresql

$ sudo -i -u postgres

>> psql

CREATE USER sano WITH PASSWORD 'sano' CREATEDB;

SET role sano;

CREATE DATABASE django_db;

$ psql -h localhost -U sano django_db

### Bootstrap

https://getbootstrap.com/docs/5.3/getting-started/introduction/

В папке templates:

1. Include Bootstrap’s CSS and JS

Вставили в файл base.html

2. Component Navbar 

Вставили в navbar.html

3. Forms

Вставили login в home.html

----------------------------

Написали в home.html:

{% user.is_authenticated %}

{% else %}

{% endif %}

---------------------------

4. Alert

Сделали сообщение об ошибке

при провале аутентификации.

и сообщение: Logged in, при успехе
