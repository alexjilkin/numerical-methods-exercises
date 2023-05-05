from sympy import *
init_printing()

Kx, Ln = symbols('Kx, Ln', constant=True)
w, Ky, g = symbols('w, Ky, g')

Kx = 2
Ln = 2

sol = solve((-w - I) * (-w - (I / (Kx**2 + Ky**2))) - ((I - g*Ky) / (Kx**2 + Ky**2))*(I + (Ky/Ln)), w)

pprint(sol)
func = lambdify([g, Ky], sol)

print(func(1, 2))
