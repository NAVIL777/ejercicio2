import os

metro=float(input(" Ingresa el valo de metro:"))
centimetro=metro*100
pulgadas=centimetro/2.54
pies=pulgadas/12
yarda=pies/3
print("valor de centimetro:"+repr(centimetro))
print("valor de pies:"+repr(pies))
print("valor de pulgadas:"+repr(pulgadas))
print("valor de yarda:"+repr(yarda))
print()
os.system("pause")