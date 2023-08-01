# Создайте функцию генератор чисел Фибоначчи (см. Википедию)

def fibonachi(z: int):
    f1 = f2 = 1
    for i in range (2, z):
        f1, f2 = f2, f1 + f2
    yield f2

print(*fibonachi(7))

