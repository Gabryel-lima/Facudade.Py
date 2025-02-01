import numpy as np
import matplotlib.pyplot as plt

# Criando gráficos para cada tópico

# 1. Funções Polinomiais
x = np.linspace(-10, 10, 400)
y1 = x**2 - 5*x + 6  # Função quadrática

plt.figure(figsize=(6, 4))
plt.plot(x, y1, label=r"$f(x) = x^2 - 5x + 6$")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Função Polinomial")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

# 2. Função Racional
y2 = 1 / (x + 0.1)  # Evitar divisão por zero

plt.figure(figsize=(6, 4))
plt.plot(x, y2, label=r"$f(x) = \frac{1}{x}$")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.ylim(-10, 10)
plt.title("Função Racional")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

# 3. Função Exponencial
y3 = np.exp(x / 3)

plt.figure(figsize=(6, 4))
plt.plot(x, y3, label=r"$f(x) = e^{x/3}$")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Função Exponencial")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

# 4. Função Logarítmica
x_pos = np.linspace(0.1, 10, 400)  # Evita log(0)
y4 = np.log(x_pos)

plt.figure(figsize=(6, 4))
plt.plot(x_pos, y4, label=r"$f(x) = \ln(x)$")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Função Logarítmica")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

# 5. Funções Trigonométricas
x_trig = np.linspace(-2*np.pi, 2*np.pi, 400)
y_sin = np.sin(x_trig)
y_cos = np.cos(x_trig)

plt.figure(figsize=(6, 4))
plt.plot(x_trig, y_sin, label=r"$\sin(x)$")
plt.plot(x_trig, y_cos, label=r"$\cos(x)$")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Funções Trigonométricas")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

# 6. Progressão Aritmética
n = np.arange(1, 11, 1)
pa = 2 + (n - 1) * 3

plt.figure(figsize=(6, 4))
plt.plot(n, pa, 'bo-', label="PA (a1=2, r=3)")
plt.title("Progressão Aritmética")
plt.xlabel("n")
plt.ylabel("a_n")
plt.legend()
plt.grid()
plt.show()

# 7. Progressão Geométrica
pg = 2 * (3**(n-1))

plt.figure(figsize=(6, 4))
plt.plot(n, pg, 'ro-', label="PG (a1=2, r=3)")
plt.title("Progressão Geométrica")
plt.xlabel("n")
plt.ylabel("a_n")
plt.legend()
plt.grid()
plt.show()

# 8. Equação da Reta
x_line = np.linspace(-10, 10, 100)
y_line = 2*x_line + 1

plt.figure(figsize=(6, 4))
plt.plot(x_line, y_line, label=r"$y = 2x + 1$")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Equação da Reta")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

# 9. Equação do Círculo
theta = np.linspace(0, 2*np.pi, 300)
x_circle = 3*np.cos(theta)
y_circle = 3*np.sin(theta)

plt.figure(figsize=(6, 4))
plt.plot(x_circle, y_circle, label=r"$(x-0)^2 + (y-0)^2 = 3^2$")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Equação do Círculo")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.axis("equal")
plt.grid()
plt.show()
