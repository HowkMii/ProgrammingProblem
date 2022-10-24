# Переводить натуральні числа (а також число нуль) з десяткової в вісімкову систему числення
# Алгоритм збудований на базі ''Класичного методу переведення'', а саме: залишку і цілій частині від ділення
# Залишок від ділення даного числа на 8 записується у кінець рядка виведення, при цьому,
# ціла частина від ділення даного числа на 8 знову використовується як аргумент функції
# Так продовжується до того моменту, доки ціла частина не буде рівною 0
# У такому разі, виконання функції припиняється, а всі залишки від ділення, що були отримані, становитимуть число у вісімковій системі
# (Опісля об'єднання усіх String в один) 


def decimal_to_octal(number):
    if number < 0:
        return 'Must be a positive integer'
    elif number == 0:
        return ''
    else:
        return decimal_to_octal(number//8) + str(number%8)
def final_result(number):
    return decimal_to_octal(number) if decimal_to_octal(number)!='' else 0

given_number=int(input("Your number: "))
print("In Octal Number System: " + final_result(given_number))