# -*- coding: utf-8 -*-
"""Retos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jcewq62fG58MFOzms5a2qya_LjFKnomi
"""

#reto1
#entradas

salario_base, horas_extra, bonificacion = input().split()
salario_base= float(salario_base)
horas_extra= int(horas_extra)
bonificacion= int(bonificacion)

#valores

valor_hora= salario_base/192
valor_extra= (valor_hora*1.25)*horas_extra
valor_bonif= (salario_base*0.05)*bonificacion
#salario_total
salario_total= salario_base+valor_extra+valor_bonif

#descuentos

desc_salud= salario_total *0.035
desc_pension= salario_total *0.04
desc_caja= salario_total *0.01

#salario_final

salario_final= salario_total-desc_salud-desc_pension-desc_caja

print(round(salario_final,1))

#RETO 2

#entradas

distancia, velocidad_maxima_permitida, tiempo = [int(valor) for valor in input().split()]
 

distancia/= 1000
tiempo/= 3600

velocidad_media= distancia/tiempo
velocidad_media_mas_porcentaje= velocidad_maxima_permitida*1.20

if velocidad_media < velocidad_maxima_permitida:
  print("OK")
elif velocidad_media > velocidad_maxima_permitida and velocidad_media < velocidad_media_mas_porcentaje:
  print("MULTA")
elif tiempo < 0 or velocidad_maxima_permitida < 0:
  print("ERROR")
elif velocidad_maxima_permitida < velocidad_media and velocidad_media >= velocidad_media_mas_porcentaje:
  print("CURSO SENSIBILIZACION")

#reto3

#entradas
N= int(input())        
bicicletas = []         

#proceso

for i in range(N):     
  bicicletas.append(input().split())

#funcion para calcular entre los rangos requeridos el pedalier, bielas, sillin y el manilar.

def calcular():
  precios = []
  for i in bicicletas:
    if int (i[0]) >= 240 and int(i[0]) <= 300 \
    and int(i[1]) >= 160 and int(i[1]) <= 180 \
    and int(i[2]) >= 240 and int (i[2]) <= 275 \
    and int(i[3]) <= 50:

      precios.append(int(i[4]))

  return  precios

resultado = calcular()

if len(resultado) ==0:
  print("NO DISPONIBLE")
else:
  for i in resultado:
    print(i)

# reto 4

#captura de datos

num_baldosas, capacidad_de_sensor= input().split()
identificador_baldosas= input().split()

num_baldosas= int(num_baldosas)
capacidad_de_sensor= int(capacidad_de_sensor)


for i in range(0,len(identificador_baldosas), 1):
  identificador_baldosas[i]= int(identificador_baldosas[i])

fallas_reales= 0
fallas_sensor= 0
contador= 0
diccionario= dict()

for valor in identificador_baldosas:
  if (valor in diccionario):
    fallas_reales +=1
  if ((valor in diccionario)and (contador - diccionario.get(valor) <= capacidad_de_sensor)):
    fallas_sensor += 1
  diccionario[valor]= contador
  contador += 1
print(fallas_reales,fallas_sensor,contador, end=" ")