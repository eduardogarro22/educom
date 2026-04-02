import pandas as pd
from sqlalchemy import create_engine

# CONEXIÓN A SQL SERVER

server = r'EDU\SQLEXPRESS'
database = 'educom'

connection_string = (
    f"mssql+pyodbc://@{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

engine = create_engine(connection_string)

# CARGA DE ARCHIVOS CSV

clientes = pd.read_csv("../data/clientes.csv")
servicios = pd.read_csv("../data/servicios.csv")
facturacion = pd.read_csv("../data/facturacion.csv")
bajas = pd.read_csv("../data/bajas.csv")

# GUARDAR ID ORIGINAL (MAPEO)

clientes["id_original"] = clientes["id_cliente"]

# ELIMINAR IDs AUTO-GENERADOS

clientes = clientes.drop(columns=["id_cliente"])
servicios = servicios.drop(columns=["id_servicio"])
facturacion = facturacion.drop(columns=["id_factura"])
bajas = bajas.drop(columns=["id_baja"])

#  CONVERSIÓN DE FECHAS

clientes["fecha_alta"] = pd.to_datetime(clientes["fecha_alta"], errors="coerce")
facturacion["fecha"] = pd.to_datetime(facturacion["fecha"], errors="coerce")
bajas["fecha_baja"] = pd.to_datetime(bajas["fecha_baja"], errors="coerce")

# LIMPIEZA DE DATOS (NOT NULL)

clientes = clientes.dropna()
servicios = servicios.dropna()
facturacion = facturacion.dropna()
bajas = bajas.dropna()

# PASO 1: INSERTAR CLIENTES

clientes.to_sql("clientes", con=engine, if_exists="append", index=False)

# PASO 2: MAPEO DE IDs

clientes_sql = pd.read_sql(
    "SELECT id_cliente, id_original FROM clientes",
    engine
)

# diccionario: id_original → id_cliente nuevo
map_ids = dict(zip(clientes_sql["id_original"], clientes_sql["id_cliente"]))

# REEMPLAZAR IDS EN TABLAS HIJAS

servicios["id_cliente"] = servicios["id_cliente"].map(map_ids)
facturacion["id_cliente"] = facturacion["id_cliente"].map(map_ids)
bajas["id_cliente"] = bajas["id_cliente"].map(map_ids)

# VALIDACIÓN (PRO)

print("Servicios sin match:", servicios["id_cliente"].isna().sum())
print("Facturación sin match:", facturacion["id_cliente"].isna().sum())
print("Bajas sin match:", bajas["id_cliente"].isna().sum())

# PASO 3: INSERTAR RELACIONES

servicios.to_sql("servicios", con=engine, if_exists="append", index=False)
facturacion.to_sql("facturacion", con=engine, if_exists="append", index=False)
bajas.to_sql("bajas", con=engine, if_exists="append", index=False)


print("✅ CARGA COMPLETA")