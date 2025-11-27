def mechanical_energy(m, h, v, g=10):
    potential_energy = m * g * h
    kinetic_energy = (m * v ** 2) / 2
    total_energy = potential_energy + kinetic_energy
    return total_energy
energy2 = mechanical_energy(m=0.5, h=20, v=15)
print(f"Масса: 0.5 кг, Высота: 20 м, Скорость: 15 м/с")
print(f"Полная механическая энергия: {energy2:.2f} Дж")
