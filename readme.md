# Решение тестового задания

[Взято отсюда](https://drive.google.com/drive/folders/1erJ45IKnKGOutmnAV20M-fEa6MRplVWY)

## SQL

Поля таблицы history

- issue_key – уникальный ключ задачи
- status – статус задачи
- minutes_in_status – количество минут, которое задача находилась в статусе
- previous_status – предыдущий статус задачи
- started_at – время создания статуса задачи, unix миллисекунды 
- ended_at – время перехода задачи в другой статус, unix миллисекунды


### Задание 1

Напишите запрос, который выведет, сколько времени в среднем задачи каждой группы находятся в статусе “Open” 
Условия:
Под группой подразумевается первый символ в ключе задачи. Например, для ключа “C-40460” группой будет “C”
Задача может переходить в один и тот же статус несколько раз.
Переведите время в часы с округлением до двух знаков после запятой.

### Задание 2

Напишите запрос, который выведет ключ задачи, последний статус и его время создания для задач, которые открыты на данный момент времени.
Условия:
Открытыми считаются задачи, у которых последний статус в момент времени не “Closed” и не “Resolved”
Задача может переходить в один и тот же статус несколько раз.
Оформите запрос таким образом, чтобы, изменив дату, его можно было использовать для поиска открытых задач в любой момент времени в прошлом
Переведите время в текстовое представление


## python

### Задание "Слияние логов"

Имеется два файла с логами в формате JSONL, пример лога:
…
{"timestamp": "2021-02-26 08:59:20", "log_level": "INFO", "message": "Hello"}
{"timestamp": "2021-02-26 09:01:14", "log_level": "INFO", "message": "Crazy"}
{"timestamp": "2021-02-26 09:03:36", "log_level": "INFO", "message": "World!"}
…
Сообщения в заданных файлах упорядочены по полю timestamp в порядке возрастания. 
Требуется написать скрипт, который объединит эти два файла в один.
При этом сообщения в получившемся файле тоже должны быть упорядочены в порядке возрастания по полю timestamp. 
