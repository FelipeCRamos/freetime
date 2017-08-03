# CODED BY FelipeCRamos
# FOR FREETIME


## Script que resolve um sistema de 3 equações com 3 incógnitas!
import sys

# Introdução

print ("\nPrograma em Python para resolver um sistema de equações com três incógnitas")
print ("Estou definindo um sistema de três equações com três incógnitas desta forma:")
print ("\n\tax + by + cz = R1\n\tdx + ey + fz = R2\n\tgx + hy + iz = R3\n")
print ("Digite os valores para: (respectivamente)")

# O usuário dá valores aos coeficientes

a, b, c, r1 = map(float, input("a b c r1: ").split())
d, e, f, r2 = map(float, input("d e f r2: ").split())
g, h, i, r3 = map(float, input("g h i r3: ").split())

# Aqui é a regra de Cramer, propriamente dita.

det = ((a * e * i) + (b * f * g) + (c * d * h)) - ((c * e * g) + (a * f * h) + (b * d * i))
detx = ((r1 * e * i) + (b * f * r3) + (c * r2 * h)) - ((c * e * r3) + (r1 * f * h) + (b * r2 * i))
dety = ((a * r2 * i) + (r1 * f * g) + (c * d * r3)) - ((c * r2 * g) + (a * f * r3) + (r1 * d * i))
detz = ((a * e * r3) + (b * r2 * g) + (r1 * d * h)) - ((r1 * e * g) + (a * r2 * h) + (b * d * r3))

# Define os valores das incógnitas, com casas decimais.

if det == 0:
   print("Divisão por zero! Não é possível completar a operação!")
   sys.exit()
else:
   x = (round(detx, 3) / round(det, 3))
   y = (round(dety, 3) / round(det, 3))
   z = (round(detz, 3) / round(det, 3))

# Mostra os resultados finais
print ("Os resultados são (aproximados com 4 casas decimais):")
print ("x = %.4f" % x)
print ("y = %.4f" % y)
print ("z = %.4f\n" % z)
