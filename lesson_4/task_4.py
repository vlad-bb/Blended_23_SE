"""
Задача 4: Физические упражнения
Напишите функцию, которая принимает количество шагов, пройденных за день, и возвращает оценку на основе следующих критериев:

Менее 5000 шагов: "Мало активности"
От 5000 до 9999 шагов: "Умеренная активность"
От 10000 до 14999 шагов: "Хорошая активность"
15000 шагов и более: "Отличная активность"
Если количество шагов не является положительным числом, функция должна вернуть "Некорректное значение".
"""

# Входные данные
steps_1 = 12000
steps_2 = 1000
steps_3 = 15000
steps_4 = -1

# Ожидаемый результат
result_1 = "Хорошая активность"
result_2 = "Мало активности"
result_3 = "Отличная активность"
result_4 = "Некорректное значение"

# Тест
assert result_1 == "Хорошая активность", f"Ожидалось {result_1}, получено {result_1}"
assert result_2 == "Мало активности", f"Ожидалось {result_2}, получено {result_2}"
assert result_3 == "Отличная активность", f"Ожидалось {result_3}, получено {result_3}"
assert result_4 == "Некорректное значение", f"Ожидалось {result_4}, получено {result_4}"
