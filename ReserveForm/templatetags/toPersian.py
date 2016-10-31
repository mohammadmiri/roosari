__author__ = 'mohammad'


from django import template



register = template.Library()

@register.filter
def IntegerToPersian(number):
    if number is None:
        return None
    if number==0:
        return '۰'
    persian_number = ''
    while(number>=1):
        digit = number%10
        persian_number = toPersianDigit(digit)+persian_number
        number = int(number/10)
    return persian_number



@register.filter
def FloatToPersian(number):
    if number is None:
        return None
    if (type(number) is int):
        return IntegerToPersian(number)
    numbers = str(number).split('.')
    integer_number = IntegerToPersian(int(numbers[0]))
    float_number = IntegerToPersian(int(numbers[1]))
    return integer_number+'.'+float_number



def toPersianDigit(digit):
    if digit is None:
        return None
    if digit==1:
        return '۱'
    if digit==2:
        return '۲'
    if digit==3:
        return '۳'
    if digit==4:
        return '۴'
    if digit==5:
        return '۵'
    if digit==6:
        return '۶'
    if digit==7:
        return '۷'
    if digit==8:
        return '۸'
    if digit==9:
        return '۹'
    if digit==0:
        return '۰'

