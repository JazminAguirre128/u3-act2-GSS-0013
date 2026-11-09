import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Problema 1: Planetas (Nombre, distancia al sol en Mkm, tiene anillos, descubridor/año)
mer = ['Mercurio', 57.9, False, 1631]
ven = ['Venus', 108.2, False, 1610]
tie = ['Tierra', 149.6, False, 0]
mar = ['Marte', 227.9, False, 1610]
jup = ['Júpiter', 778.5, True, 1610]

# Creamos una lista de listas (conformando la tabla)
lista_planetas = [mer, ven, tie, mar, jup]

# Utilizar Data para organizar la tabla (DataFrame)
df_planetas = pd.DataFrame(
    lista_planetas, 
    columns=["Nombre", "Distancia_Mkm", "Tiene_Anillos", "Año_Descubrimiento"]
)
print(df_planetas)

# Creamos el archivo CSV y lo guardamos
df_planetas.to_csv("planetas.csv", index=False)

# 1. Gráfica de líneas básica
plt.plot(df_planetas["Nombre"], df_planetas["Distancia_Mkm"])
plt.title("Gráfica Distancia al Sol")
plt.xlabel("Nombre del planeta")
plt.ylabel("Distancia al Sol (Mkm)")
plt.show()

# 2. Gráfica de puntos (scatter)
plt.scatter(df_planetas["Nombre"], df_planetas["Distancia_Mkm"])
plt.show()

# 3. Gráfica de barras simple
plt.bar(df_planetas["Nombre"], df_planetas["Distancia_Mkm"])
plt.show()

# 4. Gráfica de barras con títulos
plt.bar(df_planetas["Nombre"], df_planetas["Distancia_Mkm"])
plt.title("Comparativa de Distancia al Sol por Planeta")
plt.xlabel("Planeta")
plt.ylabel("Distancia al Sol (Mkm)")
plt.show()

# 5. Gráfica de barras ordenada descendentemente
df_pl_ordenar = df_planetas.sort_values("Distancia_Mkm", ascending=False)
plt.bar(df_pl_ordenar["Nombre"], df_pl_ordenar["Distancia_Mkm"])
plt.show()

# 6. Gráfica de barras coloreada (5 colores para 5 planetas)
plt.bar(
    df_pl_ordenar["Nombre"], 
    df_pl_ordenar["Distancia_Mkm"],
    color=["b", "g", "c", "m", "y"]  # 5 colores exactamente
)
plt.show()

# 7. Gráfica de pastel
plt.pie(df_planetas["Distancia_Mkm"], labels=df_planetas["Nombre"])
plt.show()