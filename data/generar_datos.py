import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Configuración
np.random.seed(42)
cantidad_clientes = 500

nombres = ["Juan", "Pedro", "Luis", "Ana", "Maria", "Sofia", "Carlos", "Lucia"]
estados = ["activo", "baja"]

# --- CLIENTES ---
clientes = pd.DataFrame({
    "id_cliente": range(1, cantidad_clientes + 1),
    "nombre": [random.choice(nombres) for _ in range(cantidad_clientes)],
    "edad": np.random.randint(18, 70, cantidad_clientes),
    "ciudad": ["Rio Gallegos"] * cantidad_clientes,
    "fecha_alta": [datetime.now() - timedelta(days=random.randint(0, 1000)) for _ in range(cantidad_clientes)],
    "estado": np.random.choice(estados, cantidad_clientes)
})

# --- SERVICIOS ---
tipos = ["fibra", "celular"]
planes = ["basico", "medio", "premium"]

servicios = pd.DataFrame({
    "id_servicio": range(1, cantidad_clientes + 1),
    "id_cliente": clientes["id_cliente"],
    "tipo_servicio": np.random.choice(tipos, cantidad_clientes),
    "plan": np.random.choice(planes, cantidad_clientes),
    "precio": np.random.randint(5000, 20000, cantidad_clientes)
})

# --- FACTURACION ---
facturacion = pd.DataFrame({
    "id_factura": range(1, cantidad_clientes + 1),
    "id_cliente": clientes["id_cliente"],
    "fecha": [datetime.now() - timedelta(days=random.randint(0, 365)) for _ in range(cantidad_clientes)],
    "monto": servicios["precio"]
})

# --- BAJAS ---
bajas = clientes[clientes["estado"] == "baja"].copy()
motivos = ["precio alto", "mala calidad", "competencia", "mudanza"]

bajas["id_baja"] = range(1, len(bajas) + 1)
bajas["fecha_baja"] = [datetime.now() - timedelta(days=random.randint(1, 200)) for _ in range(len(bajas))]
bajas["motivo"] = np.random.choice(motivos, len(bajas))

bajas = bajas[["id_baja", "id_cliente", "fecha_baja", "motivo"]]

# --- EXPORTAR ---
clientes.to_csv("../data/clientes.csv", index=False)
servicios.to_csv("../data/servicios.csv", index=False)
facturacion.to_csv("../data/facturacion.csv", index=False)
bajas.to_csv("../data/bajas.csv", index=False)

print("✅ Datos generados correctamente")