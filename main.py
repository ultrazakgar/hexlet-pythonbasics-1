
# Напишите функцию get_sum, в качестве параметра 
# принимает два целых числа и возвращает результат их сложения

# Пример:

# (1, 2) => 3

# (2, 2) => 4

def get_sum(a,b):
    return(a+b)

# print(get_sum(6,8))

# Написать функцию count_capital_letters, 
# которая в качестве параметра принимает строку состоящую из букв и пробелов(без цифр) 
# и возвращает количество заглавных букв в строке.

# Пример:

# "Hello World" => 2

# "   A   " =>  1

def count_capital_letters(text):
    counter = 0
    for x in text:
        if x.upper() == x and x.lower() != x.upper():
            counter += 1
    return(counter)

# print(count_capital_letters("   A   "))
# print(count_capital_letters("Hello World"))
# print(count_capital_letters("Hello World 12345"))

# Написать функцию decode_string, которая в качестве параметра 
# принимает строку и возвращает преобразованную строку так, 
# чтобы каждый символ в новой строке был «(» если этот символ встречается 
# только один раз в исходной строке, или «)» если он встречается более одного раза. 
# При определении дубликатов не учитывать регистр букв.

# Пример:
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))((" 

def decode_string(text):
    n = ""
    text = text.lower()
    for x in text:
        if text.count(x) == 1:
            n += "("
        else:
            n += ")"
    return(n)

# print(decode_string("din"))
# print(decode_string("recede"))
# print(decode_string("Success"))
# print(decode_string("(( @"))

# Написать функцию get_odd_count, которая в качестве параметра 
# принимает строку и возвращает целое число, которое соответствует количеству четных чисел в строке. 
# Строка содержит только цифры, без разделителей. Ноль считать нечетным.

# Пример:
# "2468" => 4
# "13579" => 0
# "01234567" => 3

def get_odd_count(text): # четных чисел
    counter = 0
    for x in text:
        x = int(x)
        if round(x/2) == x/2 and x != 0:
            counter += 1
    return(counter)

# print(get_odd_count("2468"))
# print(get_odd_count("13579"))
# print(get_odd_count("01234567"))

# Пишем функцию для управления умным домом

# Написать функцию check_access которая на основе булевых параметров:
#     has_keycard (bool): Наличие действующей ключ-карты.
#     has_fingerprint (bool): Совпадение отпечатка пальца.
#     is_alarm (bool): Сработала ли сигнализация (True - тревога!).
#     is_daylight (bool): Дневное ли время (True - день).

# Возвращает. Решение об открытии двери (True - открыть, False - не открывать).

# Правила доступа:
# Дверь можно открыть ключом-картой ИЛИ с помощью отпечатка пальца.
# Однако, даже при наличии ключа или отпечатка, дверь НЕ откроется, если сработала сигнализация (например, при взломе).

# Для дополнительной безопасности, если используется ключ-карта, 
# система требует, чтобы в этот момент был дневной свет (имитация работы датчика освещенности). 
# Это правило НЕ применяется к отпечатку пальца.

def check_access(has_keycard: bool,has_fingerprint: bool,is_alarm: bool, is_daylight: bool):
    if is_alarm:
        return(False)
    if has_fingerprint:
        return(True)
    if has_keycard and is_daylight:
        return(True)
        
    return(False)

# Примеры работы функции (тесты)
# print("Тест 1 (Ключ, день, нет тревоги):", check_access(True, False, False, True))   # Ожидается: True
# print("Тест 2 (Ключ, ночь, нет тревоги):", check_access(True, False, False, False))  # Ожидается: False (для ключа нужен день)
# print("Тест 3 (Палец, ночь, нет тревоги):", check_access(False, True, False, False)) # Ожидается: True (для пальца день не нужен)
# print("Тест 4 (Палец, день, но ЕСТЬ тревога):", check_access(False, True, True, True)) # Ожидается: False (тревога блокирует все)
# print("Тест 5 (Ключ И палец, день, нет тревоги):", check_access(True, True, False, True)) # Ожидается: True
# print("Тест 6 (Ничего нет):", check_access(False, False, False, True))               # Ожидается: False
