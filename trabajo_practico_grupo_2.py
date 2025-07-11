# -*- coding: utf-8 -*-
"""TRABAJO PRACTICO - GRUPO 2

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15B5LzFgtQHeCEMVlPrpBY52AwyGMvf8O
"""

import random

def crear_identificador(cadena_adn):
  lista_adn = list(cadena_adn)
  cantidad_de_cambios = random.randint (1,3)
  posiciones_a_cambiar = random.sample (range(len(lista_adn)), cantidad_de_cambios)

  for letra in posiciones_a_cambiar:
    letra_original = lista_adn[letra]
    opciones = ['A', 'T', 'G', 'C']
    opciones.remove(letra_original)
    nueva_letra = random.choice(opciones)
    lista_adn[letra] = nueva_letra
  return "".join(lista_adn)

cadena_adn = input("INGRESE SU CADENA DE ADN: ")
identificador = crear_identificador(cadena_adn)
print("\nSU IDENTIFICADOR ES:     ", identificador)

###

def crear_muestra(identificador):
  lista_adn = list(identificador)
  cantidad_de_cambios = random.randint (5,10)
  posiciones_a_cambiar = random.sample (range(len(lista_adn)), cantidad_de_cambios)

  for letra in posiciones_a_cambiar:
    letra_original = lista_adn[letra]
    opciones = ['A', 'T', 'G', 'C']
    opciones.remove(letra_original)
    nueva_letra = random.choice(opciones)
    lista_adn[letra] = nueva_letra
  return "".join(lista_adn)

muestra = crear_muestra(cadena_adn)
print("\nSU MUESTRA ES:           ", muestra)

###

def crear_muestras (muestra_inicial):
  muestras = [muestra_inicial]

  for muestra in range(19):
    nuevas_muestras = crear_muestra(muestras[-1])
    muestras.append(nuevas_muestras)
  return muestras

muestras = crear_muestras(muestra)
print("\n\nLAS 20 MUESTRAS SON:\n")

for numero, muestra in enumerate(muestras, start=1):
  print(f"MUESTRA {numero:2d}: {muestra}")

###

def corregir_letras(muestra, identificador):
  muestra_corregida = list(muestra)

  for letra in range(len(muestra)):
    if muestra[letra] != identificador[letra]:
      opciones = ['A', 'T', 'G', 'C']
      opciones.remove(muestra[letra])
      nueva_letra = random.choice(opciones)
      muestra_corregida[letra] = nueva_letra
    else:
      muestra_corregida[letra] = identificador[letra]
  return "".join(muestra_corregida)

###

def recontruccion_identifcador (muestra_actual, identificador):
  muestra_corregida = crear_muestra(muestra_actual)
  intentos = 1
  print(f"\nINTENTO {intentos:2d}: {muestra_corregida}")

  while muestra_corregida != identificador:
    muestra_corregida = corregir_letras(muestra_corregida, identificador)
    intentos += 1
    print(f"INTENTO {intentos:2d}: {muestra_corregida}")

  print("\nSE REALIZARON", intentos, "INTENTOS")
  print("SU IDENTIFICADOR ERA:    ", identificador)
  print("SU RECONSTRUCCION ES:    ", muestra_corregida)
  return muestra_corregida

print("\n\nINTENTOS DE RECONSTRUIR EL IDENTIFICADOR")
recontruccion = recontruccion_identifcador(cadena_adn, identificador)

###

def crear_pares (cadena_adn):
  pares = {
      "A": "T",
      "T": "A",
      "G": "C",
      "C": "G"
  }

  cadena_pares = ""
  for letra in cadena_adn:
    cadena_pares += pares[letra]
  return cadena_pares

pares = crear_pares(cadena_adn)
print("\n\nCADENA DE PARES")
print("\nSU CADENA DE ADN ES:     ", cadena_adn)
print("SU CADENA DE PARES ES:   ", pares)

###

def comparar_coincidencias (cadena_adn1, cadena_adn2):
  coicidencias = 0
  for letra in range(len(cadena_adn1)):
    if cadena_adn1[letra] == cadena_adn2[letra]:
      coicidencias += 1
  porcentaje_coincidencia = (coicidencias / len(cadena_adn1)) * 100
  return porcentaje_coincidencia

#EJEMPLO DE USO DE LA FUNCION EL PUNTO 7
porcentaje_coincidencia = comparar_coincidencias(identificador, muestra)
print("\n\nPORCENTAJE DE COINCIDENCIA (ENTRE EL IDENTIFICADOR Y LA MUESTRA): ", porcentaje_coincidencia, "%")

