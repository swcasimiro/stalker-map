<img src="https://www.upload.ee/image/15596682/stalker-map.jpg">
<b>Немного вводной информации :</b>
<br>
<br>
<b>С</b>айт создан для проекта на платформе SA:MP. Задача заключалась сделать платформу для того, чтобы пользователи могли находить информацию о локациях в пару кликов. Веб-приложение реализовано с помощью <b>django + postgresql</b>. Авторства не имеет, любой желающий может взять мои наработки для своего проекта. Сайт достаточно простой, присутсвует встроенная админ-панель от <b>django</b>. Сделано это для того, чтобы любой человек без каких-либо проблем мог взять и переделать сайт под свои нужды.
<br>
<br>
<b>З</b>атронем функционал - из себя это самый обычный сайт с маленьким лендингом и основной страницей где находится выборка информации о локациях. Реализована поисковая строка, которая позволяет искать по названию нужную локацию. Так же конструкция сайта представляет из себя две связанные модели. Ниже можно увидеть их. Так же оптимизированы с помощью Django ORM запросы связанных моделей, аналог JOIN в SQL. Информацию о каждой локации можно узнать детальнее с помощью DetailView. Так же реализован Пагинатор, чтобы юзеру было куда легче искать информацию и страница не выглядела слишком нагружена. Админ-панель позволяет использовать CRUD к моделяем.
<br>
<br>
<img src="https://www.upload.ee/image/15596759/db.jpg">

<b>Активация проекта :</b>
<br>
<br>
<code>python -m venv venv</code>
<br>
<br>
<code>venv\Scripts\activate.bat</code>
<br>
<br>
<code>pip install -r requirements.txt</code>
<br>
<br>
<code>python manage.py makemigrations</code>
<br>
<br>
<code>python manage.py migrate</code>
<br>
<br>
<code>python manage.py createsuperuser</code>




