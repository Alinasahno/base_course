import time

M = 2
N = 3

start = time.time()

for i in range(M + 1):
    print(i)
    time.sleep(1)
    for j in range(N + 1):
        print(j)
        time.sleep(1)

end = time.time()
print("Программа завершена!")
print(f"Время: {end - start:.1f} сек")