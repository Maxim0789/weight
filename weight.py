
from colorama import init, Fore, Back, Style
init()

print(Back.GREEN + "Программа от Flashaka")
print(Back.CYAN)
weight = float(input ("Ваш вес:"))
height = float(input ("Ваш возраст:"))
print("")

bmi = float("{0:.2f}".format(weight / (height / 100) * (height / 100)))

print(Back.RESET + "Ваш индекс массы: " + str(bmi))

if( bmi <= 16 ):
    print(Back.RED + "(Болшой дефицит массы тела", end = '')

if( bmi >= 16  and bmi <= 25 ):
    print(Back.YELLOW + "(Недостаток массы тела", end = '')

if( bmi >= 18.5  and bmi <= 25 ):
    print(Back.GREEN + "(Твоя масса тела в норме", end = '')

if( bmi >= 25  and bmi <= 30 ):
    print(Back.YELLOW + "(Большая масса тела", end = '')

if( bmi >= 30  and bmi <= 35 ):
    print(Back.RED + "(Ожирение 1 степени", end = '')

if( bmi >= 35  and bmi <= 40 ):
    print(Back.RED + "(Ожирение 2 степени", end = '')

if( bmi >= 40 ):
    print(Back.RED + "(Ожирение 3 степени", end = '')

print(")", end = '')
print(Style.RESET_ALL)
input()
