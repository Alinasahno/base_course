a = int(input("Введите год: "))
if (a % 4 == 0) or (a % 400 == 0):
    print ("Високoсный")
else:
    print("Не високосный")
