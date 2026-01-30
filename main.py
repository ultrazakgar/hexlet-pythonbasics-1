
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

