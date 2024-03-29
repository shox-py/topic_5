# Домашнее задание | 5. Основы коллекций в Python

- [Задание 0](#задание-0)
- [Задание 1](#задание-1)
- [Задание 2](#задание-2)
- [Задание 3](#задание-3)
- [Задание 4](#задание-4)
- [Задание 5](#задание-5)
- [Задание 6](#задание-6)
- [Задание 7](#задание-7)
- [Задание 8](#задание-8)

---

## [Задание 0](task_0.py)

У вас есть список:

```python
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
```

Вам нужно поменять местами первый и последний элементы этого списка используя перестановка значений.

> Примечание:
> * Задачу можно решить двумя способами: с использованием классического подхода и подхода Python.

**Примеры:**

| Вывод                                                |
|:-----------------------------------------------------|
| ['Yellow', 'Green', 'White', 'Black', 'Pink', 'Red'] |

---

## [Задание 1](task_1.py)

У вас есть список:

```python
nums = [17, 6.06534, 91, 52, 87, 340, 56]
```

Вам необходимо найти сумму всех элементов этого списка, а также определить максимальный и минимальный элементы.

**Примеры:**

| Вывод                                                                                                          |
|:---------------------------------------------------------------------------------------------------------------|
| Сумма элементов списка: 649.06534</br>Максимальный элемент списка: 340</br>Минимальный элемент списка: 6.06534 |

---

## [Задание 2](task_2.py)

Дан список дней недели:

```python
days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
```

Ваша задача написать программу, которая получает целое число и выводит день недели, соответствующий введенному числу.

> Примечание:
> * Гарантируется, что на вход будет подаваться число от 1 до 7.

**Примеры:**

| Ввод                                  | Вывод |
|:--------------------------------------|:------|
| Введите номер дня недели от 1 до 7: 3 | Среда |

| Ввод                                  | Вывод       |
|:--------------------------------------|:------------|
| Введите номер дня недели от 1 до 7: 7 | Воскресенье |

---

## [Задание 3](task_3.py)

У вас есть список чисел:

```python
nums = [12, 45, 0.34711, 67, 89, 34, 55.632781, 78.9395]
```

Вам нужно найти среднее значение этих чисел и округлить его до одного знака после запятой.

**Примеры:**

| Вывод                  |
|:-----------------------|
| Среднее значение: 47.7 |

## [Задание 4](task_4.py)

Напишите программу, которая принимает строку и выводит _список_ (тип данных) всех уникальных символов,
встречающихся в этой строке.

**Примеры:**

| Ввод                        | Вывод                                         |
|:----------------------------|:----------------------------------------------|
| Введите строку: abracadabra | Уникальные символы: ['r', 'b', 'd', 'c', 'a'] |

| Ввод                          | Вывод                                                                  |
|:------------------------------|:-----------------------------------------------------------------------|
| Введите строку: Hello, World! | Уникальные символы: [',', 'l', ' ', '!', 'o', 'e', 'r', 'H', 'd', 'W'] |

---

## [Задание 5](task_5.py)

Напишите программу, которая принимает строку и определяет минимальный и максимальный символы в ней.

> Примечание:
> * Гарантируется, что на вход будет подаваться один или более символов.

**Примеры:**

| Ввод                   | Вывод                                            |
|:-----------------------|:-------------------------------------------------|
| Введите строку: World! | Минимальный символ: !</br>Максимальный символ: r |

| Ввод                    | Вывод                                            |
|:------------------------|:-------------------------------------------------|
| Введите строку: abcdefg | Минимальный символ: a</br>Максимальный символ: g |

---

## [Задание 6](task_6.py)

Напишите программу, которая принимает строку и выводит _кортеж_ всех уникальных символов,
которые встречаются в ней, а также их количество.

**Примеры:**

| Ввод                   | Вывод                                                                                    |
|:-----------------------|:-----------------------------------------------------------------------------------------|
| Введите строку: Python | Уникальные символы: ('y', 'o', 'P', 'h', 't', 'n')</br>Количество уникальных символов: 6 |

| Ввод                                                        | Вывод                                                                                                                                                                                                   |
|:------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Введите строку: The quick brown fox jumps over the lazy dog | Уникальные символы: ('p', 'h', 'x', 'j', 'o', 'w', 'e', 'b', 'a', ' ', 'g', 'u', 'f', 'm', 'z', 'k', 'y', 'i', 'l', 'q', 'r', 'c', 'T', 'd', 'n', 't', 'v', 's')</br>Количество уникальных символов: 28 |

---

## [Задание 7](task_7.py)

У вас есть словарь с информацией о студенте в формате:

```python
student_info = {"name": "Анна", "age": 20, "group_number": "А101"}
```

Создайте множество set, содержащее только ключи этого словаря, и выведите его на экран.

**Примеры:**

| Вывод                           |
|:--------------------------------|
| {'name', 'age', 'group_number'} |

---

## [Задание 8](task_8.py)

Создайте словарь, где ключами будут названия фруктов, а значениями - их цены. Выведите на экран созданный словарь. Затем
попросите пользователя выбрать фрукт из предложенных и выведите на экран его цену.

> Примечание
> * Гарантируется, что пользователь выбирает фрукт, существующий в указанном словаре.
> * Для создания словаря используйте функцию `dict()`.

**Примеры:**

| Ввод                                                                                                                               | Вывод              |
|:-----------------------------------------------------------------------------------------------------------------------------------|:-------------------|
| Список фруктов и их цены:</br>{'яблоко': 50, 'банан': 30, 'груша': 40, 'апельсин': 35}</br></br>Выберите фрукт из списка: апельсин | Цена апельсин - 35 |

| Ввод                                                                                                                            | Вывод           |
|:--------------------------------------------------------------------------------------------------------------------------------|:----------------|
| Список фруктов и их цены:</br>{'яблоко': 50, 'банан': 30, 'груша': 40, 'апельсин': 35}</br></br>Выберите фрукт из списка: груша | Цена груша - 40 |

---
