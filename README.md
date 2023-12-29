Тестовое задание:

1. # Python.
На вход подается сжатый файл с данными физических лиц.
Необходимо декодировать и распарсить файл, записать все данные в БД.
Для каждой сущности должна быть своя таблица.
Адрес необходимо разложить на составляющие по отдельным полям (индекс, регион и т.д.)

Сущности
ExtrajudicialBankruptcyMessage - сообщение
Debtor - физическое лицо
Bank - банк
MonetaryObligation - обязательство
ObligatoryPayment - платеж


2. # SQL
С помощью запросов необходимо посчитать и вывести информацию по обязательствам:
a.	10 лиц с наибольшим количеством обязательств;
b.	10 лиц с наибольшей общей суммой задолженностей;
c.	всех физических лиц с процентом общей выплаченной суммы по всем обязательствам относительно общей суммы своих обязательств (сколько процентов от всех обязательств погашено) от меньшего к большему.
В каждом запросе выводить Имя, ИНН физического лица и вычисленное значение. 

Поля
TotalSum – общая сумма по обязательству 
DebtSum – сумма задолженности

3. # Визуализация
Вывести графики с суммами задолженностей в разрезе:
a.	регионов;
b.	возраста физических лиц (разбивка по 10 лет: 20, 30, 40 и т.д.)
Инструмент визуализации на Ваше усмотрение.
