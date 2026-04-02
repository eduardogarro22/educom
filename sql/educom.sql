USE educom
GO

--CREATE TABLE clientes (
--    id_cliente INT IDENTITY(1,1) PRIMARY KEY,
--    nombre VARCHAR(50),
--    edad INT,
--    ciudad VARCHAR(50),
--    fecha_alta DATETIME,
--    estado VARCHAR(20),
	  --id_original INT,
--);

--CREATE TABLE servicios (
--    id_servicio INT IDENTITY(1,1) PRIMARY KEY,
--    id_cliente INT,
--    tipo_servicio VARCHAR(20),
--    [plan] VARCHAR(20),
--    precio INT,
--    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
--);

--CREATE TABLE facturacion (
--    id_factura INT IDENTITY(1,1) PRIMARY KEY,
--    id_cliente INT,
--    fecha DATETIME,
--    monto INT,
--    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
--);

--CREATE TABLE bajas (
--    id_baja INT IDENTITY(1,1) PRIMARY KEY,
--    id_cliente INT,
--    fecha_baja DATETIME,
--    motivo VARCHAR(50),
--    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
--);
--CREATE INDEX idx_cliente ON servicios(id_cliente);
--CREATE INDEX idx_facturacion_cliente ON facturacion(id_cliente);

--CREATE VIEW vw_clientes_resumen AS
--SELECT 
--    c.id_cliente,
--    c.nombre,
--    c.edad,
--    c.ciudad,
--    c.estado,
--    s.tipo_servicio,
--    s.[plan],
--    s.precio,
--    f.monto,
--    f.fecha,
--    b.motivo
--FROM clientes c
--LEFT JOIN servicios s ON c.id_cliente = s.id_cliente
--LEFT JOIN facturacion f ON c.id_cliente = f.id_cliente
--LEFT JOIN bajas b ON c.id_cliente = b.id_cliente;