# Задача 4.1.
READ = 1
WRITE = 2
DELETE = 4
ADMIN = 8

permissions = READ | WRITE

print("Початкові права:", bin(permissions))

print("Читання:", bool(permissions & READ))

permissions |= DELETE
print("Після додавання DELETE:", bin(permissions))

permissions &= ~WRITE
print("Після скасування WRITE:", bin(permissions))

permissions ^= ADMIN
print("Після перемикання ADMIN:", bin(permissions))

print("Чи має право DELETE:", bool(permissions & DELETE))
print("Чи має право ADMIN:", bool(permissions & ADMIN))

# Задача 4.2.
n = int(input("Введіть ціле число: "))

is_even = (n & 1) == 0

is_power_of_two = n > 0 and (n & (n - 1)) == 0

bit_count = n.bit_count()

lowest_bit = n & -n

binary = bin(n)

print("Двійкове представлення:", binary)
print("Число парне:", is_even)
print("Число є степенем двійки:", is_power_of_two)
print("Кількість встановлених бітів:", bit_count)
print("Молодший встановлений біт:", lowest_bit)