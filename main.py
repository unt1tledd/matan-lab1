import numpy as np
import matplotlib.pyplot as plt
import time
from math import pi, sin

# Функция f(x) = x
def f(x):
    return x

# Простая функция fn(x)
def f_n(x, n):
    return (pi / (2 * n)) * np.floor((2 * n * x) / pi)

# Интеграл Лебега от fn по [0, pi/2]
def lebesgue_integral_fn(n):
    return (pi**2 / 8) * ((n - 1) / n)

# Интеграл Лебега–Стилтьеса от fn по мере, задаваемой F(x)=sin(x)
def stieltjes_integral_fn(n):
    total = 0.0
    for k in range(n):
        a_k = k * pi / (2 * n)
        left = k * pi / (2 * n)
        right = (k + 1) * pi / (2 * n)
        mu = sin(right) - sin(left)
        total += a_k * mu
    return total

# Аналитические значения
analytic_lebesgue = pi**2 / 8
analytic_stieltjes = pi / 2 - 1

# ---------------------------
# Построение графиков fn
# ---------------------------
x = np.linspace(0, pi / 2, 2000)

plt.figure(figsize=(10, 6))
plt.plot(x, f(x), label='f(x)=x')

for n in [5, 10, 30]:
    plt.step(x, f_n(x, n), where='post', label=f'f_{n}(x)')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Графики f(x)=x и ступенчатых функций f_n(x)')
plt.legend()
plt.grid(True)
plt.show()

# ---------------------------
# Интеграл Лебега
# ---------------------------
print("Интеграл Лебега ∫ fn dλ")
for n in [10, 100, 1000]:
    start = time.perf_counter()
    value = lebesgue_integral_fn(n)
    elapsed = time.perf_counter() - start
    print(f"n = {n:4d} | value = {value:.10f} | time = {elapsed:.8f} sec")

print(f"Аналитическое значение: {analytic_lebesgue:.10f}")
print()

# ---------------------------
# Интеграл Лебега–Стилтьеса
# ---------------------------
print("Интеграл Лебега–Стилтьеса ∫ fn dμ_F, F(x)=sin(x)")
for n in [50, 500, 5000]:
    start = time.perf_counter()
    value = stieltjes_integral_fn(n)
    elapsed = time.perf_counter() - start
    print(f"n = {n:4d} | value = {value:.10f} | time = {elapsed:.8f} sec")

print(f"Аналитическое значение: {analytic_stieltjes:.10f}")