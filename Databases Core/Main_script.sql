-- Verify which one is the current DB: 
SELECT current_database();

-- Parent tables
CREATE TABLE paises(
	PaisID       INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	CodigoPais    VARCHAR(3) NOT NULL UNIQUE,
    NombrePais    TEXT NOT NULL UNIQUE,
	Continente    TEXT NOT NULL
);

CREATE TABLE categorias(
	CategoriaID        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	NombreCategoria    TEXT NOT NULL UNIQUE,
	Descripcion        TEXT
);

CREATE TABLE tipo_clientes(
	TipoClienteID  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	NombreTipo     TEXT NOT NULL UNIQUE,
	Descripcion    TEXT
);


-- Child Tables
CREATE TABLE sucursales(
	SucursalID      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	NombreSucursal  TEXT NOT NULL,
	Ciudad          TEXT NOT NULL,
	PaisID          INTEGER NOT NULL REFERENCES paises(PaisID),
	DireccionCompleta TEXT NOT NULL,
	Activo          BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE productos(
	ProductoID      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	CodigoProducto  TEXT NOT NULL,
	NombreProducto  TEXT NOT NULL UNIQUE,
    CategoriaID     INTEGER NOT NULL REFERENCES categorias(CategoriaID),
	Precio          NUMERIC(10,2) NOT NULL,
	Stock           INTEGER NOT NULL DEFAULT 0,
	Descripcion     TEXT,
	Activo          BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE clientes(
	cliente_id       INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	nombre           TEXT NOT NULL,
	email            VARCHAR(100) NOT NULL UNIQUE,
	telefono         VARCHAR(20),
	fecha_registro   DATE NOT NULL DEFAULT CURRENT_DATE,
	activo           BOOLEAN NOT NULL DEFAULT TRUE,
	tipo_cliente_id  INTEGER NOT NULL REFERENCES tipo_clientes(tipo_cliente_id)
);

CREATE TABLE clientes(
	ClienteID      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	Nombre         TEXT NOT NULL,
	Apellido       TEXT NOT NULL,
    Email          VARCHAR(100) NOT NULL UNIQUE,
	Telefono       VARCHAR(20),
    PaisID         INTEGER NOT NULL REFERENCES paises(PaisID),
    Ciudad         TEXT NOT NULL,
    TipoClienteID  INTEGER NOT NULL REFERENCES tipo_clientes(TipoClienteID),
	FechaRegistro  DATE NOT NULL DEFAULT CURRENT_DATE,
	Activo         BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE empleados(
	EmpleadoID      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	Nombre          TEXT NOT NULL,
	Apellido        TEXT NOT NULL,
    Email           VARCHAR(100) NOT NULL UNIQUE,
	SucursalID      INTEGER NOT NULL REFERENCES sucursales(SucursalID),
    FechaIngreso    DATE NOT NULL DEFAULT CURRENT_DATE,
    Cargo           TEXT NOT NULL,
    Activo          BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE pedidos(
	PedidoID        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	ClienteID       INTEGER NOT NULL REFERENCES clientes(ClienteID),
    SucursalID      INTEGER NOT NULL REFERENCES sucursales(SucursalID),
    EmpleadoID      INTEGER NOT NULL REFERENCES empleados(EmpleadoID),
    FechaPedido     DATE NOT NULL DEFAULT CURRENT_DATE,
    Estado          VARCHAR(20) NOT NULL DEFAULT 'Pendiente',
	Total           NUMERIC(10,2) NOT NULL DEFAULT 0,
    Notas           TEXT
);

CREATE TABLE detalle_pedidos(
	DetalleID    INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	PedidoID     INTEGER NOT NULL REFERENCES pedidos(PedidoID),
	ProductoID   INTEGER NOT NULL REFERENCES productos(ProductoID),
	Cantidad      INTEGER NOT NULL DEFAULT 1,
	PrecioUnitario   NUMERIC(10,2) NOT NULL
);