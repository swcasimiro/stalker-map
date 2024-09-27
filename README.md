<h1>Stalker-map</h1>
<img src="https://img.shields.io/badge/django 3.2-black?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/> 

<b>Немного вводной информации :</b>
<br>
<br>
<b>С</b>айт создан для проекта на платформе SA:MP. Задача заключалась сделать платформу для того, чтобы пользователи могли находить информацию о локациях в пару кликов. Веб-приложение реализовано с помощью <b>django + postgresql</b>. Авторства не имеет, любой желающий может взять мои наработки для своего проекта. Сайт достаточно простой, присутсвует встроенная админ-панель от <b>django</b>. Сделано это для того, чтобы любой человек без каких-либо проблем мог взять и переделать сайт под свои нужды.
<br>
<br>
<b>З</b>атронем функционал - из себя это самый обычный сайт с маленьким лендингом и основной страницей где находится выборка информации о локациях. Реализована поисковая строка, которая позволяет искать по названию нужную локацию. Так же конструкция сайта представляет из себя две связанные модели. Ниже можно увидеть их. Так же оптимизированы с помощью Django ORM запросы связанных моделей, аналог JOIN в SQL. Информацию о каждой локации можно узнать детальнее с помощью <code>DetailView</code>. Так же реализован Пагинатор, чтобы юзеру было куда легче искать информацию и страница не выглядела слишком нагружена. Админ-панель позволяет использовать CRUD к моделяем.
<br>
<br>
<strong><p>Используемые технологии:</p></strong>
  <p>Все использованные инструменты, которые были задействованы в реализации данного проекта.</p>
<div>
<p><strong>Языки программирования</strong></p>
  <a>
    <img src="https://img.shields.io/badge/python-346c99?style=for-the-badge&logo=python&logoColor=fecd3a" alt="Python Badge"/>
  </a>
<br>
<br>  
<p><strong>Фреймворк</strong></p>

<a>
    <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white" alt="Django Badge"/>
</a>
<br>
<br>
<p><strong>База данных</strong></p>
<a>
  <img src="https://img.shields.io/badge/postgresql-316093?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL Badge"/>
</a>
<a>
    <img src="https://img.shields.io/badge/sqlite-3f9cd8?style=for-the-badge&logo=sqlite&logoColor=white" alt="nginx Badge"/>
</a>

</div>
<br>

<b>Активация проекта :</b>
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
<br>
<br>
<b>upd :</b>
<img src="https://cdn-icons-png.flaticon.com/512/25/25333.png" width="15px"> Так же стоит отметить, что вся активация <code>SECRET_KEY</code> и подключение DATABASE происходит через корень проекта, созданием файла <code>.env</code>. Сайт для генерации <a href="https://djecrety.ir/">SECRET_KEY</a> <img src="https://cdn-icons-png.flaticon.com/512/25/25333.png" width="15px">