###

#DICCIONARIO DE ESPECIES
especie = {
    "Tortuga": "ATTCGCACAATTCCTATCCTATTCGCACAATTCCTATCCTATTCGCACAATTCCTATCCTATTCGCACAATTCCTATCCTATTCGCACAATTCCTATCCT",
    "Perro":   "ATGCTAGCTAGCTACCGTAAATGCTAGCTAGCTACCGTAAATGCTAGCTAGCTACCGTAAATGCTAGCTAGCTACCGTAAATGCTAGCTAGCTACCGTAA",
    "Gato":    "TACGATCGATCGTACGATCGTACGATCGATCGTACGATCGTACGATCGATCGTACGATCGTACGATCGATCGTACGATCGTACGATCGATCGTACGATCG",
    "Vaca":    "GGCTAACGTAGCTAGGCTAAGGCTAACGTAGCTAGGCTAAGGCTAACGTAGCTAGGCTAAGGCTAACGTAGCTAGGCTAAGGCTAACGTAGCTAGGCTAA",
    "Caballo": "CTAGGCTAACCGTAGCTAGCCTAGGCTAACCGTAGCTAGCCTAGGCTAACCGTAGCTAGCCTAGGCTAACCGTAGCTAGCCTAGGCTAACCGTAGCTAGC",
    "Cerdo":   "AATTCCGGTTCCAATTGGCCAATTCCGGTTCCAATTGGCCAATTCCGGTTCCAATTGGCCAATTCCGGTTCCAATTGGCCAATTCCGGTTCCAATTGGCC",
    "Oveja":   "CCTAGGTAACCTAGGTAACCCCTAGGTAACCTAGGTAACCCCTAGGTAACCTAGGTAACCCCTAGGTAACCTAGGTAACCCCTAGGTAACCTAGGTAACC",
    "Conejo":  "GGAATTCCGGAATTCCGGAAGGAATTCCGGAATTCCGGAAGGAATTCCGGAATTCCGGAAGGAATTCCGGAATTCCGGAAGGAATTCCGGAATTCCGGAA",
    "Gallina": "TAGCGATAGCGATAGCGATATAGCGATAGCGATAGCGATATAGCGATAGCGATAGCGATATAGCGATAGCGATAGCGATATAGCGATAGCGATAGCGATA",
    "Pato":    "GCTAGCTAGGATCCGATCGAGCTAGCTAGGATCCGATCGAGCTAGCTAGGATCCGATCGAGCTAGCTAGGATCCGATCGAGCTAGCTAGGATCCGATCGA",
    "Paloma":  "AACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCCAACCGGTTCC",
    "Ganso":   "TTGGAACCTTGGAACCTTGGTTGGAACCTTGGAACCTTGGTTGGAACCTTGGAACCTTGGTTGGAACCTTGGAACCTTGGTTGGAACCTTGGAACCTTGG",
    "Burro":   "CGATTCGGAACCGGATTCCACGATTCGGAACCGGATTCCACGATTCGGAACCGGATTCCACGATTCGGAACCGGATTCCACGATTCGGAACCGGATTCCA",
    "Canario": "GGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCATGGCAT"
}

def comparar_muestras (cadena_adn, especies):
  mejor_coincidencia = 0
  especie_mas_parecida = ""

  for especie, cadena_adn_especie in especies.items():
    porcentaje_coincidencia = comparar_coincidencias(cadena_adn, cadena_adn_especie)

    if porcentaje_coincidencia > mejor_coincidencia:
      mejor_coincidencia = porcentaje_coincidencia
      especie_mas_parecida = especie
  return especie_mas_parecida

especie_mas_parecida = comparar_muestras(cadena_adn, especie)
print("\n\nESPECIE MAS PARECIDA: ", especie_mas_parecida)

###

def comparar_muestras2 (cadena_adn, especies):
  porcentajes = {}
  for especie, cadena_adn_especie in especies.items():
    porcentaje_coincidencia = comparar_coincidencias(cadena_adn, cadena_adn_especie)
    porcentajes[especie] = porcentaje_coincidencia
  return porcentajes

porcentajes = comparar_muestras2(cadena_adn, especie)

print("\n\nPORCENTAJE DE COINCIDENCIA DE CADA ESPECIE")
for especie, porcentaje in porcentajes.items():
  print(f"{especie}: {porcentaje:.2f}%")