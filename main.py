import yfinance as yf # Para descargar datos reales
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.interpolate import lagrange # Solo Para validar
from src.interpolacion import polinomio_lagrange

# ----- Configuración ------
ACTIVO = 'DIS'
FECHA_INICIO = '2024-03-01'
FECHA_FIN = '2025-04-01'
CARPETA_GRAFICOS = 'graficos'

# ----- Obtener Datos -----

print(f"Descargando dato para {ACTIVO}...")
try:
    datos = yf.download(ACTIVO, start=FECHA_INICIO, end=FECHA_FIN)
    if datos.empty:
        print(f"No se pudieron descargar datos para el activo {ACTIVO}. Verifica que el ticker sea correcto y no privado.")
        exit()

    precios = datos['Close'].values
    # Crear eje x
    dias = np.arange(len(precios))
    print("Datos descargados exitosamente.")

except Exception as e:
    print(f"Error al descargar datos: {e}")
    exit()


# ----- Validación y pruebas -----
print(f"Iniciando etapa de validación y prueba")