from random import *


def generatr_password():
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in "il1Lo0O":
        chars = chars.replace(i, "")

    print("Я генероатор паролей")

    kol = int(input("Введите количество паролей: "))

    for _ in range(kol):
        print(*(sample(chars, 6) +
              ["-"] + sample(chars, 6) + ["-"] + sample(chars, 6)), sep="")


generatr_password()
