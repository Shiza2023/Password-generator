from random import *


def generatr_password():
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print("Я генероатор паролей")
    kol = int(input("Введите количество паролей: "))

    for _ in range(kol):
        print(*(sample(chars, 6) + ["-"] + sample(chars, 6) + ["-"] + sample(chars, 6)), sep="")


generatr_password()
