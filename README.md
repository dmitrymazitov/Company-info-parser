Поиск юридических лиц


Простое приложение на Python для поиска информации о юридическом лице посредством сайта ЕГРЮЛ https://egrul.nalog.ru/index.html.

Приложение реализовано с помощью библиотек Requests и Tkinter.

Благодаря библиотеки Requests, делается POST-запрос на сайт ЕГРЮЛ, на выходе получается json файл с информацией по компаниям. 

Для того, чтобы найти юр. лицо необходимо в поле поиска ввести ОГРН или ИНН или наименование компании.

Приложение написано на pattern-не MVC (Model, Controller, View).

Запуск программы через Controller.
