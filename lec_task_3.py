a = int(input("Введите год: "))
if (a % 4 == 0) or (a % 100 == 0):
    print ("Високoсный")
else:
    print("Не високосный")
